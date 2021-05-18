# Generated from Gramatica.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#programa.
    def enterPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#programa.
    def exitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comando.
    def enterComando(self, ctx:GramaticaParser.ComandoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comando.
    def exitComando(self, ctx:GramaticaParser.ComandoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#listadecl.
    def enterListadecl(self, ctx:GramaticaParser.ListadeclContext):
        pass

    # Exit a parse tree produced by GramaticaParser#listadecl.
    def exitListadecl(self, ctx:GramaticaParser.ListadeclContext):
        pass


    # Enter a parse tree produced by GramaticaParser#decl.
    def enterDecl(self, ctx:GramaticaParser.DeclContext):
        pass

    # Exit a parse tree produced by GramaticaParser#decl.
    def exitDecl(self, ctx:GramaticaParser.DeclContext):
        pass


    # Enter a parse tree produced by GramaticaParser#nl.
    def enterNl(self, ctx:GramaticaParser.NlContext):
        pass

    # Exit a parse tree produced by GramaticaParser#nl.
    def exitNl(self, ctx:GramaticaParser.NlContext):
        pass


    # Enter a parse tree produced by GramaticaParser#glbal.
    def enterGlbal(self, ctx:GramaticaParser.GlbalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#glbal.
    def exitGlbal(self, ctx:GramaticaParser.GlbalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#funcion.
    def enterFuncion(self, ctx:GramaticaParser.FuncionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#funcion.
    def exitFuncion(self, ctx:GramaticaParser.FuncionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#listaBloque.
    def enterListaBloque(self, ctx:GramaticaParser.ListaBloqueContext):
        pass

    # Exit a parse tree produced by GramaticaParser#listaBloque.
    def exitListaBloque(self, ctx:GramaticaParser.ListaBloqueContext):
        pass


    # Enter a parse tree produced by GramaticaParser#bloque.
    def enterBloque(self, ctx:GramaticaParser.BloqueContext):
        pass

    # Exit a parse tree produced by GramaticaParser#bloque.
    def exitBloque(self, ctx:GramaticaParser.BloqueContext):
        pass


    # Enter a parse tree produced by GramaticaParser#listaComando.
    def enterListaComando(self, ctx:GramaticaParser.ListaComandoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#listaComando.
    def exitListaComando(self, ctx:GramaticaParser.ListaComandoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#params.
    def enterParams(self, ctx:GramaticaParser.ParamsContext):
        pass

    # Exit a parse tree produced by GramaticaParser#params.
    def exitParams(self, ctx:GramaticaParser.ParamsContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parametro.
    def enterParametro(self, ctx:GramaticaParser.ParametroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parametro.
    def exitParametro(self, ctx:GramaticaParser.ParametroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipobase.
    def enterTipobase(self, ctx:GramaticaParser.TipobaseContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipobase.
    def exitTipobase(self, ctx:GramaticaParser.TipobaseContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo.
    def enterTipo(self, ctx:GramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo.
    def exitTipo(self, ctx:GramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#var.
    def enterVar(self, ctx:GramaticaParser.VarContext):
        pass

    # Exit a parse tree produced by GramaticaParser#var.
    def exitVar(self, ctx:GramaticaParser.VarContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declvar.
    def enterDeclvar(self, ctx:GramaticaParser.DeclvarContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declvar.
    def exitDeclvar(self, ctx:GramaticaParser.DeclvarContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdif.
    def enterCmdif(self, ctx:GramaticaParser.CmdifContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdif.
    def exitCmdif(self, ctx:GramaticaParser.CmdifContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdwhile.
    def enterCmdwhile(self, ctx:GramaticaParser.CmdwhileContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdwhile.
    def exitCmdwhile(self, ctx:GramaticaParser.CmdwhileContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdasign.
    def enterCmdasign(self, ctx:GramaticaParser.CmdasignContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdasign.
    def exitCmdasign(self, ctx:GramaticaParser.CmdasignContext):
        pass


    # Enter a parse tree produced by GramaticaParser#llamada.
    def enterLlamada(self, ctx:GramaticaParser.LlamadaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#llamada.
    def exitLlamada(self, ctx:GramaticaParser.LlamadaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#listaexp.
    def enterListaexp(self, ctx:GramaticaParser.ListaexpContext):
        pass

    # Exit a parse tree produced by GramaticaParser#listaexp.
    def exitListaexp(self, ctx:GramaticaParser.ListaexpContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdreturn.
    def enterCmdreturn(self, ctx:GramaticaParser.CmdreturnContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdreturn.
    def exitCmdreturn(self, ctx:GramaticaParser.CmdreturnContext):
        pass


    # Enter a parse tree produced by GramaticaParser#exp.
    def enterExp(self, ctx:GramaticaParser.ExpContext):
        pass

    # Exit a parse tree produced by GramaticaParser#exp.
    def exitExp(self, ctx:GramaticaParser.ExpContext):
        pass



del GramaticaParser