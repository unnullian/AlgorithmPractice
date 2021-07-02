
def sort_arr(arr) :
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] :
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr
    
def solution(array, commands):
    answer = []
    
    for command in commands :
        i, j, k = command
        value = sort_arr(array[i-1:j])[k-1]
        answer.append(value)
    
    return answer
