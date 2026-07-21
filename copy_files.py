import shutil
import os

base_dir = r'C:\Users\hp\Desktop\week 11'
files_to_copy = [
    'ethiopia_fi_unified_data.xlsx',
    'reference_codes.xlsx'
]

for file in files_to_copy:
    src = os.path.join(base_dir, file)
    dst = os.path.join(base_dir, 'data', 'raw', file)
    shutil.copy(src, dst)
    print(f'Copied: {file} to data/raw/')

print('Files copied successfully')
