# Generated from OwOScriptGrammar/OwOScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,1,4,1,32,8,1,11,1,12,1,33,1,2,5,2,37,8,2,10,2,12,2,40,
        9,2,1,3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,3,4,53,8,4,1,
        5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,1,1,0,2,4,81,0,26,1,0,0,0,2,31,1,0,0,0,4,38,1,0,0,0,6,46,1,0,0,
        0,8,52,1,0,0,0,10,54,1,0,0,0,12,57,1,0,0,0,14,60,1,0,0,0,16,62,1,
        0,0,0,18,64,1,0,0,0,20,67,1,0,0,0,22,73,1,0,0,0,24,82,1,0,0,0,26,
        27,3,4,2,0,27,28,3,2,1,0,28,29,5,0,0,1,29,1,1,0,0,0,30,32,3,6,3,
        0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,3,1,
        0,0,0,35,37,3,20,10,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,
        38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,42,3,8,4,0,42,43,5,1,
        0,0,43,47,1,0,0,0,44,47,3,22,11,0,45,47,3,24,12,0,46,41,1,0,0,0,
        46,44,1,0,0,0,46,45,1,0,0,0,47,7,1,0,0,0,48,53,3,10,5,0,49,53,3,
        12,6,0,50,53,3,16,8,0,51,53,3,18,9,0,52,48,1,0,0,0,52,49,1,0,0,0,
        52,50,1,0,0,0,52,51,1,0,0,0,53,9,1,0,0,0,54,55,7,0,0,0,55,56,5,17,
        0,0,56,11,1,0,0,0,57,58,5,5,0,0,58,59,3,14,7,0,59,13,1,0,0,0,60,
        61,5,18,0,0,61,15,1,0,0,0,62,63,5,20,0,0,63,17,1,0,0,0,64,65,5,20,
        0,0,65,66,5,6,0,0,66,19,1,0,0,0,67,68,5,7,0,0,68,69,5,20,0,0,69,
        70,5,8,0,0,70,71,3,2,1,0,71,72,5,9,0,0,72,21,1,0,0,0,73,74,5,10,
        0,0,74,75,5,8,0,0,75,76,3,2,1,0,76,77,5,9,0,0,77,78,5,11,0,0,78,
        79,5,8,0,0,79,80,3,2,1,0,80,81,5,9,0,0,81,23,1,0,0,0,82,83,5,12,
        0,0,83,84,5,8,0,0,84,85,3,2,1,0,85,86,5,9,0,0,86,25,1,0,0,0,4,33,
        38,46,52
    ]

class OwOScriptParser ( Parser ):

    grammarFileName = "OwOScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'literal'", "'lit'", "'l'", "'number'", 
                     "'()'", "'func'", "'{'", "'}'", "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "LINE_COMMENT", "HASH_COMMENT", 
                      "WS", "SINGLE_HEX_DIGIT", "NUMBER", "DECIMAL_INTEGER", 
                      "IDENTIFIER" ]

    RULE_script = 0
    RULE_statements = 1
    RULE_definitions = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_number = 5
    RULE_bignumber = 6
    RULE_integer = 7
    RULE_command = 8
    RULE_functioncall = 9
    RULE_definition = 10
    RULE_ternary = 11
    RULE_whileloop = 12

    ruleNames =  [ "script", "statements", "definitions", "statement", "expression", 
                   "number", "bignumber", "integer", "command", "functioncall", 
                   "definition", "ternary", "whileloop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    COMMENT=13
    LINE_COMMENT=14
    HASH_COMMENT=15
    WS=16
    SINGLE_HEX_DIGIT=17
    NUMBER=18
    DECIMAL_INTEGER=19
    IDENTIFIER=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definitions(self):
            return self.getTypedRuleContext(OwOScriptParser.DefinitionsContext,0)


        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(OwOScriptParser.EOF, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = OwOScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.definitions()
            self.state = 27
            self.statements()
            self.state = 28
            self.match(OwOScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = OwOScriptParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1053756) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.DefinitionContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_definitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitions" ):
                listener.enterDefinitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitions" ):
                listener.exitDefinitions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitions" ):
                return visitor.visitDefinitions(self)
            else:
                return visitor.visitChildren(self)




    def definitions(self):

        localctx = OwOScriptParser.DefinitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 35
                self.definition()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OwOScriptParser.ExpressionContext,0)


        def ternary(self):
            return self.getTypedRuleContext(OwOScriptParser.TernaryContext,0)


        def whileloop(self):
            return self.getTypedRuleContext(OwOScriptParser.WhileloopContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OwOScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(OwOScriptParser.T__0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.ternary()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.whileloop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(OwOScriptParser.NumberContext,0)


        def bignumber(self):
            return self.getTypedRuleContext(OwOScriptParser.BignumberContext,0)


        def command(self):
            return self.getTypedRuleContext(OwOScriptParser.CommandContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(OwOScriptParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OwOScriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.bignumber()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.command()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_HEX_DIGIT(self):
            return self.getToken(OwOScriptParser.SINGLE_HEX_DIGIT, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = OwOScriptParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(OwOScriptParser.SINGLE_HEX_DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BignumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(OwOScriptParser.IntegerContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_bignumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBignumber" ):
                listener.enterBignumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBignumber" ):
                listener.exitBignumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBignumber" ):
                return visitor.visitBignumber(self)
            else:
                return visitor.visitChildren(self)




    def bignumber(self):

        localctx = OwOScriptParser.BignumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bignumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(OwOScriptParser.T__4)
            self.state = 58
            self.integer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(OwOScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = OwOScriptParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(OwOScriptParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = OwOScriptParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(OwOScriptParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = OwOScriptParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(OwOScriptParser.IDENTIFIER)
            self.state = 65
            self.match(OwOScriptParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = OwOScriptParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(OwOScriptParser.T__6)
            self.state = 68
            self.match(OwOScriptParser.IDENTIFIER)
            self.state = 69
            self.match(OwOScriptParser.T__7)
            self.state = 70
            self.statements()
            self.state = 71
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.StatementsContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.StatementsContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_ternary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernary" ):
                listener.enterTernary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernary" ):
                listener.exitTernary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernary" ):
                return visitor.visitTernary(self)
            else:
                return visitor.visitChildren(self)




    def ternary(self):

        localctx = OwOScriptParser.TernaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ternary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(OwOScriptParser.T__9)
            self.state = 74
            self.match(OwOScriptParser.T__7)
            self.state = 75
            self.statements()
            self.state = 76
            self.match(OwOScriptParser.T__8)
            self.state = 77
            self.match(OwOScriptParser.T__10)
            self.state = 78
            self.match(OwOScriptParser.T__7)
            self.state = 79
            self.statements()
            self.state = 80
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_whileloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileloop" ):
                listener.enterWhileloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileloop" ):
                listener.exitWhileloop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileloop" ):
                return visitor.visitWhileloop(self)
            else:
                return visitor.visitChildren(self)




    def whileloop(self):

        localctx = OwOScriptParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(OwOScriptParser.T__11)
            self.state = 83
            self.match(OwOScriptParser.T__7)
            self.state = 84
            self.statements()
            self.state = 85
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





