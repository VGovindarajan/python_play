# https://runestone.academy/runestone/static/pythonds/SortSearch/Hashing.html
# Vijayarajan Govindarajan 2017
'''
Map() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored in the map.
in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
'''


def get_int_key(key):
    if isinstance(key, int):
        return key
    str_key = str(key)
    len_key = len(str_key)
    total = 0
    for i in range(len_key):
        total += (i * ord(str_key[i]))
    return total


class HashTableImpl:
    def __init__(self):
        self.size = 13  # Prime numbers work best for slots esp when used with linear probing.
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __repr__(self):
        str_repr = ""
        for i in range(self.size):
            if self.slots[i] is not None:
                str_repr += str(self.slots[i]) + ":" + str(self.data[i]) + ","
        final_str = "{" + str_repr + "}"
        return final_str

    def __len__(self):
        hash_len = 0
        for i in range(self.size):
            if self.slots[i] is not None:
                hash_len+=1
        return hash_len

    def load_factor(self):
        hash_len = self.__len__()
        hash_size = self.size
        return hash_len/hash_size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def hash_function(self, key):
        int_key = get_int_key(key)
        return int_key % self.size

    def rehash_function(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        print("put()", key, value)
        hash_key = self.hash_function(key)
        original_hash = hash_key

        if self.slots[hash_key] is None:
            print("hash_key", hash_key, "slot is empty.")
            self.slots[hash_key] = key
            self.data[hash_key] = value
            return True
        else:
            if self.slots[hash_key] is key:
                print("hash_key", hash_key, "slot has key. overwriting", self.data[hash_key], "with", value)
                self.data[hash_key] = value #over write
                return True
            else:
                slot_found = False
                circled_once = False
                while not slot_found and not circled_once:
                    hash_key = self.rehash_function(hash_key)
                    if hash_key is original_hash:
                        circled_once = True
                    else:
                        if self.slots[hash_key] is None:
                            print("re - hash_key", hash_key, "slot is empty.")
                            slot_found = True
                            self.slots[hash_key] = key
                        else:
                            if self.slots[hash_key] is key:
                                print("re - hash_key", hash_key, "slot has same key.")
                                slot_found = True

                if slot_found:
                    print("Adding/overwriting to re-hash", hash_key, value)
                    self.data[hash_key] = value

                return slot_found

    def get(self, key):
        print("get()", key)
        hash_key = self.hash_function(key)
        original_hash = hash_key
        if self.slots[hash_key] is key:
            print("hash_key", hash_key, "slot has key. returning", self.data[hash_key])
            return self.data[hash_key]
        else:
            slot_found = False
            circled_once = False
            while not slot_found and not circled_once:
                hash_key = self.rehash_function(hash_key)
                if hash_key is original_hash:
                    circled_once = True
                else:
                    if self.slots[hash_key] is None:
                        print("re - hash_key", hash_key, "slot is empty.")
                    else:
                        if self.slots[hash_key] is key:
                            print("re - hash_key", hash_key, "slot has same key.")
                            slot_found = True
                        else:
                            print("re - hash_key", hash_key, "slot has different key.")
                if slot_found:
                    print("slot found from re-hash", hash_key, self.data[hash_key])
                    return self.data[hash_key]

            return None

    def __contains__(self, key):
        print("__contains__", key)
        hash_key = self.hash_function(key)
        original_hash = hash_key
        if self.slots[hash_key] is key:
            return True
        else:
            slot_found = False
            circled_once = False
            while not slot_found and not circled_once:
                hash_key = self.rehash_function(hash_key)
                if hash_key is original_hash:
                    circled_once = True
                else:
                    if self.slots[hash_key] is key:
                        slot_found = True
                        return slot_found
            return slot_found

    def __delitem__(self, key):
        print("__delitem__", key)
        hash_key = self.hash_function(key)
        original_hash = hash_key
        if self.slots[hash_key] is key:
            self.slots[hash_key] = None
            self.data[hash_key] = None
            return True
        else:
            slot_found = False
            circled_once = False
            while not slot_found and not circled_once:
                hash_key = self.rehash_function(hash_key)
                if hash_key is original_hash:
                    circled_once = True
                else:
                    if self.slots[hash_key] is key:
                        slot_found = True
                        self.slots[hash_key] = None
                        self.data[hash_key] = None
            return slot_found

def main():
    ht = HashTableImpl()
    print(ht)
    ht.put(1,1)
    ht.put("apple", 2)
    ht.put(14,3)
    ht[40]=4
    ht[41]=5

    print(ht)
    print(ht.get(1))
    print(ht.get("apple"))
    print(ht.get(14))
    print(27 in ht)
    print(ht.get(27))
    #del (ht[27])
    del ht[14]
    print(ht)


if __name__ == "__main__":
    main()