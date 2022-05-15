class Settings:
    """"存储游戏中所以设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (100, 150, 200)
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 35
        self.bullet_color = (60, 60, 60)
        # 子弹数量
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction -1代表左移 1代表右移
        self.fleet_direction = 1

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # 记分
        self.alien_points = 10

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction -1左 1右
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度,提高外星人的分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # 外星人的分数
        self.alien_points = int(self.alien_points * self.score_scale)
