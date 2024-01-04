n = int(input())
input2 = list(map(int, input().split()))
ans = [0] * 1000

for i in range(n):
    if (i == 0 and input2[0] > input2[1]) or (i == n - 1 and input2[n - 2] < input2[n - 1]) or (i!=0 and i!=n-1 and(input2[i] > input2[i + 1] or input2[i] > input2[i - 1])):
        cou = 0
        ch = 0
        if (input2[0] >= input2[i] and input2[1] >= input2[i]) or (input2[n-1] >= input2[i] and input2[n-2] >= input2[i]):
            ch = 1
        else:
            for j in range(n):
                if input2[j] >= input2[i]:
                    cou += 1
                else: cou = 0
                if cou == 3:
                    ch = 1
                    break
        if ch:
            ans[i] = 2
        else:
            ans[i] = 1
    else:
        ans[i] = 0

print(ans[:n])
'''
5
1 2 3 4 5
[0, 2, 2, 2, 1]
'''