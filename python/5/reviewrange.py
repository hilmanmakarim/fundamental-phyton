# RANGE
# Sebuah function yang akan me return list of integer
# range menerima 1 parameter wajib, 2 parameter tidak wajib

# menerima 1 parameter
resRange = list(range(5))
print(resRange) #[0,1,2,3,4]
en = 6
resRange =list(range(en))
print(resRange) #[0, 1, 2, 3, 4, 5]

# menerima 2 parameter
# parameter 1 : nilai awal
# parameter 2 : nilai akhir (tidak termasuk)
resRange = list(range(2,7))
print(f'range(2, 7 ) : {resRange}')# [2,3,4,5,6]

# menerima 3 parameter
# parameter 1 : nilai awal
# parameter 2 : nilai akhir (tidak termasuk)
# parameter 3 : step, loncatan setiap nilai (default : 1) 
resRange = list(range(2,15, 2))
print(f'range(2, 15, 2 ) : {resRange}')# [2,4,6,8,10,12,14]

resRange = list(range(10 ,-3, -2))
print(f'range(10, -3, -2 ) : {resRange}')# [10, 8, 6, 4, 2, 0, -2]

days = [ 'Sunday', 'Monday', 'Tuesday']
# Looping sebanyak data
for i in range(len(days)):
    print(f'loop i : {i}')