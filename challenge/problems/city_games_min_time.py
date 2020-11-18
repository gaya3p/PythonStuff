'''
A city is organising an event where every participant is required to take part in 3 events.
1st Event is on a computer, so only one can participate at a time.
2nd and 3rd (or more) events can be participated by multiple participants simultaneously.

Input: 
Line 1: Number of participating people
Line 2 to n-1: Times required complete 3 events by that particular person

Example:
Total number of participants: 3
Times taken by 1st person: 18, 7,  6
Times taken by 1st person: 23, 10, 27
Times taken by 1st person: 20, 9,  14

If the order is 1 - 2 - 3, then
Time required by 1st person = 18+7+6 = 31
Time required by 2nd person = *18* + 23+10+27 = 78
Time required by 3rd person = *18 + 23* + 20+9+14 = 84
So, total time to complete all the events = max(31, 78, 84) = 84

But, if the order is 2 - 3 - 1, then
Time required by 1st (2) person = 23+10+27 = 60
Time required by 2nd (3) person = *23* + 20+9+14 = 66
Time required by 3rd (1) person = *23 + 20* + 18+7+6 = 74
Total time = max(60, 66, 74) = 74

Therefore, the best possible order is 2 - 3 - 1.

Input 1:
3
18 7 6
23 10 27
20 9 14

Output:
74
'''
# Best way
c = {
    0: [18, 7, 6],
    1: [23, 10, 27],
    2: [20, 9, 14],
    # 3: [19, 10, 14]
}

def get_sum(item):
    # item: (key, value_list)
    return (sum(item[1]), item[1][1])

# Order by sum of the times, then time for the first event
order = sorted(c.items(), key=get_sum, reverse=True)

s = 0
n = len(order)

for i in range(n):
    if i == n-1:
        s += sum(order[i][1])
    else:
        s += order[i][1][0]

print('Min time:', s)

''' Detailed version
cits2 = dict(c)

max_t, max_i = 0, 0
total_t = []
order = []

for j in range(n):
    max_t, max_i, max_times = -1, -1, []
    
    for c, times in zip(cits.keys(),cits.values()):
        time = sum(times)
        if time > max_t:
            max_t = time
            max_i = c
            max_times = times

        # choose b/w two citizens if equal time
        if time == max_t:
            if times[0] < max_times[0]:
                max_t = time
                max_i = c
                max_times = times
                
    order.append(max_i)
    del c[max_i]

s = 0
print(order)

for key, value in cits2.items():
    if key == order[-1]:
        s += sum(value)
    else:
        s += value[0]

print(s)
'''