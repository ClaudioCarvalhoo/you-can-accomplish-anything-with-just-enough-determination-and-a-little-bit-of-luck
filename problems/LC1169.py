# O(n) or O(n²)
# n = len(transactions)

# Sol 1 - O(n) Time
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [
            self.transactionToTuple(transaction) for transaction in transactions
        ]
        transactionsInTime = {}
        for _, name, time, amount, city in transactions:
            if time not in transactionsInTime:
                transactionsInTime[time] = {}
            if name not in transactionsInTime[time]:
                transactionsInTime[time][name] = set()
            transactionsInTime[time][name].add(city)

        res = []
        for transactionString, name, time, amount, city in transactions:
            if amount > 1000:
                res.append(transactionString)
            else:
                for otherTime in range(time - 60, time + 61):
                    if (
                        otherTime in transactionsInTime
                        and name in transactionsInTime[otherTime]
                    ):
                        otherCities = len(transactionsInTime[otherTime][name])
                        if city in transactionsInTime[otherTime][name]:
                            otherCities -= 1
                        if otherCities >= 1:
                            res.append(transactionString)
                            break
        return res

    def transactionToTuple(self, transaction):
        name, time, amount, city = transaction.split(",")
        return (transaction, name, int(time), int(amount), city)


# Sol 2 - O(n²) Time
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [
            self.transactionToTuple(transaction) for transaction in transactions
        ]
        res = []
        for transactionString, name, time, amount, city in transactions:
            if amount > 1000:
                res.append(transactionString)
            else:
                for _, name2, time2, amount2, city2 in transactions:
                    if name == name2 and city != city2 and abs(time - time2) <= 60:
                        res.append(transactionString)
                        break
        return res

    def transactionToTuple(self, transaction):
        name, time, amount, city = transaction.split(",")
        return (transaction, name, int(time), int(amount), city)