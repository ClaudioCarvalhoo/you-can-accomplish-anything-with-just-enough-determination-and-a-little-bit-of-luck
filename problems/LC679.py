# O(1)


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.explore(cards)

    def explore(self, cards):
        if len(cards) == 1:
            return abs(24 - cards[0]) < 0.0001

        for i in range(len(cards)):
            for j in range(len(cards)):
                if i != j:
                    nextCards = cards[:]
                    card1 = cards[i]
                    card2 = cards[j]
                    nextCards.remove(card1)
                    nextCards.remove(card2)
                    candidates = [
                        card1 + card2,
                        card1 - card2,
                        card1 * card2,
                        card1 / card2 if card2 != 0 else 0,
                    ]
                    for candidate in candidates:
                        nextCards.append(candidate)
                        if self.explore(nextCards):
                            return True
                        nextCards.pop()
        return False
