def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return arr[a1:b1+1]+arr[a2:b2+1]