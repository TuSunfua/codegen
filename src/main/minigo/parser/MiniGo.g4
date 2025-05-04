// 2213841
grammar MiniGo;

@lexer::header {
# 2213841
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    self.lastToken = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

def isEos(self):
    if hasattr(self, 'lastToken'):
        return self.lastToken in {
                self.ID, 
                self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
                self.NIL, 
                self.DECIMAL_LIT, self.BINARY_LIT, self.OCTAL_LIT, self.HEX_LIT, 
                self.FLOAT_LIT, 
                self.TRUE, self.FALSE, 
                self.STRING_LIT, 
                self.RETURN, self.CONTINUE, self.BREAK, 
                self.R_PAREN, self.R_BRACKET, self.R_CURLY
            }
    return False
}

options{
	language=Python3;
}

// ---------------------------------------------------------------------------------------------------------------------
// Rules
    program: decl_list EOF;
    decl_list: decl decl_list | decl;
    decl: var_decl eos | const_decl eos | struct_decl eos | interface_decl eos | func_decl eos | method_decl eos;

// ---------------------------------------------------------------------------------------------------------------------
// Variable declaration
    var_decl
        : VAR ID data_type
        | var_decl_with_initialization
        ;

    var_decl_with_initialization
        : VAR ID data_type ASSIGN expr
        | VAR ID ASSIGN expr
        ;

// ---------------------------------------------------------------------------------------------------------------------
// Constant declaration
    const_decl
        : CONST ID ASSIGN expr
        ;

// ---------------------------------------------------------------------------------------------------------------------
// Struct declaration
    struct_decl
        : TYPE ID STRUCT L_CURLY struct_fields R_CURLY
        ;
    struct_fields
        : struct_field struct_fields | struct_field;
    struct_field
        : ID data_type eos
        ;

// ---------------------------------------------------------------------------------------------------------------------
// Interface declaration
    interface_decl
        : TYPE ID INTERFACE L_CURLY interface_methods R_CURLY
        ;
    interface_methods
        : interface_method interface_methods | interface_method;
    interface_method
        : ID L_PAREN params_list R_PAREN (data_type | ) eos
        ;
    params_list
        : params_list_prime | ;
    params_list_prime
        : id_list_cm data_type COMMA params_list_prime | id_list_cm data_type;

// ---------------------------------------------------------------------------------------------------------------------
// Function declaration
    func_decl
        : FUNC ID L_PAREN params_list R_PAREN (data_type | ) block_stmt
        ;
    method_decl
        : FUNC L_PAREN ID ID R_PAREN ID L_PAREN params_list R_PAREN (data_type | ) block_stmt
        ;
    block_stmt
        : L_CURLY stmt_list R_CURLY
        ;
    stmt_list
        : stmt stmt_list | stmt;
    stmt
        : var_decl eos
        | const_decl eos
        | block_stmt eos
        | call eos
        | list_ac DOT call eos
        | assign_stmt eos
        | branch_stmt eos
        | for_stmt eos
        | CONTINUE eos
        | BREAK eos
        | RETURN (expr | ) eos
        ;

    // assign_stmt
        assign_stmt
            : lhs assignment_operator rhs
            ;

        lhs
            : list_ac;
        
        rhs
            : expr
            ;

    // branch_stmt
        branch_stmt
            : IF L_PAREN expr R_PAREN block_stmt (ELSE block_stmt | ELSE branch_stmt | )
            ;
        
    // for_stmt
        for_stmt : for_basic_stmt | for_iter_stmt | for_range_stmt;

        // basic for loop
            for_basic_stmt
                : FOR expr block_stmt
                ;

        // iteration for loop
            for_iter_stmt
                : FOR (assign_stmt | var_decl_with_initialization) SEMI expr SEMI assign_stmt block_stmt
                ;

        // range for loop
            for_range_stmt
                : FOR ID COMMA ID DECLARE_ASSIGN RANGE list_ac block_stmt
                ;

    // expression
        expr_list: expr_prime | ;
        expr_prime: expr COMMA expr_prime | expr;
        sub_expr: L_PAREN expr R_PAREN;

        expr: expr LOGICAL_OR expr6 | expr6;
        expr6: expr6 LOGICAL_AND expr5 | expr5;
        expr5: expr5 relational_operator expr4 | expr4;
        expr4: expr4 PLUS expr3 | expr4 MINUS expr3 | expr3;
        expr3: expr3 STAR expr2 | expr3 DIV expr2 | expr3 MOD expr2 | expr2;
        expr2: MINUS expr2 | LOGICAL_NOT expr2| expr1;
        expr1: literal | list_ac;

