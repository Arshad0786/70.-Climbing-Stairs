import unittest
from ClimbingStairs import Solution


class ClimbingStairsTest(unittest.TestCase):
    def test_example_1(self):
        temp = Solution()
        self.input = 2
        self.assertEqual(temp.climbStairs(self.input), 2)
    
    def test_example_2(self):
        temp = Solution()
        self.input = 3
        self.assertEqual(temp.climbStairs(self.input), 3)

    def test_example_3(self):
        temp = Solution()
        self.input = 4
        self.assertEqual(temp.climbStairs(self.input), 5)

    def test_example_4(self):
        temp = Solution()
        self.input = 5
        self.assertEqual(temp.climbStairs(self.input), 8)

    def test_example_5(self):
        temp = Solution()
        self.input = 6
        self.assertEqual(temp.climbStairs(self.input), 13)

    def test_example_6(self):
        temp = Solution()
        self.input = 7
        self.assertEqual(temp.climbStairs(self.input), 21)

    def test_example_20(self):
        temp = Solution()
        self.input = 8
        self.assertEqual(temp.climbStairs(self.input), 34)
    

if __name__ == "__main__":
    unittest.main()
