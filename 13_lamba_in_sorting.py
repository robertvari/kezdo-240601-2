my_friends = ["Vári Róbert", "Kiss Balázs", "Kovács Elemér", "Tóth Krisztina", "Kiss Csaba Géza"]

default_sorting = sorted(my_friends)
print(default_sorting)


modified_sorting = sorted(my_friends, key=lambda name: name.split()[-1])
print(modified_sorting)