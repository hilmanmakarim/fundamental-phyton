
hargaApel = 10000
hargaAnggur = 15000
hargaJeruk = 20000
qtyApel = 5
qtyAnggur = 7
qtyJeruk = 8
Apel = int(input('Berapa apel yang ingin dibeli ? '))
if Apel > qtyApel :
    print ('Kesalahan dalam input karena stock yang ada hanya 5 apel')
    while Apel > qtyApel :
        Apel = int(input('Berapa apel yang ingin dibeli ?'))
Anggur = int(input('Berapa anggur yang ingin dibeli ? '))
if Anggur > qtyAnggur:
    print('kesalahan dalam input karena stock yang ada hanya 7 anggur')
    while Anggur > qtyAnggur :
        Anggur = int(input('Berapa anggur yang ingin dibeli ?'))
Jeruk = int(input('Berapa jeruk yang ingin dibeli ? '))
if Jeruk > qtyJeruk :
    print('kesalahan dalam input karena stock yang ada hanya 8 jeruk')
    Jeruk = 0
jumTotalApel = Apel * hargaApel
jumTotalAnggur = Anggur * hargaAnggur
jumTotalJeruk = Jeruk * hargaJeruk
totalBelanja = jumTotalApel + jumTotalAnggur + jumTotalJeruk
print(f'jumlah apel yang dibeli sebanyak {Apel} x {hargaApel} sehingga harganya adalah Rp. {jumTotalApel},')
print(f'jumlah anggur yang dibeli sebanyak {Anggur} x {hargaAnggur} sehingga harganya adalah Rp. {jumTotalAnggur},')
print(f'jumlah jeruk yang dibeli sebanyak {Jeruk} x {hargaJeruk} sehingga harganya adalah Rp. {jumTotalJeruk},')
print(f'total belanja anda adalah Rp. {totalBelanja}.')