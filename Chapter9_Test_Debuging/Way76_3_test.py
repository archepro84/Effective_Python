""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

# 실행 방법
"python Way76_3_test.py"

from unittest import TestCase, main
from Way76 import to_str


# with.assertRaises를 try/exxcept 문과 비슷하게 사용할 수 있다.
class UtilsErrorTestCase(TestCase):

    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_str_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b'\xfa\xfa')


if __name__ == '__main__':
    main()
