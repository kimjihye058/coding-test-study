def solution(price, money, count):
    # 총 비용을 계산합니다.
    total_cost = 0
    for i in range(1, count + 1):
        total_cost += price * i
    
    # 부족한 금액 계산
    shortage = total_cost - money
    
    # 부족한 금액이 0 이하라면 0을 반환하고, 아니면 부족한 금액을 반환
    return max(shortage, 0)
