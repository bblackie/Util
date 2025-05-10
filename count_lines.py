import os

def count_non_empty_lines(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # This checks if the line is non-empty after stripping whitespace
                count += 1
    return count

# Example usage with directory
directory = r'C:\Repos\13DGT\AdZ\PointsPlus'  # Replace with your directory path
filename = 'THE LORDE QUIZ.py'    # Replace with your filename
file_path = os.path.join(directory, filename)
print(f"Counting non-empty lines in: {file_path}")
result = count_non_empty_lines(file_path)
print(f"Number of non-empty lines: {result}")