import unittest
from math_quiz import generate_random_integer, generate_random_operator, generate_expression


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if random operator generated is one of the expected operators
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])
        pass

    def test_generate_expression(self):
            test_cases = [
                (5, 4, '+', '5 + 4', 9),
                (6, 3, '*', '6 * 3', 18),
                (9, 3, '-', '9 - 3', 6)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_expression(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
