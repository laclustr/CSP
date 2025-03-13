from settings import *
import pygame
import random

class PowerUp:
    def __init__(self, power_type, num):
        self.power_type = power_type
        self.surf = pygame.Surface((POWER_SIZE, POWER_SIZE))
        self.rect = self.surf.get_rect()
        self.num = num
        self.speed_mul = num if power_type == "ball_speed_mul" else None
        self.paddle_size = num if power_type == "paddle_size" else None
        self.paddle_speed = num if power_type == "paddle_speed" else None
        self.color = WHITE
        self.applied = False
        self.visible = False
        self.time_remaining = 5000
        self.prev_val = None

        self._set_color(power_type)
        self.surf.fill(self.color)
        self.rect.center = (-1, -1)

    def draw(self, screen, dt):
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
        if self.power_type == "ball_speed_mul":
            self.prev_val = ball.speed.copy()
            ball.speed[0] *= self.speed_mul
            ball.speed[1] *= self.speed_mul
        if self.power_type == "paddle_size":
            if ball.speed[0] > 0:
                self.prev_val = [paddles[0].rect.copy(), paddles[0].surf.copy(), True]
                paddles[0].surf = pygame.transform.scale(paddles[0].surf, (PADDLE_WIDTH, PADDLE_HEIGHT * self.paddle_size))
                paddles[0].rect = paddles[0].surf.get_rect()
                paddles[0].rect.center = (30, self.prev_val[0].center[1])
            elif ball.speed[0] < 0:
                self.prev_val = [paddles[1].rect.copy(), paddles[1].surf.copy(), False]
                paddles[1].surf = pygame.transform.scale(paddles[1].surf, (PADDLE_WIDTH, PADDLE_HEIGHT * self.paddle_size))
                paddles[1].rect = paddles[1].surf.get_rect()
                paddles[1].rect.center = (SCREEN_WIDTH - 30, self.prev_val[0].center[1])

        if self.power_type == "paddle_speed":
            if ball.speed[0] > 0:
                self.prev_val = [paddles[0].speed, True]
                paddles[0].speed *= self.paddle_speed
            elif ball.speed[0] < 0:
                self.prev_val = [paddles[1].speed, False]
                paddles[1].speed *= self.paddle_speed
        self._set_pos()
        return [ball, paddles]

    def remove(self, ball, paddles, reset=False):
        if reset:
            self._set_pos()
        if self.applied and (self.time_remaining <= 0 or reset):
            self.applied = False
            if self.power_type == "ball_speed_mul":
                ball.speed = self.prev_val
            if self.power_type == "paddle_size":
                if self.prev_val[2]:
                    player_cy = paddles[0].rect.center[1]
                    paddles[0].surf = self.prev_val[1]
                    paddles[0].rect = self.prev_val[0]
                    paddles[0].rect.center = (30, player_cy)
                else:
                    player2_cy = paddles[1].rect.center[1]
                    paddles[1].surf = self.prev_val[1]
                    paddles[1].rect = self.prev_val[0]
                    paddles[1].rect.center = (SCREEN_WIDTH - 30, player2_cy)
            if self.power_type == "paddle_speed":
                if self.prev_val[1]:
                    paddles[0].speed = self.prev_val[0]
                elif not self.prev_val[1]:
                    paddles[1].speed = self.prev_val[0]

            return [ball, paddles]
        return None

def use_powerup(active):
    if len(active) >= 3:
        return False
    return True if random.choice(POWERUP_CHANCE) == 69 else False