""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

# 실행 방법
"python Way76_2_test.py"

from unittest import TestCase, main


class AssertTestCase(TestCase):
    # unittest 모듈에서 제곧하는 assertEqual
    def test_assert_helper(self):
        expected = 12
        found = 2 * 5
        self.assertEqual(expected, found)

    # Python 내장 함수로 제공하는 assert
    def test_assert_statement(self):
        expected = 12
        found = 2 * 5
        assert expected == found


if __name__ == '__main__':
    main()
