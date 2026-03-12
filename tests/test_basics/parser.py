from antlr4 import InputStream, CommonTokenStream

from pyjsg.parser.jsgLexer import jsgLexer
from pyjsg.parser.jsgParser import jsgParser
from pyjsg.parser.jsgParserVisitor import jsgParserVisitor
from pyjsg.parser_impl.generate_python import ParseErrorListener
from pyjsg.parser_impl.jsg_doc_context import JSGDocContext


def parse(text: str, production_rule: str, listener) -> jsgParserVisitor | None:
    """ 
    Parse text fragment according to supplied production rule and evaluate with listener class.
    
    Example: parse("{1,*}", "ebnfSuffix", JSGEbnf)
    """
    error_listener = ParseErrorListener()
    lexer = jsgLexer(InputStream(text))
    lexer.addErrorListener(error_listener)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    if error_listener.n_errors:
        return None
    parser = jsgParser(tokens)
    parser.addErrorListener(error_listener)
    base_node = getattr(parser, production_rule)()
    listener_module = listener(JSGDocContext())
    listener_module.visit(base_node)
    return listener_module if not error_listener.n_errors else None
