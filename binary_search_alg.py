import random
"""В имеющийся отсортированный массив натуральных чисел найти номер позации куда необходимо вставить число <x>,
   чтобы массив остался отсортированным. Если в массиве есть числа равные числу <x>, то необходимо вставить число <x>\
   перед ними"""


def binary_search(x: int, arr: list) -> int:
    if len(arr) == 0:
        return 0

    left_pos = 0
    right_pos = len(arr)

    while left_pos < right_pos:
        center_pos = (left_pos + right_pos) // 2

        if arr[center_pos] < x:
            left_pos = center_pos + 1
        else:
            right_pos = center_pos

        return left_pos


def generate_value(count, length):
    """Генерируем массив с помощью спискового включения.
       x - Кол-во возвращаемых массивов
       l - Длинна возвращаемых массивов"""

    start = 20
    end = 50
    for i in range(count):
        arr = [random.randint(start, end)
               for _ in range(length)]
        k = random.randint(start, end)
        start = end
        end += 20
        yield sorted(arr), k


def test_binary_search():
    test_value = generate_value(5, 10)
    for mas in test_value:
        arr, x = mas
        print(f'Answer for number {x} in array {arr} is position {binary_search(x, arr)}')


if __name__ == '__main__':
    test_binary_search()
