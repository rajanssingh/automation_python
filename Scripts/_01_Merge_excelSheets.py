import os
import pandas as pd

folder_path = 'C:\Prep\Company wise DSA\LeetCode-Questions-CompanyWise'

merged_data = pd.DataFrame()

for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        df = pd.read_csv(file_path)

        df['Source_File'] = filename

        merged_data = pd.concat([merged_data, df], ignore_index=True)

output_file_path = os.path.join(folder_path, 'merged_output.csv')
merged_data.to_csv(output_file_path, index=True)

print(f"All excel sheets are merged and saved in {output_file_path}")