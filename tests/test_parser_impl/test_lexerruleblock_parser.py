import sys
import unittest
from tokenize import Double
from typing import cast

from jsonasobj import JsonObj

import pyjsg.jsglib as jsg
import pyjsg.jsglib.jsg_null
from pyjsg.parser_impl.jsg_lexerruleblock_parser import JSGLexerRuleBlock
from tests.test_basics.parser import parse

# Force the needed imports
_x = isinstance(1, (jsg.JSGPattern, jsg.JSGString, jsg.String, jsg.Number, Double, jsg.Boolean, jsg.Integer,
                    pyjsg.jsglib.jsg_null.JSGNull, jsg.JSGArray, JsonObj))


# Required to get the lexer in the correct state
terminals = """@terminals
"""


t1 = "IRI : (PN_CHARS | '.' | ':' | '/' | '\\' | '#' | '@' | '%' | '&' | UCHAR)* ; " \
     "# <http://www.w3.org/TR/turtle/#grammar-production-IRIREF> "
t2 = "BNODE : '_:' (PN_CHARS_U | [0-9]) ((PN_CHARS | '.')* PN_CHARS)? ; " \
     "# <http://www.w3.org/TR/turtle/#grammar-production-BLANK_NODE_LABEL>"
t3 = 'BOOL : "true" | "false" ; # JSON boolean tokens'
t4 = 'INTEGER : [+-]? [0-9] + ; # <http://www.w3.org/TR/turtle/#grammar-production-INTEGER>'
t5 = "DECIMAL : [+-]? [0-9]* '.' [0-9] + ; # <http://www.w3.org/TR/turtle/#grammar-production-DECIMAL>"
t6 = "DOUBLE : [+-]? ([0-9] + '.' [0-9]* EXPONENT | '.' [0-9]+ EXPONENT | [0-9]+ EXPONENT) ; " \
     "# <http://www.w3.org/TR/turtle/#grammar-production-DOUBLE>"
t7 = 'STRING : .* ;'

t8 = "PN_PREFIX  : PN_CHARS_BASE ((PN_CHARS | '.')* PN_CHARS)? ;"
t9 = """PN_CHARS_BASE    : [A-Z] | [a-z] | [\u00C0-\u00D6] | [\u00D8-\u00F6]
                 | [\u00F8-\u02FF] | [\u0370-\u037D] | [\u037F-\u1FFF]
                 | [\u200C-\u200D] | [\u2070-\u218F] | [\u2C00-\u2FEF]
                 | [\u3001-\uD7FF] | [\uF900-\uFDCF] | [\uFDF0-\uFFFD]
                 | [\u10000-\uEFFFF] ;"""
t10 = "PN_CHARS : PN_CHARS_U | '-' | [0-9] | '\u00B7' | [\u0300-\u036F] | [\u203F-\u2040] ;"
t11 = "PN_CHARS_U       : PN_CHARS_BASE | '_' ;"
t12 = """UCHAR            : '\\u' HEX HEX HEX HEX
                 | '\\U' HEX HEX HEX HEX HEX HEX HEX HEX ; """
t13 = "HEX : [0-9] | [A-F] | [a-f] ; "
t14 = "EXPONENT : [eE] [+-]? [0-9]+ ; "
t15 = "LANGTAG          : '@' [a-zA-Z] + ('-' [a-zA-Z0-9] +)* ;"
t16 = "STR_: .* @string ;"
t17 = "NUMBER_ : .* @number ;"
t18 = "INT_: .* @int ;"
t19 = "BOOL_ : .* @bool ;"
t20 = "NULL_: .* @null ;"
# TODO: Figure out how these even parsed
# t21 = "ARRAY_ : .* @array ;"
# t22 = "OBJECT_: .* @object ;"
t23 = "POS_INT : [0]|([1-9][0-9]*) @int ;"

