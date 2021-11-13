""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """
# global 문을 사용해 Module 영역에 Mock Class를 캐시해주는 도우미 함수를 정의

from typing import Optional
from datetime import datetime, timedelta
from unittest.mock import patch
import contextlib
import io


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


DATABASE: Optional[ZooDatabase] = None


def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase()
    return DATABASE


def main(argv):
    database = get_database()
    species = argv[1]
    count = do_rounds(database, species)
    print(f'급양: {count} {species}')
    return 0


# Mock utcnow를 사용하지 않고, 단위 테스트와 비슷한 결과를 낼 수 있도록 Mock이 반환하는 DB Record 시간을 상대값으로 설정한다.
with patch('__main__.DATABASE', spec=ZooDatabase):
    now = datetime.utcnow()

    DATABASE.get_food_period.return_value = timedelta(hours=3)
    DATABASE.get_animals.return_value = [
        ('점박이', now - timedelta(minutes=4.5)),
        ('털보', now - timedelta(hours=3.25)),
        ('조조', now - timedelta(hours=3)),
    ]

    fake_stdout = io.StringIO()
    with contextlib.redirect_stdout(fake_stdout):
        main(['프로그램 이름', '미어캣'])

    found = fake_stdout.getvalue()
    expected = '급양: 2 미어캣\n'

    assert found == expected
    print(found == expected)
