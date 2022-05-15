import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_game):
        """创建子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # # 在 (0, 0) 创建一个子弹矩形，再设置正确位置
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        #                         self.settings.bullet_height)
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # 用float存储子弹位置
        self.y = float(self.rect.y)
        self.xl = float(self.rect.x)
        self.xr = float(self.rect.x)

    def update(self):
        """向上移动子弹"""
        # 更新float
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def update_left(self):
        """向左移动子弹"""
        # 更新float
        self.xl -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.x = self.xl

    def update_right(self):
        """向右移动子弹"""
        # 更新float
        self.xr -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.x = self.xr

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
