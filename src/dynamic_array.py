class DynamicArray:
    def __init__(self, capacity=1):
        #number of elements array has
        self.count =0
        self.capacity = capacity # total amount of storage in array SHOULD BE LARGER THAN COUNT
        self.storage = [None] * capacity
    
    def insert(self, index, value):
        #O(n) because of the for loop
        # check if enough capacity
        if self.count >= self.capacity:
            # if not, make more room (resize, add more capacity)
            self.resize()
        # Shift/ move everyindex to the right by 1 (count backwards, -1)
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # add new value to the index
        self.storage[index] = value
        #increment count
        self.count +=1
    
    def append(self, value): #value can be anything, storing memory addresses
        #O(1) most of the time
        # check if enough capacity
        if self.count >= self.capacity:
            # if not, make more room (resize, add more capacity)
            self.resize()
        self.storage[self.count] = value
        #increment count
        self.count +=1

    def resize(self):
        # Double capacity
        self.capacity *= 2
        # Allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # Copy all elements from old storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

a = DynamicArray(2)
a.insert(0, 10)
a.insert(0, 11)
print(a.storage)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)

print(a.storage)

# self.storage = [None, None, None, None, None, None, None, None]

# #timing test
# # O(n^2)
# def add_to_front(n):
#     x = []
#     for i in range(0, n):
#         x.insert(0, n - i)
#     return x
    
# # O(n)
# def add_to_back(n):
#     x = []
#     for i in range(0, n):
#         x.append(i + 1)
#     return x

# # O(n)
# def pre_allocate(n):
#     x = [None] * n
#     for i in range(0, n):
#         x[i] = i + 1
#     return x

# import time
# ​
# start_time = time.time()
# add_to_back(100000)  # O(n)
# end_time = time.time()
# print (f"runtime: {end_time - start_time} seconds")
# # runtime: 0.07669210433959961 seconds
# ​
# ​
# ​
# ​
# ​
# start_time = time.time()
# add_to_front(100000)  # O(n^2)
# end_time = time.time()
# print (f"runtime: {end_time - start_time} seconds")
# # runtime: 56.415611743927 seconds
# ​
# ​
# ​
# ​
# n = 500000          # n = 500 thousand
# add_to_back(n)      # 0.0752871036529541 seconds
# pre_allocate(n)     # 0.05263519287109375 seconds
# ​
# ​
# n = 5000000         # n = 5 million
# add_to_back(n)      # 0.72271728515625 seconds
# pre_allocate(n)     # 0.5194799900054932 seconds
# ​
# ​
# n = 50000000        # n = 50 million
# add_to_back(n)      # 7.198451995849609 seconds
# pre_allocate(n)     # 5.220464706420898 seconds
# ​
# # Preallocating memory is consistently ~40% faster




