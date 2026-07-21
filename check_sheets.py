import pandas as pd

data_path = r'C:\Users\hp\Desktop\week 11\data\raw\ethiopia_fi_unified_data.xlsx'

# Check sheet names
xl_file = pd.ExcelFile(data_path)
print("Available sheets:")
print(xl_file.sheet_names)
