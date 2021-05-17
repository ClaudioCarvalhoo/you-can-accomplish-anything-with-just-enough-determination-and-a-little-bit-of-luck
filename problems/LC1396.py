class UndergroundSystem:
    def __init__(self):
        self.checkedCustomers = {}
        self.travelTimes = {}

    # O(1)
    def checkIn(self, id: int, checkInStation: str, t: int) -> None:
        self.checkedCustomers[id] = (checkInStation, t)

    # O(1)
    def checkOut(self, id: int, checkOutStation: str, t: int) -> None:
        checkInStation, checkInTime = self.checkedCustomers[id]
        elapsedTime = t - checkInTime
        del self.checkedCustomers[id]

        if checkInStation not in self.travelTimes:
            self.travelTimes[checkInStation] = {}
        if checkOutStation not in self.travelTimes[checkInStation]:
            self.travelTimes[checkInStation][checkOutStation] = {"count": 0, "sum": 0}

        self.travelTimes[checkInStation][checkOutStation]["count"] += 1
        self.travelTimes[checkInStation][checkOutStation]["sum"] += elapsedTime

    # O(1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (
            self.travelTimes[startStation][endStation]["sum"]
            / self.travelTimes[startStation][endStation]["count"]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)