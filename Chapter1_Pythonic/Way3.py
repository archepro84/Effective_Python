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


# Bytes나 Str 인스턴스를 받아 항상 Str을 반환
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


# Bytes나 Str 인스턴스를 받아서 항상 Bytes를 반환한다.
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


# 파일 핸들과 관련된 연산들이 Default로 유니코드 문자열을 요구하고 이진 Byte 문자열을 요구하지 않는다.
def fn_15():
    with open('data.bin', 'w') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')
    pass


# With open을 wb로 변경해 이진 텍스트 쓰기모드로 정의한다.
def fn_16():
    with open('data.bin', 'wb') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')
    pass


# 이진 파일을 'r' 옵션으로 읽으려고 시도할 때 오류가 발생한다.
def fn_17():
    with open('data.bin', 'r') as f:
        data = f.read()
    pass


# 이진 읽기 모드 'rb' 옵션으로 열면 해결할 수 있다.
def fn_18():
    with open('data.bin', 'rb') as f:
        data = f.read()
    pass


# open 함수의 encoding 피라미터를 명시하면 플랫폼에 따라 동작이 달라져 에러가 발생하는 것을 막을 수 있다.
def fn_19():
    with open('data.bin', 'r', encoding='cp1252') as f:
        data = f.read()
    assert data == 'noooo'
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
    # fn_14()
    # fn_15()
    # fn_16()
    # fn_17()
    # fn_18()
    fn_19()
    pass
