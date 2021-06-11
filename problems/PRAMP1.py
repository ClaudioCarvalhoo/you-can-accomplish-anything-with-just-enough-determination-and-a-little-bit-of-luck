# Award Budget Cuts
# The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation
# problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks,
# the budget was reduced to newBudget dollars and now they need to reallocate the grants.
# The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants.
# Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

# Given an array grantsArray of the original grants and the reduced budget newBudget,
# write a function findGrantsCap that finds in the most efficient manner a cap such that
# the least number of recipients is impacted and that the new budget constraint is met
# (i.e. sum of the N reallocated grants equals to newBudget).

# Analyze the time and space complexities of your solution.


# Time
# O(n * log(n))
# n = len(grantsArray)
# complexity comes from sorting, if not from that it would be O(n)

# Space
# O(1)

# Sol 1
def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort()
    grantsSum = 0
    for i in grantsArray:
        grantsSum += i

    if newBudget >= grantsSum:
        return grantsArray[-1]

    amountCapped = 0
    tempCap = grantsArray[-1]
    for i in range(len(grantsArray) - 1, -1, -1):
        if grantsSum <= newBudget:
            break
        else:
            amountCapped += 1
            if i == 0:
                break
            grantsSum -= amountCapped * tempCap
            tempCap = grantsArray[i - 1]
            grantsSum += amountCapped * tempCap

    nonCappedSum = 0
    for i in grantsArray[: len(grantsArray) - amountCapped]:
        nonCappedSum += i

    return (newBudget - nonCappedSum) / float(amountCapped)


# Sol 2
def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort()
    sumSoFar = 0
    for i in range(len(grantsArray)):
        capCandidate = grantsArray[i]
        if sumSoFar + (capCandidate * (len(grantsArray) - i)) > newBudget:
            return float(newBudget - sumSoFar) / (len(grantsArray) - i)
        sumSoFar += grantsArray[i]
    return grantsArray[-1]
