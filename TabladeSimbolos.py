from enum import Enum
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener
from GramaticaVisitor import GramaticaVisitor


class SymbolTableEntry():
    def __init__(self, _nombre = "", tipo=0):
        self.nombre = _nombre
        self.tipo = tipo


class SymbolTable():
    class TipoMini0(Enum):
        NUMERO = 1
        STRING = 2
        BOOL = 3
        CHAR = 4
        INVALIDO = 5
        FUNCION = 6



    def __init__(self):
        self.tabla = {}

    def insert(self, _nombre, _valor):
        entrada = SymbolTableEntry(_nombre, _valor)
        self.tabla[_nombre] = entrada
    
    def exists(self, _nombre):
        return _nombre in self.tabla
    
    def verify(self, _nombre):
        if self.tabla[_nombre] != None:
            return self.tabla[_nombre].tipo
        else:
            return self.TipoMini0.INVALIDO 

class SemanticoUtils():

   

    def __init__(self):
        self.erroresSemanticos= []
        
    def adicionarErrorSemantico(self, t, mensaje):
        linea = t.line
        columna = t.column
        self.erroresSemanticos.append("Error : Linea: "+ str(linea)+ " Columna: " + str(columna) + " " + str(mensaje))

    def verificarTipo1(self, tabla, ctx:GramaticaParser.ExprAritmeticaContext):
        ret = None
        for  ta in ctx.termAritmetico():
            aux = self.verificarTipo(tabla, ta)
            if  ret == None:
                ret = aux
            elif ret != aux and aux != SymbolTable.TipoMini0.INVALIDO :
                self.adicionarErrorSemantico(ctx.start, "Expresión " + ctx.getText() + " contiene tipos incompatibles")
                ret = SymbolTable.TipoMini0.INVALIDO
        return ret

    def verificarTipo1_2(self, tabla, ctx:GramaticaParser.TermAritmeticoContext):
        ret = None
        for  ta in ctx.factorAritmetico():
            aux = self.verificarTipo(tabla, ta)
            if  ret == None:
                ret = aux
            elif ret != aux and aux != SymbolTable.TipoMini0.INVALIDO :
                self.adicionarErrorSemantico(ctx.start, "Expresión " + ctx.getText() + " contiene tipos incompatibles")
                ret = SymbolTable.TipoMini0.INVALIDO
        return ret



    def verificarTipo2(self, tabla,ctx):
        if  ctx.LITNUMERAL() != None:
            return SymbolTable.TipoMini0.NUMERO
        if ctx.LITSTRING() != None:
            return SymbolTable.TipoMini0.STRING
        if ctx.BOOL() != None:
            return SymbolTable.TipoMini0.BOOL
        if ctx.LITCHAR() != None:
            return SymbolTable.TipoMini0.CHAR
            
        if ctx.ID() != None:
            nombreVar = ctx.ID().getSymbol().text
            if not tabla.exists(nombreVar):
                self.adicionarErrorSemantico(ctx.ID().getSymbol(), "Variable " + nombreVar +" no fue declarada antes de uso"); 
                return SymbolTable.TipoMini0.INVALIDO
            
            return self.verificarTipo(tabla, nombreVar)
        
        return self.verificarTipo(tabla, ctx.exp())


    def verificarTipo(self, tabla, ctx):
        if(not isinstance(tabla, SymbolTable)):
            print("El primer argumento debe ser la tabla de símbolos del programa")
            return 0
        if(isinstance(ctx, GramaticaParser.ExprAritmeticaContext)):
            return self.verificarTipo1(tabla,ctx)
        elif(isinstance(ctx, GramaticaParser.TermAritmeticoContext)):
            return self.verificarTipo1_2(tabla,ctx)
        elif(isinstance(ctx, GramaticaParser.FactorAritmeticoContext)):
            return self.verificarTipo2(tabla,ctx)
        elif(isinstance(ctx, str)):
            return tabla.verify(ctx)
        elif (isinstance(ctx, GramaticaParser.ExpContext)):
            return self.verificarTipo(tabla, ctx.exprAritmetica())

        
        else:
            print(type(ctx).__name__)
            print("No se están mandando los tipos de gramática correctos")

        
  

