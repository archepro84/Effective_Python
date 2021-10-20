""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# Default 값을 None으로 지정하고 실제 동작을 독스트링에 문서화 하는것이 효율적이다.
def fn_1():
    from time import sleep
    from datetime import datetime

    def log(message, when=None):
        """메시지와 타임스탬프를 로그에 남긴다.

        Args:
            message: 출력할 메시지.
            when: 메시지가 발생한 시각(datetime).
                디폴트 값은 현재 시간이다.
        """
        if when is None:
            when = datetime.now()  # 함수가 호출될 때마다 Method를 새롭게 호출한다.
        print(f'{when}: {message}')

    log('안녕!')
    sleep(0.1)
    log('다시 안녕!')
    pass


# Default 인자를 List나 Dictionary로 설정할 경우 얕은 복사가 발생하기 때문에 변수가 공유된다.
def fn_2():
    import json

    def decode(data, default={}):
        try:
            return json.loads(data)
        except ValueError:
            return default

    foo = decode('잘못된 데이터')
    foo['stuff'] = 5
    bar = decode('또 잘못된 데이터')
    bar['meep'] = 1
    print('Foo:', foo)  # 얕은 복사로 할당받은 변수가 공유된다.
    print('Bar:', bar)  # 얕은 복사로 할당받은 변수가 공유된다.
    pass


# Optional 타입 애너테이션으로 None이 허용되는 함수의 매개 변수에 타입을 명시할 때 사용한다.
def fn_3():
    from datetime import datetime
    from time import sleep
    from typing import Optional

    def log_typed(message: str,
                  when: Optional[datetime] = None) -> None:
        """메시지와 타임스탬프를 로그에 남긴다.

        Args:
            message: 출력할 메시지.
            when: 메시지가 발생한 시각(datetime).
                디폴트 값은 현재 시간이다.
        """
        if when is None:
            when = datetime.now()
        print(f'{when}: {message}')

    now = datetime.now()
    log_typed(message='안녕!')
    sleep(0.1)
    log_typed(message='안녕! 0.1초 후!')
    log_typed(message='안녕! 처음!', when=now)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
