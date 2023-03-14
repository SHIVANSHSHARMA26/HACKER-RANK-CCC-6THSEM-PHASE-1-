n, p = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans, prev = 0, -1 # to store the previous used buttons
for i in range(n):
    buttons = a[i] // p
    if buttons * p == a[i]: # this is to check if cost is completely divisble by p or not
        if buttons <= prev: # if equal to previous than answer will be the previous + 1 and our previous storing variable will be updated
            ans += prev + 1
            prev += 1
        else:
            ans += buttons
            prev = buttons
    else:
        buttons += 1
        if buttons <= prev:
            ans += prev + 1
            prev += 1
        else:
            ans += buttons
            prev = buttons

print(ans)
