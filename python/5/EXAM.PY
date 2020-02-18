# Nama : Hilman Fadhil Makarim
# Ujian Fundamental - Purwadhika 
# Job Connector - Data Science
# Lokasi Bekasi

#######################
#       No. 1         #
#######################


# def pnumber(x) :
#     res = len(x)
#     if res >9 :
#         phoneList = []
#         for num in x:
#             phoneList.append("". join(str(num)))
#         phStr = phoneList
#         print(phoneList)
#         ac = "".join(phStr[0:3])
#         prefix = "".join(phStr[3:6])
#         suffix = "".join(phStr[6:10]) 
#         print("({}) {}-{}".format(ac, prefix, suffix))
#     else :
#         print("False")
    
# pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9])



#######################
#       No. 2         #
#######################
# def kata(text) :
#     res = len(text)
#     if 1 <= res <= 20 :
#         textUpper = text.title()
#         textSplit = textUpper.split(" ")
#         textJoin = "".join(textSplit)
#         print(f"#{textJoin}")
#     else :
#         print("False")

# kata("Hello there how are you doing")
# kata("    Hello   world")
# kata("")

#######################
#       No. 3         #
#######################

def fix(a):
    list1 = []
    for item in a:
        if len(list1) == 0:
            list1.append(item)

        elif len(list1) > 0:
            if list1[-1] != item:
                list1.append(item)
    print(list1)
uniq = 'KKKKLLLMMNKKKKLLLL'
uniq1 = 'KLLMmKN'
uniq2 = [1,2,2,3,3]
fix(uniq)
fix(uniq1)
fix(uniq2)

#######################
#       No. 4         #
#######################
# number1 = int(input('Number1: '))
# if number1 < 1 or number1 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number2 = int(input('Number2: '))
# if number2 < 1 or number2 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number3 = int(input('Number3: '))
# if number3 < 1 or number3 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number4 = int(input('Number4: '))
# if number4 < 1 or number4 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number5 = int(input('Number5: '))
# if number5 < 1 or number5 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number6 = int(input('Number6: '))
# if number6 < 1 or number6 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number7 = int(input('Number7: '))
# if number7 < 1 or number7 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")

# allnumber = [number1, number2, number3, number4, number5, number6, number7]

# allnumbers= []
# for i in allnumber:
#     if 1 <= i <= 9 :
#         allnumbers.append(i)
# print(f"1. Angka yang diinput : {allnumbers}")
# def ascending(num):
#     num.sort()
#     print(f"2. Sort ascending : {num}")
# ascending(allnumbers)
# def descending (angk)
#     angk.sort(reverse =True)
#     print(f"3. Sort descending :{angk}")
# descending(angk)

# def genap(x):
#     newlist1=[]
#     newlist2=[]
#     for num in listInput:
#         numCtrl=num%2
#         if numCtrl==0:
#             newlist1.append(num) #genap
#         else:
#             newlist2.append(num) #ganjil
#     print(newlist1,newlist2)    

# # maaf pak ga selesai