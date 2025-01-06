# Generated from OwOScriptGrammar/OwOScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OwOScriptParser import OwOScriptParser
else:
    from OwOScriptParser import OwOScriptParser

# This class defines a complete generic visitor for a parse tree produced by OwOScriptParser.

class OwOScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OwOScriptParser#script.
    def visitScript(self, ctx:OwOScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#statements.
    def visitStatements(self, ctx:OwOScriptParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#definitions.
    def visitDefinitions(self, ctx:OwOScriptParser.DefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#statement.
    def visitStatement(self, ctx:OwOScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#expression.
    def visitExpression(self, ctx:OwOScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#number.
    def visitNumber(self, ctx:OwOScriptParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#bignumber.
    def visitBignumber(self, ctx:OwOScriptParser.BignumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#integer.
    def visitInteger(self, ctx:OwOScriptParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#command.
    def visitCommand(self, ctx:OwOScriptParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#functioncall.
    def visitFunctioncall(self, ctx:OwOScriptParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#definition.
    def visitDefinition(self, ctx:OwOScriptParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#ternary.
    def visitTernary(self, ctx:OwOScriptParser.TernaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#whileloop.
    def visitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        return self.visitChildren(ctx)



del OwOScriptParser