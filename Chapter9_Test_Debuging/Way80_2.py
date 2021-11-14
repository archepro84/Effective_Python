# 디버깅하려는 문제가 어떤 구체적인 조건에서만 발생한다는 사실을 알고 있다면, breakpoint를 평범한 Python 코드에 추가해 사용할 수 있다.
import math


def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0
    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        if err_2 >= 1:
            breakpoint()
        total_err_2 += err_2
        count += 1

    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse


result = compute_rmse(
    [1.8, 1.7, 3.2, 7],
    [2, 1.5, 3, 5])
print(result)
