import unittest

def in_array(a1, a2):
    res = []
    for i in a1:
        for j in a2:
            if i in j:
                if i not in res:
                    res.append(i)
    return res


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))

