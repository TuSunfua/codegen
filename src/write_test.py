import pandas as pd
import subprocess
import re, sys

def write_test(file_path, test):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(test)

def run_test():
    result = subprocess.run(['python', 'run.py', 'test', 'CodeGenSuite'], capture_output=True, text=True)
    match = re.search(r'"""(.*?)"""', result.stdout.strip(), re.DOTALL)
    if not match:
        print(result.stdout.strip())
    return match.group(1) if match else None

def escape_output(text):
    if text is None:
        return ""

    text = text.replace('\\', '\\\\')
    
    return text

def export_tests(tests, file_path):
    test_cases = [
        "import unittest",
        "from TestUtils import TestCodeGen",
        "from AST import *",
        "from itertools import count",
        "",
        "num = count(501)",
        "",
        "class CheckCodeGenSuite(unittest.TestCase):"
    ]

    for i, (input_text, output) in enumerate(tests):
        escaped_input = escape_output(input_text)
        escaped_output = escape_output(output)
        test_cases.append(f"""    def test_{i+501}(self):""")
        test_cases.append(f"""        input = \"\"\"{escaped_input}\"\"\"""")
        test_cases.append(f"""        expect = \"\"\"{escaped_output if escaped_output != "successful" else ""}\"\"\"""")
        test_cases.append(f"""        self.assertTrue(TestCodeGen.test(input, expect, next(num)))""")
        test_cases.append("")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(test_cases))

file_path = "output_gpt4.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

tests = []
start_row = int(sys.argv[1]) if len(sys.argv) > 1 else 0

for sheet_name, df in sheets.items():
    print(f"Processing sheet: {sheet_name}")

    for i, row in df.iterrows():
        if i < start_row:
            continue

        input_text = str(row.iloc[0])
        write_test('main.minigo', input_text)
        output = run_test()

        if output is None:
            print(f"⚠️ Warning: No output found for input in sheet {sheet_name}, row {i}")
            print(f"Input: {input_text}")
            exit(0)

        tests.append((input_text, output))

export_tests(tests, 'out.py')
print("✅ Exported test cases to out.py")
