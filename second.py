li = [int(n) for n in input().split()]
li.sort()
count = 1
for n in li:
    if n != count:
        break
    count += 1
print(count)