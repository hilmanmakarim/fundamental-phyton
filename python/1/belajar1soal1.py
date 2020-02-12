# solve 1
solve1 = 'solve 1'
print(solve1)
import math

x = 4
y = 3
z = 2

w =((x+y*z)/(x*y))**z
print(w)

result = (x+y*z)/(x*y)
hasil = math.pow(result, z)
print(hasil)
next = input('tekan enter apabila ingin lanjut ke solve berikutnya')

# solve 2
solve2 = 'solve 2'
print(solve2)
# meminta input dari user, disimpan di variable
# Catatan input dari user nanti akan berupa 'string'
user = input('silahkan masukkan sebuah angka : ')
userint = int(user)
hasilUser = math.pow(userint, 2)
print (f'kuadrat dari {user} adalah {hasilUser}' )
next = input('tekan enter apabila ingin lanjut ke solve berikutnya')

# solve 3
solve3 = 'solve 3'
print(solve3)
a = int(input('Berapa jumlah hari yang ingin diubah ? \n'))
tahun = 360
bulan = 30

# 1 tahun = 360 hari
# 1 bulan = 30 hari
# 1 minggu = 7 hari
print(str(math.floor(a/tahun)) + ' tahun ' + str(math.floor((a%tahun)/30)) + ' bulan ' + str(a%bulan) + ' hari.')

# Tentukan banyaknya hari
days = a
# Tentukan jumlah tahun
years =  int(days / 360)
# sisa hari setelah diambil sekian tahun
days = days % 360
# Tentukan jumlah bulan
months = int(days / 30)
# sisa hari setelah diambil sekian bulan
days = days % 30
# Tentukan jumlah minggu
weeks = int(days / 7)
# sisa hari setelah diambil sekian minggu
days = days % 7

print(f'{a} hari terdiri dari {years} tahun, {months} bulan, {weeks} minggu dan {days} hari.')