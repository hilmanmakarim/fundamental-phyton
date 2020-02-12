# untuk menampilkan teks (komentar)
# print ('My first code')

# CTRL J untuk menampilkan terminal
# Variable
# untuk menyimpan sebuah data
# Variable tidak bisa diawali dengn angka
# string, tipe data yang menympan teks = 'Vinales'
#float, tipe data yang desimal
# integer, tipe data yang berupa angka
# number, float : desimal (0.25, 3.14), integer : bulat (3, 5, 6)
# ctrl L untuk menghapus atau membersihkan di terminal
# apabila menggunakan dua kata, kata pertama, hurufnya harus kecil, kata kedua dst nya hurufnya besar
# contoh firstName
# istilah namanya adalah camelCase
# DUPLICATE CODE = shift alt + down arrow
# type untuk mengetahui tipe data misal menggunakan result = type(age)
# dari sebuah variabel
# functin input digunakan untuk menerima inputan user
# tapi untuk memudahkan cukup menggunakan print(type(age))
# membuat komentar ; CTRIL +/

# Variable

# firstName = 'Vinales'
# lastName = 'John'
# age = '32'
# print (firstName)
# print (lastName)
# print (age)
# result = type(age)
# print (result)
# print (type(age))
# day = input ('hari apakah saat ini?')
# print ('hari ini adalah hari' + day )

# Aritmatika

# usiaAndi = 40
# usiaBudi = 20
# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaBudi ** 2)
# print(4 **0.5)

# numOne = 10
# numTwo = 5
# numThree = '7'
# # result = numOne + numTwo
# # hasil = numOne + int(numThree)

# numOneString = str(numOne)
# numTwoString = str(numTwo)
# # resultString = str(result)

# result = numOne / numTwo

# print(numOneString + ' / ' + numTwoString + ' = ' +str(result))

# result = numOne * numTwo

# print(numOneString + ' * ' + numTwoString + ' = ' +str(result))

# result = numOne + numTwo
# print(numOneString + ' + ' + numTwoString + ' = ' +str(result))

# result = numOne - numTwo
# print(numOneString + ' - ' + numTwoString + ' = ' +str(result))

# result = numOne % numTwo
# print(numOneString + ' % ' + numTwoString + ' = ' +str(result))

# result = numOne ** numTwo
# print(numOneString + ' ** ' + numTwoString + ' = ' +str(result))

# ageJohn = 47
# ageKobe = 41

# # ageJohn = ageJohn + 3
# ageJohn +=3
# # ageKobe = ageKobe - 1
# ageKobe -=1
# print(ageJohn)
# print(ageKobe)

# module math
# mengimport sebuah angka
import math
# # mengabsolute sebuah nilai dengan desimal atau menjadi float
# print(math.fabs(-4))

# # mengabsolute sebuah nilai
# # print(abs(-13))

# # pangkat
# print(math.pow(2, 4))

# # Akar
# print(math.sqrt(64))

# membulatkan
print(round(4.7))
print(round(4.4))

# # floor membulatkan kebawah
print(math.floor(4.7))
print(math.floor(4.4))

# ceil membulatkan keatas
print(math.ceil(4.9))
print(math.ceil(4.1))

# # String
# x = 'Halo Dunia ku yang cerah'
# print(len(x)) #banyak karakter pada string
# # index dimulai dari nol
# #Mengetahui letak suatu kata
# print(x.index('Dunia')) 
# #memisahkan kata dalam satu kalimat
# print(x.split(' '))
# #mengeubah menjadi huruf kecil 
# print(x.lower()) 
# # mengubah menjadi huruf besar
# print(x.upper())
# #mengubah huruf besar untuk huruf pertama dalam satu kalimat
# print(x.capitalize())

print("hello, i'm ironman")
print('hello, i\'m ironman')
print("you are \"crazy\"")
print('you are "crazy"')
# /n untuk membuat baris baru / enter / new line
print("hello i'm ironamn \n and i am \"crazy\"")
print("hello i'm ironamn" + "\n" +"and i am \"crazy\"")