import pandas as pd
import matplotlib.pyplot as plt
Stock_Market = {'Year': [2017, 2017, 2017, 2017], 'Month': [12, 11, 12, 9], 'Interest_Rate': [
    1.75, 2.5, 2.5, 2.75, ], 'Unemployement_Rate': [5.4, 5.6, 6.5, 5.5], 'Stock_Index_Price': [1464, 1394, 1357, 1293]}
df = pd.DataFrame(Stock_Market, columns=[
                  'Year', 'Month', 'Interest_Rate', 'Unemployement_Rate', 'Stock_Index_Price'])
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel(['Stock Index Price'], fontsize=14)
plt.grid(True)
plt.show()
