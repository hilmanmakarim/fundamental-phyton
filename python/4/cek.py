# filter integer dari string
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# filter_list[1,2,'a','b']

# def filter_list(l):
#     new_list = []
#     for x in l:
#         if type(x) == int:
#             new_list.append(x)
#     return new_list

# def filter_list(l): #cara kedua
#     return [i for i in l if not isinstance(i, str)]

# print(filter_list([1,2,'a','b']))
# print(filter_list([1,'a','b',0,15]))
# print(filter_list([1,2,'aasf','1','123',123]))

# cara menghitung integer yang tergabung digital roots

# def digital_root(n):
#     while n >= 10:
#         n = sum(int(i) for i in str(n))
#     return n

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
# print(digital_root(16))
# print(digital_root(942))
# print(digital_root(132189))
# print(digital_root(493193))

# friend or foe

# def friend(x):
#     ans = []
#     for i in x:
#         if len(i) == 4:
#             ans.append(i)

#     return ans

# print(friend(["Ryan", "Kieran", "Mark", ]))