from typing import List


def chop_1(num: int, array: List[int]) -> int:
    """Given a num, returns its index in the sorted array.
    Returns -1 if the index was not found or the array is empty.
    """

    if not array:
        return -1
    if num not in array:
        return -1

    # Easy wins, we check both ends of the array
    if num == array[0]:
        return 0

    array_length = len(array)
    if num == array[array_length - 1]:
        return array_length - 1

    # Main loop
    while True:
        middle_index = len(array) // 2
        if num == array[middle_index]:
            return middle_index
        if num > array[middle_index]:
            array = array[middle_index:]
        else:
            array = array[:middle_index]


def chop(num: int, array: List[int]) -> int:
    """Given a num, returns its index in the sorted array.
    Returns -1 if the index was not found or the array is empty.
    """
    if not array:
        return -1
    bottom_index = 0
    top_index = len(array) - 1

    while bottom_index <= top_index:
        mid_index = (bottom_index + top_index) // 2
        if num < array[mid_index]:
            top_index = mid_index - 1
        elif num > array[mid_index]:
            bottom_index = mid_index + 1
        else:
            return mid_index
    return -1