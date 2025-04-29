
def breakingRecords(array):
    max_record_count = 0
    min_record_count = 0
    highest = array[0]
    lowest = array[0]
    for i in range(1,len(array)):
        if array[i]> highest:
            max_record_count +=1
            highest=array[i]
        elif array[i]<lowest:
            min_record_count +=1
            lowest = array[i]

    return max_record_count,min_record_count


n= int(input())
array = list(map(int, input().split()))
max_re, min_re = breakingRecords(array)
print(max_re,min_re)