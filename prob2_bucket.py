n = 10
s = [2,7,17,14,51,93,99,33,40,1]
f = [94,14,41,32,93,98,100,40,49,50]
v = [1024, 273, 115, 100, 478, 160, 2, 14, 3, 389]

# array for memoization (opt values)
M = [None] * n
M.insert(0,0)

# class Interval that keeps track of n (interval number), start time, finish time, and value
class Interval:
    def __init__(self,n, start, finish, value):
        self.n = n
        self.start = start
        self.finish = finish
        self.value = value
        self.sorted_ind = None


# HELPER FUNCTIONS ======================================================================================

# takes a list of Interval objects and sorts them by increasing finish time
def sort_finish(intervals):
    buckets = [[] for i in range(len(intervals))]
    for interval in intervals:
        ind = int((interval.finish) / 10)

        inserted = False
        for i in range(len(buckets[ind])):
            if buckets[ind][i].finish > interval.finish:
                buckets[ind].insert(i, interval)
                inserted = True
                break
        
        if not inserted:
            buckets[ind].append(interval)
    
    count = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            buckets[i][j].sorted_ind = count
            count += 1
    return buckets

# helper function that nicely prints out interval values
def print_intervals(intervals):
    print(intervals[0])
    for j in range(1,len(intervals)):
        print("i:{} n:{} start:{} finish:{} value:{}".format(j, intervals[j].n, intervals[j].start, intervals[j].finish,intervals[j].value))

# print solution to the problem, i.e. optimal set and value
def solution(buckets):
    # initalize p array
    p, intervals = get_p(buckets)
    opt_val = M_Compute_OPT(intervals,n,p)
    opt_set = find_solution(intervals,n,p)
    f = open("prob2_solution.txt", "w")
    f.write("THE SET OF OPTIMAL ITEMS IS: {}".format(opt_set))
    f.write("\n")
    f.write('WITH AN OPTIMAL VALUE OF: {}'.format(opt_val))
    f.close()
    return opt_set


# MAIN FUNCTIONS ======================================================================================

# input: sorted Intervals by finish time, interval number i
# output: max value and optimal set of intervals up to interval i
def M_Compute_OPT(intervals, j, p):
    if M[j] == None:
        M[j] = max(M_Compute_OPT(intervals, j-1, p), intervals[j].value + M_Compute_OPT(intervals, p[j],p))
    return M[j]

# computes optimal solution by making a second pass
def find_solution(intervals, j, p):
    if j == 0:
        return []
    elif (intervals[j].value + M[p[j]]) > M[j-1]:
        sol = find_solution(intervals, p[j],p)
        sol.append(intervals[j].n)
        return sol
    else:
        return find_solution(intervals,j-1,p)

# input: sorted buckets of Intervals by finish time,
# output: list of indices of rightmost interval to finish before current one starts, sorted list of intervals
def get_p(buckets):
    p = []
    intervals = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            ind = int(buckets[i][j].start / 10)
            bucket = buckets[ind]
            found = False
            for interval in reversed(bucket):
                if interval.finish <= buckets[i][j].start:
                    p.append(interval.sorted_ind)
                    found = True
                    break
            
            if not found:
                ind -= 1
                while(len(buckets[ind]) == 0):
                    ind -= 1
                p.append(buckets[ind][-1].sorted_ind)
            intervals.append(buckets[i][j])
    return p, intervals

# DRIVER CODE ====================================================================

intervals = [Interval(0, 0, 0, 0)]
for i in range(1, n+1):
    ind = i-1
    intervals.append(Interval(i, s[ind], f[ind], v[ind]))
buckets = sort_finish(intervals)
solution(buckets)