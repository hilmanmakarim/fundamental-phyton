# function
# block kode yang meiliki nama dan dapat di running secara berulang
# sebuah function dapat memilki input, output, atau keduanya
# sebuah function dapat "menghasilkan" nilai
############################################
# function tanpa input dan output
############################################
# deklaras/ pembuatan function

def pure():
    resSum = 4 + 7
    print (f'hasil penjumlahan : {resSum}')

# running function, nama function diikuti dg kurung ()
pure()

###########################################
# function dengan sebuah input
###########################################
#banyaknya jumlah input tidak terbatas
def day(x, feel) :
    # mengubah huruf pertama menjadi kapital
    x = x.capitalize()
    print(f'Today is {x} and i\'m {feel}')

day('sunday', 'haooy')
day('mOnday', 'sad or unhappy')
day('FRIDAY', 'sooo happy')

############################################
# function yang memiliki output
############################################

def summ(x, y) :
    res = x + y
    return res
    # setelah me return sesuatu
    # tidak akan membaca kode berikutnya
    print("not running")
# di sediakan variable penamung, karena 'summ' memiliki output
resultsumm = summ(5, 6)
print(f'hasil dari penjumlahan tersebut adalah : {resultsumm}')

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
for i in range(10):
  if not i % 2 == 0:
    print(i+1)