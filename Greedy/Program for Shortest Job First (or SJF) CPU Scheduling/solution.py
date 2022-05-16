from heapq import heappush, heappop

class Job:
    def __init__ (self, arrival_time, burst_time):
        self.arrival_time, self.burst_time = arrival_time, burst_time

    def __lt__ (self, other):
        if (self.arrival_time == other.arrival_time): return (self.burst_time < other.burst_time)
        return (self.arrival_time < other.arrival_time)

def sjf (n, arrivalTime, burstTime):
    jobs, waiting_heap, i = [Job(arrivalTime[i], burstTime[i]) for i in range(n)], [], 1 ; jobs.sort()
    tot_wait_time, tot_turnaround_time, current_end_time = 0, jobs[0].burst_time, (jobs[0].arrival_time + jobs[0].burst_time)
    while (i < n):
        if (jobs[i].arrival_time < current_end_time):
            heappush(waiting_heap, (jobs[i].burst_time, jobs[i])) ; i += 1
        elif (waiting_heap):
            next_job = heappop(waiting_heap)[1]
            curr_wait_time = (current_end_time - next_job.arrival_time)
            tot_wait_time += curr_wait_time
            tot_turnaround_time += (curr_wait_time + next_job.burst_time)
            current_end_time += next_job.burst_time
        else:
            tot_turnaround_time += jobs[i].burst_time
            current_end_time += ((jobs[i].arrival_time - current_end_time) + jobs[i].burst_time)
            i += 1
    while (waiting_heap):
        next_job = heappop(waiting_heap)[1]
        curr_wait_time = (current_end_time - next_job.arrival_time)
        tot_wait_time += curr_wait_time
        tot_turnaround_time += (curr_wait_time + next_job.burst_time)
        current_end_time += next_job.burst_time
    return (tot_wait_time / n), (tot_turnaround_time / n)
