def arrayManipulation(n, queries):
    # Write your code here
    diff_arr = [0]*(n+2)
    
    for q in queries:
        l, r, k = q[0], q[1], q[2]
        diff_arr[l] += k
        diff_arr[r+1] -= k
        
    summ = float("-inf")
    running_sum = 0
    for num in diff_arr:
        running_sum += num
        summ = max(summ, running_sum)
    return summ
    
