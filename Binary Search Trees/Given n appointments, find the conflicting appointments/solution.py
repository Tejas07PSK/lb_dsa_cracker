def findConflictingMeetings (meetings):
    temp_arr, res = list(enumerate(meetings)), [-1 for interval in meetings]
    temp_arr.sort(key=lambda tup: tup[1][0])
    max_interval = temp_arr[0]
    for i in range(1, len(temp_arr)):
        if (temp_arr[i][1][0] < max_interval[1][1]):
            res[temp_arr[i][0]], res[max_interval[0]] = max_interval[0] + 1, temp_arr[i][0] + 1
        if (temp_arr[i][1][1] > max_interval[1][1]): max_interval = temp_arr[i]
    return res
