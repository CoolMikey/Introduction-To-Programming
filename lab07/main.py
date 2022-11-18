def revert_in_subgroups(arr, sub_size):
    n = len(arr)
    subgroup_number = n // sub_size
    for i in range(subgroup_number):  # number of subgroups
        first_elem_index = sub_size * i
        last_elem_index = sub_size * (i + 1) - 1
        for d in range(sub_size // 2):  # mimo zagniezdzenia zlozonosc obliczeniowa wynosi n (dokladniej <=n/2)
            a = arr[last_elem_index - d]
            arr[last_elem_index - d] = arr[first_elem_index + d]
            arr[first_elem_index + d] = a
    elements_left = n % sub_size
    if elements_left > 1:
        first_elem_index = sub_size * subgroup_number
        last_elem_index = n - 1
        for d in range(elements_left // 2):
            a = arr[last_elem_index]
            arr[last_elem_index - d] = arr[first_elem_index + d]
            arr[first_elem_index + d] = a


def sort_123(arr):
    n = len(arr)
    n_of_1 = 0
    n_of_2 = 0
    n_of_3 = 0
    for i in range(n):
        if arr[i] == 1:
            n_of_1 += 1
        elif arr[i] == 2:
            n_of_2 += 1
        elif arr[i] == 3:
            n_of_3 += 1
        else:
            raise ValueError("W liscie znajduje sie element nie z {1,2,3}")
    for i in range(n_of_1):
        arr[i] = 1
    for i in range(n_of_2):
        arr[i + n_of_1] = 2
    for i in range(n_of_3):
        arr[i + n_of_1 + n_of_2] = 3


def get_top_indexes(arr):
    n = len(arr)
    number_of_peaks = 0
    for i in range(n):
        if ((i - 1) < 0 or arr[i - 1] < arr[i]) and ((i + 2) > n or arr[i + 1] < arr[i]):
            number_of_peaks += 1
    peaks = [0 for i in range(number_of_peaks)]
    peak_number = 0
    for i in range(n):
        if ((i - 1) < 0 or arr[i - 1] < arr[i]) and ((i + 2) > n or arr[i + 1] < arr[i]):
            peaks[peak_number] = i
            peak_number += 1
    return peaks


def calculate_max_sum(arr):
    max_sum = float("-inf")
    n = len(arr)
    local_sum = 0

    for i in range(n):
        local_sum = arr[i]
        for d in range(i + 1, n):
            if local_sum > max_sum:
                max_sum = local_sum
            local_sum += arr[d]

    if local_sum > max_sum:
        return local_sum
    else:
        return max_sum


def main():
    print("-------------revert_in_subgroups-------------")
    argumenty = [
        [[1, 2, 3, 4, 5], 3],
        [[1, 2, 3, 4, 5], 2],
        [[1, 2, 3, 4, 5, 6], 2],
        [[1, 2, 3, 4, 5, 6], 5],
        [[1, 2, 3, 4, 5, 6, 3, 2, 1, 5, 3, 2, 5], 5],
        [[1, 2, 3, 4, 5, 6, 3, 2, 1, 5, 3, 2, 5, 7], 5],
        [[1], 1],

    ]
    for i in range(len(argumenty)):
        print(f"{i + 1}. revert_in_subgroups({argumenty[i][0]}, {argumenty[i][1]})")
        revert_in_subgroups(argumenty[i][0], argumenty[i][1])
        print(f"Output: {argumenty[i][0]}")

    print("-------------sort_123-------------")
    argumenty = [
        [2, 1, 1, 1, 2, 3, 1, 2, 3, 3],
        [2, 1, 2, 3, 1, 2, 3, 3],
        [3, 2, 1, 3, 2, 1, 3, 1, 2, 3],
        [2, 1, 1, 3, 3]
    ]
    for i in range(len(argumenty)):
        print(f"sort_123({argumenty[i]})")
        sort_123(argumenty[i])  # funkcja sort_123 nic nie zwraca
        print(f"Output: {argumenty[i]}")

    print("-------------get_top_indexes-------------")
    argumenty = [
        [8, 3, 4, 1, 1, 4, 4, 5],
        [0],
        [3,2,6,2,7,2,9,2,2],
        [1,2,3,4,5,6,7,8,9],
        [1,1,1,1,1],
    ]
    for i in range(len(argumenty)):
        print(f"1. get_top_indexes({argumenty[i]})")
        print(f"Output: {get_top_indexes(argumenty[i])}")

    print("-------------calculate_max_sum-------------")
    argumenty = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [-2, -3, -5],
        [1, 2, 3, 4, 5, 6, -10000, 1000],
        [-1, -2, -3, -4, -100]
    ]
    for i in range(len(argumenty)):
        print(f"{i + 1}. calculate_max_sum({argumenty[i]})")
        print(f"Output: {calculate_max_sum(argumenty[i])}")

    return 0


if __name__ == '__main__':
    main()
