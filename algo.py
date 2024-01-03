import random
import math


class fisher_yates:
    """
    the algorithm currently validated by wikipedia.
    It uses the random function at each iteration
    It is based on permutations
    """
    __name__ = "Fisher Yates"

    @staticmethod
    def shuffle(deck: list) -> list:
        for i in range(len(deck)-1):
            j = random.randint(0,i)
            deck[i], deck[j] = deck[j], deck[i]
        return deck
    

class cut_in_half:

    """
    Algorithm based on shuffling a pack of cards. The pack is cut in two, and the two blocks are grouped together, one card alternating with the other.
    A random shuffle number is introduced at the start of the algorithm to avoid determinism.
    The random function is used only once and outside the loop.
    """
    __name__ = "Cut in half"

    @staticmethod
    def shuffle(deck: list) -> list:
        j = int(math.log((len(deck)/2)-1))
        f = random.randint(0, j)
        deck_shuffle = []
        for x in range(1,f):
            for x in range(1, j):
                    deck_shuffle.append(deck[x])
                    deck_shuffle.append(deck[x+j])
        return deck_shuffle


class cut_in_n:
    __name__ = "Cut in N"

    @staticmethod
    def shuffle(deck: list) -> list:
        nb_cut = random.randint(2,int(len(deck)/2))
        deck_shuffle = []
        for j in range(0,nb_cut):
            for x in range(0+j,len(deck), nb_cut):
                deck_shuffle.append(deck[x])
        return(deck_shuffle)
