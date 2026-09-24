import pandas as pd

# configure file path to be read.
file_path = f"C:\Users\Jviloria\OneDrive - Konica Minolta\ドキュメント\MCU Python Course\Fall26_104\viloriaj1\Project\Final Project Plan.xls"
sheet_name = "Main"

project_data = pd.read_excel(file_path, sheet_name=sheet_name)

print(project_data.head)


