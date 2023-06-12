arr = [2, 4, 65, 78, 34, 23]
n = len(arr)
max = arr[0]

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print(max)
