def best_revenue(n):
    if max_revs[n] != 0:
        return max_revs[n]
    if n < 0:
        return 0
    if n == 0:
        max_revs[n] = max(l[n], h[n])
        return max(l[n], h[n])
    l_res = l[n] + best_revenue(n - 1)
    h_res = h[n] + best_revenue(n - 2)
    if h_res > l_res:
        res[n - 1] = 0
        res[n] = h[n]
    else:
        res[n] = l[n]
    max_revs[n] = max(l_res, h_res)
    return max(l_res, h_res)


if __name__ == "__main__":
    l = [10, 1, 10, 10]
    h = [5, 50, 5, 1]
    # list for saving results (revenues)
    max_revs = [0] * len(l)
    # list for saving plan
    res = [0] * len(l)
    print(best_revenue(3))
    print(res)
