# '''
# Linked List hash table key/value pair
# '''
class LinkedPair: #(Node)
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"<{self.key}, {self.value}, {self.next}>"

    # # Returns a tuple as a string
    # def __str__(self):
    #     key = self.key
    #     value = self.value
    #     return "{}, {}".format(key, value)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity # Empty spaces in the list
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # 1. Compute index of key
        index = self._hash_mod(key)
        # print(index)
        # 2. Go to the current index (node) with that hashed index
        current_index = self.storage[index]

        # 3. If current index (node) is empty:
        if current_index is None:
            # Create current index (node), add it, return
            self.storage[index] = LinkedPair(key, value)
            
            return

        # 4. Collision! Iterate to the end of the linked list at provided index
        prev_index = current_index
        while current_index is not None:
            prev_index = current_index
            current_index = current_index.next
            print(f"Collision occured: {prev_index} already has the same key ")
        # Add a new previous index (node) at the end of the list with provided key/value
        prev_index.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        ''' 
        index = self._hash_mod(key)

        # Check if a pair exists with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If the pair exists, delete it
            self.storage[index] = None
        else:
            # Print warning one isn't found
            print("Warning at remove: Key does not exist.")

        
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Finds the index using the hash function
        index = self._hash_mod(key)
        # Goes to the first slot with that hashed index
        current_index = self.storage[index]
        # print(index)

        # if current_index is None:
        #     return None 
        # Goes through the LinkedPair at this hashed index (node)
        while current_index:
            # Current index is now either requested kvp OR Nonw
            if current_index.key is not key:
                current_index = current_index.next 
            else:
                return current_index.value 
        return None

       
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage.copy()

        # Replace everything and double capacity
        self.capacity = self.capacity * 2
        # Make new storage
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            while bucket_item is not None:
                self.insert(bucket_item.key, bucket_item.value)
                bucket_item = bucket_item.next

        # new_storage = [None] * self.capacity

        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]
        #     self._hash_mod(new_storage[i])
        # self.storage = new_storage

        # # Put everything in new key/value pairs
        # for bucket_item in old_storage:
        #     self.insert(bucket_item.key, bucket_item.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
