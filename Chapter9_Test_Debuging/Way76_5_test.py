""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

# 실행 방법
"python Way76_5_test.py"

from unittest import TestCase, main
from Way76 import to_str

# subTest 도우미 메서드를 사용해 한 테스트 메서드 안에 여러 텧스트를 정의할 수 있다.
class DataDrivenTestCase(TestCase):
    def test_good(self):
        good_cases = [
            (b'my bytes', 'my bytes'),
            ('no error', b'no error'),  # to_str에서 bytes를 str로 형변환시켜 에러기 발생한다.
            ('other str', 'other str'),
        ]
        for value, expected in good_cases:
            with self.subTest(value):
                self.assertEqual(expected, to_str(value))

    def test_bad(self):
        bad_cases = [
            (object(), TypeError),
            (b'\xfa\xfa', UnicodeDecodeError),
        ]
        for value, exception in bad_cases:
            with self.subTest(value):
                with self.assertRaises(exception):
                    to_str(value)


if __name__ == '__main__':
    main()
