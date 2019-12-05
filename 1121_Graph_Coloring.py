def promising(i, vcolor):
    result = True
    j = 0
    while j < i and result:
        if W[i][j] and vcolor[i] == vcolor[j]:
            result = False
        j += 1
    return result


def color(i, vcolor):
    if promising(i, vcolor):
        if i == n-1:
            print(vcolor)
        else:
            for color_num in range(0, m):
                vcolor[i+1] = color_num + 1
                color(i + 1, vcolor)


n = 4
W = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vcolor = n * [0]
m = 3
color(-1, vcolor)
