import pandas as pd
import glob

# 1. Find all sales files
# Since the script is inside the 'data' folder, we look for files starting with 'daily_sales_data_'
file_pattern = 'daily_sales_data_*.csv'
files = glob.glob(file_pattern)

print(f"Files found: {files}")

# Check if files exist to avoid errors
if not files:
    print("Error: No CSV files found! Please check if the script is in the correct folder.")
else:
    # 2. Read all files into a list
    df_list = []
    for file in files:
        temp_df = pd.read_csv(file)
        df_list.append(temp_df)

    # 3. Merge all DataFrames into one
    merged_df = pd.concat(df_list, ignore_index=True)
    print(f"Total rows after merging: {len(merged_df)}")

    # 4. Clean the 'price' column
    # We remove the '$' sign and convert it to a float so we can do math
    merged_df['price'] = merged_df['price'].replace('[\$,]', '', regex=True).astype(float)

    # 5. Calculate Revenue (Quantity * Price)
    merged_df['revenue'] = merged_df['quantity'] * merged_df['price']

    # 6. Save the final processed data to a new CSV
    merged_df.to_csv('final_processed_data.csv', index=False)
    print("Success: Revenue calculated and final_processed_data.csv saved!")

    # 7. Preview the result
    print(merged_df[['product', 'quantity', 'price', 'revenue']].head())