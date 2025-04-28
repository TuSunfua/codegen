from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # program: decl_list EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))


    # decl_list: decl decl_list | decl;
    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        if ctx.decl_list():
            return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
        else:
            return [self.visit(ctx.decl())]


    # decl: var_decl eos | const_decl eos | struct_decl eos | interface_decl eos | func_decl eos | method_decl eos;
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        elif ctx.interface_decl():
            return self.visit(ctx.interface_decl())
        elif ctx.func_decl():
            return self.visit(ctx.func_decl())
        elif ctx.method_decl():
            return self.visit(ctx.method_decl())


    # var_decl
    #     : VAR ID data_type
    #     | var_decl_with_initialization
    #     ;
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        if ctx.ID():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.data_type()), None)
        else:
            return self.visit(ctx.var_decl_with_initialization())


    # var_decl_with_initialization
    #     : VAR ID data_type ASSIGN expr
    #     | VAR ID ASSIGN expr
    #     ;
    def visitVar_decl_with_initialization(self, ctx:MiniGoParser.Var_decl_with_initializationContext):
        if ctx.data_type():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.data_type()), self.visit(ctx.expr()))
        else:
            return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))


    # const_decl
    #     : CONST ID ASSIGN expr
    #     ;
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))


    # struct_decl
    #     : TYPE ID STRUCT L_CURLY struct_fields R_CURLY
    #     ;
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.struct_fields()), [])


    # struct_fields
    #     : struct_field struct_fields | struct_field;
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        if ctx.struct_fields():
            return [self.visit(ctx.struct_field())] + self.visit(ctx.struct_fields())
        else:
            return [self.visit(ctx.struct_field())]


    # struct_field
    #     : ID data_type eos
    #     ;
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return (ctx.ID().getText(), self.visit(ctx.data_type()))


    # interface_decl
    #     : TYPE ID INTERFACE L_CURLY interface_methods R_CURLY
    #     ;
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.interface_methods()))


    # interface_methods
    #     : interface_method interface_methods | interface_method;
    def visitInterface_methods(self, ctx:MiniGoParser.Interface_methodsContext):
        if ctx.interface_methods():
            return [self.visit(ctx.interface_method())] + self.visit(ctx.interface_methods())
        else:    
            return [self.visit(ctx.interface_method())]


    # interface_method
    #     : ID L_PAREN params_list R_PAREN (data_type | ) eos
    #     ;
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        param_list = self.visit(ctx.params_list())
        data_type = [x.parType for x in param_list]
        return Prototype(ctx.ID().getText(), data_type, self.visit(ctx.data_type()) if ctx.data_type() else VoidType())


    # params_list
    #     : params_list_prime | ;
    def visitParams_list(self, ctx:MiniGoParser.Params_listContext):
        if ctx.params_list_prime():
            return self.visit(ctx.params_list_prime())
        else:
            return []


    # params_list_prime
    #     : id_list_cm data_type COMMA params_list_prime | id_list_cm data_type;
    def visitParams_list_prime(self, ctx:MiniGoParser.Params_list_primeContext):
        if ctx.params_list_prime():
            return [ParamDecl(x, self.visit(ctx.data_type())) for x in self.visit(ctx.id_list_cm())] + self.visit(ctx.params_list_prime())
        else:
            return [ParamDecl(x, self.visit(ctx.data_type())) for x in self.visit(ctx.id_list_cm())]


    # func_decl
    #     : FUNC ID L_PAREN params_list R_PAREN (data_type | ) block_stmt
    #     ;
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return FuncDecl(ctx.ID().getText(), self.visit(ctx.params_list()), self.visit(ctx.data_type()) if ctx.data_type() else VoidType(), self.visit(ctx.block_stmt()))


    # method_decl
    #     : FUNC L_PAREN ID ID R_PAREN ID L_PAREN params_list R_PAREN (data_type | ) block_stmt
    #     ;
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        funcDecl = FuncDecl(ctx.ID(2).getText(), self.visit(ctx.params_list()), self.visit(ctx.data_type()) if ctx.data_type() else VoidType(), self.visit(ctx.block_stmt()))
        return MethodDecl(ctx.ID(0).getText(), Id(ctx.ID(1).getText()), funcDecl)


    # block_stmt
    #     : L_CURLY stmt_list R_CURLY
    #     ;
    def visitBlock_stmt(self, ctx:MiniGoParser.Block_stmtContext):
        return Block(self.visit(ctx.stmt_list()))


    # stmt_list
    #     : stmt stmt_list | stmt;
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        if ctx.stmt_list():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list())
        else:
            return [self.visit(ctx.stmt())]


    # stmt
    #     : var_decl eos
    #     | const_decl eos
    #     | block_stmt eos
    #     | call eos
    #     | list_ac DOT call eos
    #     | assign_stmt eos
    #     | branch_stmt eos
    #     | for_stmt eos
    #     | CONTINUE eos
    #     | BREAK eos
    #     | RETURN (expr | ) eos
    #     ;
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.list_ac():
            receiver = self.visit(ctx.list_ac())
            name, params = self.visit(ctx.call())
            return MethCall(receiver, name, params)
        elif ctx.call():
            name, params = self.visit(ctx.call())
            return FuncCall(name, params)
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.branch_stmt():
            return self.visit(ctx.branch_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.CONTINUE():
            return Continue()
        elif ctx.BREAK():
            return Break()
        elif ctx.RETURN():
            return Return(self.visit(ctx.expr()) if ctx.expr() else None)


    # assign_stmt
    #         : lhs assignment_operator rhs
    #         ;
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.rhs())
        
        op = self.visit(ctx.assignment_operator())
        if op == '+=':
            return Assign(lhs, BinaryOp('+', lhs, rhs))
        elif op == '-=':
            return Assign(lhs, BinaryOp('-', lhs, rhs))
        elif op == '*=':
            return Assign(lhs, BinaryOp('*', lhs, rhs))
        elif op == '/=':
            return Assign(lhs, BinaryOp('/', lhs, rhs))
        elif op == '%=':
            return Assign(lhs, BinaryOp('%', lhs, rhs))
        
        return Assign(lhs, rhs)


    # lhs
    #         : list_ac;
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visit(ctx.list_ac())


    # rhs
    #         : expr
    #         ;
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visit(ctx.expr())


    # branch_stmt
    #         : IF L_PAREN expr R_PAREN block_stmt (ELSE block_stmt | ELSE branch_stmt | )
    #         ;
    def visitBranch_stmt(self, ctx:MiniGoParser.Branch_stmtContext):
        elseStmt = self.visit(ctx.block_stmt(1)) if ctx.block_stmt(1) else self.visit(ctx.branch_stmt()) if ctx.branch_stmt() else None
        return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt(0)), elseStmt)


    # for_stmt : for_basic_stmt | for_iter_stmt | for_range_stmt;
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        if ctx.for_basic_stmt():
            return self.visit(ctx.for_basic_stmt())
        elif ctx.for_iter_stmt():
            return self.visit(ctx.for_iter_stmt())
        elif ctx.for_range_stmt():
            return self.visit(ctx.for_range_stmt())


    # for_basic_stmt
    #             : FOR expr block_stmt
    #             ;
    def visitFor_basic_stmt(self, ctx:MiniGoParser.For_basic_stmtContext):
        return ForBasic(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))


    # for_iter_stmt
    #             : FOR (assign_stmt | var_decl_with_initialization) SEMI expr SEMI assign_stmt block_stmt
    #             ;
    def visitFor_iter_stmt(self, ctx:MiniGoParser.For_iter_stmtContext):
        if ctx.var_decl_with_initialization():
            return ForStep(self.visit(ctx.var_decl_with_initialization()), self.visit(ctx.expr()), self.visit(ctx.assign_stmt(0)), self.visit(ctx.block_stmt()))
        else:
            return ForStep(self.visit(ctx.assign_stmt(0)), self.visit(ctx.expr()), self.visit(ctx.assign_stmt(1)), self.visit(ctx.block_stmt()))


    # for_range_stmt
    #             : FOR ID COMMA ID DECLARE_ASSIGN RANGE list_ac block_stmt
    #             ;
    def visitFor_range_stmt(self, ctx:MiniGoParser.For_range_stmtContext):
        return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.list_ac()), self.visit(ctx.block_stmt()))


    # expr_list: expr_prime | ;
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        if ctx.expr_prime():
            return self.visit(ctx.expr_prime())
        else:
            return []


    # expr_prime: expr COMMA expr_prime | expr;
    def visitExpr_prime(self, ctx:MiniGoParser.Expr_primeContext):
        if ctx.expr_prime():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_prime())
        else:
            return [self.visit(ctx.expr())]


    # sub_expr: L_PAREN expr R_PAREN;
    def visitSub_expr(self, ctx:MiniGoParser.Sub_exprContext):
        return self.visit(ctx.expr())


    # expr: expr LOGICAL_OR expr6 | expr6;
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.LOGICAL_OR():
            return BinaryOp(ctx.LOGICAL_OR().getText(), self.visit(ctx.expr()), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr6())


    # expr6: expr6 LOGICAL_AND expr5 | expr5;
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        if ctx.LOGICAL_AND():
            return BinaryOp(ctx.LOGICAL_AND().getText(), self.visit(ctx.expr6()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())


    # expr5: expr5 relational_operator expr4 | expr4;
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.relational_operator():
            return BinaryOp(self.visit(ctx.relational_operator()), self.visit(ctx.expr5()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())


    # expr4: expr4 PLUS expr3 | expr4 MINUS expr3 | expr3;
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.PLUS():
            return BinaryOp(ctx.PLUS().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr3()))
        elif ctx.MINUS():
            return BinaryOp(ctx.MINUS().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())


    # expr3: expr3 STAR expr2 | expr3 DIV expr2 | expr3 MOD expr2 | expr2;
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.STAR():
            return BinaryOp(ctx.STAR().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr2()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr2()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr2()))
        else:
            return self.visit(ctx.expr2())


    # expr2: MINUS expr2 | LOGICAL_NOT expr2| expr1;
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.MINUS():
            return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.expr2()))
        elif ctx.LOGICAL_NOT():
            return UnaryOp(ctx.LOGICAL_NOT().getText(), self.visit(ctx.expr2()))
        else:
            return self.visit(ctx.expr1())


    # expr1: literal | list_ac;
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.list_ac())


    # nil_lit     : NIL;
    def visitNil_lit(self, ctx:MiniGoParser.Nil_litContext):
        return NilLiteral()


    # boolean_lit : TRUE | FALSE;
    def visitBoolean_lit(self, ctx:MiniGoParser.Boolean_litContext):
        return BooleanLiteral(ctx.getChild(0).getText())


    # int_lit
    #         : DECIMAL_LIT
    #         | BINARY_LIT
    #         | OCTAL_LIT
    #         | HEX_LIT
    #         ;
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return IntLiteral(ctx.getChild(0).getText())


    # struct_lit              : ID L_CURLY struct_lit_fields R_CURLY;
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.struct_lit_fields()))


    # struct_lit_fields       : struct_lit_fields_prime | ;
    def visitStruct_lit_fields(self, ctx:MiniGoParser.Struct_lit_fieldsContext):
        if ctx.struct_lit_fields_prime():
            return self.visit(ctx.struct_lit_fields_prime())
        else:
            return []


    # struct_lit_fields_prime : struct_lit_field COMMA struct_lit_fields_prime | struct_lit_field;
    def visitStruct_lit_fields_prime(self, ctx:MiniGoParser.Struct_lit_fields_primeContext):
        if ctx.struct_lit_fields_prime():
            return [self.visit(ctx.struct_lit_field())] + self.visit(ctx.struct_lit_fields_prime())
        else:
            return [self.visit(ctx.struct_lit_field())]


    # struct_lit_field        : ID COLON expr;
    def visitStruct_lit_field(self, ctx:MiniGoParser.Struct_lit_fieldContext):
        return (ctx.ID().getText(), self.visit(ctx.expr()))


    # array_lit               : dimension_list primitive_type array_lit_elements;
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.dimension_list()), self.visit(ctx.primitive_type()), self.visit(ctx.array_lit_elements()))


    # array_lit_elements      : L_CURLY array_lit_elements_list R_CURLY;
    def visitArray_lit_elements(self, ctx:MiniGoParser.Array_lit_elementsContext):
        return self.visit(ctx.array_lit_elements_list())


    # array_lit_elements_list : array_lit_element COMMA array_lit_elements_list | array_lit_element;
    def visitArray_lit_elements_list(self, ctx:MiniGoParser.Array_lit_elements_listContext):
        if ctx.array_lit_elements_list():
            return [self.visit(ctx.array_lit_element())] + self.visit(ctx.array_lit_elements_list())
        else:
            return [self.visit(ctx.array_lit_element())]


    # array_lit_element       : non_array_literal | ID | array_lit_elements; 
    def visitArray_lit_element(self, ctx:MiniGoParser.Array_lit_elementContext):
        if ctx.non_array_literal():
            return self.visit(ctx.non_array_literal())
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.array_lit_elements():
            return self.visit(ctx.array_lit_elements())


    # non_array_literal
    #     : nil_lit
    #     | boolean_lit
    #     | int_lit
    #     | FLOAT_LIT
    #     | STRING_LIT
    #     | struct_lit
    #     ;
    def visitNon_array_literal(self, ctx:MiniGoParser.Non_array_literalContext):
        if ctx.nil_lit():
            return self.visit(ctx.nil_lit())
        elif ctx.boolean_lit():
            return self.visit(ctx.boolean_lit())
        elif ctx.int_lit():
            return self.visit(ctx.int_lit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())


    # literal
    #     : non_array_literal
    #     | array_lit
    #     ;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.non_array_literal():
            return self.visit(ctx.non_array_literal())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())


    # id_list_cm
    #     : ID COMMA id_list_cm | ID;
    def visitId_list_cm(self, ctx:MiniGoParser.Id_list_cmContext):
        if ctx.id_list_cm():
            return [ctx.ID().getText()] + self.visit(ctx.id_list_cm())
        else:
            return [ctx.ID().getText()]


    # list_ac
    #     : list_ac DOT (call | ID) (dimension_list_expr | ) 
    #     | (call | sub_expr | ID) (dimension_list_expr | )
    #     | array_lit (dimension_list_expr | )
    #     | struct_lit DOT ID (dimension_list_expr | )
    #     ;
    def visitList_ac(self, ctx:MiniGoParser.List_acContext):
        # list_ac DOT (call | ID) (dimension_list_expr | ) 
        if ctx.list_ac():
            if ctx.dimension_list_expr():
                if ctx.call():
                    name, params = self.visit(ctx.call())
                    methodCall = MethCall(self.visit(ctx.list_ac()), name, params)
                    return ArrayCell(methodCall, self.visit(ctx.dimension_list_expr()))
                else:
                    filedAccess = FieldAccess(self.visit(ctx.list_ac()), ctx.ID().getText())
                    return ArrayCell(filedAccess, self.visit(ctx.dimension_list_expr()))
            else:
                if ctx.call():
                    name, params = self.visit(ctx.call())
                    return MethCall(self.visit(ctx.list_ac()), name, params)
                else:
                    return FieldAccess(self.visit(ctx.list_ac()), ctx.ID().getText())
        
        # array_lit (dimension_list_expr | )
        if ctx.array_lit():
            if ctx.dimension_list_expr():
                return ArrayCell(self.visit(ctx.array_lit()), self.visit(ctx.dimension_list_expr()))
            return self.visit(ctx.array_lit())
                
        # struct_lit DOT ID (dimension_list_expr | )
        if ctx.struct_lit():
            if ctx.dimension_list_expr():
                filedAccess = FieldAccess(self.visit(ctx.struct_lit()), ctx.ID().getText())
                return ArrayCell(filedAccess, self.visit(ctx.dimension_list_expr()))
            else:
                return FieldAccess(self.visit(ctx.struct_lit()), ctx.ID().getText())
                
        # (call | sub_expr | ID) (dimension_list_expr | )
        if ctx.dimension_list_expr():
            if ctx.call():
                name, params = self.visit(ctx.call())
                funcCall = FuncCall(name, params)
                return ArrayCell(funcCall, self.visit(ctx.dimension_list_expr()))
            elif ctx.sub_expr():
                filedAccess = FieldAccess(self.visit(ctx.sub_expr()), ctx.ID().getText())
                return ArrayCell(filedAccess, self.visit(ctx.dimension_list_expr()))
            else:
                return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.dimension_list_expr()))
        else:
            if ctx.call():
                name, params = self.visit(ctx.call())
                return FuncCall(name, params)
            elif ctx.sub_expr():
                return self.visit(ctx.sub_expr())
            else:
                return Id(ctx.ID().getText())
            
            
    # call : ID L_PAREN expr_list R_PAREN;
    def visitCall(self, ctx:MiniGoParser.CallContext):
        return ctx.ID().getText(), self.visit(ctx.expr_list())
            

    # dimension_list_expr: dimension_expr dimension_list_expr | dimension_expr;
    def visitDimension_list_expr(self, ctx:MiniGoParser.Dimension_list_exprContext):
        if ctx.dimension_list_expr():
            return [self.visit(ctx.dimension_expr())] + self.visit(ctx.dimension_list_expr())
        else:
            return [self.visit(ctx.dimension_expr())]


    # dimension_expr: L_BRACKET expr R_BRACKET;
    def visitDimension_expr(self, ctx:MiniGoParser.Dimension_exprContext):
        return self.visit(ctx.expr())


    # dimension_list: dimension dimension_list | dimension;
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        if ctx.dimension_list():
            return [self.visit(ctx.dimension())] + self.visit(ctx.dimension_list())
        else:
            return [self.visit(ctx.dimension())]


    # dimension   : L_BRACKET (int_lit | ID) R_BRACKET;
    def visitDimension(self, ctx:MiniGoParser.DimensionContext):
        return self.visit(ctx.int_lit()) if ctx.int_lit() else Id(ctx.ID().getText())


    # array_type  : dimension_list primitive_type;
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimension_list()), self.visit(ctx.primitive_type()))


    # primitive_type
    #     : INT
    #     | FLOAT
    #     | STRING
    #     | BOOLEAN
    #     | ID
    #     ;
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # data_type
    #     : primitive_type
    #     | array_type
    #     ;
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)


    # assignment_operator
    #         : DECLARE_ASSIGN
    #         | PLUS_ASSIGN
    #         | MINUS_ASSIGN
    #         | MUL_ASSIGN
    #         | DIV_ASSIGN
    #         | MOD_ASSIGN
    #         ;
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return ctx.getChild(0).getText()


    # relational_operator
    #             : EQUALS
    #             | NOT_EQUALS
    #             | LESS
    #             | LESS_OR_EQUALS
    #             | GREATER
    #             | GREATER_OR_EQUALS
    #             ;
    def visitRelational_operator(self, ctx:MiniGoParser.Relational_operatorContext):
        return ctx.getChild(0).getText()