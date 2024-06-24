def length_of_sequence(arr,n):
    count = arr.count(n)
    if count != 2:
        return 0
    start = arr.index(n)
    end = arr.index(n, start + 1)
    return end - start + 1
    pass


arr = [0, -3, 7, 4, 0, 3, 7, 9]
num = 7
result = length_of_sequence(arr, num)
print(result)