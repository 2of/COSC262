def coins_reqd(value,coinage):
    def coins_calc(value, coinage):
        """The minimum number of coins to represent value"""
        numCoins = [0] * (value + 1)
        for amt in range(min(coinage), value + 1):
            numCoins[amt] = 1 + min(numCoins[amt - c] for c in coinage if  amt >=  c)
     #   for i in range(len(numCoins)):
     #       print(f"{i}:{numCoins[i]}")
        return numCoins



    def get_min(value, coinage,nums):
        min_ = float('Inf')
        index = 0
        for i in coinage:
            if value - i >= 0:
               # break
                if nums[value - i] <= min_:
                    min_ = nums[value - i]
                    index = value-i
        return (index, min_)


    def backtrack(value,coinage,nums,coins = []):

        if value == 0:
            return coins
        else:
            index,min_ = get_min(value,coinage,nums)
            change = (value - index)
            coins.append(change)

            value -= change
            return backtrack(value,coinage,nums,coins)


    def fix_it_up(remains):
        if remains is None:
            return None
        if remains == []:
            return []
        result = []
        last = remains[0]
        count = 0
        for a in remains: 
            if a == last:
                count += 1
            else:
                result.append((last,count))
                last = a
                count = 1
        result.append((last,count))
        return sorted(result, reverse = True)



    values = coins_calc(value,coinage)
    return fix_it_up(backtrack(value,coinage,values))