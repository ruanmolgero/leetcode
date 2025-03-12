from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand_counter = Counter(hand)
        if (len(hand) % groupSize) == 0:
            for c in sorted(hand):
                if hand_counter[c]:
                    for i in range(c, c + groupSize):
                        if hand_counter[i] == 0:
                            return False
                        else:
                            hand_counter[i] -= 1
                            if hand_counter[i] == 0:
                                del hand_counter[i]
            return True
        return False


# hand = [1, 2, 3, 1, 2, 3, 4, 5, 6]
# groupSize = 3

hand = [1, 2, 3, 4, 5]
groupSize = 4

s = Solution()
print(s.isNStraightHand(hand=hand, groupSize=groupSize))
