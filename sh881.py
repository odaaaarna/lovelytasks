def F(people, limit):
    people.sort()
    a = 0
    b = len(people) - 1
    cnt = 0
    while a <= b:
        if people[a] + people[b] <= limit:
            a += 1
        else:
            b -= 1
            cnt += 1
    return cnt
print(F(people = [1,2], limit = 3))
