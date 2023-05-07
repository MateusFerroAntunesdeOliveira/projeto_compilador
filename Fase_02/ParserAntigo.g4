grammar Parser;

program : block ;
block : '{' decls? stmts? '}' ;
decls : decl (decls |);
decl : type id ('=' factor)?;
type : 'int' | 'float' | 'boolean' | 'void';
stmts : stmt (stmts |);

stmt : id '(' args? ')' block
     | id
     | conditional
     | 'for' '(' id '=' num ';' bool ';' term ')' block
     | 'return' id
     | 'break'
     | call
     | 'io_input_digital' '(' args? ')'
     | 'io_output_digital' '(' args? ')'
     | 'io_input_analog' '(' args? ')'
     | 'io_output_analog' '(' args? ')';

id : letter (letter | num)* ;

call : id '(' args? ')';
args : arglist? ;
arglist : bool (',' (bool | num | id))* ;

conditional : 'if' condition block ('else' block | 'elseif' condition block conditional?)?;
condition : '(' bool ')' ;
bool : rel (logOp rel)* ;
rel : term comparator (term | rel) ;
term : unary (operator unary)* ;
unary : '!' unary | num '=' num operator num | factor ;
factor : bool | num | 'TRUE' | 'FALSE' ;
operator : '+' | '-' | '*' | '/' | '%' ;
comparator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;
logOp : 'OR' | 'AND' ;
num : DIGITS '.' DIGITSF e? ;
e : 'exp' | ;
letter : [a-zA-Z_] ;
DIGITS : [0-9]+ ;
DIGITSF : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
