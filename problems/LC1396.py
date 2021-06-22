class CheckIn:
    def __init__(self, station, time):
        self.station = station
        self.time = time


class RouteStats:
    def __init__(self):
        self.passengers = 0
        self.totalTime = 0

    def addNewTime(self, time):
        self.passengers += 1
        self.totalTime += time

    def getAverageTime(self):
        return self.totalTime / self.passengers


class UndergroundSystem:

    # O(1)
    def __init__(self):
        self.checkIns = {}
        self.routeStats = {}

    # O(1)
    def checkIn(self, id: int, checkInStation: str, t: int) -> None:
        self.checkIns[id] = CheckIn(checkInStation, t)

    # O(1)
    def checkOut(self, id: int, checkOutStation: str, t: int) -> None:
        checkInStation, checkInTime = self.checkIns[id].station, self.checkIns[id].time
        del self.checkIns[id]
        if (checkInStation, checkOutStation) not in self.routeStats:
            self.routeStats[(checkInStation, checkOutStation)] = RouteStats()
        self.routeStats[(checkInStation, checkOutStation)].addNewTime(t - checkInTime)

    # O(1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.routeStats[(startStation, endStation)].getAverageTime()


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)