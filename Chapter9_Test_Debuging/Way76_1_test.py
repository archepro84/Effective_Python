""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

# 실행방법
"python Way76_1_test.py"
# 단일 메서드만 실행시키는 방법
"python Way76_1_test.py UtilsTestCase.test_to_str_bytes"

from unittest import TestCase, main
from Way76 import to_str


class UtilsTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    # 입력값이 서로 달라 AssertionError 발생
    def test_failing(self):
        self.assertEqual('incorrect', to_str('hello'))


if __name__ == '__main__':
    main()
