grammar newParser;

program: block;

block: '{' stmts '}';

decls: decl | decl decls ;

decl: numType id | boolType id | attr;

attr: id '=' (math|bool)? | numType id '=' math | boolType id '=' boolOp;

numType: 'int' | 'float';

void: 'void';

boolType: 'boolean';

stmts: stmt+ ;

stmt: id '(' args ')' block
    | conditional
    | 'for' '(' attr ';' boolOp ';' math ')' block
    | 'return' id
    | 'break'
    | call
    | 'io_input_digital' '(' args ')'
    | 'io_output_digital' '(' args ')'
    | 'io_input_analog' '(' args ')'
    | 'io_output_analog' '(' args ')'
    | decls
    | attr
    ;

id: letter;

call: id '(' args ')';

args: arglist | ;

arglist: bool (',' arglist)? | num (',' arglist)? | id (',' arglist)? | ;

conditional: 'if' condition block ('elseif' condition block)* ('else' block)?;

condition: '(' bool ')';

boolOp: bool logOp bool | '!'bool ;

bool: 'TRUE' | 'FALSE';

math: num operator num | num;

operator: '+' | '-' | '*' | '/' | '%';

logOp: 'OR' | 'AND' | '<' | '<=' | '>' | '>=' | '==' | '!=';

num: DIGITS '.' DIGITSF exp?;

DIGITSF: DIGITS+;

exp: ('+' | '-') DIGITSF;

letter : [A-Za-z]+ ;

DIGITS: [0-9];
