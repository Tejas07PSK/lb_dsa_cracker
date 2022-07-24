def push (arr, ele):
    if (isEmpty(arr)): arr.append((ele, ele))
    else: arr.append((ele, min(ele, arr[-1][1])))

def pop (arr): return arr.pop()[0] if (not isEmpty(arr)) else -1

def isFull (n, arr): return (len(arr) == n)

def isEmpty (arr): return (len(arr) == 0)

def getMin (n, arr): return arr[-1][1] if (not isEmpty(arr)) else -1
