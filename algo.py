import random


class fisher_yates:
    __name__ = "Fisher Yates"

    @staticmethod
    def shuffle(deck: list) -> list:
        for i in range(len(deck)-1):
            j = random.randint(0,i)
            deck[i], deck[j] = deck[j], deck[i]
        return deck


class cut_in_half:
    __name__ = "Cut in half"

    @staticmethod
    def shuffle(deck: list) -> list:
        j = int((len(deck)/2)-1)
        f = random.randint(0, j)
        for x in range(j):
            for i in range(1, f):
                deck[i], deck[j+i] = deck[j+i], deck[i]
        return deck

