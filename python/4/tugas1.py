def angka() :
    listInput = [1,2,3,4,5,6,7]
    newlist=[[],[]]
    for num in listInput:
        numCtrl=num%2
        if numCtrl==0:
            newlist[0].append(num) #genap
        else:
            newlist[1].append(num) #ganjil
    print(newlist)
angka()


print(3*'7')