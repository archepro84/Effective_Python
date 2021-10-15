""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# if, KeyError를 이용해 key를 생성
def fn_1():
    counters = {
        '품퍼니켈': 2,
        '사워도우': 1,
    }

    key = '밀'

    count = counters.get(key, 0)
    counters[key] = count + 1

    # 데이터가 존재하지 않을 때 key를 생성하는 if not in문
    if key not in counters:
        counters[key] = 0

    counters[key] += 1

    # 데이터가 존재하지 않을 때 key를 생성하는 if문
    if key in counters:
        counters[key] += 1
    else:
        counters[key] = 1

    # 데이터가 존재하지 않을 때 key를 생성하는 try.except 구문
    try:
        counters[key] += 1
    except KeyError:
        counters[key] = 1
    print(counters)

    pass


# 내부 객체가 추가된 dictionary
def fn_2():
    votes = {
        '바게트': ['철수', '순이'],
        '치아바타': ['하니', '유리'],
    }
    key = '브리오슈'
    who = '단이'

    # Key가 있으면 2번 읽어야하고, 없으면 1번 대입해야한다.
    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = []

    names.append(who)

    print(votes)
    for key, value in votes.items():
        print(key, len(value))
    pass


# 대입식과 dictionary.get을 이용해 존재하지않는 dictionary의 key를 정의
def fn_3():
    votes = {
        '바게트': ['철수', '순이'],
        '치아바타': ['하니', '유리'],
    }
    key = '브리오슈'
    who = '단이'

    if (names := votes.get(key)) is None:
        votes[key] = names = []  # 이중 대입문

    names.append(who)

    print(votes)
    for key, value in votes.items():
        print(key, len(value))
    pass


# setdefault를 이용해 동일한 동작을 한다.
def fn_4():
    votes = {
        '바게트': ['철수', '순이'],
        '치아바타': ['하니', '유리'],
    }
    key = '브리오슈'
    who = '단이'

    names = votes.setdefault(key, [])
    names.append(who)

    print(votes)
    for key, value in votes.items():
        print(key, len(value))
    pass


# key가 없으면 setdefault에 전달된 default값이 별도로 복사되지 않고 딕셔너리에 직접 대입된다. ☆
def fn_5():
    data = {}
    key = 'foo'
    value = []
    data.setdefault(key, value)
    print('이전:', data)
    value.append('hello')
    print('이후: ', data)  # default Value에 메모리 주소를 할당해 원본 객체가 변환되도 값이 변한다.
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    pass
