def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])