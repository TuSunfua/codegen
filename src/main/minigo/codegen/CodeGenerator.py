'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

class Env:
    def __init__(self, frame, sym):
        #frame: Frame
        #syms: [[Symbol]]
        self.frame:Frame = frame
        self.sym:list[list[Symbol]] = sym
        
class Access:
    def __init__(self, frame, sym, isLeft=False):
        #frame: Frame
        #syms: [[Symbol]]
        #isLeft: Bool
        self.frame:Frame = frame
        self.sym:list[list[Symbol]] = sym
        self.isLeft:bool = isLeft
    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.staticInitCode = []
        self.clinit = None
        self.astTree = None
        self.emit = None

    def init(self):
        mem = [
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True))
        ]
        return mem
    
    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.emit = Emitter(lambda context: dir_ + "/" + context + ".j")
        self.visit(ast, gl)   
        
    def emitObjectInit(self, frame: Frame, context: str, mtype=MType([], VoidType()), body=[]):
        self.emit.printout(self.emit.emitMETHOD(context, mtype, False, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), "this", ClassType(context), 
            frame.getStartLabel(), frame.getEndLabel(), frame
        ))   
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        [self.emit.printout(code) for code in body] 

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(mtype.rettype, frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()   
        return frame

    def visitProgram(self, ast:Program, o):
        # Initialize class name and emitter
        self.emit.setContext(self.className)
        self.emit.printout(self.emit.emitPROLOG(self.className, self.className, "java.lang.Object"))
        # Collect func, method and type declarations
        env = Env(None, [o])
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                if decl.name == "main":
                    mtype = MType([ArrayType([None], StringType())], VoidType())
                else:
                    mtype = MType(list(map(lambda x: x.parType, decl.params)), decl.retType)
                env.sym[0] += [Symbol(decl.name, mtype, CName(self.className))]
            elif type(decl) is MethodDecl:
                pass               
            elif type(decl) is StructType:
                env.sym[0].append(Symbol(decl.name, decl, CName(f'{self.className}${decl.name}')))              
                pass
                
            elif type(decl) is InterfaceType:
                pass
        
        # Generate class constructor
        frame = Frame("<init>", VoidType())
        self.emitObjectInit(
            frame=frame, 
            context=self.className, 
            mtype=MType([], VoidType()), 
            body=[
                self.emit.emitREADVAR("this", ClassType(self.className), 0, frame),
                self.emit.emitINVOKESPECIAL(frame)
            ]
        )
        # Generate class initializer (<clinit>)
        self.clinit = Frame("<clinit>", VoidType())
        self.staticInitCode = []
        # Code generation
        for decl in ast.decl:
            self.visit(decl, env)
        # Emit static initializer (<clinit>) if there are static field initializations
        if self.staticInitCode:
            self.emitObjectInit(
                frame=self.clinit,
                context="<clinit>",
                mtype=MType([], VoidType()),
                body=self.staticInitCode
            )
        # Emit epilog
            self.emit.printout(self.emit.emitCLINIT_START())
            for code in self.staticInitCode:
                self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(VoidType(), env.frame))
            self.emit.printout(self.emit.emitCLINIT_END())
        
        self.emit.printout(self.emit.emitEPILOG())
    
    def visitVarDecl(self, ast: VarDecl, o: Env):
        # Determine variable type
        varType = ast.varType
        varCode = ""

        if not o.frame:  # Global scope (static field)
            # Create environment for static field
            env = Access(self.clinit, o.sym, False)
            # Generate initialization code if varInit is provided
            if ast.varInit:
                varCode, varType = self.visit(ast.varInit, env)
            # Declare the static field
            field_decl = self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None)
            self.emit.printout(field_decl)
            # Type conversion if necessary
            if type(ast.varType) is not type(varType):
                if isinstance(ast.varType, FloatType) and isinstance(varType, IntType):
                    varCode += self.emit.emitI2F(env.frame)
                    varType = ast.varType
            # Explicitly set default value for the type           
            if not ast.varInit:
                if isinstance(varType, IntType):
                    varCode = self.emit.emitPUSHCONST('0', varType, env.frame)
                elif isinstance(varType, FloatType):
                    varCode = self.emit.emitPUSHCONST('0.0', varType, env.frame)
                elif isinstance(varType, BoolType):
                    varCode = self.emit.emitPUSHCONST('false', varType, env.frame)
                elif isinstance(varType, ArrayType):
                    for dim in varType.dimens:
                        dim_code, _ = self.visit(dim, env)
                        varCode += dim_code
                    varCode += self.emit.emitNEWARRAY(varType, o.frame)
                else:
                    varCode = self.emit.emitPUSHNULL(env.frame)
            # Emit assignment to static field
            assign_code = self.emit.emitPUTSTATIC(f"{self.className}/{ast.varName}", varType, env.frame)
            # Update symbol table and static initialization code
            o.sym[0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.staticInitCode.append(varCode + assign_code)
        else:  # Local scope
            # Create environment for local variable
            env = Access(o.frame, o.sym)
            # Generate initialization code if varInit is provided
            if ast.varInit:
                varCode, varType = self.visit(ast.varInit, env)  
            # Type conversion if necessary
            if type(ast.varType) is not type(varType):
                if isinstance(ast.varType, FloatType) and isinstance(varType, IntType):
                    varCode += self.emit.emitI2F(env.frame)
                    varType = ast.varType
            # Explicitly set default value for the type
            if not ast.varInit:
                if isinstance(varType, IntType):
                    varCode = self.emit.emitPUSHCONST('0', varType, env.frame)
                elif isinstance(varType, FloatType):
                    varCode = self.emit.emitPUSHCONST('0.0', varType, env.frame)
                elif isinstance(varType, BoolType):
                    varCode = self.emit.emitPUSHCONST('false', varType, env.frame)
                elif isinstance(varType, ArrayType):
                    for dim in varType.dimens:
                        dim_code, _ = self.visit(dim, env)
                        varCode += dim_code
                    varCode += self.emit.emitNEWARRAY(varType, o.frame)
                else:
                    varCode = self.emit.emitPUSHNULL(env.frame)
            # Emit initialization code
            self.emit.printout(varCode)    
            # Allocate index and declare variable first
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                index, ast.varName, varType, 
                o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame
            ))
            # Emit assignment to local variable
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, o.frame))
            # Update symbol table
            o.sym[0].append(Symbol(ast.varName, varType, Index(index)))
            
    def visitConstDecl(self, ast: ConstDecl, o: Env):
        # Determine constant type
        conType = ast.conType
        conCode = ""
        
        if not o.frame: # Global scope (static constant)
            # Create environment for static constant
            env = Access(self.clinit, o.sym, False)
            # Generate initialization code 
            conCode, conType = self.visit(ast.iniExpr, env)
            # Declare the static field
            field_decl = self.emit.emitATTRIBUTE(ast.conName, conType, True, True, None)
            self.emit.printout(field_decl)
            # Emit assignment to static constant
            assign_code = self.emit.emitPUTSTATIC(f"{self.className}/{ast.conName}", conType, env.frame)
            # Update symbol table and static initialization code
            o.sym[0].append(Symbol(ast.conName, conType, CName(self.className)))
            self.staticInitCode.append(conCode + assign_code)
        else: # Local scope
            # Create environment for local constant
            env = Access(o.frame, o.sym)          
            # Generate initialization code
            conCode, conType = self.visit(ast.iniExpr, env)      
            # Emit initialization code
            self.emit.printout(conCode)        
            # Allocate index and declare constant first
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                index, ast.conName, conType, 
                o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame
            ))         
            # Update symbol table and static initialization code
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, conType, index, o.frame))
            o.sym[0].append(Symbol(ast.conName, conType, Index(index)))
   
    def visitFuncDecl(self, ast:FuncDecl, o:Env):
        env = Env(Frame(ast.name, ast.retType), [[]] + o.sym.copy())
        
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
            
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, env.frame))
        env.frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        
        if isMain:
            self.emit.printout(self.emit.emitVAR(
                env.frame.getNewIndex(), "args", ArrayType([None], StringType()), 
                env.frame.getStartLabel(), env.frame.getEndLabel(), env.frame
            ))
        else:
            for param in ast.params:
                self.visit(param, env)
                
        self.visit(ast.body, env)
        
        self.emit.printout(self.emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), env.frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(env.frame))
        env.frame.exitScope()

    def visitMethodDecl(self, ast, o):
        return None
    
    def visitParamDecl(self, ast:ParamDecl, o:Env):
        # Determine parameter type
        parType = ast.parType

        # Create environment for parameter
        env = Access(o.frame, o.sym)

        # Declare parameter
        index = env.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            index, ast.parName, parType, 
            env.frame.getStartLabel(), env.frame.getEndLabel(), env.frame
        ))

        # Update symbol table
        env.sym[0].append(Symbol(ast.parName, parType, Index(index)))

    def visitPrototype(self, ast, o):
        return None
    
    def visitIntType(self, ast, o):
        return "", ast
    
    def visitFloatType(self, ast, o):
        return "", ast
    
    def visitBoolType(self, ast, o):
        return "", ast
    
    def visitStringType(self, ast, o):
        return "", ast
    
    def visitVoidType(self, ast, o):
        return "", ast
    
    def visitArrayType(self, ast: ArrayType, o: Env):
        return "", ast
    
    def visitStructType(self, ast: StructType, o: Env):
        context = f"{self.className}${ast.name}"
        self.emit.setContext(context)
        self.emit.printout(self.emit.emitPROLOG(self.className, context, "java.lang.Object"))
        
        frame = Frame(context, VoidType())
        body = []
        for idx, ele in enumerate(ast.elements):
            typ = ele[1] if type(ele[1]) is not Id else ClassType(context)
            body.append(self.emit.emitREADVAR("this", ClassType(context), 0, frame)) 
            body.append(self.emit.emitREADVAR(ele[0], typ, idx, frame))
            body.append(self.emit.emitPUTFIELD(f'{context}/{ele[0]}', typ, frame))
            
        self.emitObjectInit(
            frame=frame, 
            context=context, 
            mtype=MType(map(lambda ele: ele[1] if type(ele[1]) is not Id else ClassType(context), ast.elements), VoidType()),
            body=body
        )
        
        self.emit.setContext(self.className)

    def visitInterfaceType(self, ast, o):
        return None
    
    def visitBlock(self, ast:Block, o:Env):
        env = Env(o.frame, [[]] + o.sym.copy())
        env.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        for member in ast.member:
            self.visit(member, env)
        self.emit.printout(self.emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        env.frame.exitScope()
 
    def visitAssign(self, ast: Assign, o: Env):
        # Check if the left-hand side is identifier but not declared
        if type(ast.lhs) is Id:
            sym:Symbol = next(filter(lambda x: x.name == ast.lhs.name, [j for i in o.sym for j in i]), None)
            if not sym:
                self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)
                return
            
        if type(ast.lhs) is ArrayCell:
            # Visit left-hand side (LHS) expression
            lhs_code, lhs_type = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            # Visit right-hand side (RHS) expression
            rhs_code, rhs_type = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        else:
            # Visit right-hand side (RHS) expression
            rhs_code, rhs_type = self.visit(ast.rhs, Access(o.frame, o.sym, False))
            # Visit left-hand side (LHS) expression
            lhs_code, lhs_type = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            

        # Type conversion if necessary
        if isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
            rhs_code += self.emit.emitI2F(o.frame)
            
        if type(ast.lhs) is ArrayCell:
            assign_code = lhs_code + rhs_code + self.emit.emitASTORE(lhs_type, o.frame)
            self.emit.printout(assign_code)
            return

        # Emit assignment code
        self.emit.printout(rhs_code + lhs_code)
   
    def visitIf(self, ast: If, o: Env):
        if ast.elseStmt:
            label_else = o.frame.getNewLabel()  # else label
            label_end = o.frame.getNewLabel()   # end label
            # Visit condition expression
            cond_code, _ = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(cond_code)
            # Emit conditional jump to else label
            self.emit.printout(self.emit.emitIFFALSE(label_else, o.frame))
            # Visit then statement
            self.visit(ast.thenStmt, o)
            # Emit unconditional jump to end label
            self.emit.printout(self.emit.emitGOTO(label_end, o.frame))
            # Emit else label
            self.emit.printout(self.emit.emitLABEL(label_else, o.frame))
            # Visit else statement
            self.visit(ast.elseStmt, o)
            # Emit end label
            self.emit.printout(self.emit.emitLABEL(label_end, o.frame))
        else:
            label_end = o.frame.getNewLabel()  # end label
            # Visit condition expression
            cond_code, _ = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(cond_code)
            # Emit conditional jump to end label
            self.emit.printout(self.emit.emitIFFALSE(label_end, o.frame))
            # Visit then statement
            self.visit(ast.thenStmt, o)
            # Emit end label
            self.emit.printout(self.emit.emitLABEL(label_end, o.frame))
    
    def visitForBasic(self, ast: ForBasic, o: Env):
        # Enter for loop scope
        o.frame.enterLoop()
        # Generate labels for loop and end
        label_continue = o.frame.getContinueLabel()
        label_break = o.frame.getBreakLabel()
        # emit loop label
        self.emit.printout(self.emit.emitLABEL(label_continue, o.frame))
        # Visit condition expression
        cond_code, _ = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(cond_code)
        # Emit conditional jump to break label
        self.emit.printout(self.emit.emitIFFALSE(label_break, o.frame))
        # Visit loop body
        self.visit(ast.loop, o)
        # Emit unconditional jump to continue label
        self.emit.printout(self.emit.emitGOTO(label_continue, o.frame))
        # Emit break label
        self.emit.printout(self.emit.emitLABEL(label_break, o.frame))
        # Exit for loop scope
        o.frame.exitLoop()
 
    def visitForStep(self, ast: ForStep, o: Env):
        # Create new environment for the for loop
        env = Env(o.frame, o.sym.copy())
        # Enter for loop scope
        env.frame.enterLoop()
        # Generate labels for loop and end
        label_loop = env.frame.getNewLabel()
        label_continue = env.frame.getContinueLabel()
        label_break = env.frame.getBreakLabel()
        # Visit initialization expression
        self.visit(ast.init, env)
        # Emit loop label
        self.emit.printout(self.emit.emitLABEL(label_loop, env.frame))
        # Visit condition expression
        cond_code, _ = self.visit(ast.cond, Access(env.frame, env.sym, False))
        self.emit.printout(cond_code)
        # Emit conditional jump to break label
        self.emit.printout(self.emit.emitIFFALSE(label_break, env.frame))
        # Visit loop body
        self.visit(ast.loop, env)
        # Emit continue label
        self.emit.printout(self.emit.emitLABEL(label_continue, env.frame))
        # Visit update expression
        self.visit(ast.upda, env)
        # Emit unconditional jump to loop label
        self.emit.printout(self.emit.emitGOTO(label_loop, env.frame))
        # Emit break label
        self.emit.printout(self.emit.emitLABEL(label_break, env.frame))
        # Exit for loop scope
        env.frame.exitLoop()

    def visitForEach(self, ast: ForEach, o: Env):
        return None # Not implemented

    def visitContinue(self, ast: Continue, o: Env):
        # Emit jump to continue label
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
    
    def visitBreak(self, ast: Break, o: Env):
        # Emit jump to break label
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    
    def visitReturn(self, ast: Return, o: Env):
        if ast.expr:
            ec, et = self.visit(ast.expr, Access(o.frame, o.sym, False))
            if type(et) is not type(o.frame.returnType):
                if isinstance(et, IntType) and isinstance(o.frame.returnType, FloatType):
                    ec += self.emit.emitI2F(o.frame)
            self.emit.printout(ec + self.emit.emitRETURN(et, o.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))

    def visitBinaryOp(self, ast:BinaryOp, o:Access):
        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)
        
        if ast.op == '+':
            # String type
            if type(lt) is StringType:
                return lc + rc + self.emit.emitADDOP(ast.op, lt, o.frame), StringType()
                
            # Numeric type
            if type(lt) is IntType and type(rt) is IntType:
                return lc + rc + self.emit.emitADDOP(ast.op, lt, o.frame), IntType()
            if type(lt) is FloatType and type(rt) is FloatType:
                return lc + rc + self.emit.emitADDOP(ast.op, lt, o.frame), FloatType()
            if type(lt) is IntType and type(rt) is FloatType:
                return lc + self.emit.emitI2F(o.frame) + rc + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
            if type(lt) is FloatType and type(rt) is IntType:
                return lc + rc + self.emit.emitI2F(o.frame)+ self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
            
        if ast.op in ['-', '*', '/']:
            # Numeric type
            if type(lt) is IntType and type(rt) is IntType:
                if ast.op == '-':
                    return lc +rc + self.emit.emitADDOP(ast.op, lt, o.frame), IntType()
                if ast.op in ['*', '/']:
                    return lc + rc + self.emit.emitMULOP(ast.op, lt, o.frame), IntType()
                
            if type(lt) is FloatType and type(rt) is FloatType:
                if ast.op == '-':
                    return lc + rc + self.emit.emitADDOP(ast.op, lt, o.frame), FloatType()
                if ast.op in ['*', '/']:
                    return lc + rc + self.emit.emitMULOP(ast.op, lt, o.frame), FloatType()
                
            if type(lt) is IntType and type(rt) is FloatType:
                if ast.op == '-':
                    return lc + self.emit.emitI2F(o.frame) + rc + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
                if ast.op in ['*', '/']:
                    return lc + self.emit.emitI2F(o.frame) + rc + self.emit.emitMULOP(ast.op, FloatType(), o.frame), FloatType()

            if type(lt) is FloatType and type(rt) is IntType:
                if ast.op == '-':
                    return lc + rc + self.emit.emitI2F(o.frame) + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
                if ast.op in ['*', '/']:
                    return lc + rc + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ast.op, FloatType(), o.frame), FloatType()
            
        if ast.op == '%':
            if type(lt) is IntType and type(rt) is IntType:
                return lc + rc + self.emit.emitMOD(o.frame), IntType()

        if ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            # String type
            if type(lt) is StringType and type(rt) is StringType:
                return lc + rc + self.emit.emitREOP(ast.op, lt, o.frame), BoolType()
            
            # Numeric type
            return lc + rc + self.emit.emitREOP(ast.op, lt, o.frame), BoolType()

        if ast.op in ['&&', '||']:
            if type(lt) is BoolType and type(rt) is BoolType:
                if ast.op == '&&':
                    return lc + rc + self.emit.emitANDOP(o.frame), BoolType()
                if ast.op == '||':
                    return lc + rc + self.emit.emitOROP(o.frame), BoolType()
    
    def visitUnaryOp(self, ast:UnaryOp, o:Access):
        ec, et = self.visit(ast.body, o)
        
        if ast.op == '-':
            if type(et) is IntType:
                return ec + self.emit.emitNEGOP(et, o.frame), IntType()
            if type(et) is FloatType:
                return ec + self.emit.emitNEGOP(et, o.frame), FloatType()
        
        if ast.op == '!':
            if type(et) is BoolType:
                return ec + self.emit.emitNOT(et, o.frame), BoolType()
    
    def visitFuncCall(self, ast:FuncCall, o:Env|Access):
        if type(o) is Env:
            sym = next(filter(lambda x: x.name == ast.funName, o.sym[-1]), None)
            [self.emit.printout(self.visit(x, Access(o.frame, o.sym, False))[0]) for x in ast.args]
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o.frame))
        
        if type(o) is Access:
            sym = next(filter(lambda x: x.name == ast.funName, o.sym[-1]), None)
            code = ''
            for arg in ast.args:
                arc_code, _ = self.visit(arg, Access(o.frame, o.sym, False))
                code += arc_code
            code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o.frame)
            return code, sym.mtype.rettype

    def visitMethCall(self, ast, o):
        return None
    
    def visitId(self, ast:Id, o:Access):
        sym:Symbol = next(filter(lambda x: x.name == ast.name, [j for i in o.sym for j in i]), None)
        if type(sym.value) is Index: # local variable
            if o.isLeft:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype        
        
        if o.isLeft: # static/global variable
            return self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype, o.frame), sym.mtype
        return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype, o.frame), sym.mtype
    
    def visitArrayCell(self, ast: ArrayCell, o: Access):
        code = ""
    
        # Step 1: Visit ast.arr to load array reference
        arr_code, arr_type = self.visit(ast.arr, Access(o.frame, o.sym, False))
        code += arr_code
        
        # Current type tracks the type as we process indices
        current_type = arr_type
        
        # Step 2: Process each index
        for i, idx in enumerate(ast.idx):
            # Load index value
            idx_code, _ = self.visit(idx, Access(o.frame, o.sym, False))
            code += idx_code
            
            # Determine if this is the final index
            is_final_index = (i == len(ast.idx) - 1)
            ele_type = current_type.eleType
            
            if is_final_index:
                # Final index: Handle read or write
                if o.isLeft:
                    pass # No action needed for left-hand side
                else:
                    # Read: Load the element
                    code += self.emit.emitALOAD(ele_type, o.frame)
            else:
                # Intermediate index: Load sub-array
                code += self.emit.emitALOAD(current_type, o.frame)  # aaload
                # Update type to sub-array
            current_type = ArrayType(current_type.dimens[1:], ele_type) if len(current_type.dimens) > 1 else ele_type
        
        return code, current_type
    
    def visitFieldAccess(self, ast, o):
        return None
    
    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        if isinstance(ast.value, int):
            return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
        return self.emit.emitPUSHICONST(int(ast.value, 0), o.frame), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        if isinstance(ast.value, float):
            return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()
        return self.emit.emitPUSHFCONST(str(float(ast.value)), o.frame), FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        if isinstance(ast.value, bool):
            return self.emit.emitPUSHICONST(1 if ast.value else 0, o.frame), BoolType()
        return self.emit.emitPUSHICONST(1 if ast.value == "true" else 0, o.frame), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, o: Access):
        code = ""
        array_type = ArrayType(ast.dimens, ast.eleType)

        if len(ast.dimens) == 1:
            # Step 1: Push the size of the array
            dim_code, _ = self.visit(ast.dimens[0], o)
            code += dim_code
            # Step 2: emitNEWARRAY
            code += self.emit.emitNEWARRAY(array_type, o.frame)
            # Step 3: For each element
            for i, val in enumerate(ast.value):
                # emitDUP
                code += self.emit.emitDUP(o.frame)
                # emitPUSHCONST for index
                code += self.emit.emitPUSHCONST(i, IntType(), o.frame)
                # visit: Generate code for value
                val_code, _ = self.visit(val, o)
                code += val_code
                # emitIASTORE
                code += self.emit.emitASTORE(ast.eleType, o.frame)
        else:
            # Step 1: Push the size of the array
            dim_code, _ = self.visit(ast.dimens[0], o)
            code += dim_code
            # Step 2: emitANEWARRAY
            code += self.emit.emitANEWARRAY(array_type, o.frame)
            # Step 3: For each sub-array
            for i, inner_val in enumerate(ast.value):
                # emitDUP
                code += self.emit.emitDUP(o.frame)
                # emitPUSHCONST for index
                code += self.emit.emitPUSHCONST(i, IntType(), o.frame)
                # Recursive call for sub-array
                inner_literal = ArrayLiteral(array_type.dimens[1:], array_type.eleType, inner_val)
                inner_code, _ = self.visitArrayLiteral(inner_literal, o)
                code += inner_code
                # emitAASTORE
                code += self.emit.emitASTORE(array_type, o.frame)
        
        return code, array_type

    def visitStructLiteral(self, ast, o):
        return None

    def visitNilLiteral(self, ast:NilLiteral, o:Access):
        return self.emit.emitPUSHNULL(o.frame), None