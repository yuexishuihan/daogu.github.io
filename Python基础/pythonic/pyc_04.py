class Test():
    def __bool__(self):
        print('bool called')
        return False
    def __len__(self):
        print('len called')
        return True

# print(len(Test()))
print(bool(Test()))