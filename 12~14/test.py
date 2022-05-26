import unittest
from unittest.mock import Mock

from game_stats import GameStats
from scoreboard import Scoreboard


class TestFile(unittest.TestCase):
    """测试读写最高分如文件的类"""

    def setUp(self):
        # 初始化GameStatus类需要传入AlienInvasion对象，用Mock类进行模拟
        mock = Mock()
        self.gameStats = GameStats(mock)
        # self.scoreboard = Scoreboard(mock)

    def test_write_score(self):
        """测试文件写入，看文件中是否正确写入"""
        self.gameStats.high_score = 1000
        self.gameStats.indoc()

    def test_read_score(self):
        """测试从文件中读取最高分的方法"""
        self.gameStats.outdoc()
        score = self.gameStats.high_score
        # 判断从读取的值是否是文件中的预期值
        self.assertEqual(1000, score)


if __name__ == "__main__":
    unittest.main()
