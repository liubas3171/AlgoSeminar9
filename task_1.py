import random


def greedy(coords):
    if len(coords) <= 1:
        return None
    res = [1]
    val = coords[1]
    pointer = 2
    while pointer < len(coords):
        while pointer < len(coords) and coords[pointer] - val <= 5:
            pointer += 1
        if pointer >= len(coords):
            return res
        res.append(pointer)
        val = coords[pointer]
    return res


def compute_opt(j):
    if j == 0:
        return 0
    elif opt_list[j]:
        return opt_list[j]
    else:
        opt_list[j] = max(1 + compute_opt(p(j)), compute_opt(j - 1))
        return opt_list[j]


def p(j):
    pointer = j
    while pointer >= 1 and coords[j] - coords[pointer] <= 5:
        pointer -= 1
    return pointer


def find_solution(j):
    if j == 0:
        return None
    else:
        if 1 + opt_list[p(j)] >= opt_list[j - 1]:  # opt_list[p(j)] and
            return [j] + find_solution(p(j)) if find_solution(p(j)) else [j]
        else:
            return find_solution(j - 1)


if __name__ == "__main__":
    # There just create a list with possible coords of bigbords
    M = 16
    num_bords = int(random.random() * M)
    coords = []
    # We should work with counting started from 1
    coords.append(0)
    for i in range(num_bords):
        coords.append(round(random.random() * M, 2))
    coords.sort()
    # Its list with numbers of operations joint with our...
    opt_list = [0] * (num_bords + 1)

    # compute_otp, find_solution and p are from lecture
    compute_opt(num_bords)
    x = find_solution(num_bords)
    y = greedy(coords)

    print(coords)
    print(x)
    print(y)

    # Just beauty output
    # x.sort()
    # y.sort()
    #
    # res_x = []
    # for i in range(len(x)):
    #     res_x.append(coords[x[i]])
    # res_y = []
    # for i in range(len(y)):
    #     res_y.append(coords[y[i]])
