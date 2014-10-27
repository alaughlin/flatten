import unittest
import flatten as F

class FlattenTests(unittest.TestCase):
  def test_one_dimensional(self):
    self.assertEqual(F.flatten([1,2,3]), [1,2,3])

  def test_two_dimensional(self):
    self.assertEqual(F.flatten([[1, 2, 3], [6, 2 ,1]]), [1, 2, 3, 6, 2, 1])

  def test_multi_dimensional(self):
    self.assertEqual(F.flatten([[1, 3, 4], [1, [8, 9]]]), [1, 3, 4, 1, 8, 9])

if __name__ == "__main__":
  unittest.main()