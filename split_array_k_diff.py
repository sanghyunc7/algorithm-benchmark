from collections import Counter

def solution(arr, k = 5):

    # regular O(nlogn) approach
    arr = arr.sorted()
    # sliding window 
    ans = []
    for i in range(0, len(arr), 3):
        subarray = arr[i:i + 3]
        if subarray[2] - subarray[0] <= k:
            ans.append(subarray)
    return ans
        
    # what if.. count = [0] * k
    # bucket[arr[i] // k].append(arr[i])
    # if arr[i] is very sparse e.g. k - 1 spaces apart, then poor runtime O(n * k) since there are k buckets. each bucket takes k time to sort.
    # so.. logn vs k? for logn = log(10 ** 5) --> approx log(2 ** 3(5)) -> 15. if k is greater than 15 then logn is probably faster.


    # split array into subarrays of size 3 where any max(subarray) - min(subarray) <= k
    # if not possible, return empty array

    # count_sort approach using bucket from min(arr) to max(arr)
    
    

    # count_sort O(k * n)
    buckets = []
    # get count for every element
    count = [0] * (max(arr) + 1) # let's say 5 is max(arr), 0 is min(arr)
    for i in arr:
        count[i] += 1
    
    # prefix[arr[i]] - 1 stores the last index of arr[i] in sorted_arr
    prefix = []
    for i in count:
        prefix.append(i)
        if len(prefix) > 1:
            prefix[-1] += prefix[-2] # add previous prefix
    print(count)
    print(prefix)
    sorted_arr = [0] * len(arr)
    for i in range(len(arr)):
        sorted_arr[prefix[arr[i]] - 1] = arr[i]
        prefix[arr[i]] -= 1 # last index of  arr[i] is now to the left 1 cell

    print(arr)
    print(sorted_arr)

solution([1, 5, 2, 2, 4, 3, 3])

    
    

