""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 컴프리헨션의 기본 사용방법
def fn_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # flat 단일 리스트로 단순화
    flat = [x for row in matrix for x in row]
    print(flat)

    # 행렬의 곱
    squared = [[x ** 2 for x in row] for row in matrix]
    print(squared)

    # 3단계 리스트 컴프리헨션
    my_lists = [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [1, 2, 3]],
        [[4, 5, 6], [7, 8, 9]],
    ]
    flat = [x for sublist1 in my_lists
            for sublist2 in sublist1
            for x in sublist2]
    print(flat)
    pass


# 컴프리헨션의 다중 if는 암시적으로 and 식을 의미한다.
def fn_2():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    b = [x for x in a if x > 4 if x % 2 == 0]  # 다중 if
    c = [x for x in a if x > 4 and x % 2 == 0]  # 암시적 and

    print(b)
    print(c)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    pass