s1 = "pattern: r'(({PN_CHARS})|\.|:|/|\\\\|\#|@|%|\&|({UCHAR}))*'"
s2 = "pattern: r'_:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'"
s3 = "pattern: r'true|false'"
s4 = "pattern: r'[+-]?[0-9]+'"
s5 = "pattern: r'[+-]?[0-9]*\.[0-9]+'"
s6 = "pattern: r'[+-]?([0-9]+\.[0-9]*({EXPONENT})|\.[0-9]+({EXPONENT})|[0-9]+({EXPONENT}))'"
s7 = "pattern: r'.*'"
s8 = "pattern: r'({PN_CHARS_BASE})((({PN_CHARS})|\.)*({PN_CHARS}))?'"
s9 = "pattern: r'[A-Z]|[a-z]|[À-Ö]|[Ø-ö]|[ø-˿]|[Ͱ-ͽ]|[Ϳ-῿]|[‌-‍]|[⁰-↏]|[Ⰰ-⿯]|[、-퟿]|[豈-﷏]|[ﷰ-�]|[က0-F]'"
if sys.version_info < (3, 7):
    s10 = "pattern: r'({PN_CHARS_U})|\-|[0-9]|\·|[̀-ͯ]|[‿-⁀]'"
else:
    s10 = "pattern: r'({PN_CHARS_U})|\-|[0-9]|·|[̀-ͯ]|[‿-⁀]'"
s11 = "pattern: r'({PN_CHARS_BASE})|_'"
s12 = "pattern: r'\\\\u({HEX})({HEX})({HEX})({HEX})|\\\\U({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})'"
s13 = "pattern: r'[0-9]|[A-F]|[a-f]'"
s14 = "pattern: r'[eE][+-]?[0-9]+'"
if sys.version_info < (3, 7):
    s15 = "pattern: r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*'"
else:
    s15 = "pattern: r'@[a-zA-Z]+(\-[a-zA-Z0-9]+)*'"
s16 = "pattern: r'.*'"
s17 = "pattern: r'.*'"
s18 = "pattern: r'.*'"
s19 = "pattern: r'.*'"
s20 = "pattern: r'.*'"
s21 = "pattern: r'.*'"
s22 = "pattern: r'.*'"
s23 = "pattern: r'[0]|([1-9][0-9]*)'"


if sys.version_info < (3, 7):
    r1 = r'''class IRI(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(({PN_CHARS})|\.|\:|\/|\\|\#|\@|\%|\&|({UCHAR}))*'.format(PN_CHARS=PN_CHARS.pattern, UCHAR=UCHAR.pattern))'''
    r2 = '''class BNODE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'_\:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))'''
else:
    r1 = r'''class IRI(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(({PN_CHARS})|\.|:|/|\\|\#|@|%|\&|({UCHAR}))*'.format(PN_CHARS=PN_CHARS.pattern, UCHAR=UCHAR.pattern))'''
    r2 = '''class BNODE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'_:(({PN_CHARS_U})|[0-9])((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_U=PN_CHARS_U.pattern))'''

r3 = '''class BOOL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'true|false')'''
r4 = '''class INTEGER(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[+-]?[0-9]+')'''
r5 = '''class DECIMAL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[+-]?[0-9]*\.[0-9]+')'''
r6 = '''class DOUBLE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[+-]?([0-9]+\.[0-9]*({EXPONENT})|\.[0-9]+({EXPONENT})|[0-9]+({EXPONENT}))'.format(EXPONENT=EXPONENT.pattern))'''
r7 = '''class STRING(jsg.JSGString):
    pattern = jsg.JSGPattern(r'.*')'''
r8 = '''class PN_PREFIX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_BASE})((({PN_CHARS})|\.)*({PN_CHARS}))?'.format(PN_CHARS=PN_CHARS.pattern, PN_CHARS_BASE=PN_CHARS_BASE.pattern))'''
r9 = '''class PN_CHARS_BASE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z]|[a-z]|[À-Ö]|[Ø-ö]|[ø-˿]|[Ͱ-ͽ]|[Ϳ-῿]|[‌-‍]|[⁰-↏]|[Ⰰ-⿯]|[、-퟿]|[豈-﷏]|[ﷰ-�]|[က0-F]')'''
if sys.version_info < (3, 7):
    r10 = '''class PN_CHARS(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_U})|\-|[0-9]|\·|[̀-ͯ]|[‿-⁀]'.format(PN_CHARS_U=PN_CHARS_U.pattern))'''
