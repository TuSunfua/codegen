# 2213841
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class Value: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name: str = name
        self.mtype: MType = mtype
        self.value: Value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    
class Tools:
    
    def exist(lst, checker):
        for item in lst:
            if isinstance(item, list):
                for x in item:
                    if checker(x): return True
            elif checker(item): return True
        
        return False
    
    def find(lst, checker):
        for item in lst:
            if isinstance(item, list):
                for x in item:
                    if checker(x): return x
            elif checker(item): return item
        
        return None
    
    def check_type_assign(lhs, rhs): # type casting
        if type(lhs) is Id and type(rhs) is Id: return lhs.name == rhs.name
        
        if type(lhs) is InterfaceType and type(rhs) is StructType:
            return Tools.is_implemented(lhs, rhs)
        
        if type(lhs) is FloatType and type(rhs) is IntType:
            return True
            
        if type(lhs) is not type(rhs):
            return False
        
        if type(lhs) is StructType:
            return Tools.are_structs_compatible(lhs, rhs)
            
        if type(lhs) is InterfaceType:
            return Tools.are_interfaces_compatible(lhs, rhs)
            
        if type(lhs) is ArrayType:
            if (len(lhs.dimens) != len(rhs.dimens)):
                return False
            
            if not all(lhs.dimens[i] == rhs.dimens[i] for i in range(len(lhs.dimens))):
                return False
            
            if type(lhs.eleType) is FloatType and type(rhs.eleType) is IntType:
                return True
            
            if type(lhs.eleType) is not type(rhs.eleType):
                return False
            
            if type(lhs.eleType) is StructType:
                return Tools.are_structs_compatible(lhs.eleType, rhs.eleType)
            
            if type(lhs.eleType) is InterfaceType:
                return Tools.are_interfaces_compatible(lhs.eleType, rhs.eleType)
            
        return True
    
    def check_type(recv, value): # Exact same type
        if type(recv) is Id and type(value) is Id: return recv.name == value.name
        
        if type(recv) is not type(value):
            return False
        
        if type(recv) is StructType:
            return Tools.are_structs_compatible(recv, value)
            
        if type(recv) is InterfaceType:
            return Tools.are_interfaces_compatible(recv, value)
        
        if type(recv) is ArrayType:
            if (len(recv.dimens) != len(value.dimens)):
                return False
            
            if not all(recv.dimens[i] == value.dimens[i] for i in range(len(recv.dimens))):
                return False
            
            return Tools.check_type(recv.eleType, value.eleType)
        
        return True
    
    def are_structs_compatible(struct1, struct2):
        return struct1.name == struct2.name and \
            type(struct1) is StructType and type(struct2) is StructType
    
    def are_interfaces_compatible(interface1, interface2):
        return interface1.name == interface2.name \
            and type(interface1) is InterfaceType and type(interface2) is InterfaceType
    
    def is_implemented(interface, struct):
        for prototype in interface.methods:
            method = Tools.find(struct.methods, lambda x: x.name == prototype.name)
            if method is None:
                return False
            
            # Check return type
            if not Tools.check_type(prototype.retType, method.mtype.retType):
                return False
            
            # Check parameter types
            if len(prototype.params) != len(method.mtype.params):
                return False
            
            for param, arg in zip(prototype.params, method.mtype.params):
                if not Tools.check_type(param, arg.parType):
                    return False
            
        return True    

