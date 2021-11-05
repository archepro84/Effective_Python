""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

# 실행 방법
"python Way76_4_test.py"

from unittest import TestCase, main


# 제너레이터의 동작을 검증하기 위해 구현한 도우미 메서드
def sum_squares(values):
    cumulative = 0
    for value in values:
        cumulative += value ** 2
        yield cumulative


class HelperTestCase(TestCase):
    def verify_complex_case(self, values, expected):
        expect_it = iter(expected)
        found_it = iter(sum_squares(values))
        test_it = zip(expect_it, found_it)

        for i, (expect, found) in enumerate(test_it):
            self.assertEqual(
                expect,
                found,
                f'잘못된 인덱스 : {i}'
            )
        # 두 제너레이터를 모두 소진했는지 검증
        try:
            next(expect_it)
        except StopIteration:
            pass
        else:  # except가 호출되지 않았을 경우 실행된다.
            self.fail('실제로 예상한 제너레이터가 더 깁니다.')

        try:
            next(found_it)
        except StopIteration:
            pass
        else:  # except가 호출되지 않았을 경우 실행된다.
            self.fail('예상한 제너레이터보다 실제가 더 깁니다.')

    def test_wrong_lengths(self):
        values = [1.1, 2.2, 3.3]
        expected = [
            1.1 ** 2,
        ]
        self.verify_complex_case(values, expected)

    def test_wrong_results(self):
        values = [1.1, 2.2, 3.3]
        expected = [
            1.1 ** 2,
            1.1 ** 2 + 2.2 ** 2,
            1.1 ** 2 + 2.2 ** 2 + 3.3 ** 2 + 4.4 ** 2,
        ]
        self.verify_complex_case(values, expected)


if __name__ == '__main__':
    main()
