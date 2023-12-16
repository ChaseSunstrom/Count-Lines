import os
import fileinput

IGNORED_EXTENSIONS = {'.exe', '.lib', '.dll', '.vcxproj', '.csproj', '.sln', '.o', '.obj',}

def is_ignored_file(file_path):
    _, file_extension = os.path.splitext(file_path.lower())
    return file_extension in IGNORED_EXTENSIONS

def count_lines(directory):
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not is_ignored_file(d)]

        for file in files:
            file_path = os.path.join(root, file)

            if is_ignored_file(file_path):
                print(f"Ignoring file: {file_path}")
                continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = sum(1 for _ in f)
                    total_lines += lines
                    print(f"{file_path}: {lines} lines")
            except Exception as e:
                print(f"Error: {file_path} - {e}")

    print(f"Total lines in all files: {total_lines}")

if __name__ == "__main__":
    input_directory = input("Enter the input directory (press Enter for the current directory): ").strip()

    # Use the current directory if the user enters an empty input
    if not input_directory:
        input_directory = os.getcwd()

    count_lines(input_directory)
    input("Press Enter to exit...")
