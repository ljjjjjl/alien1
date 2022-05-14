class Settings:
    """"存储游戏中所以设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (100, 150, 200)
        self.bg_color = (200, 200, 200)

        # 飞船速度
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 子弹数量
        self.bullets_allowed = 2
