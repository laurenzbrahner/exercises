# %% [markdown]
# # Data preparation

# %%
# setup
import pandas as pd

# %% [markdown]
# ## Data import

# %%
URL = 'https://raw.githubusercontent.com/kirenz/datasets/master/3_4_data.csv'

df = pd.read_csv(URL)

# %%
df

# %%
df = df.melt(id_vars=['Month', 'Date', 'Goal'],
            value_vars=['Direct Sales', 'Indirect Sales'],
            var_name='Sales Type',
            value_name='Sales'
            )

df

# %% [markdown]
# ### Create new variable

# %%
df['Text'] = 'GOAL'

# %% [markdown]
# ### Change data format

# %%
df.info()

# %%
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df.info()

# %%
LIST_CAT = ['Month', 'Sales Type']

for i in LIST_CAT:
    df[i] = df[i].astype('category')


# %%
df.info()

# %% [markdown]
# ## Save data

# %%
df.to_csv('3_4_data_new.csv')