// ---------------------------------------------------------------------------------------------------------------------
// Literals
    // NIL literal
        nil_lit     : NIL;
    // Boolean literals
        boolean_lit : TRUE | FALSE;
    // Number literals
        DECIMAL_LIT : '0' | [1-9] [0-9]*;
        BINARY_LIT  : '0' [bB] [01]+;
        OCTAL_LIT   : '0' [oO] [0-7]+;
        HEX_LIT     : '0' [xX] [0-9a-fA-F]+;

        int_lit
            : DECIMAL_LIT
            | BINARY_LIT
            | OCTAL_LIT
            | HEX_LIT
            ;
    // Floating-point literals
        FLOAT_LIT   
            : [0-9]+ '.' [0-9]* ([eE] [+\-]? [0-9]+)?;
    // String literals
        STRING_LIT:   '"' CHARACTERS? '"';

        fragment CHARACTERS: CHARACTER+;
        fragment CHARACTER: ~["\\\r\n] | ESC;
        fragment ESC: '\\' ["tnr\\];

    // Struct literals
        struct_lit              : ID L_CURLY struct_lit_fields R_CURLY;
        struct_lit_fields       : struct_lit_fields_prime | ;
        struct_lit_fields_prime : struct_lit_field COMMA struct_lit_fields_prime | struct_lit_field;
        struct_lit_field        : ID COLON expr;

    // Array literals
        array_lit               : dimension_list primitive_type array_lit_elements;
        array_lit_elements      : L_CURLY array_lit_elements_list R_CURLY;
        array_lit_elements_list : array_lit_element COMMA array_lit_elements_list | array_lit_element;
        array_lit_element       : non_array_literal | ID | array_lit_elements; 

    non_array_literal
        : nil_lit
        | boolean_lit
        | int_lit
        | FLOAT_LIT
        | STRING_LIT
        | struct_lit
        ;

    literal
        : non_array_literal
        | array_lit
        ;

// ---------------------------------------------------------------------------------------------------------------------
// Keywords
    IF          : 'if';
    ELSE        : 'else';
    FOR         : 'for';
    RETURN      : 'return';
    FUNC        : 'func';
    TYPE        : 'type';
    STRUCT      : 'struct';
    INTERFACE   : 'interface';
    CONST       : 'const';
    VAR         : 'var';
    CONTINUE    : 'continue';
    BREAK       : 'break';
    RANGE       : 'range';
    INT         : 'int';
    FLOAT       : 'float';
    STRING      : 'string';
    BOOLEAN     : 'boolean';
    TRUE        : 'true';
    FALSE       : 'false';
    NIL         : 'nil';

// ---------------------------------------------------------------------------------------------------------------------
// Identifiers
    ID      : [a-zA-Z_] [a-zA-Z_0-9]*;

    // id separated by comma
    id_list_cm
        : ID COMMA id_list_cm | ID;

    // list accession
    list_ac
        : list_ac DOT (call | ID) (dimension_list_expr | ) 
        | (call | sub_expr | ID) (dimension_list_expr | )
        | array_lit (dimension_list_expr | )
        | struct_lit DOT ID (dimension_list_expr | )
        ;
    call : ID L_PAREN expr_list R_PAREN;
    dimension_list_expr: dimension_expr dimension_list_expr | dimension_expr;
    dimension_expr: L_BRACKET expr R_BRACKET;

// ---------------------------------------------------------------------------------------------------------------------
// Comments
    LINE_COMMENT    : '//' ~[\r\n]* -> skip;
    BLOCK_COMMENT   : '/*' (BLOCK_COMMENT | ~[*] | '*' ~[/])* '*/' -> skip;

// ---------------------------------------------------------------------------------------------------------------------
// Data types
    // Array type
        dimension_list: dimension dimension_list | dimension;
        dimension   : L_BRACKET (int_lit | ID) R_BRACKET;
        array_type  : dimension_list primitive_type;
    
    // Primitive data type
    primitive_type
        : INT
        | FLOAT
        | STRING
        | BOOLEAN
        | ID
        ;

    data_type
        : primitive_type
        | array_type
        ;

// ---------------------------------------------------------------------------------------------------------------------
// Symbolic
    // End of statement
        eos
            : SEMI 
            | EOF
            ;

    // Punctuation
        L_PAREN        : '(';
        R_PAREN        : ')';
        L_CURLY        : '{';
        R_CURLY        : '}';
        L_BRACKET      : '[';
        R_BRACKET      : ']';
        COMMA          : ',';
        SEMI           : ';';
        COLON          : ':';
        DOT            : '.';
        ASSIGN         : '=';
        DECLARE_ASSIGN : ':=';
        PLUS_ASSIGN    : '+=';
        MINUS_ASSIGN   : '-=';
        MUL_ASSIGN     : '*=';
        DIV_ASSIGN     : '/=';
        MOD_ASSIGN     : '%=';

        assignment_operator
            : DECLARE_ASSIGN
            | PLUS_ASSIGN
            | MINUS_ASSIGN
            | MUL_ASSIGN
            | DIV_ASSIGN
            | MOD_ASSIGN
            ;

    // Operators
        // Logical
            LOGICAL_OR          : '||';
            LOGICAL_AND         : '&&';
            LOGICAL_NOT         : '!';
        // Relational
            EQUALS              : '==';
            NOT_EQUALS          : '!=';
            LESS                : '<';
            LESS_OR_EQUALS      : '<=';
            GREATER             : '>';
            GREATER_OR_EQUALS   : '>=';

            relational_operator
                : EQUALS
                | NOT_EQUALS
                | LESS
                | LESS_OR_EQUALS
                | GREATER
                | GREATER_OR_EQUALS
                ;
        // Arithmetic
            PLUS                : '+';
            MINUS               : '-';
            STAR                : '*';
            DIV                 : '/';
            MOD                 : '%';   

// ---------------------------------------------------------------------------------------------------------------------
NEW_LINE
    : ('\r'? '\n') {
        if self.isEos():
            self.text = ';'
            self.type = self.SEMI
        else:
            self.skip()
    }
    ;

WS : [ \t\f\r]+ -> skip; 

ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: '"' CHARACTERS? '\\' ~["tnr\\] {raise IllegalEscape(self.text)};
UNCLOSE_STRING: '"' CHARACTERS? ([\n\t\\] | EOF | ) {raise UncloseString(self.text)};