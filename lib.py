# File for functions

from typing import List
import random

def sqi(deck: List[int]) -> int:
    """
    Calculate the Shuffle Quality Index (SQI)
    This index defines the quality of the blend.
    "1" is the worst quality (sequential digits)
    The higher the SQI, the better.
    This function is for testing sequential integers from 1 to n only.
    """

    sqi = 0
    for i in range(len(deck)-1):
        sqi += abs(deck[i+1]-deck[i])
    sqi = sqi / (len(deck)-1)
    return sqi


def fisher_yates(deck: list) -> list:
    for i in range(len(deck)-1):
        j = random.randint(0,i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck
