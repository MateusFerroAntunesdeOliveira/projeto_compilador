grammar newParser;

program: block;
block: '{' stmts '}';
attr: numType id '=' math | boolType id '=' boolOp | id '=' (math|boolOp)?;
numType: 'int' | 'float';
boolType: 'boolean';
stmts: stmt+ ;
stmt: conditional BREAK
    | 'for' '(' attr ';' boolOp ';' attr ') ' block BREAK
    | 'break' BREAK
    | 'io_input_digital' '(' args ')' BREAK
    | 'io_output_digital' '(' args ')' BREAK
    | 'io_input_analog' '(' args ')' BREAK
    | 'io_output_analog' '(' args ')' BREAK
    | attr BREAK
    ;
BREAK: (' ')*'\n';
id: letter+;
args: arglist | ;
arglist: bool (',' arglist)? | num (',' arglist)? | id (',' arglist)? | ;
conditional: 'if' condition block ('elseif' condition block)* ('else' block)?;
condition: '(' bool ')';
boolOp: (bool|math|id)? logOp (bool|math|id)? | '!'boolOp | bool;
bool: 'TRUE' | 'FALSE';
math: num | (num|id)? operator (num|id)?;
operator: '+' | '-' | '*' | '/' | '%';
logOp: 'OR' | 'AND' | '<' | '<=' | '>' | '>=' | '==' | '!=';
num: DIGITS | DIGITS '.' DIGITSF exp?; 
DIGITSF: DIGITS+;
exp: ('+' | '-') DIGITSF;
letter : 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z';
DIGITS: ('0' .. '9')+;
WS: [ \t\r\n]+ -> channel(HIDDEN);