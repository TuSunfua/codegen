# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2213841
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\7\2\u008f\n\2\f\2\16\2\u0092")
        buf.write("\13\2\5\2\u0094\n\2\3\3\3\3\3\3\6\3\u0099\n\3\r\3\16\3")
        buf.write("\u009a\3\4\3\4\3\4\6\4\u00a0\n\4\r\4\16\4\u00a1\3\5\3")
        buf.write("\5\3\5\6\5\u00a7\n\5\r\5\16\5\u00a8\3\6\6\6\u00ac\n\6")
        buf.write("\r\6\16\6\u00ad\3\6\3\6\7\6\u00b2\n\6\f\6\16\6\u00b5\13")
        buf.write("\6\3\6\3\6\5\6\u00b9\n\6\3\6\6\6\u00bc\n\6\r\6\16\6\u00bd")
        buf.write("\5\6\u00c0\n\6\3\7\3\7\5\7\u00c4\n\7\3\7\3\7\3\b\6\b\u00c9")
        buf.write("\n\b\r\b\16\b\u00ca\3\t\3\t\5\t\u00cf\n\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\7\37\u014b\n")
        buf.write("\37\f\37\16\37\u014e\13\37\3 \3 \3 \3 \7 \u0154\n \f ")
        buf.write("\16 \u0157\13 \3 \3 \3!\3!\3!\3!\3!\3!\3!\7!\u0162\n!")
        buf.write("\f!\16!\u0165\13!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\5A\u01b7\nA\3")
        buf.write("A\3A\3A\3A\3B\6B\u01be\nB\rB\16B\u01bf\3B\3B\3C\3C\3C")
        buf.write("\3D\3D\5D\u01c9\nD\3D\3D\3D\3D\3E\3E\5E\u01d1\nE\3E\3")
        buf.write("E\5E\u01d5\nE\3E\3E\2\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\2")
        buf.write("\21\2\23\2\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34")
        buf.write("=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61")
        buf.write("g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083")
        buf.write("@\u0085A\u0087B\u0089C\3\2\25\3\2\63;\3\2\62;\4\2DDdd")
        buf.write("\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGg")
        buf.write("g\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2\f\f\17\17\3\2,,\3\2\61\61\5\2\13\13")
        buf.write("\16\17\"\"\4\3\13\f^^\2\u01eb\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3")
        buf.write("\u0093\3\2\2\2\5\u0095\3\2\2\2\7\u009c\3\2\2\2\t\u00a3")
        buf.write("\3\2\2\2\13\u00ab\3\2\2\2\r\u00c1\3\2\2\2\17\u00c8\3\2")
        buf.write("\2\2\21\u00ce\3\2\2\2\23\u00d0\3\2\2\2\25\u00d3\3\2\2")
        buf.write("\2\27\u00d6\3\2\2\2\31\u00db\3\2\2\2\33\u00df\3\2\2\2")
        buf.write("\35\u00e6\3\2\2\2\37\u00eb\3\2\2\2!\u00f0\3\2\2\2#\u00f7")
        buf.write("\3\2\2\2%\u0101\3\2\2\2\'\u0107\3\2\2\2)\u010b\3\2\2\2")
        buf.write("+\u0114\3\2\2\2-\u011a\3\2\2\2/\u0120\3\2\2\2\61\u0124")
        buf.write("\3\2\2\2\63\u012a\3\2\2\2\65\u0131\3\2\2\2\67\u0139\3")
        buf.write("\2\2\29\u013e\3\2\2\2;\u0144\3\2\2\2=\u0148\3\2\2\2?\u014f")
        buf.write("\3\2\2\2A\u015a\3\2\2\2C\u016b\3\2\2\2E\u016d\3\2\2\2")
        buf.write("G\u016f\3\2\2\2I\u0171\3\2\2\2K\u0173\3\2\2\2M\u0175\3")
        buf.write("\2\2\2O\u0177\3\2\2\2Q\u0179\3\2\2\2S\u017b\3\2\2\2U\u017d")
        buf.write("\3\2\2\2W\u017f\3\2\2\2Y\u0181\3\2\2\2[\u0184\3\2\2\2")
        buf.write("]\u0187\3\2\2\2_\u018a\3\2\2\2a\u018d\3\2\2\2c\u0190\3")
        buf.write("\2\2\2e\u0193\3\2\2\2g\u0196\3\2\2\2i\u0199\3\2\2\2k\u019b")
        buf.write("\3\2\2\2m\u019e\3\2\2\2o\u01a1\3\2\2\2q\u01a3\3\2\2\2")
        buf.write("s\u01a6\3\2\2\2u\u01a8\3\2\2\2w\u01ab\3\2\2\2y\u01ad\3")
        buf.write("\2\2\2{\u01af\3\2\2\2}\u01b1\3\2\2\2\177\u01b3\3\2\2\2")
        buf.write("\u0081\u01b6\3\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01c3\3")
        buf.write("\2\2\2\u0087\u01c6\3\2\2\2\u0089\u01ce\3\2\2\2\u008b\u0094")
        buf.write("\7\62\2\2\u008c\u0090\t\2\2\2\u008d\u008f\t\3\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0093\u008b\3\2\2\2\u0093\u008c\3\2\2\2\u0094\4")
        buf.write("\3\2\2\2\u0095\u0096\7\62\2\2\u0096\u0098\t\4\2\2\u0097")
        buf.write("\u0099\t\5\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\6\3\2\2")
        buf.write("\2\u009c\u009d\7\62\2\2\u009d\u009f\t\6\2\2\u009e\u00a0")
        buf.write("\t\7\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\b\3\2\2\2\u00a3")
        buf.write("\u00a4\7\62\2\2\u00a4\u00a6\t\b\2\2\u00a5\u00a7\t\t\2")
        buf.write("\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\n\3\2\2\2\u00aa\u00ac")
        buf.write("\t\3\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b3\7\60\2\2\u00b0\u00b2\t\3\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00bf\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b6\u00b8\t\n\2\2\u00b7\u00b9\t\13\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba")
        buf.write("\u00bc\t\3\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3")
        buf.write("\2\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\f")
        buf.write("\3\2\2\2\u00c1\u00c3\7$\2\2\u00c2\u00c4\5\17\b\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\7$\2\2\u00c6\16\3\2\2\2\u00c7\u00c9\5\21")
        buf.write("\t\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\20\3\2\2\2\u00cc\u00cf")
        buf.write("\n\f\2\2\u00cd\u00cf\5\23\n\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\22\3\2\2\2\u00d0\u00d1\7^\2\2\u00d1")
        buf.write("\u00d2\t\r\2\2\u00d2\24\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7g\2\2\u00d7")
        buf.write("\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write("\30\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\32\3\2\2\2\u00df\u00e0\7t\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7w\2\2\u00e3")
        buf.write("\u00e4\7t\2\2\u00e4\u00e5\7p\2\2\u00e5\34\3\2\2\2\u00e6")
        buf.write("\u00e7\7h\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7p\2\2\u00e9")
        buf.write("\u00ea\7e\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write("\u00ed\7{\2\2\u00ed\u00ee\7r\2\2\u00ee\u00ef\7g\2\2\u00ef")
        buf.write(" \3\2\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2")
        buf.write("\u00f3\7t\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7e\2\2\u00f5")
        buf.write("\u00f6\7v\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8")
        buf.write("\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7g\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\u00fd\7h\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write("\u00ff\7e\2\2\u00ff\u0100\7g\2\2\u0100$\3\2\2\2\u0101")
        buf.write("\u0102\7e\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104")
        buf.write("\u0105\7u\2\2\u0105\u0106\7v\2\2\u0106&\3\2\2\2\u0107")
        buf.write("\u0108\7x\2\2\u0108\u0109\7c\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("(\3\2\2\2\u010b\u010c\7e\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write("\u010e\7p\2\2\u010e\u010f\7v\2\2\u010f\u0110\7k\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\u0112\7w\2\2\u0112\u0113\7g\2\2\u0113")
        buf.write("*\3\2\2\2\u0114\u0115\7d\2\2\u0115\u0116\7t\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117\u0118\7c\2\2\u0118\u0119\7m\2\2\u0119")
        buf.write(",\3\2\2\2\u011a\u011b\7t\2\2\u011b\u011c\7c\2\2\u011c")
        buf.write("\u011d\7p\2\2\u011d\u011e\7i\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write(".\3\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122")
        buf.write("\u0123\7v\2\2\u0123\60\3\2\2\2\u0124\u0125\7h\2\2\u0125")
        buf.write("\u0126\7n\2\2\u0126\u0127\7q\2\2\u0127\u0128\7c\2\2\u0128")
        buf.write("\u0129\7v\2\2\u0129\62\3\2\2\2\u012a\u012b\7u\2\2\u012b")
        buf.write("\u012c\7v\2\2\u012c\u012d\7t\2\2\u012d\u012e\7k\2\2\u012e")
        buf.write("\u012f\7p\2\2\u012f\u0130\7i\2\2\u0130\64\3\2\2\2\u0131")
        buf.write("\u0132\7d\2\2\u0132\u0133\7q\2\2\u0133\u0134\7q\2\2\u0134")
        buf.write("\u0135\7n\2\2\u0135\u0136\7g\2\2\u0136\u0137\7c\2\2\u0137")
        buf.write("\u0138\7p\2\2\u0138\66\3\2\2\2\u0139\u013a\7v\2\2\u013a")
        buf.write("\u013b\7t\2\2\u013b\u013c\7w\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write("8\3\2\2\2\u013e\u013f\7h\2\2\u013f\u0140\7c\2\2\u0140")
        buf.write("\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write(":\3\2\2\2\u0144\u0145\7p\2\2\u0145\u0146\7k\2\2\u0146")
        buf.write("\u0147\7n\2\2\u0147<\3\2\2\2\u0148\u014c\t\16\2\2\u0149")
        buf.write("\u014b\t\17\2\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2")
        buf.write("\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d>\3\2")
        buf.write("\2\2\u014e\u014c\3\2\2\2\u014f\u0150\7\61\2\2\u0150\u0151")
        buf.write("\7\61\2\2\u0151\u0155\3\2\2\2\u0152\u0154\n\20\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0158\u0159\b \2\2\u0159@\3\2\2\2\u015a\u015b\7")
        buf.write("\61\2\2\u015b\u015c\7,\2\2\u015c\u0163\3\2\2\2\u015d\u0162")
        buf.write("\5A!\2\u015e\u0162\n\21\2\2\u015f\u0160\7,\2\2\u0160\u0162")
        buf.write("\n\22\2\2\u0161\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\7,\2\2\u0167\u0168\7\61\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\b!\2\2\u016aB\3\2\2\2\u016b\u016c")
        buf.write("\7*\2\2\u016cD\3\2\2\2\u016d\u016e\7+\2\2\u016eF\3\2\2")
        buf.write("\2\u016f\u0170\7}\2\2\u0170H\3\2\2\2\u0171\u0172\7\177")
        buf.write("\2\2\u0172J\3\2\2\2\u0173\u0174\7]\2\2\u0174L\3\2\2\2")
        buf.write("\u0175\u0176\7_\2\2\u0176N\3\2\2\2\u0177\u0178\7.\2\2")
        buf.write("\u0178P\3\2\2\2\u0179\u017a\7=\2\2\u017aR\3\2\2\2\u017b")
        buf.write("\u017c\7<\2\2\u017cT\3\2\2\2\u017d\u017e\7\60\2\2\u017e")
        buf.write("V\3\2\2\2\u017f\u0180\7?\2\2\u0180X\3\2\2\2\u0181\u0182")
        buf.write("\7<\2\2\u0182\u0183\7?\2\2\u0183Z\3\2\2\2\u0184\u0185")
        buf.write("\7-\2\2\u0185\u0186\7?\2\2\u0186\\\3\2\2\2\u0187\u0188")
        buf.write("\7/\2\2\u0188\u0189\7?\2\2\u0189^\3\2\2\2\u018a\u018b")
        buf.write("\7,\2\2\u018b\u018c\7?\2\2\u018c`\3\2\2\2\u018d\u018e")
        buf.write("\7\61\2\2\u018e\u018f\7?\2\2\u018fb\3\2\2\2\u0190\u0191")
        buf.write("\7\'\2\2\u0191\u0192\7?\2\2\u0192d\3\2\2\2\u0193\u0194")
        buf.write("\7~\2\2\u0194\u0195\7~\2\2\u0195f\3\2\2\2\u0196\u0197")
        buf.write("\7(\2\2\u0197\u0198\7(\2\2\u0198h\3\2\2\2\u0199\u019a")
        buf.write("\7#\2\2\u019aj\3\2\2\2\u019b\u019c\7?\2\2\u019c\u019d")
        buf.write("\7?\2\2\u019dl\3\2\2\2\u019e\u019f\7#\2\2\u019f\u01a0")
        buf.write("\7?\2\2\u01a0n\3\2\2\2\u01a1\u01a2\7>\2\2\u01a2p\3\2\2")
        buf.write("\2\u01a3\u01a4\7>\2\2\u01a4\u01a5\7?\2\2\u01a5r\3\2\2")
        buf.write("\2\u01a6\u01a7\7@\2\2\u01a7t\3\2\2\2\u01a8\u01a9\7@\2")
        buf.write("\2\u01a9\u01aa\7?\2\2\u01aav\3\2\2\2\u01ab\u01ac\7-\2")
        buf.write("\2\u01acx\3\2\2\2\u01ad\u01ae\7/\2\2\u01aez\3\2\2\2\u01af")
        buf.write("\u01b0\7,\2\2\u01b0|\3\2\2\2\u01b1\u01b2\7\61\2\2\u01b2")
        buf.write("~\3\2\2\2\u01b3\u01b4\7\'\2\2\u01b4\u0080\3\2\2\2\u01b5")
        buf.write("\u01b7\7\17\2\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2")
        buf.write("\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\7\f\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01bb\bA\3\2\u01bb\u0082\3\2\2\2\u01bc")
        buf.write("\u01be\t\23\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2")
        buf.write("\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\bB\2\2\u01c2\u0084\3\2\2\2\u01c3")
        buf.write("\u01c4\13\2\2\2\u01c4\u01c5\bC\4\2\u01c5\u0086\3\2\2\2")
        buf.write("\u01c6\u01c8\7$\2\2\u01c7\u01c9\5\17\b\2\u01c8\u01c7\3")
        buf.write("\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\7^\2\2\u01cb\u01cc\n\r\2\2\u01cc\u01cd\bD\5\2\u01cd\u0088")
        buf.write("\3\2\2\2\u01ce\u01d0\7$\2\2\u01cf\u01d1\5\17\b\2\u01d0")
        buf.write("\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d5\t\24\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d7\bE\6\2\u01d7\u008a\3\2\2\2\31\2\u0090\u0093\u009a")
        buf.write("\u00a1\u00a8\u00ad\u00b3\u00b8\u00bd\u00bf\u00c3\u00ca")
        buf.write("\u00ce\u014c\u0155\u0161\u0163\u01b6\u01bf\u01c8\u01d0")
        buf.write("\u01d4\7\b\2\2\3A\2\3C\3\3D\4\3E\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DECIMAL_LIT = 1
    BINARY_LIT = 2
    OCTAL_LIT = 3
    HEX_LIT = 4
    FLOAT_LIT = 5
    STRING_LIT = 6
    IF = 7
    ELSE = 8
    FOR = 9
    RETURN = 10
    FUNC = 11
    TYPE = 12
    STRUCT = 13
    INTERFACE = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    INT = 20
    FLOAT = 21
    STRING = 22
    BOOLEAN = 23
    TRUE = 24
    FALSE = 25
    NIL = 26
    ID = 27
    LINE_COMMENT = 28
    BLOCK_COMMENT = 29
    L_PAREN = 30
    R_PAREN = 31
    L_CURLY = 32
    R_CURLY = 33
    L_BRACKET = 34
    R_BRACKET = 35
    COMMA = 36
    SEMI = 37
    COLON = 38
    DOT = 39
    ASSIGN = 40
    DECLARE_ASSIGN = 41
    PLUS_ASSIGN = 42
    MINUS_ASSIGN = 43
    MUL_ASSIGN = 44
    DIV_ASSIGN = 45
    MOD_ASSIGN = 46
    LOGICAL_OR = 47
    LOGICAL_AND = 48
    LOGICAL_NOT = 49
    EQUALS = 50
    NOT_EQUALS = 51
    LESS = 52
    LESS_OR_EQUALS = 53
    GREATER = 54
    GREATER_OR_EQUALS = 55
    PLUS = 56
    MINUS = 57
    STAR = 58
    DIV = 59
    MOD = 60
    NEW_LINE = 61
    WS = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'int'", "'float'", "'string'", "'boolean'", "'true'", 
            "'false'", "'nil'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'", "':'", "'.'", "'='", "':='", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "'||'", "'&&'", "'!'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", "HEX_LIT", "FLOAT_LIT", 
            "STRING_LIT", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
            "STRUCT", "INTERFACE", "CONST", "VAR", "CONTINUE", "BREAK", 
            "RANGE", "INT", "FLOAT", "STRING", "BOOLEAN", "TRUE", "FALSE", 
            "NIL", "ID", "LINE_COMMENT", "BLOCK_COMMENT", "L_PAREN", "R_PAREN", 
            "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "COMMA", "SEMI", 
            "COLON", "DOT", "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "LOGICAL_OR", "LOGICAL_AND", 
            "LOGICAL_NOT", "EQUALS", "NOT_EQUALS", "LESS", "LESS_OR_EQUALS", 
            "GREATER", "GREATER_OR_EQUALS", "PLUS", "MINUS", "STAR", "DIV", 
            "MOD", "NEW_LINE", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", "HEX_LIT", "FLOAT_LIT", 
                  "STRING_LIT", "CHARACTERS", "CHARACTER", "ESC", "IF", 
                  "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "INT", "FLOAT", 
                  "STRING", "BOOLEAN", "TRUE", "FALSE", "NIL", "ID", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", 
                  "L_BRACKET", "R_BRACKET", "COMMA", "SEMI", "COLON", "DOT", 
                  "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "LOGICAL_OR", 
                  "LOGICAL_AND", "LOGICAL_NOT", "EQUALS", "NOT_EQUALS", 
                  "LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", 
                  "PLUS", "MINUS", "STAR", "DIV", "MOD", "NEW_LINE", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        self.lastToken = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();

    def isEos(self):
        if hasattr(self, 'lastToken'):
            return self.lastToken in {
                    self.ID, 
                    self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
                    self.NIL, 
                    self.DECIMAL_LIT, self.BINARY_LIT, self.OCTAL_LIT, self.HEX_LIT, 
                    self.FLOAT_LIT, 
                    self.TRUE, self.FALSE, 
                    self.STRING_LIT, 
                    self.RETURN, self.CONTINUE, self.BREAK, 
                    self.R_PAREN, self.R_BRACKET, self.R_CURLY
                }
        return False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.NEW_LINE_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEW_LINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    if self.isEos():
                        self.text = ';'
                        self.type = self.SEMI
                    else:
                        self.skip()
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text)
     


