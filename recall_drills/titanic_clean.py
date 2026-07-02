# titanic_cleam.py

import pandas as pd

def drop_irrelevent_columns(df):
    #df = df.copy()
    cols_to_drop = ["alive", "class", "who", "adult_male", "embark_town", "alone", "deck"]
    return df.drop(columns = [c for c in cols_to_drop if c in df.columns])


def fill_missing_age(df):
    #fill missing age with median of passanger pclass
    df = df.copy()
    df['age'] = df.groupby('pclass')['age'].transform(
        lambda x: x.fillna(x.median())
    )
    return df

def fill_missing_embarked(df):
    #fill missing embarked with most frequent value
    df = df.copy()
    mode = df['embarked'].mode()[0]
    df['embarked'] = df['embarked'].fillna(mode)
    return df

def encode_sex(df):
    df= df.copy()
    df['sex'] = df['sex'].map({'female':0, 'male':1})
    return df

def clean_data(df):
    """full cleaning pipline- one call does it all"""
    df = (
        df
        .pipe(drop_irrelevent_columns)
        .pipe(fill_missing_age)
        .pipe(fill_missing_embarked)
        .pipe(encode_sex)
    )

    return df


#==========================================================
#  Exploration History
#==========================================================
'''
#%%
import seaborn as sns
import pandas as pd


#load data
df = sns.load_dataset('titanic')
df.head()
df.info()
df.describe(include='all')
df.isnull().sum()
# %%


#%%
df_test = df.copy()
df_test['age'] = df_test.groupby('pclass')['age'].transform(lambda x: x.fillna(x.median()))
#check if any missing remain
df_test['age'].isnull().sum()

# %%


#%%
import matplotlib.pyplot as plt

df['age'].hist(alpha=0.5, label = 'before')
df_test['age'].hist(alpha=0.5, label = 'after')
plt.legend()
plt.show()

'''

if __name__ == "__main__":
    import seaborn as sns

    raw_df = sns.load_dataset('titanic')

    clean_df = clean_data(raw_df)

    print(f" missing values after cleaning: \n {clean_df.isnull().sum()}")
    print(f"First 5 rows: \n {clean_df.head()}")