class StaticChecker(BaseVisitor,Utils):
        
    def __init__(self,ast):
        self.ast = ast
        self.ret = None
        self.evaluator = StaticEvaluator()
        self.global_decl = []
        self.global_envi = [ 
            [
                Symbol("getInt",      FuncDecl("getInt",      [],                             IntType(),    Block([]))),
                Symbol("putInt",      FuncDecl("putInt",      [ParamDecl("a", IntType())],    VoidType(),   Block([]))),
                Symbol("putIntLn",    FuncDecl("putIntLn",    [ParamDecl("a", IntType())],    VoidType(),   Block([]))),
                Symbol("getFloat",    FuncDecl("getFloat",    [],                             FloatType(),  Block([]))),
                Symbol("putFloat",    FuncDecl("putFloat",    [ParamDecl("a", FloatType())],  VoidType(),   Block([]))),
                Symbol("putFloatLn",  FuncDecl("putFloatLn",  [ParamDecl("a", FloatType())],  VoidType(),   Block([]))),
                Symbol("getBool",     FuncDecl("getBool",     [],                             BoolType(),   Block([]))),
                Symbol("putBool",     FuncDecl("putBool",     [ParamDecl("a", BoolType())],   VoidType(),   Block([]))),
                Symbol("putBoolLn",   FuncDecl("putBoolLn",   [ParamDecl("a", BoolType())],   VoidType(),   Block([]))),
                Symbol("getString",   FuncDecl("getString",   [],                             StringType(), Block([]))),
                Symbol("putString",   FuncDecl("putString",   [ParamDecl("a", StringType())], VoidType(),   Block([]))),
                Symbol("putStringLn", FuncDecl("putStringLn", [ParamDecl("a", StringType())], VoidType(),   Block([]))),
                Symbol("putLn",       FuncDecl("putLn",       [],                             VoidType(),   Block([]))),
            ]                    
        ]
    
    def check(self):
        return self.visit(self.ast, self.global_envi)
    
    def infer(self, lst, checker, typ=None): 
        for item in lst:
            if isinstance(item, list):
                for x in item:
                    if checker(x):
                        if typ is not None: x.mtype = typ
                        return x.mtype
            elif checker(item):
                if typ is not None: item.mtype = typ
                return item.mtype   
        
        if self.global_decl is not None:
            for item in self.global_decl:
                if checker(item):
                    if typ is not None: item.mtype = typ
                    return item.mtype
        
        return None
    
    # decl : List[Decl]
    def visitProgram(self, ast:Program, c):
        # Pre-pass
        self.global_decl = []
        methods = []
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                if Tools.exist(self.global_decl, lambda x: x.name == decl.name):
                    raise Redeclared(Function(), decl.name)
                self.global_decl += [Symbol(decl.name, decl)]
                
            elif type(decl) is MethodDecl:
                if Tools.exist(self.global_decl, lambda x: x.name == decl.fun.name):
                    raise Redeclared(Function(), decl.fun.name)
                methods += [decl]
                
            elif type(decl) is StructType:
                if Tools.exist(self.global_decl, lambda x: x.name == decl.name):
                    raise Redeclared(Type(), decl.name)
                self.global_decl += [Symbol(decl.name, decl)]
                
            elif type(decl) is InterfaceType:
                if Tools.exist(self.global_decl, lambda x: x.name == decl.name):
                    raise Redeclared(Type(), decl.name)
                self.global_decl += [Symbol(decl.name, decl)]
                
        # Mid-pass
        for method in methods:
            if type(method.recType) is Id:
                struct = self.infer(c, lambda x: isinstance(x.mtype, StructType) and x.name == method.recType.name)
                if struct is None: continue
            struct.methods += [Symbol(method.fun.name, method.fun)]
        
        # Main-pass
        for decl in ast.decl:
            self.visit(decl, c)   
            
        return c
            
    # varName : str
    # varType : Type # None if there is no type
    # varInit : Expr # None if there is no initialization
    def visitVarDecl(self, ast:VarDecl, c):
        if Tools.exist(c[0], lambda x: x.name == ast.varName):
            raise Redeclared(Variable(), ast.varName)
        
        mtype = None
        if ast.varType is not None:
            # varType could be StructType or InterfaceType
            if type(ast.varType) is Id:
                mtype = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == ast.varType.name)
                if mtype is None:
                    raise Undeclared(Identifier(), ast.varType.name)
            else:
                mtype = self.visit(ast.varType, c)
        
        if ast.varInit is not None:
            exp = self.visit(ast.varInit, c)
        
            if type(exp) is VoidType:
                raise TypeMismatch(ast)
        
            if mtype is None:
                mtype = exp
                
            # Checking
            if not Tools.check_type_assign(mtype, exp):
                raise TypeMismatch(ast)
                
        try: value = self.evaluator.visit(ast.varInit, c)
        except: value = None
        symbol = Symbol(ast.varName, VarDecl(ast.varName, mtype, ast.varInit), value)
        c[0] += [symbol]

    # conName : str
    # conType : Type # None if there is no type 
    # iniExpr : Expr
    def visitConstDecl(self, ast:ConstDecl, c):
        if Tools.exist(c[0], lambda x: x.name == ast.conName):
            raise Redeclared(Constant(), ast.conName)
        
        exp = self.visit(ast.iniExpr, c)
        if type(exp) is VoidType:
            raise TypeMismatch(ast)
        
        mtype = exp
        
        try: value = self.evaluator.visit(ast.iniExpr, c)
        except: value = None
        symbol = Symbol(ast.conName, ConstDecl(ast.conName, mtype, ast.iniExpr), value)
        c[0] += [symbol]
   
    # name: str
    # params: List[ParamDecl]
    # retType: Type # VoidType if there is no return type
    # body: Block
    def visitFuncDecl(self, ast:FuncDecl, c):
        # Check function name
        if Tools.exist(c[0], lambda x: x.name == ast.name):
            raise Redeclared(Function(), ast.name)
        
        # Check parameter types
        env = [[]] + c
        for param in ast.params:
            if Tools.exist(env[0], lambda x: x.name == param.parName):
                raise Redeclared(Parameter(), param.parName)
            
            if type(param.parType) is Id:
                parType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.parType.name)
                if parType is None:
                    raise Undeclared(Identifier(), param.parType.name)
            else:
                parType = self.visit(param.parType, c)
                
            env[0] += [Symbol(param.parName, VarDecl(param.parName, parType, None))]
          
        # Check return type  
        if type(ast.retType) is Id:
            retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == ast.retType.name)
            if retType is None:
                raise Undeclared(Identifier(), ast.retType.name)
        else:
            retType = self.visit(ast.retType, c)
                    
        # Check body
        self.ret = retType
        self.visit(ast.body, [[]] + env)
        self.ret = None
        
        # Update env
        symbol = Symbol(ast.name, FuncDecl(ast.name, ast.params, ast.retType, Block([])))
        c[0] += [symbol]

    # receiver: str
    # recType: Type 
    # fun: FuncDecl
    def visitMethodDecl(self, ast:MethodDecl, c):
        # Check receiver types
        if type(ast.recType) is Id:
            struct = self.infer(c, lambda x: isinstance(x.mtype, StructType) and x.name == ast.recType.name)
            if struct is None:
                raise Undeclared(Identifier(), ast.recType.name)
        else:
            raise TypeMismatch(ast)
            
        env = [[]] + [[Symbol(ast.receiver, VarDecl(ast.receiver, struct, None))]] + c
            
        # Check method name
        for field in struct.elements:
            if field[0] == ast.fun.name:
                raise Redeclared(Method(), ast.fun.name)
        foundMethod = False
        for method in struct.methods:
            if method.name == ast.fun.name:
                if foundMethod:
                    raise Redeclared(Method(), ast.fun.name)
                foundMethod = True
                method.value = True
                    
        # Check parameter types
        for param in ast.fun.params:
            if Tools.exist(env[0], lambda x: x.name == param.parName):
                raise Redeclared(Parameter(), param.parName)
            
            if type(param.parType) is Id:
                parType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.parType.name)
                if parType is None:
                    raise Undeclared(Identifier(), param.parType.name)
            else:
                parType = self.visit(param.parType, c)
                
            env[0] += [Symbol(param.parName, VarDecl(param.parName, parType, None))]
            
        # Check return type
        if type(ast.fun.retType) is Id:
            retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == ast.fun.retType.name)
            if retType is None:
                raise Undeclared(Identifier(), ast.fun.retType.name)
        else:
            retType = self.visit(ast.fun.retType, c)
            
        # Check body
        self.ret = retType
        self.visit(ast.fun.body, [[]] + env)
        self.ret = None
    
    def visitIntType(self, ast, c):
        return IntType()
    
    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    # dimens:List[Expr]
    # eleType:Type
    def visitArrayType(self, ast:ArrayType, c):
        if type(ast.eleType) is Id:
            eleType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == ast.eleType.name)
            if eleType is None:
                raise Undeclared(Identifier(), ast.eleType.name)
        else:
            eleType = self.visit(ast.eleType, c)
                
        dimens = []
        for dim in ast.dimens:
            exp = self.visit(dim, c)
            if type(exp) is not IntType:
                raise TypeMismatch(ast)
        
            try: value = self.evaluator.visit(dim, c)
            except: value = 0
            dimens.append(value)
            
        return ArrayType(dimens, eleType)
    
    # name: str
    # elements:List[Tuple[str,Type]]
    # methods:List[MethodDecl]
    def visitStructType(self, ast:StructType, c):
        if Tools.exist(c[0], lambda x: x.name == ast.name):
            raise Redeclared(Type(), ast.name)
                
        elements = []
        for element in ast.elements:
            if Tools.exist(elements, lambda x: x.name == element[0]):
                raise Redeclared(Field(), element[0])
            
            if type(element[1]) is Id:
                eleType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == element[1].name)
                if eleType is None:
                    raise Undeclared(Identifier(), element[1].name)
            else:
                eleType = self.visit(element[1], c)
                
            elements += [Symbol(element[0], eleType)]
            
        # Update env
        symbol = Symbol(ast.name, StructType(ast.name, ast.elements, ast.methods))
        c[0] += [symbol]

    # name: str
    # methods:List[Prototype]
    def visitInterfaceType(self, ast:InterfaceType, c):
        if Tools.exist(c[0], lambda x: x.name == ast.name):
            raise Redeclared(Type(), ast.name)
        
        methods = []
        for method in ast.methods:
            if Tools.exist(methods, lambda x: x.name == method.name):
                raise Redeclared(Prototype(), method.name)
            
            params = []
            for param in method.params:
                if type(param) is Id:
                    paramType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.name)
                    if paramType is None:
                        raise Undeclared(Identifier(), param.name)
                else:
                    paramType = self.visit(param, c)
                    
                params += [Symbol("a", VarDecl("a", paramType, None))]
            
            if type(method.retType) is Id:
                retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == method.retType.name)
                if retType is None:
                    raise Undeclared(Identifier(), method.retType.name)
            else:
                retType = self.visit(method.retType, c)
                
            methods += [Symbol(method.name, FuncDecl(method.name, params, retType, Block([])))]
        
        # Update env
        symbol = Symbol(ast.name, InterfaceType(ast.name, ast.methods))
        c[0] += [symbol]
    
    # member:List[BlockMember]
    def visitBlock(self, ast:Block, c):
        for member in ast.member:
            if isinstance(member, (FuncCall, MethCall)):
                typ = self.visit(member, c)
                if type(typ) is not VoidType:
                    raise TypeMismatch(member)
            elif type(member) is Block:
                self.visit(member, [[]] + c)
            else: self.visit(member, c)
 
    # lhs: LHS
    # rhs: Expr # if assign operator is +=, rhs is BinaryOp(+,lhs,rhs), similar to -=,*=,/=,%=
    def visitAssign(self, ast:Assign, c):
        rhs = self.visit(ast.rhs, c)
        try: r_val = self.evaluator.visit(ast.rhs, c)
        except: r_val = None
        
        if type(rhs) is VoidType:
            raise TypeMismatch(ast)
        
        try:
            lhs = self.visit(ast.lhs, c)
        except Undeclared as e:
            if type(ast.lhs) is not Id: raise e
            c[0] += [Symbol(ast.lhs.name, VarDecl(ast.lhs.name, rhs, None), r_val)]
            return
            
        # Checking
        if type(lhs) is VoidType:
            raise TypeMismatch(ast)
        
        if not Tools.check_type_assign(lhs, rhs):
            raise TypeMismatch(ast)
            
        # Update value
        if type(ast.lhs) is Id:
            identifier = Tools.find(c, lambda x: isinstance(x.mtype, VarDecl) and x.name == ast.lhs.name)
            identifier.value = r_val
            
        return lhs
   
    # expr:Expr
    # thenStmt:Stmt
    # elseStmt:Stmt # None if there is no else
    def visitIf(self, ast:If, c):
        expr = self.visit(ast.expr, c) 
        if type(expr) is not BoolType:
            raise TypeMismatch(ast)
        
        self.visit(ast.thenStmt, [[]] + c)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [[]] + c)
    
    # cond:Expr
    # loop:Block
    def visitForBasic(self, ast:ForBasic, c):
        cond = self.visit(ast.cond, c)
        if type(cond) is not BoolType:
            raise TypeMismatch(ast)
        
        self.visit(ast.loop, [[]] + c)
    
    # init:Stmt
    # cond:Expr
    # upda:Assign
    # loop:Block
    def visitForStep(self, ast:ForStep, c):
        env = [[]] + c
        self.visit(ast.init, env)
        cond = self.visit(ast.cond, env)
        if type(cond) is not BoolType:
            raise TypeMismatch(ast)
        
        self.visit(ast.upda, env)
        self.visit(ast.loop, env)

    # idx: Id
    # value: Id
    # arr: Expr
    # loop:Block
    def visitForEach(self, ast:ForEach, c):
        arr = self.visit(ast.arr, c)
        if type(arr) is not ArrayType:
            raise TypeMismatch(ast)
        
        idx = self.visit(ast.idx, c)
        if type(idx) is not IntType:
            raise TypeMismatch(ast)
        
        val = self.visit(ast.value, c)
        if len(arr.dimens) == 1: arr = arr.eleType
        else: arr = ArrayType(arr.dimens[1:], arr.eleType)
        
        if type(arr) is Id:
            if not Tools.check_type(arr, val):
                raise TypeMismatch(ast)
        if type(arr) is not type(val):
            if not Tools.check_type(arr, val):
                raise TypeMismatch(ast)
            
        if ast.idx.name == ast.value.name:
            raise Redeclared(Variable(), ast.value.name)
        
        self.visit(ast.loop, [[]] + c)

    def visitContinue(self, ast, c):
        return None
    
    def visitBreak(self, ast, c):
        return None
    
    # expr:Expr # None if there is no expr
    def visitReturn(self, ast:Return, c):
        if ast.expr is None:
            if self.ret is not None and type(self.ret) is not VoidType:
                raise TypeMismatch(ast)
            return None
        
        if self.ret is None:
            raise TypeMismatch(ast)
        
        expr = self.visit(ast.expr, c)   
        if type(expr) is VoidType:
            raise TypeMismatch(ast)
        
        if not Tools.check_type(self.ret, expr):
            raise TypeMismatch(ast)
        
        return expr

    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast:BinaryOp, c):
        ltype = self.visit(ast.left, c)
        rtype = self.visit(ast.right, c)
        
        if type(ltype) is VoidType or type(rtype) is VoidType:
            raise TypeMismatch(ast)
        
        if ast.op == '+':
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            
            if type(ltype) is IntType and type(rtype) is FloatType:
                return FloatType()
            if type(ltype) is FloatType and type(rtype) is IntType:
                return FloatType()
            
            if type(ltype) is IntType and type(rtype) is IntType:
                return IntType()
            if type(ltype) is FloatType and type(rtype) is FloatType:
                return FloatType()
            
            raise TypeMismatch(ast)
        
        if ast.op in ['-', '*', '/']:
            if type(ltype) is IntType and type(rtype) is IntType:
                return IntType()
            if type(ltype) is FloatType and type(rtype) is FloatType:
                return FloatType()
            
            if type(ltype) is IntType and type(rtype) is FloatType:
                return FloatType()
            if type(ltype) is FloatType and type(rtype) is IntType:
                return FloatType()
            
            raise TypeMismatch(ast)
        
        if ast.op == '%':
            if type(ltype) is IntType and type(rtype) is IntType:
                return IntType()
            
            raise TypeMismatch(ast)
        
        if ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(ltype) is IntType and type(rtype) is IntType:
                return BoolType()
            if type(ltype) is FloatType and type(rtype) is FloatType:
                return BoolType()
            if type(ltype) is StringType and type(rtype) is StringType:
                return BoolType()
            
            raise TypeMismatch(ast)

        if ast.op in ['&&', '||']:
            if type(ltype) is BoolType and type(rtype) is BoolType:
                return BoolType()
            
            raise TypeMismatch(ast)
    
    # op:str
    # body:Expr
    def visitUnaryOp(self, ast:UnaryOp, c):
        body = self.visit(ast.body, c)
        
        if type(body) is VoidType:
            raise TypeMismatch(ast)
        
        if ast.op == '-':
            if type(body) is IntType:
                return IntType()
            if type(body) is FloatType:
                return FloatType()
            
            raise TypeMismatch(ast)
        
        if ast.op == '!':
            if type(body) is BoolType:
                return BoolType()
            
            raise TypeMismatch(ast)
    
    # funName:str
    # args:List[Expr] # [] if there is no arg 
    def visitFuncCall(self, ast:FuncCall, c):
        func = self.infer(c, lambda x: x.name == ast.funName)
        if func is None:
            raise Undeclared(Function(), ast.funName)
        
        if type(func) is not FuncDecl:
            raise Undeclared(Function(), ast.funName)
        
        if len(func.params) != len(ast.args):
            raise TypeMismatch(ast)
        
        for param, arg in zip(func.params, ast.args):
            if isinstance(param.parType, (Id, StructType, InterfaceType)):
                paramType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.parType.name)
                if paramType is None:
                    raise Undeclared(Identifier(), param.parType.name)
            else:
                paramType = self.visit(param.parType, c)
            
            argType = self.visit(arg, c)
                
            # Checking
            if not Tools.check_type(paramType, argType):
                raise TypeMismatch(ast)
                
        if type(func.retType) is Id:
            retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == func.retType.name)
            if func.retType is None:
                raise Undeclared(Identifier(), func.retType.name)
        else:
            retType = self.visit(func.retType, c)
        return retType

    # receiver: Expr
    # metName: str
    # args:List[Expr]
    def visitMethCall(self, ast:MethCall, c):
        receiver = self.visit(ast.receiver, c)
        
        if not isinstance(receiver, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        
        if type(receiver) is StructType:
            method = Tools.find(receiver.methods, lambda x: x.name == ast.metName)
            if method is None:
                raise Undeclared(Method(), ast.metName)
            
            if len(method.mtype.params) != len(ast.args):
                raise TypeMismatch(ast)
            
            for param, arg in zip(method.mtype.params, ast.args):
                if isinstance(param.parType, (Id, StructType, InterfaceType)):
                    paramType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.parType.name)
                    if paramType is None:
                        raise Undeclared(Identifier(), param.parType.name)
                else:
                    paramType = self.visit(param.parType, c)
                
                argType = self.visit(arg, c)
                    
                # Checking
                if not Tools.check_type(paramType, argType):
                    raise TypeMismatch(ast)
                    
            if type(method.mtype.retType) is Id:
                retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == method.mtype.retType.name)
                if retType is None:
                    raise Undeclared(Identifier(), method.mtype.retType.name)
            else:
                retType = self.visit(method.mtype.retType, c)
            return retType
        
        # Interface type
        method = Tools.find(receiver.methods, lambda x: x.name == ast.metName)
        if method is None:
            raise Undeclared(Method(), ast.metName)
        
        if len(method.params) != len(ast.args):
            raise TypeMismatch(ast)
        
        for param, arg in zip(method.params, ast.args):
            if isinstance(param, (Id, StructType, InterfaceType)):
                paramType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == param.name)
                if paramType is None:
                    raise Undeclared(Identifier(), param.name)
            else:
                paramType = self.visit(param, c)
            
            argType = self.visit(arg, c)
                
            # Checking
            if not Tools.check_type(paramType, argType):
                raise TypeMismatch(ast)
            
        if type(method.retType) is Id:
            retType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == method.retType.name)
            if retType is None:
                raise Undeclared(Identifier(), method.retType.name)
        else:
            retType = self.visit(method.retType, c)
        return retType
    
    def visitId(self, ast, c):
        identifier = Tools.find(c, lambda x: isinstance(x.mtype, (VarDecl, ConstDecl)) and x.name == ast.name)
        if identifier is not None:
            if type(identifier.mtype) is VarDecl:
                return identifier.mtype.varType
            if type(identifier.mtype) is ConstDecl:
                return identifier.mtype.conType
                
        raise Undeclared(Identifier(), ast.name)
    
    # arr:Expr
    # idx:List[Expr]
    def visitArrayCell(self, ast:ArrayCell, c):
        arr = self.visit(ast.arr, c)
        if type(arr) is not ArrayType:
            raise TypeMismatch(ast)
        
        list_idx = []
        for idx in ast.idx:
            exp = self.visit(idx, c)
            if type(exp) is not IntType:
                raise TypeMismatch(ast)
            
            try: value = self.evaluator.visit(idx, c)
            except: value = 0
            list_idx.append(value)
        
        dims = arr.dimens[:]  
        access = len(list_idx)
        if access > len(dims):
            raise TypeMismatch(ast)

        if access == len(dims): return arr.eleType
        return ArrayType(dims[access:], arr.eleType)
    
    # receiver:Expr
    # field:str
    def visitFieldAccess(self, ast:FieldAccess, c):
        receiver = self.visit(ast.receiver, c)
        if type(receiver) is not StructType:
            raise TypeMismatch(ast)
        
        field = Tools.find(receiver.elements, lambda x: x[0] == ast.field)
        if field is None:
            raise Undeclared(Field(), ast.field)
        
        if type(field[1]) is Id:
            fieldType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == field[1].name)
            if fieldType is None:
                raise Undeclared(Identifier(), field[1].name)
        else:
            fieldType = self.visit(field[1], c)
        return fieldType
    
    def visitIntLiteral(self, ast, c):
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    # dimens:List[Expr]
    # eleType: Type
    # value: NestedList
    def visitArrayLiteral(self, ast:ArrayLiteral, c):
        if type(ast.eleType) is Id:
            eleType = self.infer(c, lambda x: isinstance(x.mtype, (StructType, InterfaceType)) and x.name == ast.eleType.name)
            if eleType is None:
                raise Undeclared(Identifier(), ast.eleType.name)
        else:
            eleType = self.visit(ast.eleType, c)
        
        dims = []
        for dim in ast.dimens:
            exp = self.visit(dim, c)
            if not isinstance(exp, IntType):
                raise TypeMismatch(ast)
            
            try: value = self.evaluator.visit(dim, c)
            except: value = 0
            dims.append(value)
        
        return ArrayType(dims, eleType)

    # name:str
    # elements: List[Tuple[str,Expr]] # [] if there is no elements
    def visitStructLiteral(self, ast:StructLiteral, c):
        struct = self.infer(c, lambda x: isinstance(x.mtype, StructType) and x.name == ast.name)
        if struct is None:
            raise Undeclared(Identifier(), ast.name)
        
        for element in ast.elements:
            fieldName = element[0]
            fieldType = self.visit(element[1], c)
                
            existField = Tools.find(struct.elements, lambda x: x[0] == fieldName)
            if existField is None:
                raise Undeclared(Field(), fieldName)
            existFieldType = self.visit(existField[1], c)

            # Checking
            if not Tools.check_type(existFieldType, fieldType):
                raise TypeMismatch(ast)
        
        # if len(ast.elements) != len(struct.mtype.elements) and len(ast.elements):
        #     raise TypeMismatch(ast)
        
        return struct

    def visitNilLiteral(self, ast, c):
        return NilLiteral()
    
