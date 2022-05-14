import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕的底中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """根据移动标志飞船位置"""
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
