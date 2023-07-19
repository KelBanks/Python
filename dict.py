#Dictionary Comprehension expression with if statements

original_dict = {'Jack': 38, 'Lincoln': 48, 'Theodore': 57, 'John': 33, 
                 'Sam': 23, 'Billy': 58, 'Zack': 56, 'Thomas': 29, 
                 'Patrick': 19, 'Ruddy': 66, 'Benjamin': 22, 'Brenda': 88}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

odd_dict = {k: v for (k, v) in original_dict.items() if v % 3 == 0}
print(odd_dict)