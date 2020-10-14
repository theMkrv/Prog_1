class Pascall:
    def __init__(self, lst=None):
        self.lst = lst

    def __getitem__(self, poz):
        return self.lst[poz - 1]

    def __setitem__(self, poz, zn):
        self.lst[poz - 1] = zn

    def __str__(self):
        return self.lst.__str__()

nums = Pascall([1, 2, 3, 3, 4])
print(nums)
print(nums[1])
print(nums[0])