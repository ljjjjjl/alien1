import sys
import pygame


class AlienInvasion:
    """"管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏斌创建游戏资源"""
        pygame.init()

        # 设置背景色
        self.bg_color = (100, 150, 200)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘和鼠标的事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都会重绘屏幕
            self.screen.fill(self.bg_color)
            # 让最近绘制屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
