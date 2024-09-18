from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    elif direction == "left":
        numbers.rotate(-1)
    return list(numbers)