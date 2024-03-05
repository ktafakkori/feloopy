import os
import contextlib

input_dir = './docs/inputs'
output_dir = './docs/outputs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk(input_dir):
    if files:
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)
        os.makedirs(output_subdir, exist_ok=True)

        for filename in files:
            if filename.endswith('.py'):
                input_file_path = os.path.join(root, filename)
                output_file_path = os.path.join(output_subdir, f"{os.path.splitext(filename)[0]}.txt")

                with open(input_file_path, 'r', encoding='utf-8') as code_file:
                    code = code_file.read()

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    try:
                        with contextlib.redirect_stdout(output_file):
                            exec(code)
                    except Exception as e:
                        output_file.write(f"Error in {filename}: {str(e)}\n")