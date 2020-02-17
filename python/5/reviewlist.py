animals = ["Tiger", "Eagle", "Bear", "Koala", "Dolphin", "Shark"]

# Akses satu nilai tertentu
animals[0] #Tiger
animals[2] #Bear
animals[-1] #Shark

# Akses lebih dari satu nilai
# dari index 1 sampai 3
animals [1:4] # Eagle, Bear, Koala
# dari index 0 sampai 3
# print(animals [:3]) # Tiger Eagle Bear Koala
# DARI INDEX 2 SAMPAI HABIS
animals[2:] # Bear Koala Dholpin Shark

# Sort #
# mengurutkan secara ascending
animals.sort()
# print(animals)

# mengurutkan secara descending
animals.sort(reverse=True)
#print(animals)

# APPEND#
# print(animals)
# animals.append("Bird")
# animals.append("Cat")
# print(animals)

# REMOVE #
# menghapus data pada list
print(animals)
animals.remove("Shark")
animals.remove("Tiger")
print(animals)