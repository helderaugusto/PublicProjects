import pandas as pd

# Read CSV
df = pd.read_csv('csv_file.csv')

# Clean invalid rows
df_clean = df.dropna()  # remove rows with null values
df_clean = df_clean[df_clean['Quantity'] > 0]  # remove negative quantities

# Create summary
summary = df_clean.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_revenue=('Price', lambda x: (x*df_clean.loc[x.index,'Quantity']).sum())
)

# Save cleaned CSV
df_clean.to_csv('sales_clean.csv', index=False)
summary.to_csv('sales_summary.csv')

print("Cleaned CSV and summary generated successfully!")