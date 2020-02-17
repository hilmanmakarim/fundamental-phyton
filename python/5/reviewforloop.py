# for in loop
# sebuah block kode yang akan di terus di running dalam jumlah tertentu
# for in akan dibarengi dengan tipe data yang sifatnya 'iterable'
# iterable :
    # string : 'hello from the outherside"
    # list : [1,2,3] / ['senin', 'selasa'] / [{"nama" : "Hulk"}, {"nama" : "thor"}]
    # tuple : (1,2,3) / ('senin', 'selasa') / ({"nama" : "Hulk"}, {"nama" : "thor"})

lorem = "lorem ipsum"

count = 1
# nama variable setelah keyword "for" adalah bebas
for x in lorem:
    print(f'huruf ke - {count} : {x}')
    count +=1

list = [1, 2, 3, 4]
if len(list) % 2 == 0:

  print(list[0])
# List
# first
numbers = [2,4,6,8]
powNumbers = []
for number in numbers :
    respow = pow(number, 2)
    powNumbers.append(respow)
print(powNumbers)

# second
people = [

    {"name": "avanza","color":"grey","price":139000},
    {"name": "xPander","color":"Black","price":299000},
    {"name": "Fortuner","color":"yellow","price":172000}
]
carName, carColor, carPrice = [],[],[]
for car in people :
    carName.append(car["name"])
    carColor.append(car["color"])
    carPrice.append(car["price"])
print(carName)
print(carColor)
print(carPrice)

#########
# tuple
#########

buuleans = (True, False, True, True, False)
for buul in buuleans :
    if buul :
        print(f'Aku yakin besok ujian akan mudah.')
    else :
        print(f'Aku yakin besok ujian akan dimudahkan')