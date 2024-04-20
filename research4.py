import pandas as pd
import numpy as np
# Specify the path to your Excel file
excel_file_path = r"C:\Users\Muhammad Yasser\Downloads\CLEAN Phase I. Water Consumption Form copy (Responses) (2).xlsx"
# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Print the DataFrame
df.dropna(subset=[df.columns[0]], inplace=True)
df.rename(columns={df.columns[0]: 'district'}, inplace=True)
df.rename(columns={df.columns[1]: 'day'}, inplace=True)
df.rename(columns={df.columns[2]: 'hoursHome'}, inplace=True)
df.rename(columns={df.columns[3]: 'showerHome'}, inplace=True)
df.rename(columns={df.columns[4]: 'flushingHome'}, inplace=True)
df.rename(columns={df.columns[5]: 'washingDishHomeHand'}, inplace=True)
df.rename(columns={df.columns[6]: 'washingHandsHome'}, inplace=True)
df.rename(columns={df.columns[7]: 'wateringPlantsHome'}, inplace=True)
df.rename(columns={df.columns[8]: 'drinkingHome'}, inplace=True)
df.rename(columns={df.columns[9]: 'hoursUni'}, inplace=True)
df.rename(columns={df.columns[10]: 'showeringUni'}, inplace=True)
df.rename(columns={df.columns[11]: 'flushingUni'}, inplace=True)
df.rename(columns={df.columns[12]: 'washingHandsUni'}, inplace=True)
df.rename(columns={df.columns[13]: 'drinkingUni'}, inplace=True)
df.rename(columns={df.columns[14]: 'otherPlaces'}, inplace=True)
df.rename(columns={df.columns[15]: 'hoursOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[16]: 'showeringOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[17]: 'washingHandsOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[18]: 'flushingOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[19]: 'drinkingOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[20]: 'washingDishMachHome'}, inplace=True)
df.rename(columns={df.columns[21]: 'washingDishMachOtherPlaces'}, inplace=True)
df.rename(columns={df.columns[22]: 'washingDishHandsOtherPlace'}, inplace=True)
df = df[df['day'] != 0]
uni_columns = [col for col in df.columns if col.endswith('Uni') and col != 'hoursUni']

# Convert str type columns to float


# UNI COLUMNS
for col in uni_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['sum_Uni'] = df[uni_columns].sum(axis=1)
df['sum_Uni_Norm'] = df['sum_Uni'] / df['hoursUni']
df.fillna(0, inplace=True)
df.replace([np.inf, -np.inf], 0, inplace=True)
# print(df['sum_Uni_Norm'])
df_grouped_mean_UNI = df.groupby('district')['sum_Uni_Norm'].mean().round(3)
# print(df_grouped_mean)
df_grouped_mean_UNI.to_excel('E:\outputUNI_first.xlsx', index=True)
# df_export = pd.DataFrame(df_grouped_mean.items(), columns=['Day', 'HOME L/hr averaged by day'])

# # Export the DataFrame to an Excel file
# df_export.to_excel('E:\outp.xlsx', index=False)

# HOME COLUMNS
def safe_division(x, y):
    if y == 0:
        return 0
    else:
        return x / y

home_columns = [col for col in df.columns if col.endswith('Home') and col != 'hoursHome']
for col in home_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert 'hoursHome' to numeric
df['hoursHome'] = pd.to_numeric(df['hoursHome'], errors='coerce')

df['sum_Home'] = df[home_columns].sum(axis=1)

# Use the safe_division function for division
df['sum_Home_Norm'] = df.apply(lambda row: safe_division(row['sum_Home'], row['hoursHome']), axis=1)

df.fillna(0, inplace=True)
df.replace([np.inf, -np.inf], 0, inplace=True)

df_grouped_mean = df.groupby('district')['sum_Home_Norm'].mean().round(3)
# print(df_grouped_mean)
df_grouped_mean.to_excel('E:\outputHOME_first.xlsx', index=True)

# df_export = pd.DataFrame(df_grouped_mean.items(), columns=['Day', 'HOME L/hr averaged by day'])

# # Export the DataFrame to an Excel file
# df_export.to_excel('E:\outp.xlsx', index=False)