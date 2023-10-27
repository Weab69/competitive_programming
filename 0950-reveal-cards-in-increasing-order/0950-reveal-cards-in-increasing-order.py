class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() # sorting

        queue = deque(range(len(deck)))
        # [2,3,4,5,6,1]

        result = [0] * len(deck)
        # [2,0,0,0,0,0,0]

        for card in deck:
            val = queue.popleft() # 0
            result[val] = card
            if queue:
                val2 = queue.popleft()
                queue.append(val2)

        return result