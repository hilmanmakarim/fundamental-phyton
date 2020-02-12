# solve 6
# Jarak A dan B = 120 km
# A 60 km/jam
# B 40 km/jam
A = int (input('masukkan kecepatan A : '))
B = int (input("masukkan kecepatan B : "))
jarak = int(input('Masukkan jarak antara keduanya: '))
Tawal = input('masukkan waktu saat ini : ')
Tawal_jam = int(Tawal[0:2])
Tawal_menit = int(Tawal[3:5])
t=jarak/(A+B)
konversi=t*60
jam = int(konversi/60)
menit = int(konversi % 60)
HasilJam =Tawal_jam+jam
HasilMenit=Tawal_menit+menit
print(f"waktu yang dibutuhkan adalah jam {HasilJam} lewat {HasilMenit} menit")

speedA = int(input('Masukkan kecepatan A = \n'))
speedB = int(input('Masukkan keccepatan B = \n'))
speedTotal = speedA + speedB
distance = int(input ('Masukkan jarak antara keduanya = \n'))

timeCrash = distance / speedTotal
timeInHour = int(timeCrash)
timeInMinute = int((timeCrash*60)%60)

print(f'A dan B akan bertemu setelah {timeInHour} jam {timeInMinute} menit.')