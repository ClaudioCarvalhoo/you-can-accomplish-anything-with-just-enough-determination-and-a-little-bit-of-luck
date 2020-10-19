def isPredecessor(a, b):
    if len(a) != len(b) - 1:
        return False
    if len(a) == 0:
        return True
    found = False
    for i in range(len(a)):
        if a[i] != b[i + found]:
            if found:
                return False
            else:
                found = True
                i -= 1
    return found


print(isPredecessor("", "a"))