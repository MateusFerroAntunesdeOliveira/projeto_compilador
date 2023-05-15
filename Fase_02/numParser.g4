grammar numParser;

program: block;
block: '{' stmts '}';
attr: numType ID '=' math? | 'bool' ID '=' boolOp | ID '=' (math|boolOp)?;
numType: 'int' | 'float';
stmts: stmt+ ;
stmt: conditional
    | attr
    | 'for' attr ';' boolOp ';' attr block
    | 'break'
    | 'io_input_digital' args
    | 'io_output_digital' args
    | 'io_input_analog' args
    | 'io_output_analog' args
    ;
ID: [a-zA-Z] [a-zA-Z0-9]*;
conditional: 'if' condition block ('elseif' condition block)* ('else' block)?;
condition: boolOp;
args: ID (',' args)? ;
boolOp: ((bool|math|ID)? logOp (bool|math|ID)?)+ | '!'(boolOp|ID)? | bool;
math: numeric | (numeric|ID)? operator (numeric|ID)?;
operator: '+' | '-' | '*' | '/' | '%';
logOp: 'OR' | 'AND' | '<' | '<=' | '>' | '>=' | '==' | '!=';
bool : 'TRUE' | 'FALSE';
numeric : NUM | NUM '.' NUM exp?;
exp: 'e' ('+' | '-') NUM;
NUM: [0-9]+; 
WS: [ \t\r\n]+ -> channel(HIDDEN);