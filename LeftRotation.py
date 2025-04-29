def leftRotation(d,array):
    d%=len(array)
    return array[d:]+array[:d]

n, d = map(int,input().split())
array = list(map(int,input().split()))
print(*leftRotation(d, array))