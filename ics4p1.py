def possible(prefix, arr):
    if len(arr) == 2:
        print(prefix + "".join(arr))
        print(prefix + "".join(arr[::-1]))
        return
    for i in range(len(arr)):
        possible(prefix + arr[i], arr[:i] + arr[i + 1:])


letters = sorted([x for x in input()])
if len(letters) == 1:
    print(letters[0])
else:
    possible("", letters)
