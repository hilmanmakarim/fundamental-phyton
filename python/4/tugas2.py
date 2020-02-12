# word = input(f'masukkan kata : ')
# vokal = ['a', 'i', 'u', 'e', 'o']

# def changeWord(text) :
#     if text[0] in vokal:
#         text = text +'ay'
#     else :
#         text = text[1:] + text[0] + 'ay'
#     return text

# res = changeWord(word)
# print(res)


# strList =  ['ab', 'bb', 'cb', 'dc']
# # strList.reverse()
# # print(strList)

# rest = list(reversed(strList))
# print(rest)

# sente = input (f'Masukkan kalimat yang ingin anda reverse : ')

# def sentRev (word) :
#     wSplit = word.split(' ')
#     wRev = reversed(wSplit)
#     word = ' '.join(wRev)
#     return word


# print(sentRev(sente))

# has 99

# cara sulit 
# def has99(lis):
#     idx = lis.index(9)
#     if lis[idx + 1] == 9:
#         return True
#     else :
#         return False
# cara mudah
def has99(lis):
    idx = lis.index(9)
    return lis[idx + 1] == 9

print(has99([1, 9, 9]))
print(has99([5, 9, 2, 9]))
print(has99([9, 3, 9]))
print(has99([7, 9, 9, 6]))

