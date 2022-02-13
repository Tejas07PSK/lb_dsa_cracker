import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def kth_smallest_again ():
    T = int(input().decode()) ; comparator = lambda x : x[0]
    for t in range(T):
        N, Q = map(int, input().decode().split(' '))
        intervals_arr = [[0, 0] for i in range(N)]
        for n in range(N):
            intervals_arr[n][0], intervals_arr[n][1] = map(int, input().decode().split(' '))
        intervals_arr.sort(key=comparator) ; intervals_merged_lst = [intervals_arr[0]]
        for i in range(1, N):
            if (intervals_merged_lst[-1][1] < intervals_arr[i][0]):
                intervals_merged_lst.append(intervals_arr[i])
            elif (intervals_merged_lst[-1][1] < intervals_arr[i][1]):
                intervals_merged_lst[-1][1] = intervals_arr[i][1]
        for q in range(Q):
            kth_small = int(input().decode()) ; found = False
            for interval in intervals_merged_lst:
                dist = interval[1] - interval[0] + 1
                if kth_small <= dist:
                    sys.stdout.write(str(interval[0] + kth_small - 1) + '\n') ; found = True ; break
                kth_small -= dist
            if (not found):
                sys.stdout.write("-1\n")
kth_smallest_again()
