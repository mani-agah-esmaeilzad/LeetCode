class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = {}
        min_length = float('inf')
        
        for i, card in enumerate(cards):
            if card in mp:
                min_length = min(min_length, i - mp[card] + 1)
            mp[card] = i
        
        return min_length if min_length != float('inf') else -1