class Mini0Semantico(GramaticaVisitor):

    def __init__(self):
        self.tabla = SymbolTable()
        self.utils = SemanticoUtils()

    def visitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        return super().visitPrograma(ctx)

    def visitDeclvar(self, ctx:GramaticaParser.DeclvarContext):
        nombreVar = ctx.ID().getSymbol().text
        strTipoVar = ctx.tipo().getText()
        tipoVar = SymbolTable.TipoMini0.INVALIDO
        if (strTipoVar == "int"):
            tipoVar = SymbolTable.TipoMini0.NUMERO
        elif (strTipoVar == "char"):
            tipoVar = SymbolTable.TipoMini0.CHAR
        elif (strTipoVar == "string"):
            tipoVar = SymbolTable.TipoMini0.STRING
        elif (strTipoVar == "bool"):
            tipoVar = SymbolTable.TipoMini0.BOOL
        
        if(self.tabla.exists(nombreVar)):
            self.utils.adicionarErrorSemantico(ctx.ID().getSymbol(),"Variable " + nombreVar + " ya existe")
        else:
            self.tabla.insert(nombreVar, tipoVar)
        
        return super().visitDeclvar(ctx)

    def visitParametro(self, ctx: GramaticaParser.ParametroContext):
        nombreVar = ctx.ID().getSymbol().text
        strTipoVar = ctx.tipo().getText()
        tipoVar = SymbolTable.TipoMini0.INVALIDO
        if (strTipoVar == "int"):
            tipoVar = SymbolTable.TipoMini0.NUMERO
        elif (strTipoVar == "char"):
            tipoVar = SymbolTable.TipoMini0.CHAR
        elif (strTipoVar == "string"):
            tipoVar = SymbolTable.TipoMini0.STRING
        elif (strTipoVar == "bool"):
            tipoVar = SymbolTable.TipoMini0.BOOL
        
        if(self.tabla.exists(nombreVar)):
            self.utils.adicionarErrorSemantico(ctx.ID().getSymbol(),"Variable " + nombreVar + " ya existe")
        else:
            self.tabla.insert(nombreVar, tipoVar)
        
        return super().visitParametro(ctx)
        

    def visitCmdasign(self,ctx:GramaticaParser.CmdasignContext):
        tipoExpresion = self.utils.verificarTipo(self.tabla, ctx.exp())
        #print("Tipo de expresión------   "+str(tipoExpresion))
        if tipoExpresion != SymbolTable.TipoMini0.INVALIDO :
            nombreVar = ctx.var().getText()
            if not self.tabla.exists(nombreVar):
                self.utils.adicionarErrorSemantico(ctx.var().ID().getSymbol(), "Variable " + nombreVar + " no fue declarada antes de uso")
            else :
                tipoVariable = self.utils.verificarTipo(self.tabla,nombreVar)
                if tipoVariable != tipoExpresion and tipoExpresion != SymbolTable.TipoMini0.INVALIDO :
                    self.utils.adicionarErrorSemantico(ctx.var().ID().getSymbol() ,"Tipo de la variable " + nombreVar + " no es compatible con el tipo de la expresión")
                
        return super().visitCmdasign(ctx)
    
    def visitFuncion(self, ctx:GramaticaParser.FuncionContext):
        nombreFuncion = ctx.ID().getSymbol().text
        tipoVar = SymbolTable.TipoMini0.FUNCION
        if(self.tabla.exists(nombreFuncion) and self.tabla[nombreFuncion].tipo == SymbolTable.TipoMini0.FUNCION):
            self.utils.adicionarErrorSemantico(ctx.ID().getSymbol(), "La función "+nombreFuncion+" fue declarada más de una vez")
        else:
            self.tabla.insert(nombreFuncion, tipoVar)
        return super().visitFuncion(ctx)
    
    def visitLlamada(self, ctx:GramaticaParser.LlamadaContext):
        nombreFuncion = ctx.ID().getSymbol().text
        if not self.tabla.exists(nombreFuncion):
            self.utils.adicionarErrorSemantico(ctx.ID().getSymbol(), "La función " + nombreFuncion +" no fue declarada antes de su uso")

        return super().visitLlamada(ctx)


    def visitExprAritmetica(self,ctx:GramaticaParser.ExprAritmeticaContext):
        self.utils.verificarTipo(self.tabla,ctx)
        return super().visitExprAritmetica(ctx)
    