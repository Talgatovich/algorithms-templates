ASD = []


def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        ASD.append(mid)
        return
    elif x != arr[mid]:
        binarySearch(arr, x, left, mid)
        binarySearch(arr, x, mid + 1, right)


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums)
    binarySearch(nums, target, left, right)
    return ASD[0] if len(ASD) != 0 else -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