else:
    r10 = '''class PN_CHARS(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_U})|\-|[0-9]|·|[̀-ͯ]|[‿-⁀]'.format(PN_CHARS_U=PN_CHARS_U.pattern))'''
r11 = '''class PN_CHARS_U(jsg.JSGString):
    pattern = jsg.JSGPattern(r'({PN_CHARS_BASE})|_'.format(PN_CHARS_BASE=PN_CHARS_BASE.pattern))'''
r12 = '''class UCHAR(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\\\\u({HEX})({HEX})({HEX})({HEX})|\\\\U({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})({HEX})'.format(HEX=HEX.pattern))'''
r13 = '''class HEX(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]|[A-F]|[a-f]')'''
r14 = '''class EXPONENT(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[eE][+-]?[0-9]+')'''
if sys.version_info < (3, 7):
    r15 = '''class LANGTAG(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')'''
else:
    r15 = '''class LANGTAG(jsg.JSGString):
    pattern = jsg.JSGPattern(r'@[a-zA-Z]+(\-[a-zA-Z0-9]+)*')'''
r16 = '''class STR_(jsg.String):
    pattern = jsg.JSGPattern(r'.*')'''
r17 = '''class NUMBER_(jsg.Number):
    pattern = jsg.JSGPattern(r'.*')'''
r18 = '''class INT_(jsg.Integer):
    pattern = jsg.JSGPattern(r'.*')'''
r19 = '''class BOOL_(jsg.Boolean):
    pattern = jsg.JSGPattern(r'.*')'''
r20 = '''class NULL_(jsg.JSGNull):
    pattern = jsg.JSGPattern(r'.*')'''
r21 = '''class ARRAY_(Array):
    pattern = jsg.JSGPattern(r'.*')'''
r22 = '''class OBJECT_(JsonObj):
    pattern = jsg.JSGPattern(r'.*')'''
r23 = '''class POS_INT(jsg.Integer):
    pattern = jsg.JSGPattern(r'[0]|([1-9][0-9]*)')'''


exec(r13)
exec(r12)
exec(r9)
exec(r11)
exec(r10)
exec(r14)


tests = [(t1, 'IRI', r1, s1), (t2, 'BNODE', r2, s2), (t3, 'BOOL', r3, s3), (t4, 'INTEGER', r4, s4),
         (t5, 'DECIMAL', r5, s5), (t6, 'DOUBLE', r6, s6), (t7, 'STRING', r7, s7), (t8, 'PN_PREFIX', r8, s8),
         (t9, 'PN_CHARS_BASE', r9, s9), (t10, 'PN_CHARS', r10, s10), (t11, 'PN_CHARS_U', r11, s11),
         (t12, 'UCHAR', r12, s12), (t13, 'HEX', r13, s13), (t14, 'EXPONENT', r14, s14), (t15, 'LANGTAG', r15, s15),
         (t16, 'STR_', r16, s16), (t17, 'NUMBER_', r17, s17), (t18, 'INT_', r18, s18),
         (t19, 'BOOL_', r19, s19), (t20, 'NULL_', r20, s20),
         # (t21, 'ARRAY_', r21, s21), (t22, 'OBJECT_', r22, s22),
         (t23, 'POS_INT', r23, s23)]


class LexerRuleBlockTestCase(unittest.TestCase):
    def test1(self):
        i = 0
        for text, k, rslt, s in tests:
            i += 1
            t = cast(JSGLexerRuleBlock, parse(terminals + text, "lexerRules", JSGLexerRuleBlock))
            self.assertEqual(s, str(t))
            t_python = t.as_python(k)
            self.assertEqual(rslt, t_python.strip())
            exec(t_python, globals(), locals())


if __name__ == '__main__':
    unittest.main()
