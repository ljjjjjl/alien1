import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类"""

    def __init__(self, ai_game):
        """初始化外星人并设置位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 定位到精确位置
        self.x = float(self.rect.x)
