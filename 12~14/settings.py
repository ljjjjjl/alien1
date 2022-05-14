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
