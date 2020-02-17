# WHILE
# Looping selama sebuah kondisi terpenuhi
# apa yang ada setelah keyword 'while' haruslah merupakan sebuah
# boolean
# akan menjalankan kode pada block while ketika bernilai True
# setiap kali menyelesaikan kode didalam while maka akan kembali
# check kondisi boolean setelah keyword "while"
# number = 0
# while number < 5 :
#     print(f'Ini adalah looping ke - {number}')
#     number+=1

# Ini adalah looping ke - 0
# Ini adalah looping ke - 1
# Ini adalah looping ke - 2
# Ini adalah looping ke - 3
# Ini adalah looping ke - 4

again = True
number = 0
while again :
    if number < 3 :
        print (f"Do it again!")
        number +=1
    else:
        again = False
        print (f"Stop!")
        