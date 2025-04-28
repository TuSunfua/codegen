# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0253\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u009c\n\4\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00a2\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6\u00ae\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00c0\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00d1\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00d9\n\r\3\r\3\r\3\16\3\16\5\16\u00df\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e9\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f2\n\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u0101\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\5\23\u010d\n\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0130\n\24\3\24\5")
        buf.write("\24\u0133\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0147\n\30\3\31\3\31\3\31\5\31\u014c\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\5\33\u0155\n\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\5\35\u0168\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u016f\n\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \7 \u017b\n \f \16 \u017e\13 \3!\3!\3!\3!\3!\3!\7")
        buf.write("!\u0186\n!\f!\16!\u0189\13!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u0192\n\"\f\"\16\"\u0195\13\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\7#\u01a0\n#\f#\16#\u01a3\13#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\7$\u01b1\n$\f$\16$\u01b4\13$\3")
        buf.write("%\3%\3%\3%\3%\5%\u01bb\n%\3&\3&\5&\u01bf\n&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3*\3*\3*\3+\3+\5+\u01ce\n+\3,\3,\3,\3")
        buf.write(",\3,\5,\u01d5\n,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u01e8\n\60\3\61\3\61\3\61")
        buf.write("\5\61\u01ed\n\61\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01f5")
        buf.write("\n\62\3\63\3\63\5\63\u01f9\n\63\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u01ff\n\64\3\65\3\65\3\65\3\65\5\65\u0205\n\65\3\65")
        buf.write("\3\65\5\65\u0209\n\65\3\65\3\65\3\65\5\65\u020e\n\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u0215\n\65\5\65\u0217\n\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u021d\n\65\3\65\3\65\5\65\u0221")
        buf.write("\n\65\7\65\u0223\n\65\f\65\16\65\u0226\13\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u0231\n\67\3")
        buf.write("8\38\38\38\39\39\39\39\59\u023b\n9\3:\3:\3:\5:\u0240\n")
        buf.write(":\3:\3:\3;\3;\3;\3<\3<\3=\3=\5=\u024b\n=\3>\3>\3?\3?\3")
        buf.write("@\3@\3@\2\b>@BDFhA\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\2\b\3\2\32\33\3\2\3\6\4\2\26\31\35\35\3\3\'\'")
        buf.write("\3\2+\60\3\2\649\2\u025a\2\u0080\3\2\2\2\4\u0087\3\2\2")
        buf.write("\2\6\u009b\3\2\2\2\b\u00a1\3\2\2\2\n\u00ad\3\2\2\2\f\u00af")
        buf.write("\3\2\2\2\16\u00b4\3\2\2\2\20\u00bf\3\2\2\2\22\u00c1\3")
        buf.write("\2\2\2\24\u00c5\3\2\2\2\26\u00d0\3\2\2\2\30\u00d2\3\2")
        buf.write("\2\2\32\u00de\3\2\2\2\34\u00e8\3\2\2\2\36\u00ea\3\2\2")
        buf.write("\2 \u00f5\3\2\2\2\"\u0104\3\2\2\2$\u010c\3\2\2\2&\u0132")
        buf.write("\3\2\2\2(\u0134\3\2\2\2*\u0138\3\2\2\2,\u013a\3\2\2\2")
        buf.write(".\u013c\3\2\2\2\60\u014b\3\2\2\2\62\u014d\3\2\2\2\64\u0151")
        buf.write("\3\2\2\2\66\u015c\3\2\2\28\u0167\3\2\2\2:\u016e\3\2\2")
        buf.write("\2<\u0170\3\2\2\2>\u0174\3\2\2\2@\u017f\3\2\2\2B\u018a")
        buf.write("\3\2\2\2D\u0196\3\2\2\2F\u01a4\3\2\2\2H\u01ba\3\2\2\2")
        buf.write("J\u01be\3\2\2\2L\u01c0\3\2\2\2N\u01c2\3\2\2\2P\u01c4\3")
        buf.write("\2\2\2R\u01c6\3\2\2\2T\u01cd\3\2\2\2V\u01d4\3\2\2\2X\u01d6")
        buf.write("\3\2\2\2Z\u01da\3\2\2\2\\\u01de\3\2\2\2^\u01e7\3\2\2\2")
        buf.write("`\u01ec\3\2\2\2b\u01f4\3\2\2\2d\u01f8\3\2\2\2f\u01fe\3")
        buf.write("\2\2\2h\u0216\3\2\2\2j\u0227\3\2\2\2l\u0230\3\2\2\2n\u0232")
        buf.write("\3\2\2\2p\u023a\3\2\2\2r\u023c\3\2\2\2t\u0243\3\2\2\2")
        buf.write("v\u0246\3\2\2\2x\u024a\3\2\2\2z\u024c\3\2\2\2|\u024e\3")
        buf.write("\2\2\2~\u0250\3\2\2\2\u0080\u0081\5\4\3\2\u0081\u0082")
        buf.write("\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\6\4\2\u0084\u0085")
        buf.write("\5\4\3\2\u0085\u0088\3\2\2\2\u0086\u0088\5\6\4\2\u0087")
        buf.write("\u0083\3\2\2\2\u0087\u0086\3\2\2\2\u0088\5\3\2\2\2\u0089")
        buf.write("\u008a\5\b\5\2\u008a\u008b\5z>\2\u008b\u009c\3\2\2\2\u008c")
        buf.write("\u008d\5\f\7\2\u008d\u008e\5z>\2\u008e\u009c\3\2\2\2\u008f")
        buf.write("\u0090\5\16\b\2\u0090\u0091\5z>\2\u0091\u009c\3\2\2\2")
        buf.write("\u0092\u0093\5\24\13\2\u0093\u0094\5z>\2\u0094\u009c\3")
        buf.write("\2\2\2\u0095\u0096\5\36\20\2\u0096\u0097\5z>\2\u0097\u009c")
        buf.write("\3\2\2\2\u0098\u0099\5 \21\2\u0099\u009a\5z>\2\u009a\u009c")
        buf.write("\3\2\2\2\u009b\u0089\3\2\2\2\u009b\u008c\3\2\2\2\u009b")
        buf.write("\u008f\3\2\2\2\u009b\u0092\3\2\2\2\u009b\u0095\3\2\2\2")
        buf.write("\u009b\u0098\3\2\2\2\u009c\7\3\2\2\2\u009d\u009e\7\22")
        buf.write("\2\2\u009e\u009f\7\35\2\2\u009f\u00a2\5x=\2\u00a0\u00a2")
        buf.write("\5\n\6\2\u00a1\u009d\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\t\3\2\2\2\u00a3\u00a4\7\22\2\2\u00a4\u00a5\7\35\2\2\u00a5")
        buf.write("\u00a6\5x=\2\u00a6\u00a7\7*\2\2\u00a7\u00a8\5> \2\u00a8")
        buf.write("\u00ae\3\2\2\2\u00a9\u00aa\7\22\2\2\u00aa\u00ab\7\35\2")
        buf.write("\2\u00ab\u00ac\7*\2\2\u00ac\u00ae\5> \2\u00ad\u00a3\3")
        buf.write("\2\2\2\u00ad\u00a9\3\2\2\2\u00ae\13\3\2\2\2\u00af\u00b0")
        buf.write("\7\21\2\2\u00b0\u00b1\7\35\2\2\u00b1\u00b2\7*\2\2\u00b2")
        buf.write("\u00b3\5> \2\u00b3\r\3\2\2\2\u00b4\u00b5\7\16\2\2\u00b5")
        buf.write("\u00b6\7\35\2\2\u00b6\u00b7\7\17\2\2\u00b7\u00b8\7\"\2")
        buf.write("\2\u00b8\u00b9\5\20\t\2\u00b9\u00ba\7#\2\2\u00ba\17\3")
        buf.write("\2\2\2\u00bb\u00bc\5\22\n\2\u00bc\u00bd\5\20\t\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00c0\5\22\n\2\u00bf\u00bb\3\2\2")
        buf.write("\2\u00bf\u00be\3\2\2\2\u00c0\21\3\2\2\2\u00c1\u00c2\7")
        buf.write("\35\2\2\u00c2\u00c3\5x=\2\u00c3\u00c4\5z>\2\u00c4\23\3")
        buf.write("\2\2\2\u00c5\u00c6\7\16\2\2\u00c6\u00c7\7\35\2\2\u00c7")
        buf.write("\u00c8\7\20\2\2\u00c8\u00c9\7\"\2\2\u00c9\u00ca\5\26\f")
        buf.write("\2\u00ca\u00cb\7#\2\2\u00cb\25\3\2\2\2\u00cc\u00cd\5\30")
        buf.write("\r\2\u00cd\u00ce\5\26\f\2\u00ce\u00d1\3\2\2\2\u00cf\u00d1")
        buf.write("\5\30\r\2\u00d0\u00cc\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\27\3\2\2\2\u00d2\u00d3\7\35\2\2\u00d3\u00d4\7 \2\2\u00d4")
        buf.write("\u00d5\5\32\16\2\u00d5\u00d8\7!\2\2\u00d6\u00d9\5x=\2")
        buf.write("\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\5z>\2\u00db\31")
        buf.write("\3\2\2\2\u00dc\u00df\5\34\17\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\33\3\2\2\2\u00e0")
        buf.write("\u00e1\5f\64\2\u00e1\u00e2\5x=\2\u00e2\u00e3\7&\2\2\u00e3")
        buf.write("\u00e4\5\34\17\2\u00e4\u00e9\3\2\2\2\u00e5\u00e6\5f\64")
        buf.write("\2\u00e6\u00e7\5x=\2\u00e7\u00e9\3\2\2\2\u00e8\u00e0\3")
        buf.write("\2\2\2\u00e8\u00e5\3\2\2\2\u00e9\35\3\2\2\2\u00ea\u00eb")
        buf.write("\7\r\2\2\u00eb\u00ec\7\35\2\2\u00ec\u00ed\7 \2\2\u00ed")
        buf.write("\u00ee\5\32\16\2\u00ee\u00f1\7!\2\2\u00ef\u00f2\5x=\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3")
        buf.write("\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5\"\22\2\u00f4")
        buf.write("\37\3\2\2\2\u00f5\u00f6\7\r\2\2\u00f6\u00f7\7 \2\2\u00f7")
        buf.write("\u00f8\7\35\2\2\u00f8\u00f9\7\35\2\2\u00f9\u00fa\7!\2")
        buf.write("\2\u00fa\u00fb\7\35\2\2\u00fb\u00fc\7 \2\2\u00fc\u00fd")
        buf.write("\5\32\16\2\u00fd\u0100\7!\2\2\u00fe\u0101\5x=\2\u00ff")
        buf.write("\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\5\"\22\2\u0103!\3\2\2")
        buf.write("\2\u0104\u0105\7\"\2\2\u0105\u0106\5$\23\2\u0106\u0107")
        buf.write("\7#\2\2\u0107#\3\2\2\2\u0108\u0109\5&\24\2\u0109\u010a")
        buf.write("\5$\23\2\u010a\u010d\3\2\2\2\u010b\u010d\5&\24\2\u010c")
        buf.write("\u0108\3\2\2\2\u010c\u010b\3\2\2\2\u010d%\3\2\2\2\u010e")
        buf.write("\u010f\5\b\5\2\u010f\u0110\5z>\2\u0110\u0133\3\2\2\2\u0111")
        buf.write("\u0112\5\f\7\2\u0112\u0113\5z>\2\u0113\u0133\3\2\2\2\u0114")
        buf.write("\u0115\5\"\22\2\u0115\u0116\5z>\2\u0116\u0133\3\2\2\2")
        buf.write("\u0117\u0118\5j\66\2\u0118\u0119\5z>\2\u0119\u0133\3\2")
        buf.write("\2\2\u011a\u011b\5h\65\2\u011b\u011c\7)\2\2\u011c\u011d")
        buf.write("\5j\66\2\u011d\u011e\5z>\2\u011e\u0133\3\2\2\2\u011f\u0120")
        buf.write("\5(\25\2\u0120\u0121\5z>\2\u0121\u0133\3\2\2\2\u0122\u0123")
        buf.write("\5.\30\2\u0123\u0124\5z>\2\u0124\u0133\3\2\2\2\u0125\u0126")
        buf.write("\5\60\31\2\u0126\u0127\5z>\2\u0127\u0133\3\2\2\2\u0128")
        buf.write("\u0129\7\23\2\2\u0129\u0133\5z>\2\u012a\u012b\7\24\2\2")
        buf.write("\u012b\u0133\5z>\2\u012c\u012f\7\f\2\2\u012d\u0130\5>")
        buf.write(" \2\u012e\u0130\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\5z>\2\u0132\u010e")
        buf.write("\3\2\2\2\u0132\u0111\3\2\2\2\u0132\u0114\3\2\2\2\u0132")
        buf.write("\u0117\3\2\2\2\u0132\u011a\3\2\2\2\u0132\u011f\3\2\2\2")
        buf.write("\u0132\u0122\3\2\2\2\u0132\u0125\3\2\2\2\u0132\u0128\3")
        buf.write("\2\2\2\u0132\u012a\3\2\2\2\u0132\u012c\3\2\2\2\u0133\'")
        buf.write("\3\2\2\2\u0134\u0135\5*\26\2\u0135\u0136\5|?\2\u0136\u0137")
        buf.write("\5,\27\2\u0137)\3\2\2\2\u0138\u0139\5h\65\2\u0139+\3\2")
        buf.write("\2\2\u013a\u013b\5> \2\u013b-\3\2\2\2\u013c\u013d\7\t")
        buf.write("\2\2\u013d\u013e\7 \2\2\u013e\u013f\5> \2\u013f\u0140")
        buf.write("\7!\2\2\u0140\u0146\5\"\22\2\u0141\u0142\7\n\2\2\u0142")
        buf.write("\u0147\5\"\22\2\u0143\u0144\7\n\2\2\u0144\u0147\5.\30")
        buf.write("\2\u0145\u0147\3\2\2\2\u0146\u0141\3\2\2\2\u0146\u0143")
        buf.write("\3\2\2\2\u0146\u0145\3\2\2\2\u0147/\3\2\2\2\u0148\u014c")
        buf.write("\5\62\32\2\u0149\u014c\5\64\33\2\u014a\u014c\5\66\34\2")
        buf.write("\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a\3")
        buf.write("\2\2\2\u014c\61\3\2\2\2\u014d\u014e\7\13\2\2\u014e\u014f")
        buf.write("\5> \2\u014f\u0150\5\"\22\2\u0150\63\3\2\2\2\u0151\u0154")
        buf.write("\7\13\2\2\u0152\u0155\5(\25\2\u0153\u0155\5\n\6\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\7\'\2\2\u0157\u0158\5> \2\u0158\u0159\7\'")
        buf.write("\2\2\u0159\u015a\5(\25\2\u015a\u015b\5\"\22\2\u015b\65")
        buf.write("\3\2\2\2\u015c\u015d\7\13\2\2\u015d\u015e\7\35\2\2\u015e")
        buf.write("\u015f\7&\2\2\u015f\u0160\7\35\2\2\u0160\u0161\7+\2\2")
        buf.write("\u0161\u0162\7\25\2\2\u0162\u0163\5h\65\2\u0163\u0164")
        buf.write("\5\"\22\2\u0164\67\3\2\2\2\u0165\u0168\5:\36\2\u0166\u0168")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("9\3\2\2\2\u0169\u016a\5> \2\u016a\u016b\7&\2\2\u016b\u016c")
        buf.write("\5:\36\2\u016c\u016f\3\2\2\2\u016d\u016f\5> \2\u016e\u0169")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f;\3\2\2\2\u0170\u0171")
        buf.write("\7 \2\2\u0171\u0172\5> \2\u0172\u0173\7!\2\2\u0173=\3")
        buf.write("\2\2\2\u0174\u0175\b \1\2\u0175\u0176\5@!\2\u0176\u017c")
        buf.write("\3\2\2\2\u0177\u0178\f\4\2\2\u0178\u0179\7\61\2\2\u0179")
        buf.write("\u017b\5@!\2\u017a\u0177\3\2\2\2\u017b\u017e\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d?\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0180\b!\1\2\u0180\u0181\5B\"\2\u0181")
        buf.write("\u0187\3\2\2\2\u0182\u0183\f\4\2\2\u0183\u0184\7\62\2")
        buf.write("\2\u0184\u0186\5B\"\2\u0185\u0182\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("A\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\b\"\1\2\u018b")
        buf.write("\u018c\5D#\2\u018c\u0193\3\2\2\2\u018d\u018e\f\4\2\2\u018e")
        buf.write("\u018f\5~@\2\u018f\u0190\5D#\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u018d\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194C\3\2\2\2\u0195\u0193\3\2\2")
        buf.write("\2\u0196\u0197\b#\1\2\u0197\u0198\5F$\2\u0198\u01a1\3")
        buf.write("\2\2\2\u0199\u019a\f\5\2\2\u019a\u019b\7:\2\2\u019b\u01a0")
        buf.write("\5F$\2\u019c\u019d\f\4\2\2\u019d\u019e\7;\2\2\u019e\u01a0")
        buf.write("\5F$\2\u019f\u0199\3\2\2\2\u019f\u019c\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("E\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b$\1\2\u01a5")
        buf.write("\u01a6\5H%\2\u01a6\u01b2\3\2\2\2\u01a7\u01a8\f\6\2\2\u01a8")
        buf.write("\u01a9\7<\2\2\u01a9\u01b1\5H%\2\u01aa\u01ab\f\5\2\2\u01ab")
        buf.write("\u01ac\7=\2\2\u01ac\u01b1\5H%\2\u01ad\u01ae\f\4\2\2\u01ae")
        buf.write("\u01af\7>\2\2\u01af\u01b1\5H%\2\u01b0\u01a7\3\2\2\2\u01b0")
        buf.write("\u01aa\3\2\2\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3G\3\2\2")
        buf.write("\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7;\2\2\u01b6\u01bb")
        buf.write("\5H%\2\u01b7\u01b8\7\63\2\2\u01b8\u01bb\5H%\2\u01b9\u01bb")
        buf.write("\5J&\2\u01ba\u01b5\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bbI\3\2\2\2\u01bc\u01bf\5d\63\2\u01bd\u01bf")
        buf.write("\5h\65\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("K\3\2\2\2\u01c0\u01c1\7\34\2\2\u01c1M\3\2\2\2\u01c2\u01c3")
        buf.write("\t\2\2\2\u01c3O\3\2\2\2\u01c4\u01c5\t\3\2\2\u01c5Q\3\2")
        buf.write("\2\2\u01c6\u01c7\7\35\2\2\u01c7\u01c8\7\"\2\2\u01c8\u01c9")
        buf.write("\5T+\2\u01c9\u01ca\7#\2\2\u01caS\3\2\2\2\u01cb\u01ce\5")
        buf.write("V,\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ceU\3\2\2\2\u01cf\u01d0\5X-\2\u01d0\u01d1")
        buf.write("\7&\2\2\u01d1\u01d2\5V,\2\u01d2\u01d5\3\2\2\2\u01d3\u01d5")
        buf.write("\5X-\2\u01d4\u01cf\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5W")
        buf.write("\3\2\2\2\u01d6\u01d7\7\35\2\2\u01d7\u01d8\7(\2\2\u01d8")
        buf.write("\u01d9\5> \2\u01d9Y\3\2\2\2\u01da\u01db\5p9\2\u01db\u01dc")
        buf.write("\5v<\2\u01dc\u01dd\5\\/\2\u01dd[\3\2\2\2\u01de\u01df\7")
        buf.write("\"\2\2\u01df\u01e0\5^\60\2\u01e0\u01e1\7#\2\2\u01e1]\3")
        buf.write("\2\2\2\u01e2\u01e3\5`\61\2\u01e3\u01e4\7&\2\2\u01e4\u01e5")
        buf.write("\5^\60\2\u01e5\u01e8\3\2\2\2\u01e6\u01e8\5`\61\2\u01e7")
        buf.write("\u01e2\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8_\3\2\2\2\u01e9")
        buf.write("\u01ed\5b\62\2\u01ea\u01ed\7\35\2\2\u01eb\u01ed\5\\/\2")
        buf.write("\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01eb\3")
        buf.write("\2\2\2\u01eda\3\2\2\2\u01ee\u01f5\5L\'\2\u01ef\u01f5\5")
        buf.write("N(\2\u01f0\u01f5\5P)\2\u01f1\u01f5\7\7\2\2\u01f2\u01f5")
        buf.write("\7\b\2\2\u01f3\u01f5\5R*\2\u01f4\u01ee\3\2\2\2\u01f4\u01ef")
        buf.write("\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5c\3\2\2\2\u01f6")
        buf.write("\u01f9\5b\62\2\u01f7\u01f9\5Z.\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9e\3\2\2\2\u01fa\u01fb\7\35\2\2\u01fb")
        buf.write("\u01fc\7&\2\2\u01fc\u01ff\5f\64\2\u01fd\u01ff\7\35\2\2")
        buf.write("\u01fe\u01fa\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffg\3\2\2")
        buf.write("\2\u0200\u0204\b\65\1\2\u0201\u0205\5j\66\2\u0202\u0205")
        buf.write("\5<\37\2\u0203\u0205\7\35\2\2\u0204\u0201\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0203\3\2\2\2\u0205\u0208\3\2\2\2")
        buf.write("\u0206\u0209\5l\67\2\u0207\u0209\3\2\2\2\u0208\u0206\3")
        buf.write("\2\2\2\u0208\u0207\3\2\2\2\u0209\u0217\3\2\2\2\u020a\u020d")
        buf.write("\5Z.\2\u020b\u020e\5l\67\2\u020c\u020e\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020d\u020c\3\2\2\2\u020e\u0217\3\2\2\2\u020f")
        buf.write("\u0210\5R*\2\u0210\u0211\7)\2\2\u0211\u0214\7\35\2\2\u0212")
        buf.write("\u0215\5l\67\2\u0213\u0215\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0214\u0213\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0200\3")
        buf.write("\2\2\2\u0216\u020a\3\2\2\2\u0216\u020f\3\2\2\2\u0217\u0224")
        buf.write("\3\2\2\2\u0218\u0219\f\6\2\2\u0219\u021c\7)\2\2\u021a")
        buf.write("\u021d\5j\66\2\u021b\u021d\7\35\2\2\u021c\u021a\3\2\2")
        buf.write("\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u0221")
        buf.write("\5l\67\2\u021f\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0218\3\2\2\2")
        buf.write("\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3")
        buf.write("\2\2\2\u0225i\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228")
        buf.write("\7\35\2\2\u0228\u0229\7 \2\2\u0229\u022a\58\35\2\u022a")
        buf.write("\u022b\7!\2\2\u022bk\3\2\2\2\u022c\u022d\5n8\2\u022d\u022e")
        buf.write("\5l\67\2\u022e\u0231\3\2\2\2\u022f\u0231\5n8\2\u0230\u022c")
        buf.write("\3\2\2\2\u0230\u022f\3\2\2\2\u0231m\3\2\2\2\u0232\u0233")
        buf.write("\7$\2\2\u0233\u0234\5> \2\u0234\u0235\7%\2\2\u0235o\3")
        buf.write("\2\2\2\u0236\u0237\5r:\2\u0237\u0238\5p9\2\u0238\u023b")
        buf.write("\3\2\2\2\u0239\u023b\5r:\2\u023a\u0236\3\2\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023bq\3\2\2\2\u023c\u023f\7$\2\2\u023d\u0240")
        buf.write("\5P)\2\u023e\u0240\7\35\2\2\u023f\u023d\3\2\2\2\u023f")
        buf.write("\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242\7%\2\2")
        buf.write("\u0242s\3\2\2\2\u0243\u0244\5p9\2\u0244\u0245\5v<\2\u0245")
        buf.write("u\3\2\2\2\u0246\u0247\t\4\2\2\u0247w\3\2\2\2\u0248\u024b")
        buf.write("\5v<\2\u0249\u024b\5t;\2\u024a\u0248\3\2\2\2\u024a\u0249")
        buf.write("\3\2\2\2\u024by\3\2\2\2\u024c\u024d\t\5\2\2\u024d{\3\2")
        buf.write("\2\2\u024e\u024f\t\6\2\2\u024f}\3\2\2\2\u0250\u0251\t")
        buf.write("\7\2\2\u0251\177\3\2\2\2\61\u0087\u009b\u00a1\u00ad\u00bf")
        buf.write("\u00d0\u00d8\u00de\u00e8\u00f1\u0100\u010c\u012f\u0132")
        buf.write("\u0146\u014b\u0154\u0167\u016e\u017c\u0187\u0193\u019f")
        buf.write("\u01a1\u01b0\u01b2\u01ba\u01be\u01cd\u01d4\u01e7\u01ec")
        buf.write("\u01f4\u01f8\u01fe\u0204\u0208\u020d\u0214\u0216\u021c")
        buf.write("\u0220\u0224\u0230\u023a\u023f\u024a")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'int'", "'float'", "'string'", "'boolean'", 
                     "'true'", "'false'", "'nil'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'", "'.'", "'='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'||'", "'&&'", "'!'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", 
                      "HEX_LIT", "FLOAT_LIT", "STRING_LIT", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "INT", 
                      "FLOAT", "STRING", "BOOLEAN", "TRUE", "FALSE", "NIL", 
                      "ID", "LINE_COMMENT", "BLOCK_COMMENT", "L_PAREN", 
                      "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", 
                      "COMMA", "SEMI", "COLON", "DOT", "ASSIGN", "DECLARE_ASSIGN", 
                      "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "LOGICAL_OR", "LOGICAL_AND", "LOGICAL_NOT", 
                      "EQUALS", "NOT_EQUALS", "LESS", "LESS_OR_EQUALS", 
                      "GREATER", "GREATER_OR_EQUALS", "PLUS", "MINUS", "STAR", 
                      "DIV", "MOD", "NEW_LINE", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_var_decl = 3
    RULE_var_decl_with_initialization = 4
    RULE_const_decl = 5
    RULE_struct_decl = 6
    RULE_struct_fields = 7
    RULE_struct_field = 8
    RULE_interface_decl = 9
    RULE_interface_methods = 10
    RULE_interface_method = 11
    RULE_params_list = 12
    RULE_params_list_prime = 13
    RULE_func_decl = 14
    RULE_method_decl = 15
    RULE_block_stmt = 16
    RULE_stmt_list = 17
    RULE_stmt = 18
    RULE_assign_stmt = 19
    RULE_lhs = 20
    RULE_rhs = 21
    RULE_branch_stmt = 22
    RULE_for_stmt = 23
    RULE_for_basic_stmt = 24
    RULE_for_iter_stmt = 25
    RULE_for_range_stmt = 26
    RULE_expr_list = 27
    RULE_expr_prime = 28
    RULE_sub_expr = 29
    RULE_expr = 30
    RULE_expr6 = 31
    RULE_expr5 = 32
    RULE_expr4 = 33
    RULE_expr3 = 34
    RULE_expr2 = 35
    RULE_expr1 = 36
    RULE_nil_lit = 37
    RULE_boolean_lit = 38
    RULE_int_lit = 39
    RULE_struct_lit = 40
    RULE_struct_lit_fields = 41
    RULE_struct_lit_fields_prime = 42
    RULE_struct_lit_field = 43
    RULE_array_lit = 44
    RULE_array_lit_elements = 45
    RULE_array_lit_elements_list = 46
    RULE_array_lit_element = 47
    RULE_non_array_literal = 48
    RULE_literal = 49
    RULE_id_list_cm = 50
    RULE_list_ac = 51
    RULE_call = 52
    RULE_dimension_list_expr = 53
    RULE_dimension_expr = 54
    RULE_dimension_list = 55
    RULE_dimension = 56
    RULE_array_type = 57
    RULE_primitive_type = 58
    RULE_data_type = 59
    RULE_eos = 60
    RULE_assignment_operator = 61
    RULE_relational_operator = 62

    ruleNames =  [ "program", "decl_list", "decl", "var_decl", "var_decl_with_initialization", 
                   "const_decl", "struct_decl", "struct_fields", "struct_field", 
                   "interface_decl", "interface_methods", "interface_method", 
                   "params_list", "params_list_prime", "func_decl", "method_decl", 
                   "block_stmt", "stmt_list", "stmt", "assign_stmt", "lhs", 
                   "rhs", "branch_stmt", "for_stmt", "for_basic_stmt", "for_iter_stmt", 
                   "for_range_stmt", "expr_list", "expr_prime", "sub_expr", 
                   "expr", "expr6", "expr5", "expr4", "expr3", "expr2", 
                   "expr1", "nil_lit", "boolean_lit", "int_lit", "struct_lit", 
                   "struct_lit_fields", "struct_lit_fields_prime", "struct_lit_field", 
                   "array_lit", "array_lit_elements", "array_lit_elements_list", 
                   "array_lit_element", "non_array_literal", "literal", 
                   "id_list_cm", "list_ac", "call", "dimension_list_expr", 
                   "dimension_expr", "dimension_list", "dimension", "array_type", 
                   "primitive_type", "data_type", "eos", "assignment_operator", 
                   "relational_operator" ]

    EOF = Token.EOF
    DECIMAL_LIT=1
    BINARY_LIT=2
    OCTAL_LIT=3
    HEX_LIT=4
    FLOAT_LIT=5
    STRING_LIT=6
    IF=7
    ELSE=8
    FOR=9
    RETURN=10
    FUNC=11
    TYPE=12
    STRUCT=13
    INTERFACE=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    INT=20
    FLOAT=21
    STRING=22
    BOOLEAN=23
    TRUE=24
    FALSE=25
    NIL=26
    ID=27
    LINE_COMMENT=28
    BLOCK_COMMENT=29
    L_PAREN=30
    R_PAREN=31
    L_CURLY=32
    R_CURLY=33
    L_BRACKET=34
    R_BRACKET=35
    COMMA=36
    SEMI=37
    COLON=38
    DOT=39
    ASSIGN=40
    DECLARE_ASSIGN=41
    PLUS_ASSIGN=42
    MINUS_ASSIGN=43
    MUL_ASSIGN=44
    DIV_ASSIGN=45
    MOD_ASSIGN=46
    LOGICAL_OR=47
    LOGICAL_AND=48
    LOGICAL_NOT=49
    EQUALS=50
    NOT_EQUALS=51
    LESS=52
    LESS_OR_EQUALS=53
    GREATER=54
    GREATER_OR_EQUALS=55
    PLUS=56
    MINUS=57
    STAR=58
    DIV=59
    MOD=60
    NEW_LINE=61
    WS=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.decl_list()
            self.state = 127
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = MiniGoParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decl()
                self.state = 130
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.var_decl()
                self.state = 136
                self.eos()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.const_decl()
                self.state = 139
                self.eos()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.struct_decl()
                self.state = 142
                self.eos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.interface_decl()
                self.state = 145
                self.eos()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.func_decl()
                self.state = 148
                self.eos()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.method_decl()
                self.state = 151
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def var_decl_with_initialization(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_with_initializationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(MiniGoParser.VAR)
                self.state = 156
                self.match(MiniGoParser.ID)
                self.state = 157
                self.data_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.var_decl_with_initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_with_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_with_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_with_initialization" ):
                return visitor.visitVar_decl_with_initialization(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_with_initialization(self):

        localctx = MiniGoParser.Var_decl_with_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl_with_initialization)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(MiniGoParser.VAR)
                self.state = 162
                self.match(MiniGoParser.ID)
                self.state = 163
                self.data_type()
                self.state = 164
                self.match(MiniGoParser.ASSIGN)
                self.state = 165
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(MiniGoParser.VAR)
                self.state = 168
                self.match(MiniGoParser.ID)
                self.state = 169
                self.match(MiniGoParser.ASSIGN)
                self.state = 170
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.CONST)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.ASSIGN)
            self.state = 176
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.TYPE)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 180
            self.match(MiniGoParser.STRUCT)
            self.state = 181
            self.match(MiniGoParser.L_CURLY)
            self.state = 182
            self.struct_fields()
            self.state = 183
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_fields" ):
                return visitor.visitStruct_fields(self)
            else:
                return visitor.visitChildren(self)




    def struct_fields(self):

        localctx = MiniGoParser.Struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_fields)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.struct_field()
                self.state = 186
                self.struct_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.struct_field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.ID)
            self.state = 192
            self.data_type()
            self.state = 193
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodsContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.TYPE)
            self.state = 196
            self.match(MiniGoParser.ID)
            self.state = 197
            self.match(MiniGoParser.INTERFACE)
            self.state = 198
            self.match(MiniGoParser.L_CURLY)
            self.state = 199
            self.interface_methods()
            self.state = 200
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_methods" ):
                return visitor.visitInterface_methods(self)
            else:
                return visitor.visitChildren(self)




    def interface_methods(self):

        localctx = MiniGoParser.Interface_methodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interface_methods)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.interface_method()
                self.state = 203
                self.interface_methods()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.interface_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interface_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.ID)
            self.state = 209
            self.match(MiniGoParser.L_PAREN)
            self.state = 210
            self.params_list()
            self.state = 211
            self.match(MiniGoParser.R_PAREN)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN, MiniGoParser.ID, MiniGoParser.L_BRACKET]:
                self.state = 212
                self.data_type()
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 216
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_list_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Params_list_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = MiniGoParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params_list)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.params_list_prime()
                pass
            elif token in [MiniGoParser.R_PAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class Params_list_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_cm(self):
            return self.getTypedRuleContext(MiniGoParser.Id_list_cmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params_list_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Params_list_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params_list_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list_prime" ):
                return visitor.visitParams_list_prime(self)
            else:
                return visitor.visitChildren(self)




    def params_list_prime(self):

        localctx = MiniGoParser.Params_list_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params_list_prime)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.id_list_cm()
                self.state = 223
                self.data_type()
                self.state = 224
                self.match(MiniGoParser.COMMA)
                self.state = 225
                self.params_list_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.id_list_cm()
                self.state = 228
                self.data_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MiniGoParser.FUNC)
            self.state = 233
            self.match(MiniGoParser.ID)
            self.state = 234
            self.match(MiniGoParser.L_PAREN)
            self.state = 235
            self.params_list()
            self.state = 236
            self.match(MiniGoParser.R_PAREN)
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN, MiniGoParser.ID, MiniGoParser.L_BRACKET]:
                self.state = 237
                self.data_type()
                pass
            elif token in [MiniGoParser.L_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 241
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def L_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.L_PAREN)
            else:
                return self.getToken(MiniGoParser.L_PAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def R_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.R_PAREN)
            else:
                return self.getToken(MiniGoParser.R_PAREN, i)

        def params_list(self):
            return self.getTypedRuleContext(MiniGoParser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MiniGoParser.FUNC)
            self.state = 244
            self.match(MiniGoParser.L_PAREN)
            self.state = 245
            self.match(MiniGoParser.ID)
            self.state = 246
            self.match(MiniGoParser.ID)
            self.state = 247
            self.match(MiniGoParser.R_PAREN)
            self.state = 248
            self.match(MiniGoParser.ID)
            self.state = 249
            self.match(MiniGoParser.L_PAREN)
            self.state = 250
            self.params_list()
            self.state = 251
            self.match(MiniGoParser.R_PAREN)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN, MiniGoParser.ID, MiniGoParser.L_BRACKET]:
                self.state = 252
                self.data_type()
                pass
            elif token in [MiniGoParser.L_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 256
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MiniGoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.L_CURLY)
            self.state = 259
            self.stmt_list()
            self.state = 260
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt_list)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.stmt()
                self.state = 263
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def call(self):
            return self.getTypedRuleContext(MiniGoParser.CallContext,0)


        def list_ac(self):
            return self.getTypedRuleContext(MiniGoParser.List_acContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def branch_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Branch_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.var_decl()
                self.state = 269
                self.eos()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.const_decl()
                self.state = 272
                self.eos()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.block_stmt()
                self.state = 275
                self.eos()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.call()
                self.state = 278
                self.eos()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.list_ac(0)
                self.state = 281
                self.match(MiniGoParser.DOT)
                self.state = 282
                self.call()
                self.state = 283
                self.eos()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.assign_stmt()
                self.state = 286
                self.eos()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.branch_stmt()
                self.state = 289
                self.eos()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 291
                self.for_stmt()
                self.state = 292
                self.eos()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 294
                self.match(MiniGoParser.CONTINUE)
                self.state = 295
                self.eos()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 296
                self.match(MiniGoParser.BREAK)
                self.state = 297
                self.eos()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 298
                self.match(MiniGoParser.RETURN)
                self.state = 301
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.ID, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.LOGICAL_NOT, MiniGoParser.MINUS]:
                    self.state = 299
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.EOF, MiniGoParser.SEMI]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 303
                self.eos()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.lhs()
            self.state = 307
            self.assignment_operator()
            self.state = 308
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ac(self):
            return self.getTypedRuleContext(MiniGoParser.List_acContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.list_ac(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def branch_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Branch_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_branch_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_stmt" ):
                return visitor.visitBranch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def branch_stmt(self):

        localctx = MiniGoParser.Branch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_branch_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MiniGoParser.IF)
            self.state = 315
            self.match(MiniGoParser.L_PAREN)
            self.state = 316
            self.expr(0)
            self.state = 317
            self.match(MiniGoParser.R_PAREN)
            self.state = 318
            self.block_stmt()
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 319
                self.match(MiniGoParser.ELSE)
                self.state = 320
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 321
                self.match(MiniGoParser.ELSE)
                self.state = 322
                self.branch_stmt()
                pass

            elif la_ == 3:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_basic_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_basic_stmtContext,0)


        def for_iter_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_iter_stmtContext,0)


        def for_range_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_range_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.for_basic_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.for_iter_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.for_range_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basic_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic_stmt" ):
                return visitor.visitFor_basic_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_basic_stmt(self):

        localctx = MiniGoParser.For_basic_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_basic_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.FOR)
            self.state = 332
            self.expr(0)
            self.state = 333
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iter_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,i)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def var_decl_with_initialization(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_with_initializationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_iter_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_iter_stmt" ):
                return visitor.visitFor_iter_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_iter_stmt(self):

        localctx = MiniGoParser.For_iter_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_iter_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.FOR)
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET]:
                self.state = 336
                self.assign_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 337
                self.var_decl_with_initialization()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 340
            self.match(MiniGoParser.SEMI)
            self.state = 341
            self.expr(0)
            self.state = 342
            self.match(MiniGoParser.SEMI)
            self.state = 343
            self.assign_stmt()
            self.state = 344
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_range_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def list_ac(self):
            return self.getTypedRuleContext(MiniGoParser.List_acContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range_stmt" ):
                return visitor.visitFor_range_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_range_stmt(self):

        localctx = MiniGoParser.For_range_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_range_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MiniGoParser.FOR)
            self.state = 347
            self.match(MiniGoParser.ID)
            self.state = 348
            self.match(MiniGoParser.COMMA)
            self.state = 349
            self.match(MiniGoParser.ID)
            self.state = 350
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 351
            self.match(MiniGoParser.RANGE)
            self.state = 352
            self.list_ac(0)
            self.state = 353
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.ID, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.LOGICAL_NOT, MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.expr_prime()
                pass
            elif token in [MiniGoParser.R_PAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class Expr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_prime" ):
                return visitor.visitExpr_prime(self)
            else:
                return visitor.visitChildren(self)




    def expr_prime(self):

        localctx = MiniGoParser.Expr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr_prime)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.expr(0)
                self.state = 360
                self.match(MiniGoParser.COMMA)
                self.state = 361
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = MiniGoParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.L_PAREN)
            self.state = 367
            self.expr(0)
            self.state = 368
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LOGICAL_OR(self):
            return self.getToken(MiniGoParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 373
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 374
                    self.match(MiniGoParser.LOGICAL_OR)
                    self.state = 375
                    self.expr6(0) 
                self.state = 380
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LOGICAL_AND(self):
            return self.getToken(MiniGoParser.LOGICAL_AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 384
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 385
                    self.match(MiniGoParser.LOGICAL_AND)
                    self.state = 386
                    self.expr5(0) 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def relational_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 395
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 396
                    self.relational_operator()
                    self.state = 397
                    self.expr4(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 413
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 407
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 408
                        self.match(MiniGoParser.PLUS)
                        self.state = 409
                        self.expr3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(MiniGoParser.MINUS)
                        self.state = 412
                        self.expr3(0)
                        pass

             
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def STAR(self):
            return self.getToken(MiniGoParser.STAR, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 421
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 422
                        self.match(MiniGoParser.STAR)
                        self.state = 423
                        self.expr2()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 424
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 425
                        self.match(MiniGoParser.DIV)
                        self.state = 426
                        self.expr2()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 427
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 428
                        self.match(MiniGoParser.MOD)
                        self.state = 429
                        self.expr2()
                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def LOGICAL_NOT(self):
            return self.getToken(MiniGoParser.LOGICAL_NOT, 0)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = MiniGoParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr2)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(MiniGoParser.MINUS)
                self.state = 436
                self.expr2()
                pass
            elif token in [MiniGoParser.LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(MiniGoParser.LOGICAL_NOT)
                self.state = 438
                self.expr2()
                pass
            elif token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.ID, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.expr1()
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


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def list_ac(self):
            return self.getTypedRuleContext(MiniGoParser.List_acContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MiniGoParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr1)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.list_ac(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nil_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nil_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_lit" ):
                return visitor.visitNil_lit(self)
            else:
                return visitor.visitChildren(self)




    def nil_lit(self):

        localctx = MiniGoParser.Nil_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_nil_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_boolean_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_lit" ):
                return visitor.visitBoolean_lit(self)
            else:
                return visitor.visitChildren(self)




    def boolean_lit(self):

        localctx = MiniGoParser.Boolean_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def BINARY_LIT(self):
            return self.getToken(MiniGoParser.BINARY_LIT, 0)

        def OCTAL_LIT(self):
            return self.getToken(MiniGoParser.OCTAL_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = MiniGoParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECIMAL_LIT) | (1 << MiniGoParser.BINARY_LIT) | (1 << MiniGoParser.OCTAL_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def struct_lit_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_fieldsContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MiniGoParser.ID)
            self.state = 453
            self.match(MiniGoParser.L_CURLY)
            self.state = 454
            self.struct_lit_fields()
            self.state = 455
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_lit_fields_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_fields_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_fields" ):
                return visitor.visitStruct_lit_fields(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_fields(self):

        localctx = MiniGoParser.Struct_lit_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_lit_fields)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.struct_lit_fields_prime()
                pass
            elif token in [MiniGoParser.R_CURLY]:
                self.enterOuterAlt(localctx, 2)

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


    class Struct_lit_fields_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_lit_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_fieldContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_lit_fields_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_fields_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_fields_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_fields_prime" ):
                return visitor.visitStruct_lit_fields_prime(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_fields_prime(self):

        localctx = MiniGoParser.Struct_lit_fields_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_lit_fields_prime)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.struct_lit_field()
                self.state = 462
                self.match(MiniGoParser.COMMA)
                self.state = 463
                self.struct_lit_fields_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.struct_lit_field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_field" ):
                return visitor.visitStruct_lit_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_field(self):

        localctx = MiniGoParser.Struct_lit_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_lit_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.ID)
            self.state = 469
            self.match(MiniGoParser.COLON)
            self.state = 470
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_lit_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.dimension_list()
            self.state = 473
            self.primitive_type()
            self.state = 474
            self.array_lit_elements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def array_lit_elements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elements_listContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_elements" ):
                return visitor.visitArray_lit_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_elements(self):

        localctx = MiniGoParser.Array_lit_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_lit_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.L_CURLY)
            self.state = 477
            self.array_lit_elements_list()
            self.state = 478
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_lit_elements_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elements_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_elements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_elements_list" ):
                return visitor.visitArray_lit_elements_list(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_elements_list(self):

        localctx = MiniGoParser.Array_lit_elements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_lit_elements_list)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.array_lit_element()
                self.state = 481
                self.match(MiniGoParser.COMMA)
                self.state = 482
                self.array_lit_elements_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.array_lit_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Non_array_literalContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_lit_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_element" ):
                return visitor.visitArray_lit_element(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_element(self):

        localctx = MiniGoParser.Array_lit_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_lit_element)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.non_array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 489
                self.array_lit_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nil_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Nil_litContext,0)


        def boolean_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Boolean_litContext,0)


        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_non_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_array_literal" ):
                return visitor.visitNon_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def non_array_literal(self):

        localctx = MiniGoParser.Non_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_non_array_literal)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.nil_lit()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.boolean_lit()
                pass
            elif token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 496
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 497
                self.struct_lit()
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Non_array_literalContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.non_array_literal()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.array_lit()
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


    class Id_list_cmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_list_cm(self):
            return self.getTypedRuleContext(MiniGoParser.Id_list_cmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list_cm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list_cm" ):
                return visitor.visitId_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def id_list_cm(self):

        localctx = MiniGoParser.Id_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_id_list_cm)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(MiniGoParser.ID)
                self.state = 505
                self.match(MiniGoParser.COMMA)
                self.state = 506
                self.id_list_cm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_acContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(MiniGoParser.CallContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Sub_exprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dimension_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_exprContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def list_ac(self):
            return self.getTypedRuleContext(MiniGoParser.List_acContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ac

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ac" ):
                return visitor.visitList_ac(self)
            else:
                return visitor.visitChildren(self)



    def list_ac(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.List_acContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_list_ac, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 514
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 511
                    self.call()
                    pass

                elif la_ == 2:
                    self.state = 512
                    self.sub_expr()
                    pass

                elif la_ == 3:
                    self.state = 513
                    self.match(MiniGoParser.ID)
                    pass


                self.state = 518
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 516
                    self.dimension_list_expr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 520
                self.array_lit()
                self.state = 523
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 521
                    self.dimension_list_expr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 3:
                self.state = 525
                self.struct_lit()
                self.state = 526
                self.match(MiniGoParser.DOT)
                self.state = 527
                self.match(MiniGoParser.ID)
                self.state = 530
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 528
                    self.dimension_list_expr()
                    pass

                elif la_ == 2:
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.List_acContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_list_ac)
                    self.state = 534
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 535
                    self.match(MiniGoParser.DOT)
                    self.state = 538
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        self.state = 536
                        self.call()
                        pass

                    elif la_ == 2:
                        self.state = 537
                        self.match(MiniGoParser.ID)
                        pass


                    self.state = 542
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 540
                        self.dimension_list_expr()
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MiniGoParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.L_PAREN)
            self.state = 551
            self.expr_list()
            self.state = 552
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_list_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_exprContext,0)


        def dimension_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list_expr" ):
                return visitor.visitDimension_list_expr(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list_expr(self):

        localctx = MiniGoParser.Dimension_list_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_dimension_list_expr)
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.dimension_expr()
                self.state = 555
                self.dimension_list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.dimension_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_expr" ):
                return visitor.visitDimension_expr(self)
            else:
                return visitor.visitChildren(self)




    def dimension_expr(self):

        localctx = MiniGoParser.Dimension_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_dimension_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(MiniGoParser.L_BRACKET)
            self.state = 561
            self.expr(0)
            self.state = 562
            self.match(MiniGoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = MiniGoParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_dimension_list)
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.dimension()
                self.state = 565
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MiniGoParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(MiniGoParser.L_BRACKET)
            self.state = 573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT]:
                self.state = 571
                self.int_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 572
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 575
            self.match(MiniGoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.dimension_list()
            self.state = 578
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_data_type)
        try:
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.primitive_type()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.array_type()
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


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.EOF or _la==MiniGoParser.SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECLARE_ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(MiniGoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MiniGoParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_OR_EQUALS(self):
            return self.getToken(MiniGoParser.LESS_OR_EQUALS, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_OR_EQUALS(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQUALS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = MiniGoParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALS) | (1 << MiniGoParser.NOT_EQUALS) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESS_OR_EQUALS) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_OR_EQUALS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.expr_sempred
        self._predicates[31] = self.expr6_sempred
        self._predicates[32] = self.expr5_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[51] = self.list_ac_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def list_ac_sempred(self, localctx:List_acContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         




