import os

base_dir = r'C:\Users\hp\Desktop\week 11'
directories = [
    'data/raw',
    'data/processed',
    'notebooks',
    'src',
    'dashboard',
    'tests',
    'models',
    'reports/figures',
    '.github/workflows'
]

for directory in directories:
    full_path = os.path.join(base_dir, directory)
    os.makedirs(full_path, exist_ok=True)
    print(f'Created: {full_path}')

print('Directory structure created successfully')
