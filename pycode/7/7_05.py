def solve():
    cnt = list(map(int, input().split()))
    odd_cnt = 0
    middle = ""
    for i in range(10):
        if cnt[i] % 2 != 0:
            odd_cnt += 1
            midddle = str(i)
    if odd_cnt > 1:
        print("-1")
        return
    left_half = []
    for i in range(10):
        if cnt[i] >= 2:
            half_cnt = cnt[i] // 2
            left_half.extend([str(i)] * half_cnt)
    if left_half:
        if left_half[0] == '0':
            is_all_zero = True
            for idx in range(1, len(left_half)):
                if left_half[idx] != '0':
                    left_half[0], left_half[idx] = left_half[idx], left_half[0]
                    is_all_zero = False
                    break
            if is_all_zero:
                if len(left_half) * 2 + middle > 1:
                    print("-1")
                    return
    left_str = "".join(left_half)
    right_str = "".join(reversed(left_half))
    res = left_str + middle + right_str
    print(res)            
solve()           