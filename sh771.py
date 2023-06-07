def F(jewels, stones):
        count=0
        a=jewels.split()
        b=stones.split()
        for d in jewels:
            for f in stones:
                if d == f:
                    count+=1
        return count
print(F(jewels = "aA", stones = "aAAbbbb"))
