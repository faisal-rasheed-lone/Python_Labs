# Practicing the fundaments of pandas library
# creating a data set using the dictionary
import pandas as pd
dict = {'Name': ['faisal', 'Aamir', 'Hanan', 'Huzaif', 'Mudasir', 'Owais'],
        'Marks': [88, 89, 90, 70, 75, 86],
        'Gender': ["male",'female', 'female', 'male', 'male', 'female']}

df = pd.DataFrame(dict)
# printing the dataframe

print(df)
print('------------------------------------------------')
# printing only ist three rows
print(df.head(3))
print('--------------------------------------------------')
# printing last 3 rows
print(df.tail(3))
print('--------------------------------------------------')
# finding the shape of the dataset
print(df.shape)
print('--------------------------------------------------')
# getting information about the dataset
print(df.info())
print('--------------------------------------------------')
# getting overall statistics of the dataset
print(df.describe(include='all'))
print('--------------------------------------------------')
# finding the unique values from the gender column
print(df['Gender'].nunique())
print(df['Gender'].value_counts())
print('--------------------------------------------------')
# Name of students having marks between 90 and 100
print(df[df['Marks'].between(90, 100)])
#     Name  Marks  Gender
# 2  Hanan     90  female
print('--------------------------------------------------')
# Finding Average , min, max of the Marks column
print(df['Marks'].mean())
# Adding this average column to the dataFrame
df['Average'] = df['Marks'].mean()
print(df)
#       Name  Marks  Gender  Average
# 0   faisal     88    male     83.0
# 1    Aamir     89  female     83.0
# 2    Hanan     90  female     83.0
# 3   Huzaif     70    male     83.0
# 4  Mudasir     75    male     83.0
# 5    Owais     86  female     83.0
print('--------------------------------------------------')
# printing Max marks
print(df['Marks'].max())
print('--------------------------------------------------')
# Using map function
df['Male_Female'] = df['Gender'].map({'male': 1, 'female': 0})
print(df)
#       Name  Marks  Gender  Average  Male_Female
# 0   faisal     88    male     83.0            1
# 1    Aamir     89  female     83.0            0
# 2    Hanan     90  female     83.0            0
# 3   Huzaif     70    male     83.0            1
# 4  Mudasir     75    male     83.0            1
# 5    Owais     86  female     83.0            0
print('--------------------------------------------------')
# Dropping the Average column
print(df.drop('Average', axis=1))
#       Name  Marks  Gender  Male_Female
# 0   faisal     88    male            1
# 1    Aamir     89  female            0
# 2    Hanan     90  female            0
# 3   Huzaif     70    male            1
# 4  Mudasir     75    male            1
# 5    Owais     86  female            0
print('--------------------------------------------------')
# sorting the dataFrame
print(df.sort_values(by=['Marks'], ascending=False))
#       Name  Marks  Gender  Average  Male_Female
# 2    Hanan     90  female     83.0            0
# 1    Aamir     89  female     83.0            0
# 0   faisal     88    male     83.0            1
# 5    Owais     86  female     83.0            0
# 4  Mudasir     75    male     83.0            1
# 3   Huzaif     70    male     83.0            1





