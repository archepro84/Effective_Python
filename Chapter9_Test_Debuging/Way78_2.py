""" unittest.mock.patch를 확인하기위해 별도의 파일로 분리합니다. """

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

# unittest.mock.patch를 이용해 DB에 접근하는 함수를 다른 함수로 대치한다.
print('패치 외부:', get_animals)

with patch('__main__.get_animals'):
    print('패치 내부: ', get_animals)

print('다시 외부:', get_animals)

# # C 확장 모듈에서는 unittest.mock.patch로 Mocking을 직접할 수 없다.
# with patch('datetime.datetime.utcnow'):
#    datetime.utcnow.return_value = fake_now


# patch.multiple : 여러 Mock을 만들고 각각의 예상 값을 설정할 수 있다.
with patch.multiple('__main__',
                    autospec=True,
                    get_food_period=DEFAULT,
                    get_animals=DEFAULT,
                    feed_animal=DEFAULT):
    now_func = Mock(spec=datetime.utcnow)
    now_func.return_value = datetime(2020, 6, 5, 15, 45)
    get_food_period.return_value = timedelta(hours=3)
    get_animals.return_value = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45))
    ]

# # utcnow 인자가 정의되어있지 않아 오류가 발생한다.
# result = do_rounds(database, '고양이', utcnow=now_func)
# assert result == 2

food_func.assert_called_once_with(database, '고양이')
animals_func.assert_called_once_with(database, '고양이')
feed_func.assert_has_calls(
    [
        call(database, '점박이', now_func.return_value),
        call(database, '털보', now_func.return_value),
    ],
    any_order=True)
