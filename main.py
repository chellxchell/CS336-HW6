n = 10
s = [2,7,17,14,51,93,99,33,40,1]
f = [94,14,41,32,93,98,100,40,49,50]
v = [1024, 273, 115, 100, 478, 160, 2, 14, 3, 389]

# class Interval that keeps track of n (interval number), start time, finish time, and value
class Interval:
    def __init__(self,n, start, finish, value):
        self.n = n
        self.start = start
        self.finish = finish
        self.value = value


# HELPER FUNCTIONS ======================================================================================

# takes a list of Interval objects and sorts them by increasing finish time
def sort_finish(intervals):
    return sorted(intervals, key=lambda x: x.finish, reverse=False)

# helper function that nicely prints out interval values
def print_interval(intervals):
    for j in range(len(intervals)):
        print("n:{} start:{} finish:{} value:{} p:{}".format(intervals[j].n, intervals[j].start, intervals[j].finish,intervals[j].value,intervals[j].P))

# print solution to the problem, i.e. optimal set and value
def solution(intervals):
    opt_value = float("-inf")
    opt_intervals = None
    for i in range(0,n):
        # print(OPT(intervals,i))
        val, inter = OPT(intervals,i)
        if val > opt_value:
            opt_value = val
            opt_intervals = inter
    print("THE SET OF OPTIMAL ITEMS IS: {}".format(opt_intervals))
    print('WITH AN OPTIMAL VALUE OF: {}'.format(opt_value))
    return opt_intervals


# MAIN FUNCTIONS ======================================================================================

# input: sorted Intervals by finish time, interval number i
# output: max value and optimal set of intervals up to interval i
def OPT(intervals, i):
    n = intervals[i].n
    p = P(intervals, n)

    # base case: v1
    if i == 0:
        return intervals[i].value, [n]
    
    # value and optimal list if i is NOT in optimal solution
    val_not_in, list_not_in = OPT(intervals, i-1)

    # value and optimal list if i IS in optimal solution
    val_in = float("-inf")
    if p != None:
        p_i = intervals.index([x for x in intervals if x.n == p][0]) # index of p in sorted array
        val_in, list_in = OPT(intervals,p_i)
        val_in = intervals[i].value + val_in
        list_in.append(n)
    
    # if its the only interval so far and its higher than OPT(i-1)
    if p==None and intervals[i].value > val_not_in:
        return intervals[i].value, [n]

    # if its in the opt solution
    if val_in > val_not_in:
        return val_in, list_in
    # if its not in the opt solution
    else:
        return val_not_in, list_not_in

# input: sorted Intervals by finish time,
# output: number of rightmost interval to finish before current one starts
def P(intervals, n):
    found = False
    ind = intervals.index([x for x in intervals if x.n == n][0]) # index of job n in sorted array
    i = intervals[ind] # actual interval of job n

    while not found:
        # if first job, no other job ends before it
        if ind == 0:
            return None

        # find first job j that finishes before job i starts
        j = intervals[ind-1]
        if j.finish <= i.start:
            return j.n
        else:
            ind -=1


# DRIVER CODE ====================================================================

intervals = []
for i in range(1, n+1):
    ind = i-1
    intervals.append(Interval(i, s[ind], f[ind], v[ind]))
intervals = sort_finish(intervals)
solution(intervals)