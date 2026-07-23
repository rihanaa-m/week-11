import os

file_to_remove = r'C:\Users\hp\Desktop\week 11\FINAL_README.md'

if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"Removed {file_to_remove}")
else:
    print(f"File {file_to_remove} does not exist")
