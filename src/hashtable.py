# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


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
        # start from an arbitrary large prime such as (5381)
        # set the ahs value to 5381
        hash_value = 5381
        # iterate over each char in the key
        for char in key:
            # set the hash value to the bit shift left by 5 of the hash value and sum of the hash value  then add the value for the char 
            ((hash_value << 5) + hash_value) + ord(char) #(hash_value * 33) + ord(char)) 
        # return the hash value
            return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)
        
        if self.storage[hash_value] is None:
            self.storage[hash_value] = LinkedPair(key,value)
            return
        else:
            curr_item = self.storage[hash_value]

            while curr_item:
                if curr_item.key == key:
                    curr_item.value = value 
                    break
                elif curr_item.next:
                    curr_item = curr_item.next
                else:
                    break

            curr_item.next = LinkedPair(key, value)

        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)
        if not self.storage[hash_value]:
            print('Key not found')
        else:
            curr_node = self.storage[hash_value]
            prev_node = None
            next_node = curr_node.next

            while True:
                if curr_node.key == key:
                    if prev_node is None:
                        self.storage[hash_value] = next_node
                        break
                    elif next_node is None and prev_node:
                        prev_node.next = None
                        break
                elif curr_node.next:
                    prev_node = curr_node
                    curr_node = next_node
                    next_node = curr_node.next
                else:
                    print('Key not found')
                    break
                



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        # get the position in the array
        position = self._hash_mod(key)

        # get the node at the current position
        current_node = self.storage[position]

        # Tranverse the linked list
        while current_node:
            # compare the key of the node in the linked list with the hashed key
            if current_node.key == key:
                # return the value of the current node
                return current_node.value
            # move on to the next node
            current_node = current_node.next
        return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        new_storage = HashTable(self.capacity * 2)
        for i in range(self.capacity):
            current_node = self.storage[i]
            while current_node:
                new_storage.insert(current_node.key, current_node.value)
                current_node = current_node.next
        self.storage = new_storage.storage
        self.capacity = new_storage.capacity



if __name__ == "__main__":
    ht = HashTable(7)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

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
