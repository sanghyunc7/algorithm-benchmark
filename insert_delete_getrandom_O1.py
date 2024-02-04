import random


class RandomizedSet:
    # overwrite the key being removed with last index of an array
    # then decrease array size by 1
    def __init__(self):
        self.elements = []
        self.e_i = {}

    def insert(self, val: int) -> bool:
        if val in self.e_i:
            return False

        self.elements.append(val)
        self.e_i[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.e_i:
            return False

        i = self.e_i[val]
        self.elements[i] = self.elements[-1]
        self.e_i[self.elements[i]] = i
        self.e_i.pop(val)
        self.elements.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
