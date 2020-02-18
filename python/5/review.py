# tuple
# menggunakan kurung()
# akses value menggunakan index

# days = ('sunday','monday','tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


# x = input('masukkan kalimat yang ingin dimasukkan : ')
# vowel = ("aiueoAIUEO")
# def no_vowel(string): #cara ketiga
#   for l in vowel:
#     string = string.replace(l,"")
#   return string

# res = no_vowel(x)
# print(res)

# new = "" #cara kedua
# for i in x:
#     if i not in vowel:
#         new += i

# print(new)

# def check(x):
#     # resCheck = x not in vowel
#     # if resCheck==True:
#     #     return True
#     # else:
#     #     return False
#     return x not in vowel


# def no_vowel(text) :
#     resFilter = list(filter(check, text))
#     return"".join(resFilter)

# print(no_vowel(x))


# numbers = [1, 7, 34, 12, 6 , 9, 16]

# def even(x) :
#     resModulus = x % 2
#     if resModulus == 0 :
#         return True
#     else :
#         return False

# resFilter = list(filter(even, numbers))
# print(resFilter)

# Python program to print Even Numbers in a List 

# list of numbers 
# angka1 = [2, 12, 4, 7, 8] 
# angka2 = [3, 5, 7, 14, 15]
# # even_nos = list(filter(lambda x: (x % 2 == 0), x)) 

# # print(even_nos) 
# def outliers(lis) :
#     oddlist =[]
#     evenlist = []
#     ganjil = 0
#     genap = 0
#     for i in lis:
#         if i % 2 == 0:
#             genap +=1 
#             evenlist.append(i)
#         else :
#             ganjil +=1
#             oddlist.append(i)
#     if ganjil > genap :
#         return evenlist[0]
#     else :
#         return oddlist[0]

# print(outliers(angka1))
# print(outliers(angka2))

angka = input(f"masukkan angka :" )

def num(x) :
    x = str(x)
    x = list(x)
    b = 1
    for i in x:
        i = int(i)
        b *= i
    return b

def count(y):
    i = 0
    while y >= 10:
        i += 1
        y = num(y)
    return i

print (count(int(angka)))
# g = 1
# for i in range (len(angka)):
#     n = int(angka[i])
#     g = g* n
#     i+=1


# print(g)
# Buatlah sebuah function yang menerima string
# akan menghilangkan semua huruf vokal
# dan me return string yang masuk setelah di hilangkan huruf vokalnya

# CLUE :
# filter
# ... not in ...
# join

# Today is friday
def check(x):
    # hasil evaluasi dari .. not in .. adalah boolean
    # sehingga bisa langsung kita return
    return x not in ['a', 'i', 'u', 'e', 'o']

def no_vowel(string):
    resFilter = list(filter(check, string))
    return "".join(resFilter)
    
no_vowel('Today is friday')

# resVowel = no_vowel('Today is friday')
# print(resVowel)


# Happy weekend

####################################################################
# Berapa jumlah perkalian yang dapat dilakukan untuk sebuah integer
# 399 -> 3*9*9 = 243 -> 2*4*3 = 24 -> 2*4 = 8 (3 kali)
# 39 -> 3*9 = 27 -> 2*7 = 14 -> 1*4 = 4 (3 kali)
# 24 -> 2*4 = 8 (1 kali)
# 4 -> nol kali
####################################################################

def yep(numb):
    # numb : 399
    numb = str(numb)

    # numb = '399'
    listInt = []
    for i in numb: # '3', '9', '9'
        listInt.append(int(i))

    #listInt = [3, 9, 9]

    count = 0
    while len(listInt) > 1:
        # Mengalikan semua angka pada list
        res = 1
        for i in listInt: # listInt = [3, 9, 9]
            res *= i 

        # res = 8
        
        # Hasil akhir dari perkalian akan diubah menjadi list lagi
        # Untuk kemudian dilakukan perkalian seperti di atas
        res = str(res)
        # res = '243'
        listInt = []
        for i in res:
            listInt.append(int(i))

        # listInt = [8]

        count += 1

    return count


print('Banyaknya perkalian : ', yep(399))



##################################################################
# tentukan apakah sebuah kata memiliki perulangan huruf atau tidak
# buatlah function untuk mendeteksi itu
# Hello -> false
# Sunday -> true
# ini -> false
# Sunkis -> false
#################################################################

kata = input('Masukkan sebuah kata: ')
def repeatWord(word):
    word = word.lower()
    word = list(word)
    word1 = list(dict.fromkeys(word))
    if len(word) == len(word1):
        return True
    else:
        return False
print(repeatWord(kata))