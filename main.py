n = 10
s = [2,7,17,14,51,93,99,33,40,1]
f = [94,14,41,32,93,98,100,40,49,50]
v = [1024, 273, 115, 100, 478, 160, 2, 14, 3, 389]
opt_intervals = []

class Interval:
    def __init__(self,n, start, finish, value):
        self.n = n
        self.start = start
        self.finish = finish
        self.value = value
        self.P = None
        self.OPT = None

# takes a list of Interval objects and sorts them by increasing finish time
def sort_finish(intervals):
    return sorted(intervals, key=lambda x: x.finish, reverse=False)


def OPT(intervals, n):
    i = n-1 # for indexing through arrays

    # base case: v1
    if n==1:
        return intervals[i].value
    
    # if n in optimal solution
    in_opt = float("-inf")
    p = P(intervals, n)
    if p != None:
        in_opt = intervals[i].value + OPT(intervals, p.n)

    # if n not in optimal solution
    not_in_opt = OPT(intervals, n-1)

    if in_opt > not_in_opt:
        opt_intervals.append(n)
    
    return max(not_in_opt, in_opt)


# returns number of rightmost interval to finish before current one starts
def P(intervals, n):
    found = False
    sorted_intervals = sort_finish(intervals)
    ind = sorted_intervals.index([x for x in sorted_intervals if x.n == n][0])
    i = sorted_intervals[ind]

    while not found:
        if ind == 0:
            return None
        j = sorted_intervals[ind-1]
        if j.finish <= i.start:
            return j.n
        else:
            ind -=1

def assign_P(intervals, n):
    for i in range(0, n):
        if i == 0:
            intervals[i].P = intervals[i].value
        else:
            intervals[i].P = P(intervals,i)

intervals = []
for i in range(1, n+1):
    intervals.append(Interval(i, s[i-1], f[i-1], v[i-1]))
assign_P(intervals,n)

for j in range(10):
    print(intervals[j].P)
# OPT(intervals, n)

print(opt_intervals)
# p = P(intervals,10)
# print("p:",p.n)
# print(p.n, p.start, p.finish, p.value)

# sort_f = sort_finish(intervals)
# for j in range(len(sort_f)):
#     print(sort_f[j].n, sort_f[j].start, sort_f[j].finish, sort_f[j].value)