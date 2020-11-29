def best_revenue(n):
    if n < 0:
        return 0
    if n == 0:
        return max(l[n], h[n])
    l_res = l[n] + best_revenue(n - 1)
    h_res = h[n] + best_revenue(n - 2)
    if h_res > l_res:
        res[n - 1] = 0
        res[n] = h[n]
    else:
        res[n] = l[n]
    return max(l_res, h_res)


if __name__ == "__main__":
    l = [10, 1, 10, 10]
    h = [5, 50, 5, 1]
    res = [0] * len(l)
    # [0, 50, 10, 10]
    print(best_revenue(3))
    print(res)
