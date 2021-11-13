""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """
# 래퍼 객체를 사용해 데이터베이스를 캡슐화

from datetime import datetime, timedelta
from unittest.mock import Mock, call


class ZooDatabase:
    ...

    def get_animals(self, species):
        ...

    def get_food_period(self, species):
        ...

    def feed_animal(self, name, when):
        ...


def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = database.get_food_period(species)
    animals = database.get_animals(species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) >= feeding_timedelta:
            database.feed_animal(name, now)
            fed += 1
    return fed


# Mock Class 생성 및 테스트
database = Mock(spec=ZooDatabase)
print(database.feed_animal)
database.feed_animal()
database.feed_animal.assert_any_call()

# datetime을 Mock
now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2019, 6, 5, 15, 45)

# Zoodatabase 캡슐화를 사용하도록 Mock을 다시 정의
database = Mock(spec=ZooDatabase)
database.get_food_period.return_value = timedelta(hours=3)
database.get_animals.return_value = [
    ('점박이', datetime(2019, 6, 5, 11, 15)),
    ('털보', datetime(2019, 6, 5, 12, 30)),
    ('조조', datetime(2019, 6, 5, 12, 55))
]

# return Value Test
result = do_rounds(database, '미어캣', utcnow=now_func)
assert result == 2
print(result == 2)

database.get_food_period.assert_called_once_with('미어캣')
database.get_animals.assert_called_once_with('미어캣')
database.feed_animal.assert_has_calls(
    [
        call('점박이', now_func.return_value),
        call('털보', now_func.return_value),
    ],
    any_order=True)

try:
    # bad_method_name의 이름을 가진 Method가 존재하지 않으므로 AttributeError가 발생한다.
    database.bad_method_name()
except AttributeError as Ae:
    print(f"{AttributeError.__name__} : {Ae}")
