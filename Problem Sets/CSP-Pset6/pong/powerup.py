from settings import *
import pygame
import random

class PowerUp:
    def __init__(self, power_type, num):
        self.power_type = power_type
        self.surf = pygame.Surface((POWER_SIZE, POWER_SIZE))
        self.rect = self.surf.get_rect()
        self.num = num
        self.color = WHITE
        self.applied = False
        self.visible = False
        self.time_remaining = POWER_SPAWN_LEN
        self.prev_val = None

        self._set_color(power_type)
        self.surf.fill(self.color)
        self.rect.center = (-1, -1)

    def draw(self, screen, dt):
        print(self.time_remaining) if self.applied else None
        self.time_remaining -= dt
        if self.rect.center == (-1, -1):
            self._set_pos()
        if self.visible:
            screen.blit(self.surf, self.rect)

    def _set_color(self, power_type):
        if power_type == "ball_speed_mul":
            self.color = RED
        elif power_type == "paddle_size":
            self.color = ORANGE
        elif power_type == "paddle_speed":
            self.color = YELLOW

    def _set_pos(self):
        x_pos = int(random.uniform(POWER_X_OFFSET, SCREEN_WIDTH - POWER_X_OFFSET))
        y_pos = int(random.uniform(POWER_Y_OFFSET, SCREEN_HEIGHT - POWER_Y_OFFSET))
        self.rect.center = (x_pos, y_pos)

    def apply(self, ball, paddles):
        self.applied = True
        self.visible = False
        self.time_remaining = POWER_APPLIED_LEN
        if self.power_type == "ball_speed_mul":
            self.prev_val = ball.speed.copy()
            ball.speed[0] *= self.num
            ball.speed[1] *= self.num
        if self.power_type == "paddle_size":
            pidx = 0 if ball.speed[0] > 0 else 1
            oldrect = paddles[pidx].rect.copy()
            paddles[pidx].surf = pygame.transform.scale(paddles[pidx].surf, (PADDLE_WIDTH, PADDLE_HEIGHT * self.num))
            paddles[pidx].rect = paddles[pidx].surf.get_rect()
            paddles[pidx].rect.center = (30, oldrect.centery) if paddles[pidx].playernum == 1 else (SCREEN_WIDTH - 30, oldrect.centery)
            self.prev_val = "player1" if pidx == 0 else "player2"

        if self.power_type == "paddle_speed":
            if ball.speed[0] > 0:
                self.prev_val = "player1"
                paddles[0].speed *= self.num
            elif ball.speed[0] < 0:
                self.prev_val = "player2"
                paddles[1].speed *= self.num
        self._set_pos()
        return ball, paddles

    def remove(self, ball, paddles, reset=False):
        if reset:
            self._set_pos()
        if self.applied and (self.time_remaining <= 0 or reset):
            self.applied = False
            if self.power_type == "ball_speed_mul":
                if abs(ball.speed[0]) == ball.speed[0] and abs(ball.speed[1]) == ball.speed[1]:
                    ball.set_speed(abs(self.prev_val[0]), abs(self.prev_val[1]))
                elif -abs(ball.speed[0]) == ball.speed[0] and abs(ball.speed[1]) == ball.speed[1]:
                    ball.set_speed(-abs(self.prev_val[0]), abs(self.prev_val[1]))
                elif abs(ball.speed[0]) == ball.speed[0] and -abs(ball.speed[1]) == ball.speed[1]:
                    ball.set_speed(abs(self.prev_val[0]), -abs(self.prev_val[1]))
                elif -abs(ball.speed[0]) == ball.speed[0] and -abs(ball.speed[1]) == ball.speed[1]:
                    ball.set_speed(-abs(self.prev_val[0]), -abs(self.prev_val[1]))

            if self.power_type == "paddle_size":
                paddles[0].reset_size() if self.prev_val == "player1" else paddles[1].reset_size()
            if self.power_type == "paddle_speed":
                paddles[0].reset_speed() if self.prev_val == "player1" else paddles[1].reset_size()

            return [ball, paddles]
        return None

def use_powerup(active):
    if len(active) >= 3:
        return False
    return True if random.choice(POWERUP_CHANCE) == 69 else False