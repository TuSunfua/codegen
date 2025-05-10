import pandas as pd
import re
# from write_test import write_test, run_lexer_test, escape_output

# Đọc file Excel và xử lý từng sheet
file_path = "test/CodeGenSuite.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    input = re.findall(r'input = """(.*?)"""', content.strip(), re.DOTALL)
tests = input

# Loại bỏ khoảng trắng đầu và cuối
tests = [test.strip() for test in tests]

# Tạo DataFrame từ danh sách đã lấy
output = pd.DataFrame(tests, columns=["Input"])

# Ghi vào file Excel, không có dòng tiêu đề
output_file = "output.xlsx"
output.to_excel(output_file, sheet_name='Sheet1', index=False, header=False)

print(f"Đã lưu kết quả vào {output_file}")
