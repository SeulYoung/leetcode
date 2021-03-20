from typing import List


def game(guess: List[int], answer: List[int]) -> int:
    return (guess[0] == answer[0]) + (guess[1] == answer[1]) + (guess[2] == answer[2])


def game(guess: List[int], answer: List[int]) -> int:
    return sum(guess[i] == answer[i] for i in range(len(guess)))


def game(guess: List[int], answer: List[int]) -> int:
    return [guess[i] == answer[i] for i in range(len(guess))].count(True)
