from typing import List, Tuple

def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

#matches - 4 - n^2

def question6(n: int) -> int:
    step=0
    while n > 1:
        print(f"step {step}: n={n}")
        n /= 2
        step += 1
    print(f"step {step}: n={n}(end)")
    return n

#matches 1 - log n

def question2(n: int) -> int:
    for _ in range(5):
        if 0<= _ <=5:
            s=str(n)
            print(f"step {_}: n={s[:20]}...(total {len(s)} numbers)")
        n **= 3
    return n

#matches to # 5 - 1

def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res

# print(question4([1, 2, 3]))

#matches to # 3 - n

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# print(question1([], []))

#matches to # 6 - n


def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(el_second_list)
   return temp

# print(question3([1], [1]))
#matches 2 - n^2

if __name__ == '__main__':
    print("\nquestion1: O(n)")
    a = [6, 5, 2, 4]
    b = [3, 4, 5, 6]
    result = question1(a, b)
    print(result)


    print("\nquestion2: O(1)")
    start = 2
    result = question2(start)
    print(f"Final result has {len(str(result))} digits")


    print("\nquestion3: O(n^2)")
    x = [1, 6, 3]
    y = [3, 4, 5]
    print(question3(x, y))


    print("\nquestion4: O(n)")
    list_numbers = [450, 250, 360, 500]
    max_number = question4(list_numbers)
    print(f"Final result {max_number}")


    print("\nquestion5: O(n^2)[")
    for i in range(3):
        result = question5(3)
        row = result[i * 3: (i + 1) * 3]
        print(" ", ", ".join(str(t) for t in row) + ",")
    print("]")


    print("\nquestion6: O(log n)")
    final_n = question6(100)
    print(f"Final value: {final_n}")