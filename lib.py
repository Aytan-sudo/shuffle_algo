from typing import List
import timeit
import algo

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

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

class test_algo:
    def __init__(self):
        self.algo = [
            algo.fisher_yates,
            algo.cut_in_half,
            algo.cut_in_n,
        ]
        
    def test(self, deck):
        for algo_class in self.algo:
            algo = algo_class()
            time_algo = timeit.timeit(lambda:algo.shuffle(deck.copy()), number=1000)
            sqi_algo = sqi(algo.shuffle(deck.copy()))
            print(f"{algo.__name__} pass in {red}{time_algo*1000:.2f} milliseconds{reset} with a SQI of {green}{sqi_algo:.1f}{reset}")


    