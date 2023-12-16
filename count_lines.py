import os
import fileinput

def count_lines(directory):
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

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
