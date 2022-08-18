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
