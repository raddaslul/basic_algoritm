input = 20

# 소수는 자기 자신과 1 외에는 아무 것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 즉, 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시 N의 제곱근 이하이다.
def find_prime_list_under_number(number):
    prime_number_array = []
    # 0, 1은 소수가 아니기 때문에 2부터 시작, number + 1 로 설정해야 n이 20까지 탐색한다.
    for n in range(2, number + 1):
        # 2와 3으로 안 나눠 떨어지면 6으로도 안 나눠 떨이지기 때문에 소수로만 판단해도 된다.
        # 제곱근까지만 나눠도 된다.
        for i in prime_number_array:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_number_array.append(n)
    return prime_number_array


result = find_prime_list_under_number(input)
print(result)