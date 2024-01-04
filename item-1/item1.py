def count_ways(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return b

print(count_ways(20)) 