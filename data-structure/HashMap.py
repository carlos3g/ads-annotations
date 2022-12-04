class HashMap:
    def __init__(self, size=50):
        self.size = size
        self.hash_table = self._create_buckets()

    def _create_buckets(self):
        return [[] for _ in range(self.size)]

    def set(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, _ = record

            if (record_key == key):
                found_key = True
                break

        if (found_key):
            bucket[index] = (key, val)
            return

        bucket.append((key, val))

    def get(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for _, record in enumerate(bucket):
            record_key, record_val = record

            if (record_key == key):
                found_key = True
                break

        if (found_key):
            return record_val

        return None

    def delete(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, _ = record

            if (record_key == key):
                found_key = True
                break

        if (found_key):
            bucket.pop(index)

    def __repr__(self):
        return ''.join(str(item) for item in self.hash_table)

    def __str__(self):
        return self.__repr__()
