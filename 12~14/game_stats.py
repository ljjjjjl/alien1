import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 活跃状态
        self.game_active = False

        # 最高得分
        self.high_score = 0
        self.outdoc()

    def reset_stats(self):
        """初始化可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def outdoc(self):
        with open('score', 'r', encoding='utf-8') as f:
            doc = json.load(f)
            if doc:
                self.high_score = int(doc)

    def indoc(self):
        with open('score', 'w', encoding='utf-8') as f:
            json.dump(self.high_score, f)
