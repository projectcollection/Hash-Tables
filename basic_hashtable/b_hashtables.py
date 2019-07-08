

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
       self.capacity = capacity
       self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
# https://gist.github.com/mengzhuo/180cd6be8ba9e2743753 and http://www.goodmath.org/blog/2013/10/20/basic-data-structures-hash-tables/
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (hash * 33) + ord(x)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_hash = hash(key, hash_table.capacity)
    print()
    if  hash_table.storage[new_hash] is None :
        hash_table.storage[new_hash] = Pair(key,value)
    elif hash_table.storage[new_hash].key != key:
        print('Warning key mismatch') 


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    _hash = hash(key, hash_table.capacity)
    if hash_table.storage[_hash] is not None:
        hash_table.storage[_hash] = None
    else:
        print('Does not exist')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    _hash = hash(key, hash_table.capacity)
    if hash_table.storage[_hash] is not None:
        return hash_table.storage[_hash].value
    else:
        return None 


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
