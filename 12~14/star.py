import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """"星星类"""
    def __init__(self, ai_game):
        """初始化星星并设置位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载星星图像并设置rect属性
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 定位到精确位置
        self.x = float(self.rect.x)
