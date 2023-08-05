class Hashtable:
    def __init__(self):
        self.table_size = 100
        self.table = [None] * self.table_size

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char)) % self.table_size
        return hash_value

    def set(self, key, value):
        index = self.hash(key)
        if not self.table[index]:
            self.table[index] = []

        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value

        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if not self.table[index]:
            return None

        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]

        return None

    def has(self, key):
        index = self.hash(key)
        if not self.table[index]:
            return False

        for entry in self.table[index]:
            if entry[0] == key:
                return True

        return False 

    def keys(self):
        keys = []
        for bucket in self.table:
            if bucket:
                for entry in bucket:
                    keys.append(entry[0])
        return keys
