import sys,os
sys.path.append('./test/')
sys.path.append('./main/minigo/parser/')
sys.path.append('./main/minigo/utils/')
sys.path.append('./main/minigo/astgen/')
sys.path.append('./main/minigo/checker/')
sys.path.append('./main/minigo/codegen/')
import subprocess
import unittest
from antlr4 import *

ANTLR_JAR = os.environ.get('ANTLR_JAR')
if ANTLR_JAR is None:
    ANTLR_JAR = 'antlr-4.9.2-complete.jar'
TARGET_DIR = '../target'
GENERATE_DIR = 'main/minigo/parser'

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-Dlanguage=Python3","-no-listener","-visitor","main/minigo/parser/MiniGo.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm","-rf",TARGET_DIR + "/*"])
               
    elif argv[0] == 'test':     
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java","-jar",ANTLR_JAR,"-o",GENERATE_DIR,"-no-listener","-visitor","main/minigo/parser/MiniGo.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            getAndTest(LexerSuite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            getAndTest(ParserSuite)
        elif argv[1] == 'ASTGenSuite':
            from ASTGenSuite import ASTGenSuite
            getAndTest(ASTGenSuite)
        elif argv[1] == 'CheckSuite':
            from CheckSuite import CheckSuite
            getAndTest(CheckSuite)
        elif argv[1] == 'CodeGenSuite':
            from CodeGenSuite import CheckCodeGenSuite
            getAndTest(CheckCodeGenSuite)
        else:
            printUsage()
    else:
        printUsage()



def getAndTest(cls): 
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
    test(suite)

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")
    print("python3 run.py test CheckerSuite")
    print("python3 run.py test CodeGenSuite")

if __name__ == "__main__":
   main(sys.argv[1:])
