def make_operation(operation,*numbers):
    if not numbers:
        return 0
    if operation == '+':
        result=0
        for n in numbers:
            result+=n
    elif operation == '-':
        result=numbers[0]
        for n in numbers[1:]:
            result-=n
    elif operation == '*':
        result=1
        for n in numbers:
            result*=n
    else:
        raise ValueError('Invalid operation')
    return result

print(make_operation('+',8,2))
print(make_operation('-',5,9))
print(make_operation('*',2,2))



import unittest

class TestMakeOperation(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(make_operation('+', 1, 4, 2), 7)
        self.assertEqual(make_operation('+', 0, 0, 0), 0)
        self.assertEqual(make_operation('+', -1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(make_operation('-', 8, 5), 3)
        self.assertEqual(make_operation('-', 4, 10), -6)
        self.assertEqual(make_operation('-', 100), 100)

    def test_multiplication(self):
        self.assertEqual(make_operation('*', 3, 3), 9)
        self.assertEqual(make_operation('*', 3, 0, 5), 0)
        self.assertEqual(make_operation('*', -1, 3), -3)

    def test_no_numbers(self):
        self.assertEqual(make_operation('+'), 0)
        self.assertEqual(make_operation('-'), 0)
        self.assertEqual(make_operation('*'), 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            make_operation('/', 1, 2)

if __name__ == '__main__':
    unittest.main()