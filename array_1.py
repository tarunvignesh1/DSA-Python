
arr = ["bob","alice","tarun","vignesh"]

arr.sort(key=lambda x: -len(x))

print(arr)
