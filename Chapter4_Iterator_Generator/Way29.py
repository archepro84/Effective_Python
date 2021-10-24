""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 딕셔너리 컴프리헨션으로 구현한 주문 관리 프로그램
def fn_1():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    order = ['나사못', '나비너트', '클립']

    def get_batches(count, size):
        return count // size

    # 중복된 get_batches 함수를 호출한다.
    found = {name: get_batches(stock.get(name, 0), 8)
             for name in order
             if get_batches(stock.get(name, 0), 8)}
    print(found)
    pass


# 왈러스 연산자로 중복 함수 호출을 하지않는 딕셔너리 컴프리헨션
def fn_2():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    order = ['나사못', '나비너트', '클립']

    def get_batches(count, size):
        return count // size

    # get_batches를 왈러스 연산자로 변경
    found = {name: batches
             for name in order
             if (batches := get_batches(stock.get(name, 0), 8))}
    print(found)
    pass


# 왈러스 연산자를 컴프리헨션에서 사용할 때 대입식을 조건 쪽에 정의하고 만들어진 변수를 Value에서 참조하라.
def fn_3():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    # 컴프리헨션에서 왈러스 연산자의 실행 순서가 잘못돼 오류가 발생
    # result = {name: (tenth := count // 10)
    #          for name, count in stock.items() if tenth > 0}
    # print(result)

    result = {name: tenth
              for name, count in stock.items()
              if (tenth := count // 10)}
    print(result)
    pass


# 컴프리헨션이 Value부분에서 왈러스 연산자를 사용할 때 Value에 대한 조건 부분이 없다면 루프 밖 영역으로 변수가 누출된다.
def fn_4():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    # 왈러스 연산자의 루프 변수 누출
    half = [(last := count // 2) for count in stock.values()]
    print(f'{half}의 마지막 원소는 {last}')

    # for 문의 루프 변수 누출
    for count in stock.values():
        pass
    print(f'{list(stock.values())}의 마지막 원소는 {count}')
    pass


# 컴프리헨션의 루프 변수는 for문과 왈러스 연산자와 같은 비슷한 누출이 발생하지 않는다.
def fn_5():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    half = [count // 2 for count in stock.values()]
    print(half)
    # print(count)  # 루프 변수가 누출되지 않기 때문에 에러가 발생함
    pass


# 왈러스 연산자의 대입식은 제너레이터의 경우에도 동일한 방식으로 작동한다.
def fn_6():
    stock = {
        '못': 125,
        '나사못': 35,
        '나비너트': 8,
        '와셔': 24,
    }

    order = ['나사못', '나비너트', '클립']

    def get_batches(count, size):
        return count // size

    # 왈러스 연산자로 정의한 tuple을 반환하는 제너레이터의 컴프리헨션
    found = ((name, batches) for name in order
             if (batches := get_batches(stock.get(name, 0), 8)))
    print(type(found))
    print(next(found))
    print(next(found))
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    pass
