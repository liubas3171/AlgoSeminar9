def min_price(i):
    if res_recursion[i] != 0:
        return res_recursion[i]
    if i < 0:
        return 0
    elif i == 0:
        schedule[0] = "A"
        return r * vals[0]
    elif i == 1:
        schedule[0], schedule[1] = 'A', 'A'
        return (vals[0] + vals[1]) * r
    elif i == 2:
        schedule[0], schedule[1], schedule[2] = 'A', 'A', 'A'
        return (vals[0] + vals[1] + vals[2]) * r
    else:
        comp_a = r * vals[i] + min_price(i - 1)
        comp_b = 4 * c + min_price(i - 4)
        if comp_a < comp_b:
            schedule[i] = 'A'
        else:
            for j in range(4):
                schedule[i - j] = 'B'
        res_recursion[i] = min(comp_a, comp_b)
        return min(comp_a, comp_b)
    


if __name__ == "__main__":
    # A
    r = 1
    # B
    c = 10
    vals = [11, 9, 9, 12, 12, 12, 12, 9, 9, 11]
    # [A, A, A, B, B, B, B, A, A, A] = 98
    schedule = [0] * len(vals)
    # For saving results of recursive calls
    res_recursion = [0] * len(vals)
    print(min_price(9))
    print(schedule)
