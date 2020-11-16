'''
print sum of all numbers not in given range till 10^6
'''

def not_in_range(ranges):
    end_ = 0
    t_sum = 0
    for start in sorted(ranges):
        if start > end_:
            t_sum += (end_ + start) * (start - 1 - end_) / 2
        
        print(start, end_)

        end_ = max(end_, ranges[start])
        print(t_sum)

    max_num = 10 ** 6
    t_sum += (end_ + 1 + max_num) * (max_num - end_) / 2
    return t_sum

ranges = {
    2: 20,
    23: 200,
    21: 21,
    101: 2000,
    2002: 999998
}
n = len(ranges)

print(not_in_range(ranges))