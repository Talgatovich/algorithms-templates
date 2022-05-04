""" 
    Формат ввода
Функция принимает массив натуральных чисел и искомое число k

В примерах:
В первой строке записано число n –— длина массива.
Во второй строке записано положительное число k –— искомый элемент. 
Далее в строку через пробел записано n натуральных чисел – элементы массива.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве 
(нумерация с нуля). Если элемент не найден, функция должна вернуть -1
.
Изменять массив нельзя.
"""
def broken_search(nums, target) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end-start) // 2
        if nums[mid] == target:
            return mid       
        if nums[start] <= nums[mid]:
            if target < nums[mid] and target >= nums[start]:
                end = mid - 1
            else:
                start = mid + 1            
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
            
    return -1



def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


nums = [5, 1]
target = 1
print(broken_search(nums, target))



# =======================================================================
def binary_search_for_broken(arr: list, search_value: int) -> int:
    start_value  = arr[0]
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = start + (end-start) // 2
        if search_value == arr[middle]:
            return middle
        
        if (arr[middle] < start_value) is not (search_value < start_value) or (arr[middle] > search_value):
            end = middle - 1
        else:
            start = middle + 1
    return -1  
