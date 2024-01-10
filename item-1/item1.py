def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways(n-1) + count_ways(n-2)

    #a, b = 0, 1
    #for _ in range(n):
    #   a, b = b, a + b
    #return b

print(count_ways(20)) 