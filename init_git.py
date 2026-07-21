import subprocess
import os

os.chdir(r'C:\Users\hp\Desktop\week 11')

# Initialize git repository
result = subprocess.run('git init', shell=True, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

print("Git repository initialized in current directory")
