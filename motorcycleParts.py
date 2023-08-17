import plistlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('dataSets/sales_data.csv')
sns.set()
print(df.head())

# what are the total sales for each payment method
total_sales = df.groupby(by='payment')[['total']].sum()
print(total_sales)
_ = total_sales.plot(kind='bar', rot=360,
                     xlabel='payment method', ylabel='total sales')


# avarage unit price per product line
avg_unit_price_per_line = df.groupby('product_line')[['unit_price']].mean()
print(avg_unit_price_per_line)
_ = avg_unit_price_per_line.sort_values(by='unit_price').plot(
    kind='bar', rot='360', xlabel='product line', ylabel='average price', fontsize=6)


# total purchases and average amount per purchase
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)
total_per_client = df.groupby(by='client_type')[['total']].sum()
print(total_per_client)

_ = sns.histplot(data=df, x='client_type', ax=ax0)
_ = sns.boxplot(data=df, x='client_type', y='total', ax=ax1)


# purchases per client, per product line
fig, (ax2, ax3) = plt.subplots(nrows=1, ncols=2)

retail = df[df['client_type'] == 'Retail']
retail_per_line_total = retail.groupby(by='product_line')[['total']].sum()
_ = retail_per_line_total.sort_values(by='total').plot(
    kind='bar', xlabel='prduct_line', ylabel='retail total', rot='360', fontsize=6, ax=ax2)


wholesale = df[df['client_type'] == 'Wholesale']
wholesale_per_line_total = wholesale.groupby(by='product_line')[
    ['total']].sum()
_ = wholesale_per_line_total.sort_values(by='total').plot(
    kind='bar', ylabel='wholesale total', rot='360', fontsize=6, ax=ax3)


# sales per client by warehouse
fig, ax = plt.subplots()
_ = sns.countplot(data=df, x='warehouse', hue='client_type')

plt.show()
