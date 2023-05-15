grammar Parser;

program: block;
block: '{' stmts '}';
attr: numType ID '=' MATH? | boolType ID '=' boolOp | ID '=' (MATH|boolOp)?;
numType: 'int' | 'float';
boolType: 'boolean';
stmts: stmt+ ;
stmt: conditional
    | 'for' '(' attr ';' boolOp ';' attr ') ' block
    | 'break'
    | 'io_input_digital' '(' args ')'
    | 'io_output_digital' '(' args ')'
    | 'io_input_analog' '(' args ')'
    | 'io_output_analog' '(' args ')'
    | attr
    ;
ID: [a-zA-Z] [a-zA-Z0-9]*;
args: arglist | ;
arglist: bool (',' arglist)? | NUM (',' arglist)? | ID (',' arglist)? | ;
conditional: 'if' condition block ('elseif' condition block)* ('else' block)?;
condition: '(' boolOp ')';
boolOp: (bool|MATH|ID)? logOp (bool|MATH|ID)? | '!'boolOp | bool;
bool: 'TRUE' | 'FALSE';
MATH: NUM | (NUM|ID)? operator (NUM|ID)?;
operator: '+' | '-' | '*' | '/' | '%';
logOp: 'OR' | 'AND' | '<' | '<=' | '>' | '>=' | '==' | '!=';
NUM: DIGITS | DIGITSF; 
DIGITSF: DIGITS '.' DIGITS exp?;
exp: ('+' | '-') DIGITS;
DIGITS: [0-9]+;
WS: [ \t\r\n]+ -> channel(HIDDEN);