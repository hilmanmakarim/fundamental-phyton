# angka = 1
# while(angka <= 10) :
#         print(angka)
#         angka =

# y = 'Nomor urut '

# for item in range(0,20,2) :
#         print(y + str(item))





print('solve 1 \n')
# z= ''
# # solve 1
# # for yang awal menentukan banyaknya baris
# for item in range(5) :
#         # for kedua mementukan banyaknya bintang di baris
#         for item1 in range(5-item) :
#                 z += ' * '
#         z += '\n'
# print(z)
# print('selanjutnya solve 2 \n \n solve 2')


# solve 2

y = ''
for items in range(5) :
        for item2 in range(5-items) :
                y += '* '
        y += '\n'
print(y)

for items in range(1,5) :
        for item2 in range (0,items+1) :
                y += '* '
        y += '\n'
print(y)

print('selanjutnya solve 2 cara lain \n')

w = ''
for items in range(9) :
        for item2 in range(-1, abs(4-items)) :
                w += '* '
        w += '\n'
print(w)

print('\n solve 3 \n')

# solve 3

solv3 = ''
for solve3 in range(10) :
        for solves3 in range(9-solve3):
                solv3+= '  '
        for bintang in range((2*solve3)+1):
                solv3+= '* '
        solv3 += "\n"
print(solv3)

print('\n solve 4 \n')

# solve 4

solv4 = ''
for solve4 in range(10) :
        for solves4 in range(solve4):
                solv4+= '  '
        for bintang in range(19-(2*solve4)):
                solv4+= '* '
        solv4 += "\n"
print(solv4)

print('\n solve 5 \n')

solv3 = ''
for solve3 in range(5) :
        for solves3 in range(4-solve3):
                solv3+= '  '
        for bintang in range((2*solve3)+1):
                solv3+= '* '
        solv3 += "\n"
        enter = 4- solve3
        if enter>0 :
                 solv3 +='\n'
print(solv3)
solv4 = ''
for solve4 in range(5) :
        for solves4 in range(solve4):
                solv4+= '  '
        for bintang in range(9-(2*solve4)):
                solv4+= '* '
        solv4 += "\n"
        enter = 9-solve4
        if enter>0 :
                solv4 += '\n'
print(solv4)