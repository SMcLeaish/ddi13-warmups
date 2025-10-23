import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "product": ["pen","mug","book","lamp","cable","notebook","bottle","mouse"],
    "price":   ["2.5", "12.0", "22.0", "18.5", "9.5", "11.0", "25.0", "15.0"],
    "cat":     ["office","kitchen","books","home","electronics","office","kitchen","electronics"]
}
df = pd.DataFrame(data)
df['price'] = df['price'].astype('float')
electronics_mean  = df.groupby('cat')['price'].mean().loc['electronics']
office_mean =  df.groupby('cat')['price'].mean().loc['office']
electronics_items = df[df['cat'] == 'electronics']
office_items = df[df['cat'] == 'office']
print(f''' 
Electronics mean: {electronics_mean}
Electronics items: 
{electronics_items}
Office mean: {office_mean}
Office items: 
{office_items}
''')
sns.histplot(data=df, x='price', color='darkgreen',bins=10 ).set_title('Average Prices')
plt.show()