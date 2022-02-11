def can_reach_last_index(array):
    pos = 0
    max_reachable_pos = 0
    while pos < len(array):
        if pos > max_reachable_pos:
            return False
        if pos + array[pos] > max_reachable_pos:
            max_reachable_pos = pos + array[pos]
        if max_reachable_pos >= len(array) - 1:
            return True
        pos += 1

a = list(map(int, input().split()))
if(can_reach_last_index(a)):
    print(1)
else:
    print(0)
