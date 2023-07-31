# dictionary and its operations
# creating a dictionary
dict = { 'faisal': '555-444',
         'Hanan': '444-555',
         'Shahan': '777-888',
         'Owais': '666-333'
}
print(dict)     # o/p {'faisal': '555-444', 'Hanan': '444-555', 'shahaan': '777-888', 'owais': '666-333'}

# updating dictionary
dict['faisal'] = '111-444'
print(dict)     # o/p {'faisal': '111-444', 'Hanan': '444-555', 'Shahan': '777-888', 'Owais': '666-333'}

# printing using for loop
for a in dict:
    print(a, dict[a])      # o/p faisal 111-444
                            #   Hanan 444-555
                            #   Shahan 777-888
                            #   Owais 666-333
# functions
# del used to delete item
del dict['Shahan']
print(dict)                 # o/p {'faisal': '111-444', 'Hanan': '444-555', 'Owais': '666-333'}

# get() ... used to get item using key
print(dict.get('faisal', 'element not in dictionary'))           # o/p 111-444

# keys() ... used to get keys
print(dict.keys())              # o/p dict_keys(['faisal', 'Hanan', 'Owais'])

# values()... used to get only values from dictionary
print(dict.values())               # dict_values(['111-444', '444-555', '666-333'])

# items()... used to get both keys and values
print(dict.items())     # o/p dict_items([('faisal', '111-444'), ('Hanan', '444-555'), ('Owais', '666-333')])
for a, b in dict.items():
    print(a, b, end=" ")        # o/p faisal 111-444 Hanan 444-555 Owais 666-333
print()

# pop()... used to delete item using key ..but it returns ..irrespective of del
a = dict.pop('Owais')
print(a)                # o/p 666-333

# update ...used to update the dictionary
dict.update({'danish': '444-444'})
print(dict)             # o/p {'faisal': '111-444', 'Hanan': '444-555', 'danish': '444-444'}

# clear().. used to clear the dictionary
dict.clear()
print(dict)             # o/p {}
