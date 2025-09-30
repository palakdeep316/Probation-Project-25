import pandas as pd
df = pd.read_csv("DataClean.csv")
text_cols = ['Status', 'Education', 'Industry', 'Location', 'AI Risk']
for col in text_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()
df['Date Recorded'] = pd.to_datetime(df['Date Recorded'], errors='coerce')
for col in text_cols + ['Age Group']:
    df[col] = df[col].replace('nan', 'Unknown')
df['Location'] =df['Location'].str.replace('delhi','urban').str.replace('hyderabad','urban').str.replace('bangalore','urban').str.replace('mumbai','urban')
age_col = df['Age Group'].astype(str)
age_col = age_col.str.replace('_', ' ').str.replace('-', ' ').str.replace('to', ' ').replace('  ', ' ').replace('  ', ' ')
age_col = age_col.str.strip().str.replace(' ','-')
df['Age Group'] = age_col
median_years = df['Years of Experience'].median()
median_salary = df['Monthly Salary (INR)'].median()
df['Years of Experience'] = df['Years of Experience'].fillna(median_years)
df['Monthly Salary (INR)'] = df['Monthly Salary (INR)'].fillna(median_salary)
edu={'phd': 'phd', 'ph.d': 'phd', 'masters': 'masters', 'master': 'masters','diploma': 'diploma','high school': 'high school', 'hs': 'high school','bachelors': 'bachelors', 'bachelor': 'bachelors'}
df['Education'] = df['Education'].replace(edu)
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)
print(df)