# Generated from Gramatica.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#programa.
    def visitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#comando.
    def visitComando(self, ctx:GramaticaParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#listadecl.
    def visitListadecl(self, ctx:GramaticaParser.ListadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#decl.
    def visitDecl(self, ctx:GramaticaParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#nl.
    def visitNl(self, ctx:GramaticaParser.NlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#glbal.
    def visitGlbal(self, ctx:GramaticaParser.GlbalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#funcion.
    def visitFuncion(self, ctx:GramaticaParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#listaBloque.
    def visitListaBloque(self, ctx:GramaticaParser.ListaBloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#bloque.
    def visitBloque(self, ctx:GramaticaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#listaComando.
    def visitListaComando(self, ctx:GramaticaParser.ListaComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#params.
    def visitParams(self, ctx:GramaticaParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#parametro.
    def visitParametro(self, ctx:GramaticaParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#tipobase.
    def visitTipobase(self, ctx:GramaticaParser.TipobaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#tipo.
    def visitTipo(self, ctx:GramaticaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#var.
    def visitVar(self, ctx:GramaticaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#declvar.
    def visitDeclvar(self, ctx:GramaticaParser.DeclvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#cmdif.
    def visitCmdif(self, ctx:GramaticaParser.CmdifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#cmdwhile.
    def visitCmdwhile(self, ctx:GramaticaParser.CmdwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#cmdasign.
    def visitCmdasign(self, ctx:GramaticaParser.CmdasignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#llamada.
    def visitLlamada(self, ctx:GramaticaParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#listaexp.
    def visitListaexp(self, ctx:GramaticaParser.ListaexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#cmdreturn.
    def visitCmdreturn(self, ctx:GramaticaParser.CmdreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#op1.
    def visitOp1(self, ctx:GramaticaParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#op2.
    def visitOp2(self, ctx:GramaticaParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#exprAritmetica.
    def visitExprAritmetica(self, ctx:GramaticaParser.ExprAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#termAritmetico.
    def visitTermAritmetico(self, ctx:GramaticaParser.TermAritmeticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#factorAritmetico.
    def visitFactorAritmetico(self, ctx:GramaticaParser.FactorAritmeticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#exprRelacional.
    def visitExprRelacional(self, ctx:GramaticaParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#termRelacional.
    def visitTermRelacional(self, ctx:GramaticaParser.TermRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#exp.
    def visitExp(self, ctx:GramaticaParser.ExpContext):
        return self.visitChildren(ctx)



del GramaticaParser