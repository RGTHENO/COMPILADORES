grammar Gramatica;
programa  :    {print("Comenzó un nuevo programa")} NL* listadecl EOF {print("Fin del programa")};


comando returns [tipoComando]   
         :  cmdif {$tipoComando="Condicion"}|
            cmdwhile {$tipoComando="Repeticion"} |
            cmdasign {$tipoComando="Asignacion"}|
            cmdreturn {$tipoComando="Retornar"}| 
            llamada {$tipoComando="Llamada"};

listadecl: {print("Empezó la declaración")}decl listadecl  | decl;
 
decl : funcion | glbal ;

nl         : NL;

glbal     :  declvar nl;




funcion   :  FUN ID LEFTPAREN params RIGHTPAREN (COLON tipo)? nl

               listaBloque

            END nl
            ;



listaBloque: bloque | bloque listaBloque ;
bloque : (declvar nl)* listaComando?  nl;

listaComando :cmd=comando {print("Aparecio un comando de tipo",$cmd.tipoComando)} nl  listaComando |
                                  cmd=comando {print("Aparecio un comando de tipo",$cmd.tipoComando)};  
                     


params     : parametro ( COMMA parametro )* | /*vacio*/;

parametro  : ID COLON tipo;

tipobase returns[tipoDato] :  INT {$tipoDato= "INT"} | BOOL {$tipoDato = "BOOL"} | CHAR {$tipoDato = "CHAR"} | STRING {$tipoDato= "STRING"};

tipo  returns[tipoDato]    
            : tipobase {$tipoDato = $tipobase.tipoDato}| LEFTBRACKET RIGHTBRACKET tipo {$tipoDato = "[]" + $tipo.tipoDato};

var       : ID | var LEFTBRACKET exp RIGHTBRACKET;

declvar    :  ID COLON tipo
              {print("  Declaración: ID="+str($ID.text)+" Tipo="+str($tipo.tipoDato))};



cmdif     :  IF exp nl {print("Inicio condicional if")}

              listaBloque

                
               
              (ELSE IF exp nl

                 listaBloque

              )*


              (ELSE nl

                 listaBloque

              )?

             END {print("Fin condicional if")}
            ;
cmdwhile   : WHILE exp nl {print("Inicio While")}

               listaBloque

             LOOP  {print("Fin While")}
             ;

cmdasign   : var EQUAL exp;

llamada   :  ID LEFTPAREN listaexp RIGHTPAREN;

listaexp  : /*vacio*/ | exp {print("Expresión: ", $exp.text)} ( COMMA exp )* ;

cmdreturn : RETURN exp | RETURN ;



op1 :    PLUS
         | MINUS;

op2 :    STAR
         | DIV;

exprAritmetica : termAritmetico (op1 termAritmetico)*;

termAritmetico : factorAritmetico (op2 factorAritmetico)*;

factorAritmetico : LITNUMERAL
                  | LITSTRING
                  | ID
                  | LEFTPAREN exprAritmetica RIGHTPAREN
                  | BOOL
                  | CHAR
                  | LITCHAR;

exprRelacional: termRelacional (OP_BOOL termRelacional)*;
               

termRelacional: exprAritmetica OP_REL exprAritmetica;

OP_BOOL: AND
         | OR;
         
        
OP_REL: GREATEREQUAL
      |GREATER
      |LESS
      |LESSEQUAL
      |DIFFERENT;
      

exp       :  NEW LEFTBRACKET exp RIGHTBRACKET tipo

          | LEFTPAREN exp RIGHTPAREN

          | llamada

          | NOT exp

          | MINUS exp

          | exprAritmetica

          |exprRelacional
          ;


COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;

NL: ( '\n' )+;
LITNUMERAL: ( [0-9]+ | '0x'[0-9a-fA-F]+ );
LITSTRING: '"' ('\\' | '\n' | '\t' | '”' | [a-zA-Z]|[0-9])+  '"';
LITCHAR:'\'' ('\\' | '\n' | '\t' | '”' | ' '| [a-zA-Z]|[0-9])  '\'';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
END: 'end';
WHILE: 'while';
LOOP: 'loop';
FUN: 'fun';
RETURN: 'return';
NEW: 'new';
STRING: 'string';
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
AND: 'and';
OR: 'or';
NOT: 'not';

LESS: '<';
GREATER: '>';
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
LEFTBRACE: '{';
RIGHTBRACE: '}';
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
COMMA: ',';
COLON: ':';
GREATEREQUAL: '>=';
LESSEQUAL: '<=';
EQUAL: '=';
DIFFERENT: '<>';
DOT : '.';
ID: ([a-zA-Z_]) ([a-zA-Z_]|[0-9])*;
WS : [ \t\r]+ -> skip;

