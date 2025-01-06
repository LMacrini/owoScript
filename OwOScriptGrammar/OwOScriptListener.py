# Generated from OwOScriptGrammar/OwOScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OwOScriptParser import OwOScriptParser
else:
    from OwOScriptParser import OwOScriptParser

# This class defines a complete listener for a parse tree produced by OwOScriptParser.
class OwOScriptListener(ParseTreeListener):

    # Enter a parse tree produced by OwOScriptParser#script.
    def enterScript(self, ctx:OwOScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#script.
    def exitScript(self, ctx:OwOScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#statements.
    def enterStatements(self, ctx:OwOScriptParser.StatementsContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#statements.
    def exitStatements(self, ctx:OwOScriptParser.StatementsContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#definitions.
    def enterDefinitions(self, ctx:OwOScriptParser.DefinitionsContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#definitions.
    def exitDefinitions(self, ctx:OwOScriptParser.DefinitionsContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#statement.
    def enterStatement(self, ctx:OwOScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#statement.
    def exitStatement(self, ctx:OwOScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#expression.
    def enterExpression(self, ctx:OwOScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#expression.
    def exitExpression(self, ctx:OwOScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#number.
    def enterNumber(self, ctx:OwOScriptParser.NumberContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#number.
    def exitNumber(self, ctx:OwOScriptParser.NumberContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#bignumber.
    def enterBignumber(self, ctx:OwOScriptParser.BignumberContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#bignumber.
    def exitBignumber(self, ctx:OwOScriptParser.BignumberContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#integer.
    def enterInteger(self, ctx:OwOScriptParser.IntegerContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#integer.
    def exitInteger(self, ctx:OwOScriptParser.IntegerContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#command.
    def enterCommand(self, ctx:OwOScriptParser.CommandContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#command.
    def exitCommand(self, ctx:OwOScriptParser.CommandContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#functioncall.
    def enterFunctioncall(self, ctx:OwOScriptParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#functioncall.
    def exitFunctioncall(self, ctx:OwOScriptParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#definition.
    def enterDefinition(self, ctx:OwOScriptParser.DefinitionContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#definition.
    def exitDefinition(self, ctx:OwOScriptParser.DefinitionContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#ternary.
    def enterTernary(self, ctx:OwOScriptParser.TernaryContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#ternary.
    def exitTernary(self, ctx:OwOScriptParser.TernaryContext):
        pass


    # Enter a parse tree produced by OwOScriptParser#whileloop.
    def enterWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        pass

    # Exit a parse tree produced by OwOScriptParser#whileloop.
    def exitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        pass



del OwOScriptParser