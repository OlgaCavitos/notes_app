#Task 1

class Withindex:
    def __init__(self, iterable, start=0):
        self.iterable = iter(iterable)
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterable)
        res=(self.index,item)
        self.index += 1
        return res


if __name__ == '__main__':
    for i,value in Withindex('world',start=1):
        print(i,value)

    for i,value in Withindex(['b','c','e'],start=0):
        print(i,value)


print('\n')

#Task2

class InRange:
    def __init__(self, start, end=None, step=1):
        if end is None:
            end=start
            start=0

        if step==0:
            raise ValueError("start cannot be zero")
        self.start = start
        self.end = end
        self.step = step
        self.current=start

    def __iter__(self):
        return self

    def __next__(self):
        if(self.step>0 and self.current>=self.end) or (self.step<0 and self.current<=self.end):
            raise StopIteration
        current_value=self.current
        self.current+=self.step
        return current_value

if __name__=='__main__':
    for i in InRange(3):
        print(i)
    print(list(InRange(2,10,2)))

print('\n')

#Task3

class OwnIterable:
    def __init__(self, data):
        self._data=list(data)

    def __iter__(self):
        for element in self._data:
            yield element

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"OwnIterable({self._data})"


if __name__=='__main__':
    numbers=OwnIterable([1,2,3,4,5])
    for number in numbers:
        print(number)
    print(numbers[1])

    del numbers[1]
    print(numbers)