class StaticEvaluator(BaseVisitor):
    
    def visitBinaryOp(self, ast:BinaryOp, c):
        l_val = self.visit(ast.left, c)
        r_val = self.visit(ast.right, c)
        if ast.op == "&&":
            return l_val and r_val
        if ast.op == "||":
            return l_val or r_val
        res = eval(f"{l_val} {ast.op} {r_val}")
        if ast.op == '/' and isinstance(l_val, int) and isinstance(r_val, int):
            return int(res)
        return res
    
    def visitUnaryOp(self, ast:UnaryOp, c):
        val = self.visit(ast.body, c)
        if ast.op == "!":
            return not val
        return eval(f"{ast.op}{val}")
    
    def visitId(self, ast:Id, c):
        identifier = Tools.find(c, lambda x: isinstance(x.mtype, (VarDecl, ConstDecl)) and x.name == ast.name)
        if identifier is not None: return identifier.value
        return None
    
    def visitIntLiteral(self, ast:IntLiteral, c):
        if isinstance(ast.value, int): return ast.value
        return int(ast.value, 0)
    
    def visitFloatLiteral(self, ast:FloatLiteral, c):
        if isinstance(ast.value, float): return ast.value
        return float(ast.value)
    
    def visitBooleanLiteral(self, ast:BooleanLiteral, c):
        if ast.value == "true": return True
        if ast.value == "false": return False
        return ast.value
    
    def visitStringLiteral(self, ast:StringLiteral, c):
        return ast.value
    
    def visitNilLiteral(self, ast:NilLiteral, c):
        return None