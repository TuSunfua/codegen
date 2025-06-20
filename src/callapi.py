from openai import OpenAI
import pandas as pd
import numpy as np
import re

GITHUB_KEY = '<paste your key here>'

token = GITHUB_KEY
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def generate_rationale_gpt4(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Use the image to answer the question."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            },
        ],
        temperature=0.7,
        top_p=1,
        max_tokens=1000,
        model=model_name,
    )
    
    return response.choices[0].message.content

file_path = "output.xlsx"
df = pd.read_excel(file_path, sheet_name='Sheet1') 

# Template prompt
prompt = '''
I have a set of MiniGo code snippets (a simplified version of Go), and I want you to generate 5 new and unique MiniGo code snippets that follow these guidelines:
0. Each code snippet should be a valid MiniGo program that can be executed without errors and has a main function as the entry point.
1. Maintain the structure and logic of the input code snippets: Analyze the syntax and structure of my provided examples to understand the conventions and patterns used in MiniGo.
2. Rename identifiers and change values: In the new code snippets, change all variable names, function names, and literal values. These changes must preserve the intent and logic of the original code but create variety and uniqueness.
3. Introduce syntactic variation: Use a mix of newlines and semicolons for statement endings. While semicolons are preferred, ensure some statements end with newlines for natural variation.
4. Preserve complexity level: If the original snippet is simple, you may increase its complexity slightly by adding nested control flow (e.g., if, for, function calls) as long as the structure is still recognizable and not significantly different.
5. Showcase a range of language features: Include different MiniGo features such as variable declarations, loops, conditionals, function definitions and calls, and mathematical or logical operations. Each snippet should demonstrate at least one key language feature.
6. Avoid repetition: Each new code snippet should be distinct in logic and identifiers from both the original and from the other generated snippets.
7. Output format: For each snippet, format your output like this:
```
MiniGo
<your code snippet here>
```
'''

# Get the first column (130 test cases)
first_column = df.iloc[:, 0].tolist()
data = np.array(first_column)

# No need to shuffle if you want sequential splitting, but keeping it for randomness
np.random.shuffle(data)

responses = ''
# Process 10 requests, each with 13 test cases (130 / 10 = 13 per request)
for i in range(20):
    # Slice 13 test cases for each iteration
    sample_test = data[i*5:(i+1)*5]
    # Format each test case with ```MiniGo\n...\n```
    sample_test = ['```MiniGo\n' + x + '\n```' for x in sample_test]
    sample_test = '\n'.join(sample_test)
    # Append the response from the API call
    responses += generate_rationale_gpt4(prompt + sample_test) + '\n\n'
    
np.random.shuffle(data)
for i in range(1):
    # Slice 13 test cases for each iteration
    sample_test = data[i*10:(i+1)*10]
    # Format each test case with ```MiniGo\n...\n```
    sample_test = ['```MiniGo\n' + x + '\n```' for x in sample_test]
    sample_test = '\n'.join(sample_test)
    # Append the response from the API call
    responses += generate_rationale_gpt4(prompt + sample_test) + '\n\n'

# Extract all MiniGo snippets from the responses
match = re.findall(r'```MiniGo\n(.*?)\n```', responses, re.DOTALL)
responses = match

# Save the output to a DataFrame and Excel file
output = pd.DataFrame(responses, columns=["Output"])
output_file = "output_gpt4.xlsx"

output.to_excel(output_file, sheet_name='Sheet1', index=False, header=False)
