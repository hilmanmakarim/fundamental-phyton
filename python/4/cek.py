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
# print(digital_root(399))
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

# # mengurutkan 1 2 3 4 5
# i = 1
# while i <=5:
#    print(i)
#    i = i + 1

# print("Finished!")

# # mengurutkan 3 ke 0
# i = 3
# while i>=0:
#    print(i)
#    i = i - 1

# # mengurtkan 5 ke 3
# i = 5
# while True:
#   print(i)
#   i = i - 1
#   if i <= 2:
#     break

# # print true
# print(range(20) == range(0, 20))
# # print range 3 ke 15 dengan perbedaan 3 angka
# numbers = list(range(3, 15, 3))
# print(numbers)

# # bikin option
# while True:
#    print("Options:")
#    print("Enter 'add' to add two numbers")
#    print("Enter 'subtract' to subtract two numbers")
#    print("Enter 'multiply' to multiply two numbers")
#    print("Enter 'divide' to divide two numbers")
#    print("Enter 'quit' to end the program")
#    user_input = input(": ")

#    if user_input == "quit":
#       break
#    elif user_input == "add":
#       ...
#    elif user_input == "subtract":
#       ...
#    elif user_input == "multiply":
#       ...
#    elif user_input == "divide":
#       ...
#    else:
#       print("Unknown input")


# # spin word yang katanya lebih dari sama dengan 5
# def spin_words(sentence):
#     arr = sentence.split()
#     ans = []
#     for i in arr:
#         if len(i) >= 5:
#             ans.append(i[::-1])
#         else:
#             ans.append(i)
#     return ' '.join(ans)


# print(spin_words("Welcome to the world"))

# # menghitung bit
# def countBits(n):
#     return str(bin(n)).count('1')

# print(countBits(1234))

# you're a square

def is_square(n):
    if n < 0:
        return False
    return n**0.5 == int(n**0.5)

print(is_square(-1))