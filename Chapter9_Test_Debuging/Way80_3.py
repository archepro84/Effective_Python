# 에러가 발생하는 코드를 작성하여 사후 디버깅을 진행
import math


def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0
    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        total_err_2 += err_2
        count += 1

    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse


result = compute_rmse(
    [1.8, 1.7, 3.2, 7j],  # 7j는 Real Number가 아니라 에러발생
    [2, 1.5, 3, 5])
print(result)

# python -m pdb -c continue Way80_3.py
# pdb 모듈이 프로그램 실행을 제어하게 할 수 있다.
