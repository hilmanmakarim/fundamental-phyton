
########
# SORT #
########

# Mengurutkan data ASCENDING / ASC / kecil - besar

# listStr = ['Can', 'Angry', 'Evil', 'Forgive']
# listInt = [7, 5, 9, 1, 3]
# listBool = [False, True, True, False]

# ['Angry', 'Can', 'Evil', 'Forgive']
# listStr.sort()
# print(
#     listStr
# )

# [1, 3, 5, 7, 9]
# listInt.sort()
# print(
#     listInt
# )

# [False, False, True, True]
# listBool.sort()
# print(
#     listBool
# )

# Mengurutkan data DESCENDING / DESC / besar - kecil

# listStr = ['Can', 'Angry', 'Evil', 'Forgive']
# listInt = [7, 5, 9, 1, 3]
# listBool = [False, True, True, False]

# ['Forgive', 'Evil', 'Can', 'Angry']
# listStr.sort(reverse = True)
# [9, 7, 5, 3, 1]
# listInt.sort(reverse = True)
# [True, True, False, False]
# listBool.sort(reverse = True)

# print(listStr)
# print(listInt)
# print(listBool)

# Ambil 3 gaji terendah dan 3 gaji tertinggi

# listSalary =[
#     7500000,
#     9000000,
#     300000,
#     200000,
#     1700000
# ]

# # Terendah
# listSalary.sort()
# print(
#     listSalary[0:3]
# )

# # Tertinggi
# listSalary.sort(reverse=True)
# print(
#     listSalary[0:3]
# )

# listStr = ['can', 'angry', 'evil', 'forgive']
# listInt = [7, 5, 9, 1, 3]
# listBool = [False, True, True, False]

# # Forgive, evil, can, angry
# listStr.sort(reverse=True)
# # [9, 7, 5, 3, 1]
# listInt.sort(reverse=True)
# # [true, true, false, false]
# listBool.sort(reverse=True)

# print(listStr)
# print(listInt)
# print(listBool)

# Latihan pertama
# print(f'\n \n latihan pertama \n \n')

# listX= [40,100, 1, 5, 25, 10]
# def minmax(listNumber):
#     listNumber.sort()
#     return listNumber
# sortX= minmax(listX)

# print(listX)
# print(sortX)
# print(max(listX))
# print(min(listX))


# X= [40,100, 1, 5, 25, 10]
# y = (5, 25, 10)

# def maxMin(listNum) :
#     startList = listNum
#     parentList = []

#     #  [1, 5, 10, 25, 40, 100]
#     listNum.sort()
#     min = listNum(0)
#     max = listNum(-1)

#     # return [ nilai awal, terendah, tertinggi]
#     parentList.append(startList)
#     parentList.append(min)
#     parentList.append(max)

#     return parentList

# temp = maxMin(y)
# print(max(y))

X= [40,100, 1, 5, 25, 10]
z = []
while X:
    minimum = X [0]  # arbitrary number in list 
    for y in X: 
        if y < minimum:
            minimum = y
    z.append(minimum)
    X.remove(minimum)    

print (z)
print (max(z))
print (min(z))