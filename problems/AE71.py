# Valid IP Adressess

# O(1)


def validIPAddresses(string):
    return explore(string, 0, 3, [])


def explore(string, pos, remainingDots, dotPositionsSoFar):
    if remainingDots <= 0:
        IP = buildIP(string, dotPositionsSoFar)
        if validateIP(IP):
            return [IP]
        else:
            return []

    res = []
    for i in range(3):
        dotPositionsSoFar.append(pos + i)
        res += explore(string, pos + i + 1, remainingDots - 1, dotPositionsSoFar)
        dotPositionsSoFar.pop()
    return res


def buildIP(string, dotPositions):
    res = []
    dots = set(dotPositions)
    for i in range(len(string)):
        res.append(string[i])
        if i in dots:
            res.append(".")
    return "".join(res)


def validateIP(IP):
    parts = IP.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if (
            len(part) <= 0
            or len(part) > 3
            or int(part) > 255
            or (len(part) != 1 and part[0] == "0")
        ):
            return False
    return True
