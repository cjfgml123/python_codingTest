def Mysolution(sizes):
    x, y = 0, 0
    for _size in sizes:
        _size.sort(reverse=True)
        if x < _size[0]:
            x = _size[0]
        if y < _size[1]:
            y = _size[1]

    return x*y

def solution1(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

def solution2(sizes):
    solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)