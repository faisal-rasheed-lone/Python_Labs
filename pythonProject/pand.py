import pandas as pd
obj = pd.read_csv("pokemon_data.txt", delimiter='\t')
print(obj.head(3))
#print(obj.columns)
#print(obj['Name'])
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
