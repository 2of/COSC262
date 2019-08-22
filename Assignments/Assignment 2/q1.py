
def longest_common_substring(s1, s2): 
    ''' returns the assignment question friends'''

    cache = {}
    def compute(s1, s2):
        '''recursvive boi'''
       # print(f"called on {s1}, {s2}")
        if not s1 or not s2:
            return ""
        s1start, s1end, s2start, s2end = s1[0], s1[1:], s2[0], s2[1:]
        key = (s1 + s2) 
        if key not in cache: 
            if s1start == s2start: 
                cache[key] = s1start + compute(s1end, s2end)
            else:
                cache[key] = max(compute(s1, s2end), compute(s1end, s2), key=len)
        return cache[key]
    def format_(value):
        '''fix it up for submission'''
        return value
    return format_(compute(s1, s2))