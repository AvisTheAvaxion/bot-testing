import hikari
import random
import hidden

w, h = 3, 3

player_pos = {0, 0}
chunk_pos = {0, 0}

chunk_cont = [[0 for x in range(w)] for y in range(h)]


def make_arr(h1, w1, arr):
    for i in range(h1):
        for i1 in range(w1):
            arr[i][i1] = random.randint(1000, 2000)


make_arr(3, 3, chunk_cont)


def print_array(h1, w1):
    s = ""
    for i in range(h1):
        for i1 in range(w1):
            s = s + str(chunk_cont[i][i1]) + "|"

        s = s + "\n"

    return s


print(print_array(3, 3))
