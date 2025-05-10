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
from abc import ABC

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
        
    def emitMethod(self, isInit, frame: Frame, context: str, mtype=MType([], VoidType()), body=[]):
        self.emit.printout(self.emit.emitMETHOD(frame.name, mtype)) 
        frame.enterScope(False)  
        if isInit:
            frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                0, "this", ClassType(context), 
                frame.getStartLabel(), frame.getEndLabel(), frame
            ))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
        [self.emit.printout(code) for code in body] 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(mtype.rettype, frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()   
        
    def setDefaultValue(self, typ, env: Access):
        varCode = ""
        if isinstance(typ, IntType):
            varCode = self.emit.emitPUSHCONST('0', typ, env.frame)
        elif isinstance(typ, FloatType):
            varCode = self.emit.emitPUSHCONST('0.0', typ, env.frame)
        elif isinstance(typ, BoolType):
            varCode = self.emit.emitPUSHCONST('false', typ, env.frame)
        elif isinstance(typ, ArrayType):
            for dim in typ.dimens:
                dim_code, _ = self.visit(dim, env)
                varCode += dim_code
            varCode += self.emit.emitNEWARRAY(typ, env.frame)
        else:
            varCode = self.emit.emitPUSHNULL(env.frame)
        return varCode
                    
    def visitProgram(self, ast:Program, o):
        # Collect func, method and type declarations
        env = Env(None, [o])
        identifiers, types, functions, methods  = [], [], [], []
        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                identifiers.append(decl)
            else:
                if type(decl) is FuncDecl:
                    functions.append(decl)
                    if decl.name == "main":
                        mtype = MType([ArrayType([None], StringType())], VoidType())
                    else:
                        mtype = MType(list(map(lambda x: x.parType, decl.params)), decl.retType)
                    env.sym[0] += [Symbol(decl.name, mtype, CName(self.className))]
                elif type(decl) is MethodDecl:
                    methods.append(decl)
                elif isinstance(decl, (StructType, InterfaceType)):
                    types.append(decl)
                    env.sym[0].append(Symbol(decl.name, decl, CName(self.className)))
                
        # Append methods to structs
        for decl in methods:
            struct_type: StructType = next(filter(lambda x: x.name == decl.recType.name, [j for i in env.sym for j in i]), None).mtype
            mtype = MType(list(map(lambda x: x.parType, decl.fun.params)), decl.fun.retType)
            struct_type.methods.append(Symbol(decl.fun.name, mtype, CName(struct_type.name)))
        
        # Initialize class name and emitter
        self.emit.setContext(self.className)
        self.emit.printout(self.emit.emitPROLOG(self.className, self.className))
        
        # Generate class initializer (<clinit>)
        self.clinit = Frame("<clinit>", VoidType())
        self.staticInitCode = []
        
        # 1. Generate code for var/const declarations
        for decl in identifiers:
            self.visit(decl, env)
            
        # 2. Generate code for function declarations
        for decl in functions:
            self.visit(decl, env)
        
        # 3. Gen code for types declarations
        for decl in types:
            self.visit(decl, env)
            
        # 4. Generate code for method declarations
        for decl in methods:
            self.visit(decl, env)
        
        # Emit static initializer (<clinit>) if there are static field initializations
        if self.staticInitCode:
            self.emitMethod(
                isInit=False,
                frame=self.clinit,
                context="<clinit>",
                body=self.staticInitCode
            )
        # Generate class constructor (<init>)
        frame = Frame("<init>", VoidType())
        self.emitMethod(
            isInit=True,
            frame=frame, 
            context=self.className
        )
        # Emit epilog
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
                if type(ast.varType) is ArrayType and type(ast.varInit) is ArrayLiteral:
                    if type(ast.varType.eleType) is FloatType and type(ast.varInit.eleType) is IntType:
                        ast.varInit.eleType = FloatType()
                varCode, varType = self.visit(ast.varInit, env)
            # Type conversion if necessary
            if isinstance(ast.varType, FloatType) and isinstance(varType, IntType):
                varCode += self.emit.emitI2F(env.frame)
                varType = ast.varType
            if type(ast.varType) is Id and type(varType) is ClassType:
                interface_def = next((j for i in o.sym for j in i if j.name == ast.varType.name), None).mtype
                if type(interface_def) is InterfaceType:
                    struct_def = next((j for i in o.sym for j in i if j.name == varType.name), None).mtype
                    struct_def.implements.append(ClassType(ast.varType.name))
                    varType = ast.varType
            # Explicitly set default value for the type           
            if not ast.varInit:
                varCode += self.setDefaultValue(varType, env)
            # Emit assignment to static field
            assign_code = self.emit.emitPUTSTATIC(f"{self.className}/{ast.varName}", varType, env.frame)
            # Update symbol table and static initialization code
            o.sym[0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.staticInitCode.append(varCode + assign_code)
            # Declare the static field
            field_decl = self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None)
            self.emit.printout(field_decl)
        else:  # Local scope
            # Create environment for local variable
            env = Access(o.frame, o.sym)
            # Generate initialization code if varInit is provided
            if ast.varInit:
                if type(ast.varType) is ArrayType and type(ast.varInit) is ArrayLiteral:
                    if type(ast.varType.eleType) is FloatType and type(ast.varInit.eleType) is IntType:
                        ast.varInit.eleType = FloatType()
                varCode, varType = self.visit(ast.varInit, env)  
            # Type conversion if necessary
            if isinstance(ast.varType, FloatType) and isinstance(varType, IntType):
                varCode += self.emit.emitI2F(env.frame)
                varType = ast.varType
            if type(ast.varType) is Id and type(varType) is ClassType:
                interface_def = next((j for i in o.sym for j in i if j.name == ast.varType.name), None).mtype
                if type(interface_def) is InterfaceType:
                    struct_def = next((j for i in o.sym for j in i if j.name == varType.name), None).mtype
                    struct_def.implements.append(ClassType(ast.varType.name))
                    varType = ast.varType
                
            # Explicitly set default value for the type
            if not ast.varInit:
                varCode += self.setDefaultValue(varType, env)
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
            # Emit assignment to static constant
            assign_code = self.emit.emitPUTSTATIC(f"{self.className}/{ast.conName}", conType, env.frame)
            # Update symbol table and static initialization code
            o.sym[0].append(Symbol(ast.conName, conType, CName(self.className)))
            self.staticInitCode.append(conCode + assign_code)
            # Declare the static field
            field_decl = self.emit.emitATTRIBUTE(ast.conName, conType, True, True, None)
            self.emit.printout(field_decl)
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
   
    def visitFuncDecl(self, ast: FuncDecl, o: Env):
        env = Env(Frame(ast.name, ast.retType), [[]] + o.sym.copy())
        
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
            
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True))
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

    def visitMethodDecl(self, ast: MethodDecl, o: Env):
        # Resolve struct type and set context
        struct_type: StructType = next(filter(lambda x: x.name == ast.recType.name, [j for i in o.sym for j in i]), None).mtype
        context = struct_type.name
        self.emit.setContext(context)

        # Setup frame and environment
        env = Env(Frame(context, ast.fun.retType), [[]] + o.sym.copy())

        # Define method type and emit declaration
        mtype = MType([param.parType for param in ast.fun.params], ast.fun.retType)
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype))
        env.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env.frame.getStartLabel(), env.frame))

        # Add receiver and process parameters
        env.sym[0].append(Symbol(ast.receiver, ClassType(context), Index(env.frame.getNewIndex())))
        for param in ast.fun.params:
            self.visit(param, env)

        # Generate body
        self.visit(ast.fun.body, env)

        # Emit method footer and exit scope
        self.emit.printout(self.emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), env.frame))
        self.emit.printout(self.emit.emitENDMETHOD(env.frame))
        env.frame.exitScope()

        # Restore context
        self.emit.setContext(self.className)
    
    def visitParamDecl(self, ast: ParamDecl, o: Env):
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

    def visitPrototype(self, ast: AST.Prototype, o: Env):
        mtype = MType(ast.params, ast.retType)
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, False, True))
        self.emit.printout(self.emit.emitENDMETHOD(o.frame))
    
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
        context = ast.name
        self.emit.setContext(context)
        self.emit.printout(self.emit.emitPROLOG(self.className, context))
        
        # Remove duplicate interface names
        ast.implements = list({implement.name: implement for implement in ast.implements}.values())
        for implement in ast.implements:
            self.emit.printout(self.emit.emitIMPLEMENTS(implement.name))
        
        frame = Frame("<init>", VoidType())
        body = []
        for ele in ast.elements:
            typ = ele[1] if type(ele[1]) is not Id else ClassType(ele[1].name)
            self.emit.printout(self.emit.emitATTRIBUTE(ele[0], typ, False, False, None))
            
            body.append(self.emit.emitREADVAR('this', ClassType(context), 0, frame))
            body.append(self.emit.emitREADVAR(ele[0], typ, frame.getNewIndex() + 1, frame))
            body.append(self.emit.emitPUTFIELD(f'{context}/{ele[0]}', typ, frame))
            
        self.emitMethod(
            isInit=True,
            frame=frame, 
            context=context,
            mtype=MType(list(map(lambda ele: ele[1] if type(ele[1]) is not Id else ClassType(ele[1].name), ast.elements)), VoidType()),
            body=body
        )
        
        self.emit.setContext(self.className)

    def visitInterfaceType(self, ast: InterfaceType, o: Env):
        context = ast.name
        self.emit.setContext(context)
        self.emit.printout(self.emit.emitPROLOG(self.className, context, False))
        
        for method in ast.methods:
            self.visit(method, o)
        
        self.emit.setContext(self.className)
    
    def visitBlock(self, ast:Block, o:Env):
        env = Env(o.frame, [[]] + o.sym.copy())
        env.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        for member in ast.member:
            self.visit(member, env)
        self.emit.printout(self.emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        env.frame.exitScope()
 
    def visitAssign(self, ast: Assign, o: Env):
        # Check if LHS is an Id and if it exists in the symbol table
        if isinstance(ast.lhs, Id):
            sym = next((j for i in o.sym for j in i if j.name == ast.lhs.name), None)
            if not sym:
                self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)
                return

        if isinstance(ast.lhs, (ArrayCell, FieldAccess)):
            # Visit LHS with isLeft = True
            lhs_code, lhs_type = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            # Visit RHS with isLeft = False
            rhs_code, rhs_type = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        else:
            # Visit RHS with isLeft = False
            rhs_code, rhs_type = self.visit(ast.rhs, Access(o.frame, o.sym, False))
            # Visit LHS with isLeft = True
            lhs_code, lhs_type = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        
        if type(lhs_type) is ArrayType and type(ast.rhs) is ArrayLiteral:
            if type(lhs_type.eleType) is FloatType and type(ast.rhs.eleType) is IntType:
                ast.rhs.eleType = FloatType()
                rhs_code, rhs_type = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        
        # Type conversion if necessary
        if isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
            rhs_code += self.emit.emitI2F(o.frame)
            
        # Check if LHS is interface type and RHS is class type
        if isinstance(lhs_type, Id) and isinstance(rhs_type, ClassType):
            interface_def = next((j for i in o.sym for j in i if j.name == lhs_type.name), None).mtype
            if type(interface_def) is InterfaceType:
                struct_def = next((j for i in o.sym for j in i if j.name == rhs_type.name), None).mtype
                struct_def.implements.append(ClassType(lhs_type.name))

        # Check if LHS is an array cell
        if isinstance(ast.lhs, ArrayCell):
            assign_code = lhs_code + rhs_code + self.emit.emitASTORE(lhs_type, o.frame)
            self.emit.printout(assign_code)
            return

        # Check if LHS is a field access
        if isinstance(ast.lhs, FieldAccess):
            recv_code, recv_type = self.visit(ast.lhs.receiver, Access(o.frame, o.sym, False))
            # Find the struct definition for the receiver type
            struct_def = next((j for i in o.sym for j in i if j.name == recv_type.name), None)
            # Get the field type from the struct definition
            field_type = next((ele[1] for ele in struct_def.mtype.elements if ele[0] == ast.lhs.field), None)
            if isinstance(field_type, Id):
                field_type = ClassType(field_type.name)

            # emit: receiver + rhs + putfield
            assign_code = recv_code + rhs_code + self.emit.emitPUTFIELD(f"{recv_type.name}/{ast.lhs.field}", field_type, o.frame)
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
            if type(o.frame.returnType) is ArrayType and type(ast.expr) is ArrayLiteral:
                if type(o.frame.returnType.eleType) is FloatType and type(ast.expr.eleType) is IntType:
                    ast.expr.eleType = FloatType()
            ec, et = self.visit(ast.expr, Access(o.frame, o.sym, False))
            if isinstance(et, IntType) and isinstance(o.frame.returnType, FloatType):
                ec += self.emit.emitI2F(o.frame)
                et = o.frame.returnType
            if isinstance(et, ClassType) and isinstance(o.frame.returnType, Id):
                interface_def = next((j for i in o.sym for j in i if j.name == o.frame.returnType.name), None).mtype
                if type(interface_def) is InterfaceType:
                    struct_def = next((j for i in o.sym for j in i if j.name == et.name), None).mtype
                    struct_def.implements.append(ClassType(o.frame.returnType.name))
            self.emit.printout(ec + self.emit.emitRETURN(et, o.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))

    def visitBinaryOp(self, ast: BinaryOp, o: Access):
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
            # Get labels for control flow
            label_short_circuit = o.frame.getNewLabel()  # Label for short-circuit result
            label_end = o.frame.getNewLabel()            # Label for end of expression

            if ast.op == '&&':
                # Short-circuit for &&: If left is false, skip right and return false
                code = lc  # Evaluate left operand
                code += self.emit.emitIFEQ(label_short_circuit, o.frame)  # If false, jump to short-circuit
                code += rc  # Evaluate right operand
                code += self.emit.emitGOTO(label_end, o.frame)  # Jump to end
                code += self.emit.emitLABEL(label_short_circuit, o.frame)  # Short-circuit: push false
                code += self.emit.emitPUSHCONST(0, BoolType(), o.frame)  # Push 0 (false)
                code += self.emit.emitLABEL(label_end, o.frame)  # End label
                return code, BoolType()

            if ast.op == '||':
                # Short-circuit for ||: If left is true, skip right and return true
                code = lc  # Evaluate left operand
                code += self.emit.emitIFNE(label_short_circuit, o.frame)  # If true, jump to short-circuit
                code += rc  # Evaluate right operand
                code += self.emit.emitGOTO(label_end, o.frame)  # Jump to end
                code += self.emit.emitLABEL(label_short_circuit, o.frame)  # Short-circuit: push true
                code += self.emit.emitPUSHCONST(1, BoolType(), o.frame)  # Push 1 (true)
                code += self.emit.emitLABEL(label_end, o.frame)  # End label
                return code, BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        ec, et = self.visit(ast.body, o)
        
        if ast.op == '-':
            if type(et) is IntType:
                return ec + self.emit.emitNEGOP(et, o.frame), IntType()
            if type(et) is FloatType:
                return ec + self.emit.emitNEGOP(et, o.frame), FloatType()
        
        if ast.op == '!':
            if type(et) is BoolType:
                return ec + self.emit.emitNOT(et, o.frame), BoolType()
    
    def visitFuncCall(self, ast: FuncCall, o: Env|Access):
        sym = next(filter(lambda x: x.name == ast.funName, o.sym[-1]), None)
        if type(o) is Env:
            for idx in range(len(ast.args)):
                arg, par_type = ast.args[idx], sym.mtype.partype[idx]
                if type(par_type) is ArrayType and type(arg) is ArrayLiteral:
                    if type(par_type.eleType) is FloatType and type(arg.eleType) is IntType:
                        arg.eleType = FloatType()
                arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym, False))
                if isinstance(arg_type, IntType) and isinstance(par_type, FloatType):
                    arg_code += self.emit.emitI2F(o.frame)
                if isinstance(arg_type, ClassType) and isinstance(par_type, Id):
                    interface_def = next((j for i in o.sym for j in i if j.name == par_type.name), None).mtype
                    if type(interface_def) is InterfaceType:
                        struct_def = next((j for i in o.sym for j in i if j.name == arg_type.name), None).mtype
                        struct_def.implements.append(ClassType(par_type.name))
                self.emit.printout(arg_code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o.frame))
        
        if type(o) is Access:
            code = ''
            for idx in range(len(ast.args)):
                arg, par_type = ast.args[idx], sym.mtype.partype[idx]
                if type(par_type) is ArrayType and type(arg) is ArrayLiteral:
                    if type(par_type.eleType) is FloatType and type(arg.eleType) is IntType:
                        arg.eleType = FloatType()
                arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym, False))
                if type(arg_type) is not type(par_type):
                    if isinstance(arg_type, IntType) and isinstance(par_type, FloatType):
                        arg_code += self.emit.emitI2F(o.frame)
                    if isinstance(arg_type, ClassType) and isinstance(par_type, Id):
                        interface_def = next((j for i in o.sym for j in i if j.name == par_type.name), None).mtype
                        if type(interface_def) is InterfaceType:
                            struct_def = next((j for i in o.sym for j in i if j.name == arg_type.name), None).mtype
                            struct_def.implements.append(ClassType(par_type.name))
                code += arg_code
            code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o.frame)
            return code, sym.mtype.rettype

    def visitMethCall(self, ast: MethCall, o: Env|Access):
        rec_code, rec_type = self.visit(ast.receiver, Access(o.frame, o.sym, False))
        typ: StructType|InterfaceType = next(filter(lambda x: x.name == rec_type.name, [j for i in o.sym for j in i]), None).mtype
        sym: Symbol = next(filter(lambda x: x.name == ast.metName, typ.methods), None)
        if type(typ) is InterfaceType:
            sym = Symbol(ast.metName, MType(sym.params, sym.retType), CName(typ.name))
        if type(o) is Env:
            self.emit.printout(rec_code)
            for idx in range(len(ast.args)):
                arg, par_type = ast.args[idx], sym.mtype.partype[idx]
                if type(par_type) is ArrayType and type(arg) is ArrayLiteral:
                    if type(par_type.eleType) is FloatType and type(arg.eleType) is IntType:
                        arg.eleType = FloatType()
                arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym, False))
                if type(arg_type) is not type(par_type):
                    if isinstance(arg_type, IntType) and isinstance(par_type, FloatType):
                        arg_code += self.emit.emitI2F(o.frame)
                    if isinstance(arg_type, ClassType) and isinstance(par_type, Id):
                        interface_def = next((j for i in o.sym for j in i if j.name == par_type.name), None).mtype
                        if type(interface_def) is InterfaceType:
                            struct_def = next((j for i in o.sym for j in i if j.name == arg_type.name), None).mtype
                            struct_def.implements.append(ClassType(par_type.name))
                self.emit.printout(arg_code)
            if type(typ) is StructType:
                self.emit.printout(self.emit.emitINVOKEVIRTUAL(f"{rec_type.name}/{ast.metName}", sym.mtype, o.frame))
            else:
                self.emit.printout(self.emit.emitINVOKEINTERFACE(f"{rec_type.name}/{ast.metName}", sym.mtype, o.frame))
        
        if type(o) is Access:
            code = rec_code
            for idx in range(len(ast.args)):
                arg, par_type = ast.args[idx], sym.mtype.partype[idx]
                if type(par_type) is ArrayType and type(arg) is ArrayLiteral:
                    if type(par_type.eleType) is FloatType and type(arg.eleType) is IntType:
                        arg.eleType = FloatType()
                arc_code, arc_type = self.visit(arg, Access(o.frame, o.sym, False))
                if type(arc_type) is not type(par_type):
                    if isinstance(arc_type, IntType) and isinstance(par_type, FloatType):
                        arc_code += self.emit.emitI2F(o.frame)
                    if isinstance(arc_type, ClassType) and isinstance(par_type, Id):
                        interface_def = next((j for i in o.sym for j in i if j.name == par_type.name), None).mtype
                        if type(interface_def) is InterfaceType:
                            struct_def = next((j for i in o.sym for j in i if j.name == arc_type.name), None).mtype
                            struct_def.implements.append(ClassType(par_type.name))
                code += arc_code
            if type(typ) is StructType:
                code += self.emit.emitINVOKEVIRTUAL(f"{rec_type.name}/{ast.metName}", sym.mtype, o.frame)
            else:
                code += self.emit.emitINVOKEINTERFACE(f"{rec_type.name}/{ast.metName}", sym.mtype, o.frame)
            return code, sym.mtype.rettype
    
    def visitId(self, ast: Id, o: Access):
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
            
            # If this is not the final dimension, we just want the subarray
            if i < len(ast.idx) - 1:
                # Emit AALOAD to get the subarray reference
                current_type = ArrayType(current_type.dimens[1:], current_type.eleType)
                code += self.emit.emitALOAD(current_type, o.frame)
            else:
                # Last dimension
                current_type = current_type.eleType if len(current_type.dimens) == 1 else ArrayType(current_type.dimens[1:], current_type.eleType)
                if o.isLeft:
                    # For assignment (left side), we don't need to do anything
                    pass
                else:
                    # Emit ALOAD to get the element value
                    code += self.emit.emitALOAD(current_type, o.frame)
        
        return code, current_type
    
    def visitFieldAccess(self, ast: FieldAccess, o: Access):
        code = ""
        recv_code, recv_type = self.visit(ast.receiver, Access(o.frame, o.sym, False))
        code += recv_code

        # Find the struct type from the receiver
        # If the receiver is a class type, find the corresponding struct type
        struct_type = None
        if isinstance(recv_type, (ClassType, Id)):
            struct_type = next(filter(lambda x: x.name == recv_type.name, [j for i in o.sym for j in i]), None).mtype
        elif isinstance(recv_type, StructType):
            struct_type = recv_type

        # Find the field type from the struct type
        field_info = next(filter(lambda x: x[0] == ast.field, struct_type.elements), None)
        field_type = field_info[1]

        if type(field_type) is Id:
            field_type = ClassType(field_type.name)

        # If the field is a static field, emit GETSTATIC
        if not o.isLeft:
            code += self.emit.emitGETFIELD(f"{struct_type.name}/{ast.field}", field_type, o.frame)

        return code, field_type
    
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
        array_type = ArrayType(ast.dimens, ClassType(ast.eleType.name) if isinstance(ast.eleType, Id) else ast.eleType)

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
                val_code, val_type = self.visit(val, o)
                if type(array_type.eleType) is not type(val_type):
                    if isinstance(array_type.eleType, FloatType) and isinstance(val_type, IntType):
                        val_code += self.emit.emitI2F(o.frame)
                    if isinstance(array_type.eleType, Id) and isinstance(val_type, ClassType):
                        interface_def = next((j for i in o.sym for j in i if j.name == array_type.eleType.name), None).mtype
                        if type(interface_def) is InterfaceType:
                            struct_def = next((j for i in o.sym for j in i if j.name == val_type.name), None).mtype
                            struct_def.implements.append(ClassType(val_type.name))
                code += val_code
                # emitIASTORE
                code += self.emit.emitASTORE(array_type.eleType, o.frame)
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

    def visitStructLiteral(self, ast: StructLiteral, o: Access):
        sym: Symbol = next(filter(lambda x: x.name == ast.name, [j for i in o.sym for j in i]), None)
        context = ast.name
        code = self.emit.emitNEW(context, o.frame) + self.emit.emitDUP(o.frame)
        for param in sym.mtype.elements:
            arg = next(filter(lambda ele: ele[0] == param[0], ast.elements), None)
            if arg: 
                if type(param[1]) is ArrayType and type(arg[1]) is ArrayLiteral:
                    if type(param[1].eleType) is FloatType and type(arg[1].eleType) is IntType:
                        arg[1].eleType = FloatType()
                arg_code, arg_type = self.visit(arg[1], o)
                if isinstance(param[1], FloatType) and isinstance(arg_type, IntType):
                    arg_code += self.emit.emitI2F(o.frame)
                    arg_type = param[1]
                if type(param[1]) is Id and type(arg_type) is ClassType:
                    interface_def = next((j for i in o.sym for j in i if j.name == param[1].name), None).mtype
                    if type(interface_def) is InterfaceType:
                        struct_def = next((j for i in o.sym for j in i if j.name == arg_type.name), None).mtype
                        struct_def.implements.append(ClassType(param[1].name))
                        arg_type = param[1]
                code += arg_code
            else: code += self.setDefaultValue(param[1], o)
        
        code += self.emit.emitINVOKESPECIAL(
            o.frame, f'{context}/<init>', 
            MType(list(map(lambda ele: ele[1] if type(ele[1]) is not Id else ClassType(ele[1].name), sym.mtype.elements)), VoidType())
        )
        
        return code, ClassType(context)

    def visitNilLiteral(self, ast: NilLiteral, o: Access):
        return self.emit.emitPUSHNULL(o.frame), None