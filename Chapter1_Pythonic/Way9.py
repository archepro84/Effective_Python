# for / else의 사용 문법
def fn_1():
    for i in range(3):
        print('Loop', i)
    else:
        print('Else block!')
    pass


# for / else로 서로소 검사
def fn_2():
    a = 4
    b = 9
    for i in range(2, min(a, b) + 1):
        print('검사 중', i)
        if a % i == 0 and b % i == 0:
            print('서로소 아님')
            break
    else:
        print('서로소')
    pass


# 원하는 조건을 찾을 때 함수를 반환하는 도우미 함수
def fn_3():
    def coprime(a, b):
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return False
        return True

    assert coprime(4, 9)
    assert not coprime(3, 6)

    pass


# 루프 안에서 원하는 대상을 찾았는지 나타내는 결과 변수를 반환하는 도우미 함수
def fn_4():
    def coprime_alternate(a, b):
        is_coprime = True

        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                is_coprime = False
                break
        return is_coprime

    assert coprime_alternate(4, 9)
    assert not coprime_alternate(3, 6)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    pass
