
def change_greedy(amount, coinage):
    a = sorted(coinage, reverse = True)
    #coins is the tuple list

    def calculate(amount_remains,coins,result):
        if amount_remains == 0:
            return result
        for a in coins: #remember these are ordered 
            if a <= amount_remains:
                result.append(a)
                return calculate(amount_remains - a, coins,result)
        return None #no result

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
                result.append((count,last))
                last = a
                count = 1
        result.append((count,last))
        
        return result
    return fix_it_up(calculate(amount, a, []))


