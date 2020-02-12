# DICTIONARY
# Menggunakan kurung kurawal {}
# Tidak menggunakan index, melainkan key
# Penulisan nama key bersifat case-sensitive
# Nama property ditulis menggunakan kutip (seperti string)

# price = {
#     'apple' : 10000,
#     "grape" : 15000,
#     'orange' : 15000
# }

# price['grape'] // 15000
# print(price['grape'])
# d = {
#     'numInt' : 123,
#     'numList' : [0, 1, 2],
#     'numStr' : 'Hello',
#     'numDict' : {'insideKey' : 100}
# }

# d['numList'] # [0, 1, 2]
# d['numDict'] # {'insideKey' : 100}
# d['numDict']['insideKey'] # 100

# heroes = {
#     'batman' : {'name' : 'Bruce', 'age' : 41}, 
#     'ironman' : {'name' : 'Tony', 'age' : 42}, 
#     'thor' : {'name' : 'Thor', 'age' : 39} 
# }

# heroes['ironman'] # {'name' : 'Tony', 'age' : 42}
# heroes['ironman']['name'] # 'Tony

# KEYS
# Untuk mendapatkan semua key dari dictionary
# keys = heroes.keys()

# keys # dict_keys(['batman', 'ironman', 'thor'])

# for i in keys:
#     print(i)

# VALUES
# Untuk mendapatkan semua value dari dictionary
# values = heroes.values()

# i = {"name" : 'Bruce', 'age' :41}
# for i in values :
#     print(
#         'Name: ' + i['name']
#     )


# TUPLE
# Menggunakan kurung ()
# Mengenal indexing, dimulai dari nol
# Nilainya tidak dapat dirubah

# colorTpl = ('Red', 'Green', 'Blue', 'Green', 'Blue')

# colorTpl[1] # Green
# colorTpl[-1] # Blue

# # Error, tidak bisa merubah nilai tuple
# # colorTpl[0] = 'Merah'

# # Count
# # Menghitung banyak data pada tuple
# count = colorTpl.count('Green') # 2

# # print(f'Jumlah warna hijau : {count}')

# # Index
# # Mencari index data tertentu
# index = colorTpl.index('Blue')

# # print(f'Index warna Blue : {index}')


# persons = (
#     {'name' : 'John', 'job' : 'Assasin'},
#     {'name' : 'Bruce', 'job' : 'Hunter'},
#     {'name' : 'Tony', 'job' : 'Engineer'},
# )

# persons[1]['name'] = 'Bruce Wyne'

# print(persons[1])

#  for in
# if else
# len()
# join
# print()
employee = [
    {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
    {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
    {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
]

# Mr. Steve has 2 hobbies, they are Video games, Football

# Mrs. Lina has 2 hobbies, they are Shop, Cook

# Mr. Reynald has 3 hobbies, they are Run, Hide, Jump

 

for i in employee :
    
    s= ", ".join(i['hobbies'])
    count = len(i['hobbies'])
    if i["gender"] == 'male' :
        i["name"] = 'Mr.' + i["name"]
    else :
        i["name"] = 'Mrs.' + i["name"]
    y = i["name"]
    print(f'{y} has {count} hobbies, they are {s}')
