""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# mock은 대상에 대한 잘못된 요청이 들어오면 오류를 발생시킨다.
def fn_1():
    from datetime import datetime
    from unittest.mock import Mock

    def get_animals(database, species):
        # 데이터베이스에 질의한다
        ...
        # (이름, 급양시간) 튜플 리스트를 반환한다
        return [("", datetime(2020, 1, 1, 1, 1, 1))]

    mock = Mock(spec=get_animals)
    expected = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45)),
    ]
    mock.return_value = expected
    # 존재하지않는 메서드 호출로 인한 에러
    mock.does_not_exist
    pass


# Mock 객체에서 제공하는 assert_called_once_with
def fn_2():
    from datetime import datetime
    from unittest.mock import Mock

    def get_animals(database, species):
        # 데이터베이스에 질의한다
        ...
        # (이름, 급양시간) 튜플 리스트를 반환한다
        return [("", datetime(2020, 1, 1, 1, 1, 1))]

    mock = Mock(spec=get_animals)
    expected = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45)),
    ]
    mock.return_value = expected

    database = object()
    result = mock(database, '고양이')
    assert result == expected

    # 어떤 파라미터가 Mock 객체에게 정확히 한 번 전달됐는지를 검증한다.
    mock.assert_called_once_with(database, '고양이')

    # 한 번도 호출하지 않는 파라미터를 전달해 에러가 발생한다.
    mock.assert_called_once_with(database, '달마시안')
    pass


#  여러 파라미터에 대한 기댓값을 하나하나 지정해 과도하게 구체적인 것 보다 ANY를 좀 더 자유롭게 사용해 테스트를 느슨하게 하면 좋을 때가 있다.
def fn_3():
    from datetime import datetime
    from unittest.mock import ANY, Mock

    def get_animals(database, species):
        # 데이터베이스에 질의한다
        ...
        # (이름, 급양시간) 튜플 리스트를 반환한다
        return [("", datetime(2020, 1, 1, 1, 1, 1))]

    mock = Mock(spec=get_animals)
    expected = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45)),
    ]
    mock.return_value = expected

    mock = Mock(spec=get_animals)
    mock('database 1', '토끼')
    mock('database 2', '들소')
    mock('database 3', '고양이')

    # 가장 최근에 Mock을 호출할 때 어떤 인자가 전달됐는지 확인할 수도 있다.
    mock.assert_called_with(ANY, '고양이')
    pass


# MyError를 사용해 예외 발생을 쉽게 Mocking 할 수 있는 도구를 제공한다.
def fn_4():
    from datetime import datetime
    from unittest.mock import Mock

    def get_animals(database, species):
        # 데이터베이스에 질의한다
        ...
        # (이름, 급양시간) 튜플 리스트를 반환한다
        return [("", datetime(2020, 1, 1, 1, 1, 1))]

    mock = Mock(spec=get_animals)
    expected = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45)),
    ]
    mock.return_value = expected

    class MyError(Exception):
        pass

    database = object()
    mock = Mock(spec=get_animals)
    mock.side_effect = MyError('큰 문제 발생!')
    mock(database, '고양이')
    pass


# DB와 상호작용하기 위해 여러 동물들에게 먹이를 나누어주는 함수
def fn_5():
    from datetime import datetime
    from datetime import timedelta
    from unittest.mock import Mock, call, patch, DEFAULT

    def get_animals(database, species):
        # 데이터베이스에 질의한다
        ...
        # (이름, 급양시간) 튜플 리스트를 반환한다
        return [("", datetime(2020, 1, 1, 1, 1, 1))]

    def get_food_period(database, species):
        # 데이터베이스에 질의한다
        ...
        # 주기를 반환한다
        return 3

    def feed_animal(database, name, when):
        # 데이터베이스에 기록한다
        ...

    def do_rounds(database, species, *,
                  now_func=datetime.utcnow,
                  food_func=get_food_period,
                  animals_func=get_animals,
                  feed_func=feed_animal):
        now = now_func()
        feeding_timedelta = food_func(database, species)
        animals = animals_func(database, species)
        fed = 0

        for name, last_mealtime in animals:
            if (now - last_mealtime) > feeding_timedelta:
                feed_func(database, name, now)
                fed += 1
        return fed

    # Mock 함수 생성
    now_func = Mock(spec=datetime.utcnow)
    now_func.return_value = datetime(2020, 6, 5, 15, 45)

    food_func = Mock(spec=get_food_period)
    food_func.return_value = timedelta(hours=3)

    animals_func = Mock(spec=get_animals)
    animals_func.return_value = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45)),
    ]

    feed_func = Mock(spec=feed_animal)

    # 함수 테스트
    database = object()

    result = do_rounds(
        database,
        '고양이',
        now_func=now_func,
        food_func=food_func,
        animals_func=animals_func,
        feed_func=feed_func)

    assert result == 2

    # Mock 객체에서 단 한번 호출되었는지 검증
    food_func.assert_called_once_with(database, '고양이')
    animals_func.assert_called_once_with(database, '고양이')

    # DB에 기록하는 함수가 순서 상관없이 두 번 호출됐는지 검증
    feed_func.assert_has_calls(
        [
            call(database, '점박이', now_func.return_value),
            call(database, '털보', now_func.return_value),
        ],
        any_order=True)
    # TODO Way78_1 파일로
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    pass
