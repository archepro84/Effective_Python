""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 리스트를 슬라이싱한 결과는 완전히 새로운 리스트가 반환된다.
def fn_1():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    b = a[3:]
    print('이전:', b)
    b[1] = 99
    print('이후:', b)
    print('변화 없음:', a)
    pass


# 리스트를 슬라이싱한 결과는 얕은 복사 (shallow copy) 되므로 내부에 존재하는 List는 동일한 주솟값을 참조한다.
def fn_2():
    a = [['aa', 'ab', 'ac'], 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    b = a[:3]
    print('이전:', b)
    b[0][0] = 99
    print('이후:', b)
    print('변화 발생:', a)
    pass


# 대입에 슬라이스를 사용하면 지정한 범위에 들어있는 원소를 변경한다.
# 지정한 슬라이스 길이보다 대입되는 배열의 길이가 더 짧다면 리스트가 줄어든다.
def fn_3():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    print('이전:', a)
    a[2:7] = [99, 22, 14]
    print('이후:', a)
    pass


# 지정한 슬라이스 길이보다 대입되는 배열의 길이가 더 길다면 리스트가 늘어난다.
def fn_4():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    print('이전:', a)
    a[2:3] = [47, 11]
    print('이후:', a)
    pass


# 시작과 끝 인덱스가 없는 슬라이스에 대입하면 슬라이스가 참조하는 리스트의 복사본으로 덮어 쓴다.
def fn_5():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = a

    print('이전 a:', a)
    print('이전 b:', b)
    assert a is b  # 같은 리스트 객체

    a[:] = [101, 102, 103]
    print('이후 a:', a)  # 새로운 내용이 들어 있음
    print('이후 b:', b)  # 같은 리스트 객체이기 때문에 a와 내용이 같음
    assert a is b  # 여전히 같은 리스트 객체
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    pass