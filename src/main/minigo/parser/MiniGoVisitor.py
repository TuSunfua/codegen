# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_list.
    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_with_initialization.
    def visitVar_decl_with_initialization(self, ctx:MiniGoParser.Var_decl_with_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_fields.
    def visitStruct_fields(self, ctx:MiniGoParser.Struct_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field.
    def visitStruct_field(self, ctx:MiniGoParser.Struct_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_methods.
    def visitInterface_methods(self, ctx:MiniGoParser.Interface_methodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params_list.
    def visitParams_list(self, ctx:MiniGoParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params_list_prime.
    def visitParams_list_prime(self, ctx:MiniGoParser.Params_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_stmt.
    def visitBlock_stmt(self, ctx:MiniGoParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#branch_stmt.
    def visitBranch_stmt(self, ctx:MiniGoParser.Branch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_basic_stmt.
    def visitFor_basic_stmt(self, ctx:MiniGoParser.For_basic_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_iter_stmt.
    def visitFor_iter_stmt(self, ctx:MiniGoParser.For_iter_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range_stmt.
    def visitFor_range_stmt(self, ctx:MiniGoParser.For_range_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_prime.
    def visitExpr_prime(self, ctx:MiniGoParser.Expr_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#sub_expr.
    def visitSub_expr(self, ctx:MiniGoParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nil_lit.
    def visitNil_lit(self, ctx:MiniGoParser.Nil_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#boolean_lit.
    def visitBoolean_lit(self, ctx:MiniGoParser.Boolean_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#int_lit.
    def visitInt_lit(self, ctx:MiniGoParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_fields.
    def visitStruct_lit_fields(self, ctx:MiniGoParser.Struct_lit_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_fields_prime.
    def visitStruct_lit_fields_prime(self, ctx:MiniGoParser.Struct_lit_fields_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_field.
    def visitStruct_lit_field(self, ctx:MiniGoParser.Struct_lit_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_elements.
    def visitArray_lit_elements(self, ctx:MiniGoParser.Array_lit_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_elements_list.
    def visitArray_lit_elements_list(self, ctx:MiniGoParser.Array_lit_elements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_element.
    def visitArray_lit_element(self, ctx:MiniGoParser.Array_lit_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#non_array_literal.
    def visitNon_array_literal(self, ctx:MiniGoParser.Non_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_list_cm.
    def visitId_list_cm(self, ctx:MiniGoParser.Id_list_cmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ac.
    def visitList_ac(self, ctx:MiniGoParser.List_acContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call.
    def visitCall(self, ctx:MiniGoParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list_expr.
    def visitDimension_list_expr(self, ctx:MiniGoParser.Dimension_list_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_expr.
    def visitDimension_expr(self, ctx:MiniGoParser.Dimension_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list.
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension.
    def visitDimension(self, ctx:MiniGoParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational_operator.
    def visitRelational_operator(self, ctx:MiniGoParser.Relational_operatorContext):
        return self.visitChildren(ctx)



del MiniGoParser