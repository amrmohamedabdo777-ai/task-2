
import pandas as pd

df=pd.read_csv("Walmart_Sales.csv")

print("1. First 3 rows:")
print(df.head(3))

print("\n2. Last 2 rows:")
print(df.tail(2))

print("\n3. Dataset information:")
df.info()

print("\n4. Statistical information:")
print(df.describe())

print("\n5. Number of rows and columns:")
print(df.shape)

print("\n6. Column names:")
print(df.columns)

print("\n7. Number of rows:")
print(len(df))

print("\n8. Check missing values:")
print(df.isnull())

print("\n9. Number of missing values:")
print(df.isnull().sum())

print("\n10. Total weekly sales for each store:")
print(df.groupby("Store")["Weekly_Sales"].sum())

print("\n11. Sort by weekly sales:")
print(df.sort_values("Weekly_Sales", ascending=False))

print("\n12. Records for Store 1:")
print(df[df["Store"]==1])

print("\n13. Number of records for each store:")
print(df["Store"].value_counts())

print("\n14. Rename columns:")
df_renamed=df.rename(columns={'Weekly_Sales': 'Sales', 'Holiday_Flag': 'Holiday'})
print(df_renamed)

print("\n15. First row using iloc:")
print(df.iloc[0])

print("\n16. First row using loc:")
print(df.loc[0])

print("\n17. Total weekly sales during holidays and non-holidays:")
print(df.groupby("Holiday_Flag")["Weekly_Sales"].sum())

print("\n18. Records where weekly sales are greater than 1,000,000:")
print(df[df["Weekly_Sales"]>1000000])

print("\n19. Number of unique stores:")
print(df["Store"].nunique())

print("\n20. Average weekly sales:")
print(df["Weekly_Sales"].mean())

