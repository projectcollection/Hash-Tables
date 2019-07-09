

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (hash * 33) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        key_exists = False
        current = hash_table.storage[index]

        #check if the root if linked list has the key if so return early
        if current.key == key:
            current.value = value
            return

        #traverse through the linked list looking for the key 
        while current.next is not None:
            current = current.next
            if current.key == key:
                current.value = value
                key_exists = True
                break
        #add at the end if its not found
        if not key_exists:
            current.next = LinkedPair(key, value)
    else:
        hash_table.storage[index] = LinkedPair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        key_found = False
        current = hash_table.storage[index] 
        # check if the root of linkedlist has the key and return early
        if current.key == key:
            current.value = None
            return

        while current.key != key and current.next is not None:
            current = current.next
            if current.key == key:
                key_found = True
                current.value = None
                break
        if not key_found:
            print('Key not found')
    else:
        print('Key not found')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        key_found = False
        current = hash_table.storage[index] 

        # check if root of linked list has the key and return the value
        if current.key == key:
            return current.value

        while current.next is not None:
            current = current.next
            if current.key == key:
                key_found = True
                return current.value

        return None
    else:
        return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_ht = HashTable(hash_table.capacity * 2)
    for index, pair in enumerate(hash_table.storage):
        new_ht.storage[index] = pair
    return new_ht



def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
