#  Number one
# def wordRev
# Buatlah sebuah function yang meneria sebuah kata
# reverse huruf setiap kata

# contoh :
# Hello my friend -- > olleH ym dneirf
# # abc de efg --> cba ed gfe
y = input("masukkan sebuah kalimat yang ingin direverse :")

# print (' '.join((word[::-1] for word in y.split())))
def wordrev(word) :
    word = ''.join(reversed(word))
    word = word.split()
    word.reverse()
    word = ' '.join(word)
    return word
print(wordrev(y))
  
# Number Two
# def sum01
# Buat function yang menerima list of number
# Jumlahkan semua angka, kecuali angka yang ada diantara angka 0 - 1

# [2, 4, 0, 1, 11] -- > 17 (0, 1 tidak masuk hitungan)
# [7, 0, 3, 1, 7, 9] --> 23 (0, 3, 1 tidak masuk hitungan)
# [5, 0, 3, 2, 1] --> 5 (0, 3, 2, 1 tidak masuk hitungan)

# a = [2, 4, 0, 1, 11]
# b = [7, 0, 3, 1, 7, 9]
# c = [5, 0, 3, 2, 1]
# def sum01(lis) :
#     # temukan index angka 0 dan 1
#     # untuk index angka 1 dijumlahkan dengan angka 1 
#     zero = lis.index(0)
#     one = lis.index(1)+1
    
#     # delete data dari index angka 0 hingga index angka 1
#     del lis[zero:one]

#     result = sum(lis)

#     # print hasil jumlah dari daa lis
#     print(result)

# sum01(a)
# sum01(b)
# sum01(c)
