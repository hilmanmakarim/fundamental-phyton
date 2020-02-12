# solve 4
# diketahui jumlah umur 49
# rasionya 0.4
solve4 = ('Solve 4')
print(solve4)
x = 49
rAndiBudi= 0.4
Budi = x/(1+rAndiBudi)
Andi = x - Budi
print(Budi)
print(Andi)

totalUmur = 49
rasioAndi = 2
rasioBudi = 5
totalRasio = rasioAndi + rasioBudi

# cari tahu umur Andi
umurAndi = totalUmur * (rasioAndi/totalRasio) + 2
# cari tahu umur Budi
umurBudi = totalUmur * (rasioBudi/totalRasio) + 2

print(f'Umur Andi dua tahun lagi adalah {umurAndi} tahun')
print(f'Umur Budi dua tahun lagi adalah {umurBudi} tahun')
next = input('tekan enter apabila ingin lanjut ke solve berikutnya')

solve5 = 'solve 5'
print(solve5)

# tentukan kalimat awal
text = input('tentukan kalimat awal terlebih dahulu \n')
textlower = text.lower()
# tentukan karakter yang ingin dicari
word = input('huruf apa yang ingin dicari ? \n')
wordlower = word.lower()
jumlahHuruf = textlower.count(wordlower)

print(f'Jumlah huruf - {word} pada kalimat "{text}" adalah sebanyak {jumlahHuruf}.')
