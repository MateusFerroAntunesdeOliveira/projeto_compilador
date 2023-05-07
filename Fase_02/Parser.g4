grammar Parser;

program : block ;
block : '{' decls stmts '}' ;
decls : (decl)* ;
decl : (type)? id ('=' factor)? ;
type : 'int' | 'float' | 'boolean' | 'void' ;
stmts : stmt | ;

stmt : 
      | id '(' args ')' block
      | id
      | 'if' condition block ('elseif' condition block)* ('else' block)? 
      | 'for' '(' decl ';' bool ';' term ')' block
      | 'return' id
      | 'break'
      | call
      | 'io_input_digital' '(' args ')'
      | 'io_output_digital' '(' args ')'
      | 'io_input_analog' '(' args ')'
      | 'io_output_analog' '(' args ')'
      ;
call : id '(' args ')' ;
args : arg (',' arg)* | ;
arg : bool | num | id ;
condition : '(' bool ')' ;

bool : rel (logOp rel)* ;
rel : term (comparator term)* ;
term : unary (operator unary)* ;
unary : '!'unary | num '=' num operator num | factor ;
factor : num | 'TRUE' | 'FALSE' | id ;
operator : '+' | '-' | '*' | '/' | '%' ;
comparator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;
logOp : 'OR' | 'AND' ;
id : LETTER+ | DIGIT+ ;

num : DIGIT+ ('.' DIGIT+)? (exp)? ;
exp : 'e' ('+'|'-')? DIGIT+ ;
LETTER : [a-zA-Z_] ;
DIGIT : [0-9] ;
WS : [ \t\r\n]+ -> skip ;
