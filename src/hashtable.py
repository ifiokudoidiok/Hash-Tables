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
        

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)
        
        if self.storage[hash_value] is None:
            self.storage[hash_value] = LinkedPair(key,value)
            return
        else:
            curr_item = self.storage[hash_value]

            while curr_item.next is not None:
                curr_item = curr_item.next
            curr_item.next = LinkedPair(key, value)
            return
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Hash the key to get the correct location
        hash_value = self._hash_mod(key)
        # Check there is something stored at this index, if not, return None
        if self.storage[hash_value] is None:
            return None
        else:
        # set the temporary variable to be the first item in the linked list at the correct index
        # Loop through checking if the current key matches the key provided
        # if so, return the value
        # once we reach the end of the chain, check the last value to see if it matches
        # if it does, return the value
        # if not, return None
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.capacity):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

print('Hash Dammy:')
print(hash('dammy') % 6)

ht = HashTable(2)

ht.insert("line_1", "Tiny hash table")
ht.insert("line_2", "Filled beyond capacity")
ht.insert("line_3", "Linked list saves the day!")
print('------------------')
print(ht)
print('------------------')

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
