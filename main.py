def union(set1, set2):
    ans1 = [a for a in set1] + [b for b in set2 if b not in set1]
    ans1.sort()
    return ans1

def intersection(set1, set2):
    return [a for a in set1 if a in set2]

def setDifference(set1, set2):
    return [a for a in set1 if a not in set2]

def symmetricDifference(set1, set2):
    return setDifference(set1, set2) + setDifference(set2, set1);

def cartesianProduct(set1, set2):
    return [(a, b) for a in set1 for b in set2]

