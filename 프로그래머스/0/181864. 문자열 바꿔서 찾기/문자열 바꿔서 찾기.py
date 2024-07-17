def solution(myString, pat):
    tmp = "".join(["B" if char == "A" else "A" for char in myString])
    return 1 if pat in tmp else 0