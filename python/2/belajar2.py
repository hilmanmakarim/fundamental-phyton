# andi = 40
# andi*=2
# print(andi)
# andi/=2
# print(andi)
# andi+=2
# print(andi)
# andi-=2
# print(andi)
# andi%=2
# print(andi)

# x = 5
# y = '5'
# z = 6

# print(x==int(y) and int(z)<z);
# print(x==int(y) or int(y)<z);
# print(not(x==int(y) or int(y)<z));

jomblo = input( 'apakah dirimu jomblo ? ')
if jomblo :
    print('Masih jomblo!')
else :
    print('Udah taken!')

# > lebih besar
# < lebih kecil
# =< lebih kecil sama dengan
# >= lebih besar sama dengan
satu = 1
dua = 2
one = '1'
print(4 > 5)
print(7 >= 6)
print(8 < 8)
print (8 <= 8)
print(satu == satu)

# and merupakan keadaan yang dimana keduanya harus bernilai true,
# apabila ada satu yang berbeda maka akan menghasilkan false
# or merupakan keadaan yang dimana salah satunya cukup menghasilkan true maka akan menghasilkan true untuk
# keduanya.

payday = True
if payday :
    print('Ayo kita berbelanja')
else :
    print('tidur yuk.')


age = int(input('silahkan masukkan umurmu ? '))
if age >= 18 :
    print('masuk')
elif age >= 15 and age <= 17 :
    print('masuk dengan bimbingan orang tua')
else:
    print('katakan Tidak')