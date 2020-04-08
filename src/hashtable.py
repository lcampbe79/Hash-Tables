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

    # Returns a tuple as a string
    def __str__(self):
        key = self.key
        value = self.value
        return "A tuple of {}, {}".format(key, value)


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
        # Go to the node corresponding to the hash
        node = self.storage[index]

        # 3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.storage[index] = LinkedPair(key, value)
            
            return

        # 4. Collision! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
            print("Collision occured: node already has the same key ")
        # Add a new node at the end of the list with provided key/value
        prev.next = LinkedPair(key, value)



        # # Checks for index of a key
        # index = self._hash_mod(key)
        # # Current value of the hash (node)
        # current_value = self.storage[index]
        # print(index)
        # # If a node already has the same key
        # if current_value is not None:
        #     # print("Collision occured: node already has the same key ")

        #     # Create a new kvp from the LinkedPair class
        #     # newLinkedPair = LinkedPair(key, value)
        #     prev_value = None
        #     while current_value is not None:
        #         if prev_value.key == key:
        #             current_value.value = value
        #             return
        #         prev_value = current_value
        #         current_value = current_value.next
        #     current_value.next = LinkedPair(key, value)
        # else:
        #     self.storage[index] = LinkedPair(key, value)

            # while current_value is not None:
            #     prev_value = current_value
            #     current_value = current_value.next
            # # Adds new node to the end
            # newLinkedPair.next = self.storage[index]
            # self.storage[index] = newLinkedPair
        # If node doesnt't already has the same key and exist make new and add
        # else:
        #     self.storage[index] = LinkedPair(key, value)
        
       
      

    
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

        # # Check the index
        # if self.storage[index] is not None:
        #     head = self.storage[index]
        #     if head.next is None:
        #         # Since at the head, can just remove it
        #         self.storage[index] = None
        #     else:
        #         # Traverse the LinkedPair
        #         if head.key == key:
        #             self.storage[index] = head.next
        #         else:
        #             prev = head
        #             current = prev.next
                    
        #             while current is not None:
        #                 # Check for the right key
        #                 if key == current.key:
        #                     # If it's the right key, replace with None
        #                     prev.next = current.next
        #                 current = current.next
            
        # # If doesn't exist, return None
        # else:
        #     return None
       
        # # Find the index
        # index = self._hash_mod(key) #<- puts into the index
        # # Checks if there is a value store at the index
        # if self.storage[index] is not None:
        #     # Sets it to NONE
        #     self.storage[index] = None
        # else:
        #     print("Warning: Key is not found.")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        value_item = self.storage[index]
        print(index)
        if value_item is None:
            return None 

        while value_item:
            if value_item.key is not key:
                value_item = value_item.next 
            else:
                return value_item.value 
        return None

        # # Check if a pair exists with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     return self.storage[index].value
        # else:
        #     # Return None
        #     return None
       


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
