# %%
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

#%%
url  = 'https://en.wikipedia.org/wiki/List_of_most-produced_aircraft'
page = requests.get(url)
soup = bs(page.text, 'html')
print(soup)

#%%
soup.find_all('table')[1]

#%%
soup.find('table', class_='wikitable sortable')

#%%
table = soup.find_all('table')[1]
print(table)

#%%
label = table.find_all('th')
print(label)

#%%
label_of_data = [label_name.text.strip() for label_name in label]
print(label_of_data)

#%%
df = pd.DataFrame(columns=label_of_data)
df
#%%
df.drop('Production period', axis=1, inplace=True)
#%%
column_data = table.find_all('tr')
#%%
for row in column_data[2:]:
    row_data = row.find_all('td')
    feature_of_data = [features.text.strip() for features in row_data]
    
    if len(feature_of_data) == len(df.columns):
        length_df = len(df)
        df.loc[length_df] = feature_of_data
    else:
        print(f"Skipping row with mismatched number of columns: {feature_of_data}")

# %%
df.rename(columns={'Notes': 'Start', 'Start': 'End', 'End': 'Notes'}, inplace=True)
# %%
df.to_csv('df_web.csv')


# %%
# test