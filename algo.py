import random
import math

class no_shuffle:
    """
    For evaluation, no shuffle
    """
    __name__ = "No shuffle"

    @staticmethod
    def shuffle(deck: list) -> list:
        return deck


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
        deck_work = deck
        j = int((len(deck)/2))
        f = 2 + random.randint(0, int(math.log(j, 2)))
        for x in range(0,f):
            deck_shuffle = []
            for x in range(0, j):
                    deck_shuffle.append(deck_work[x+j])
                    deck_shuffle.append(deck_work[x])
            if (len(deck) % 2) != 0:
                deck_shuffle.append(deck[len(deck)-1])
            deck_work = deck_shuffle
        return deck_shuffle


class cut_in_n:
    """
    The deck is cut into n pieces, and the elements in each piece are added one by one to the global list.
    N is randomly chosen between 2 and half the size of the deck.
    Randomness avoids determinism.
    """

    __name__ = "Cut in N"

    @staticmethod
    def shuffle(deck: list) -> list:
        nb_cut = random.randint(2,int(len(deck)/2))
        deck_shuffle = []
        for j in range(0,nb_cut):
            for x in range(0+j,len(deck), nb_cut):
                deck_shuffle.append(deck[x])
        return(deck_shuffle)
