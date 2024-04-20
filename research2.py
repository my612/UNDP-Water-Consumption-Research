import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
excel2_file_path = r"C:\Users\Muhammad Yasser\Downloads\Cleaned Phase III. Water Consumption Form (Responses).xlsx"
# Read the Excel sheet into a pandas DataFrame
df2 = pd.read_excel(excel2_file_path)

# Print the DataFrame
df2.drop(df2.columns[-1], axis=1, inplace=True)
# print(df2)
df2.rename(columns={df2.columns[0]: 'district'}, inplace=True)
df2.rename(columns={df2.columns[1]: 'day'}, inplace=True)
df2.rename(columns={df2.columns[2]: 'hoursHome'}, inplace=True)
df2.rename(columns={df2.columns[3]: 'showerHome'}, inplace=True)
df2.rename(columns={df2.columns[4]: 'washingHandsHome'}, inplace=True)
df2.rename(columns={df2.columns[5]: 'flushingHome'}, inplace=True)
df2.rename(columns={df2.columns[6]: 'washingDishHomeHand'}, inplace=True)
df2.rename(columns={df2.columns[7]: 'washingDishHomeMach'}, inplace=True)
df2.rename(columns={df2.columns[8]: 'wateringPlantsHome'}, inplace=True)
df2.rename(columns={df2.columns[9]: 'drinkingHome'}, inplace=True)
df2.rename(columns={df2.columns[10]: 'hoursUni'}, inplace=True)
df2.rename(columns={df2.columns[11]: 'showeringUni'}, inplace=True)
df2.rename(columns={df2.columns[12]: 'flushingUni'}, inplace=True)
df2.rename(columns={df2.columns[13]: 'washingHandsUni'}, inplace=True)
df2.rename(columns={df2.columns[14]: 'drinkingUni'}, inplace=True)
df2.rename(columns={df2.columns[15]: 'otherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[16]: 'hoursOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[17]: 'showeringOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[18]: 'washingHandsOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[19]: 'flushingOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[20]: 'drinkingOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[21]: 'washingDishMachOtherPlaces'}, inplace=True)
df2.rename(columns={df2.columns[22]: 'washingDishOtherPlace'}, inplace=True)
df2 = df2[df2['day'] != 0]
# print(df2.columns)


#UNI COLUMNS 
uni_columns = [col for col in df2.columns if col.endswith('Uni') and col != 'hoursUni']
for col in uni_columns:
    df2[col] = pd.to_numeric(df2[col], errors='coerce')

df2['sum_Uni'] = df2[uni_columns].sum(axis=1)
df2['sum_Uni_Norm'] = df2['sum_Uni'] / df2['hoursUni']
df2.fillna(0, inplace=True)
df2.replace([np.inf, -np.inf], 0, inplace=True)
# print(df2['sum_Uni_Norm'])
df2_grouped_mean = df2.groupby('day')['sum_Uni_Norm'].mean()
# print(df2_grouped_mean.to_string())


# # import matplotlib.pyplot as plt

# # ... your existing code ...

# df2_grouped_mean = df2.groupby('day')['sum_Uni_Norm'].mean().round(3)

# # Create a new figure
# fig, ax = plt.subplots(1, 1)

# # Create table_data from df2_grouped_mean
# table_data = [[index, value] for index, value in df2_grouped_mean.items()]

# # Create a table
# table = plt.table(cellText=table_data, colLabels=['Day', 'UNI L/hr averaged by day'], loc='center')

# # Hide axes
# ax.axis('off')

# # Show the plot
# plt.show()
# import pandas as pd

# ... your existing code ...

# df2_grouped_mean = df2.groupby('day')['sum_Uni_Norm'].mean().round(3)

# Create a DataFrame from df2_grouped_mean
# df_export = pd.DataFrame(df2_grouped_mean.items(), columns=['Day', 'HOME L/hr averaged by day'])

# # Export the DataFrame to an Excel file
# df_export.to_excel('E:\outp.xlsx', index=False)
# HOME COLUMNS
home_columns = [col for col in df2.columns if col.endswith('Home') and col != 'hoursHome']
for col in home_columns:
    df2[col] = pd.to_numeric(df2[col], errors='coerce')
df2['sum_Home'] = df2[home_columns].sum(axis=1)
df2['sum_Home_Norm'] = df2['sum_Home'] / df2['hoursHome']
df2.fillna(0, inplace=True)
df2.replace([np.inf, -np.inf], 0, inplace=True)
# print(df2['sum_Home_Norm'])
df2_grouped_mean = df2.groupby('day')['sum_Home_Norm'].mean().round(3)
# print(df2_grouped_mean)
df_export = pd.DataFrame(df2_grouped_mean.items(), columns=['Day', 'HOME L/hr averaged by day'])

# Export the DataFrame to an Excel file
df_export.to_excel('E:\outp.xlsx', index=False)