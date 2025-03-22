from utils.config import *

class LoserState:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.scroll_speed = SCROLL_SPEED
        self.animation_time = SCROLL_SPEED / SCROLL_SPEED_SLOWER
        self.initial_list = ['A', 'A']
        self.sel_idx = 0
        self.font_size = 60
        self.dt = 0

    def update(self, dt):
        self.dt = dt

        if self.scroll_speed > 0:
            self.scroll_speed -= SCROLL_SPEED_SLOWER
        else:
            self.scroll_speed = 0
        self.state_machine.background_pos -= (self.scroll_speed * (dt // 5))
        if self.state_machine.background_pos <= -self.state_machine.background.width:
            self.state_machine.background_pos += self.state_machine.background.width

        if self.animation_time > 0:
            self.animation_time -= SCROLL_SPEED_SLOWER * dt * 4
            self.state_machine.bird1.update(dt, set())
            if self.state_machine.bird2:
                self.state_machine.bird2.update(dt, set())

        if self.animation_time < 0:
            if pygame.K_DOWN in self.state_machine.keysdown:
                new_letter = (ord(self.initial_list[self.sel_idx]) - 65 + 1) % 26 + 65
                self.initial_list[self.sel_idx] = chr(new_letter)
            elif pygame.K_UP in self.state_machine.keysdown:
                new_letter = (ord(self.initial_list[self.sel_idx]) - 65 - 1) % 26 + 65
                self.initial_list[self.sel_idx] = chr(new_letter)
            elif pygame.K_LEFT in self.state_machine.keysdown:
                new_idx = self.sel_idx - 1
                if new_idx < 0:
                    new_idx = 0
                self.sel_idx = new_idx
            elif pygame.K_RIGHT in self.state_machine.keysdown:
                new_idx = self.sel_idx + 1
                if new_idx > len(self.initial_list) - 1:
                    new_idx = len(self.initial_list) - 1
                self.sel_idx = new_idx

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        if self.animation_time > 0:
            for pipe in self.state_machine.pipe_list:
                pipe.draw(self.state_machine.screen)

            self.state_machine.bird1.draw(self.state_machine.screen)
            if self.state_machine.bird2:
                self.state_machine.bird2.draw(self.state_machine.screen)

        if self.animation_time > 0 and self.font_size < 120: self.font_size += self.dt / 15

        self.state_machine.font.set_color(WHITE)
        self.state_machine.font.set_size(int(self.font_size))
        self.state_machine.font.print(self.state_machine.screen, f"{self.state_machine.bird1.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8)

        if self.animation_time < 0:
            self.state_machine.font.set_size(30)

            self.state_machine.font.print(self.state_machine.screen, f"Enter Your Initials", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)
            self.state_machine.font.print(self.state_machine.screen, f"Press Return to Continue", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5)

            for initial in range(len(self.initial_list)):
                self.state_machine.font.set_size(180)
                if self.sel_idx == initial:
                    self.state_machine.font.set_color(BLUE)
                else:
                    self.state_machine.font.set_color(WHITE)

                if initial == 0:
                    self.state_machine.font.print(self.state_machine.screen, f"{self.initial_list[initial]}", SCREEN_WIDTH // 3, SCREEN_HEIGHT - SCREEN_HEIGHT // 3)
                elif initial == 1:
                    self.state_machine.font.print(self.state_machine.screen, f"{self.initial_list[initial]}", SCREEN_WIDTH - SCREEN_WIDTH // 3, SCREEN_HEIGHT - SCREEN_HEIGHT // 3)
