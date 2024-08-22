test1 = ["?4:5?", "23:5?", "2?:22", "0?:??", "??:??"]
output1 = ["14:59", "23:59", "23:22", "09:59", "23:59"]

def maximum_time(arr):

    if arr[0] == "?":
        # 0 1 2
        if arr[1] == "?":
            arr[0] = 2
        else:
            if int(arr[1]) <= 3:
                arr[0] = 2
            else:
                arr[0] = 1
    
    if arr[1] == "?":
        if arr[0] == 2:
            arr[1] = 3
        else:
            arr[1] = 9

    if arr[2] == "?":
        arr[2] = 5
    
    if arr[3] == "?":
        arr[3] = 9
    
    arr = [str(i) for i in arr]
    return arr[:2] + ":" + arr[2:]
        

    

    

