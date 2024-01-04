def water(wall:list):
    a = 0
    b = 1

    result = []
    while b < len(wall):
        if wall[a] > wall[b]:
            b = max(range(b, len(wall)), key=wall.__getitem__)
            result.extend([min(wall[a], wall[b])] * (b - a))
        # elif wall[a] < wall[b]:
        #    a = max(range(a+1), key=wall.__getitem__)
        #   result.extend([min(wall[a], wall[b])] * (b - a))
        else:
            result.append(wall[a])
        a = b 
        b = a+1
    return result

print(water([10,4,1,10,3,4,5, 9]))