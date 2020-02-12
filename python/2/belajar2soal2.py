angka = int(input('Masukkan angka yang ingin diketahui ganjil atau genap ? '))
if angka % 2 == 0 :
    print('Genap')
else :
    print('ganjil')

massa = int(input('berapakah berat badan kamu ? '))
tinggi = int(input('berapakah tinggi badan kamu ? '))
tinggi = tinggi / 100
IMT = massa/(tinggi**2)

if IMT < 18.5 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan kurang!')
elif IMT >= 18.5 and IMT < 24.9 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan ideal.')
elif 29.9 > IMT >= 24.9 : #PENGGUNAAN RANGE tanpa menggunakan and
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan berlebih!')
elif IMT >= 29.9 and IMT < 39.9 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan sangat berlebih!')
else :
    print(f'IMT kamu adalah sebesar {IMT} sehingga Obesitas!')

# cara simple untuk yang diatas
IMT = 30.01
if IMT >= 39.9 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga Obesitas!')
elif IMT >= 30.0 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan sangat berlebih!')
elif IMT >= 25.0 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan berlebih!')
elif IMT >= 18.5 :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan ideal.')
else :
    print(f'IMT kamu adalah sebesar {IMT} sehingga berat badan kurang!')