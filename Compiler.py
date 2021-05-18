from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener
 
from TabladeSimbolos import *

import sys
import unittest
from io import StringIO
from os import listdir
from os.path import isfile, join

def getTypeName(lex, tokenType):
    return str(lex.ruleNames[tokenType - 1])
 
class PruebaSemantica(unittest.TestCase):    

    def test_run(self):
        
        mypath = "./tests-lexico/"
        #mypath= "./tests-sintactico/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        print("Lista de archivos :", onlyfiles)

        for fileTest in onlyfiles:

            print("=============== Prueba de uso "+fileTest+" =========================")
            lexer = GramaticaLexer(FileStream(mypath+fileTest))
            tokens = CommonTokenStream(lexer)
            parser = GramaticaParser(tokens)
            arbol = parser.programa()
            ars = Mini0Semantico()
            ars.visitPrograma(arbol)
            for s in ars.utils.erroresSemanticos:
                print(s)   
            print("=============== Fin Prueba de uso "+fileTest+" =======================\n\n\n")

         
    
if __name__ == "__main__" :
    unittest.main()
 
