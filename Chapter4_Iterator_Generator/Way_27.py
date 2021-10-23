""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 리스트 컴프리헨션 : 다른 시퀀스나 이터러블에서 새 리스트를 만들어내는 간결한 구문을 제공한다.
def fn_1():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = []
    for x in a:
        squares.append(x ** 2)
    print(squares)
    pass


# 루프로 처리할 대상인 입력 시퀀스의 원소에 적용할 변환식을 지정함으로써 같은 결과를 얻을 수 있다.
def fn_2():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = [x ** 2 for x in a]  # 리스트 컴프리핸션
    print(squares)
    pass


# 인자가 하나인 함수를 적용하는 경우가 아니라면 map보다 리스트 컴프리헨션이 더 명확하다.
def fn_3():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    alt = map(lambda x: x ** 2, a)
    even_squares = [x ** 2 for x in a if x % 2 == 0]

    print(list(alt))
    print(even_squares)
    pass


# map과 달리 입력 리스트에서 원소를 쉽게 필터링해 결과에서 원하는 원소를 제거할 수 있다.
def fn_4():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_squares = [x ** 2 for x in a if x % 2 == 0]  # 짝수인 결과값만 제곱해 반환한다.
    alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))  # map과 lambda로 구현

    print(even_squares)
    print(list(alt))
    # assert even_squares == list(alt)
    pass


# 딕셔너리와 집합에서의 컴프리헨션 구현
def fn_5():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}  # 딕셔너리 컴프리헨션
    threes_cubed_set = {x ** 3 for x in a if x % 3 == 0}  # 집합 컴프리헨션

    print(even_squares_dict)
    print(threes_cubed_set)
    pass


# 호출을 적절한 생성자로 감싸면 같은 결과를 map과 filter를 사용해 만들 수 있다. / 비효율적이다.
def fn_6():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    alt_dict = dict(map(lambda x: (x, x ** 2),
                        filter(lambda x: x % 2 == 0, a)))
    alt_set = set(map(lambda x: x ** 3,
                      filter(lambda x: x % 3 == 0, a)))

    print(alt_dict)
    print(alt_set)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    pass
