print('from FindPairsMethods.py')

def find_pairs_brute_force(arr, k):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if k == arr[i] + arr[j]:
                print (f'Yes: {arr[i], arr[j]}')

def find_pairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            print(f'Yes: {k - arr[i]}')