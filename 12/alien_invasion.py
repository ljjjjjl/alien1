import sys
import pygame
from settings import Settings
from ship import Ship
from buulet import Bullet


class AlienInvasion:
    """"管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏斌创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        # 设置全屏
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            # 删除消失的子弹
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _check_events(self):
        """响应键盘和鼠标的事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # 松开时才停止移动
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按建"""
        if event.key == pygame.K_d:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            sys.exit()
        elif event.key == pygame.K_w:
            # fire开火
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并创建编组bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都会重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
