# %%
import seaborn as sns
import pandas as pd
#  Load the Diamonds dataset from seaborn
diamonds_df=sns.load_dataset('diamonds')
diamonds_df
# %%
# Calculate the average price for each cut of diamonds.
avg_price_by_cut=diamonds_df.groupby('cut')['price'].mean()
print("Average price for each cut of diamonds:")
print(avg_price_by_cut)
# %%
# Find the diamond with the highest carat and display its details, including its cut, color, and clarity.
highest_carat_dimond=diamonds_df.loc[diamonds_df['carat'].idxmax()]
print("\nDiamond with the highest carat:")
print(highest_carat_dimond)
# %%
# Create a new DataFrame containing only the diamonds with 'cut' as 'Ideal' and 'color' as 'D'.
ideal_d_color_diamonds = diamonds_df[(diamonds_df['cut'] == 'Ideal') & (diamonds_df['color'] == 'D')]
print("\nDataFrame containing diamonds with 'cut' as 'Ideal' and 'color' as 'D':")
print(ideal_d_color_diamonds)
# %%
ideal_d_color_diamonds
# %%
# Calculate the correlation matrix for 'carat', 'depth', 'table', and 'price' columns.
corr_mat=diamonds_df[['carat', 'depth', 'table', 'price']].corr()
print("\nCorrelation matrix:")
print(corr_mat)
# %%
corr_mat
# %%
# For each clarity grade of diamonds, find the mean, median, minimum, and maximum 'carat'.
clarity_carat_stats = diamonds_df.groupby('clarity')['carat'].agg(['mean', 'median', 'min', 'max'])
print("\nCarat statistics for each clarity grade of diamonds:")
print(clarity_carat_stats)
# %%
clarity_carat_stats
# %%
# Replace any missing values in the 'depth' column with the mean value of that column.
mean_depth=diamonds_df['depth'].mean()
diamonds_df['depth'].fillna(mean_depth, inplace=True)
diamonds_df.head()
# %%
# Create a new column in the DataFrame called 'volume', which is the product of 'x', 'y', and 'z' columns.
diamonds_df['volume'] = diamonds_df['x'] * diamonds_df['y'] * diamonds_df['z']
diamonds_df.head()
# %%
# Group the DataFrame by 'cut' and 'color' and calculate the average price and carat for each group.
grouped_stats = diamonds_df.groupby(['cut', 'color']).agg({'price': 'mean', 'carat': 'mean'})
print("\nAverage price and carat for each group (cut and color):")
print(grouped_stats)
# %%
grouped_stats
# %%
# Calculate the total count of diamonds for each 'cut' and 'clarity' combination.
diamonds_count_by_cut_clarity = diamonds_df.groupby(['cut', 'clarity']).size().reset_index(name='count')
print("\nTotal count of diamonds for each 'cut' and 'clarity' combination:")
print(diamonds_count_by_cut_clarity)
# %%
diamonds_count_by_cut_clarity
# %%
diamonds_df.to_csv('diamonds.csv')
# %%
