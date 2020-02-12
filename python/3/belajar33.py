# Belajar Loop satu
# belajar mencari angka ganjil dan genap menggunakan while, list range, dan for in
Ganjil = 1
while Ganjil <= 10 :
    print(f'Ganjil : {Ganjil}')
    Ganjil +=2
Genap = 0
while Genap <= 10 :
    print(f'Genap : {Genap}')
    Genap +=2

k = 1 
for k in range (0, 9 ,2) :
    print (f'genap :{k}') 
for k in range (1, 10, 2):
    print (f'ganjil : {k}')
# genap = list(range(0,11,2))
# print(genap)
# for ganjil in range(1,11,2):
#     print(ganjil)


stars = ''
for i in range(5) :
    stars += '*'
    stars += '\n'
print (stars)

stars = ''
row = 7

# menentukan banyaknya baris
for i in range(row) :
    # menentukan banyak bintang per baris
    for j in range(row) :
        stars += ' + '
    stars+='\n'
print(stars)

# membuat segi empat
row = 5
x = ''
for h in range (row) :
    for g in range (row) :
        x += ' * '
    x += '\n'
print(x)