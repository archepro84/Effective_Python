# Bytes
def fn_1():
    a = b'h\x65llo'
    print(list(a))
    print(a)
    print(a.decode())


# Str
def fn_2():
    a = 'a\u0300 propos'
    print(list(a))
    print(a)
    print(a.encode())


# Bytes나 Str 인스턴스를 받아서 항상 Str을 반환
def fn_3():
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))
    print(repr(to_str(b'\xed\x95\x9c')))  # UTF-8에서 한글은 3Byte


# Bytes나 Str 인스턴스르 받아서 항상 Bytes를 반환한다.
def fn_4():
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value  # bytes 인스턴스

    print(repr(to_bytes(b'foo')))
    print(repr(to_bytes('bar')))
    print(repr(to_bytes('한글')))


# + 연산자를 사용하면 bytes를 bytes에 더하거나 str을 str에 더할 수 있다.
def fn_5():
    print(b'one' + b'two')
    print('one' + 'two')


# str 인스턴스를 bytes 인스턴스에 더할 수 없다.
def fn_6():
    print(b'one' + 'two')
    pass


# bytes 인스턴스를 str 인스턴스에 더할 수 없다.
def fn_7():
    print('one' + b'two')
    pass


# 이항 연산자를 사용하면 bytes를 bytes와 비교하거나 str을 str과 비교할 수 있다.
def fn_8():
    assert b'red' > b'blue'
    assert 'red' > 'blue'
    pass


# str 인스턴스와 bytes 인스턴스를 비교할 수 없다.
def fn_9():
    assert 'red' > b'blue'
    pass


# bytes 인스턴스와 str 인스턴스를 비교할 수 없다.
def fn_10():
    assert b'blue' < 'red'
    pass


# 내부에 똑같은 문자들이 들어있더라도 bytes와 str 인스턴스가 같은지 비교하면 항상 False가 나온다.
def fn_11():
    print(b'foo' == 'foo')
    pass


# % 연산자는 각 타입의 형식화 문자열(format string)에 해당한다.
def fn_12():
    print(b'red %s' % b'blue')
    print('red %s' % 'blue')
    pass


# Python이 어떤 이진 텍스트 인코딩을 사용할지 알 수 없으므로 str 인스턴스를 bytes 형식화 문자열에 넘길 수 없다.
def fn_13():
    print(b'red %s' % 'blue')
    pass


# str 형식화 문자열에 bytes 인스턴스를 넘길 수는 있지만, 이 경우에는 예상과 다르게 작동한다.
def fn_14():
    print('red %s' % b'blue')
    pass


def fn_15():
    pass


def fn_16():
    pass


def fn_17():
    pass


def fn_18():
    pass


def fn_19():
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    # fn_7()
    # fn_8()
    # fn_9()
    # fn_10()
    # fn_11()
    # fn_12()
    # fn_13()
    fn_14()
    # fn_15()
    # fn_16()
    # fn_17()
    # fn_18()
    # fn_19()
    pass
