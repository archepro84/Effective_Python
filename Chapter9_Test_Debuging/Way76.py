""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('str이나 bytes를 전달해야 합니다, '
                        '찾은 값: %r' % data)
