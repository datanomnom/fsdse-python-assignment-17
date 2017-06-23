d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def solution_asc(dic):
    return sorted(dic.items())

def solution_desc(dic):
    return sorted(dic.items(), reverse=True)
