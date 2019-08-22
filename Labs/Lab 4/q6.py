def fib(n):     # im genuinely confused :()
                # 
    topl = 1
    bl = 1
    topr = 0
    a = bin(n)
    for rec in a[3:]: 
        calc = bl*bl
        topl, bl, topr = topl*topl+calc, (topl+topr)*bl, calc+topr*topr
        if rec=='1':    topl, bl, topr = topl+bl, topl, bl
    return bl