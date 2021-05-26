class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketsDict = {}
        for ticket in tickets:
            if ticket[0] not in ticketsDict:
                ticketsDict[ticket[0]] = {}
            if ticket[1] not in ticketsDict[ticket[0]]:
                ticketsDict[ticket[0]][ticket[1]] = 0
            ticketsDict[ticket[0]][ticket[1]] += 1
        for origin in ticketsDict:
            destinations = list(ticketsDict[origin].keys())
            destinations.sort()
            ticketsDict[origin]["sortedDestinations"] = destinations

        itinerary = ["JFK"]
        self.explore(ticketsDict, itinerary, len(tickets) + 1)
        return itinerary

    def explore(self, tickets, itinerary, targetLen):
        if len(itinerary) == targetLen:
            return True
        origin = itinerary[-1]
        if origin in tickets:
            for destination in tickets[origin]["sortedDestinations"]:
                if tickets[origin][destination] > 0:
                    tickets[origin][destination] -= 1
                    itinerary.append(destination)
                    found = self.explore(tickets, itinerary, targetLen)
                    if found:
                        return True
                    itinerary.pop()
                    tickets[origin][destination] += 1
        return False
