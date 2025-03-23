from utils.config import *
import json
import pygame

class HighScoreState:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        with open("high_scores.json", "r") as f:
            self.top3 = sorted(json.load(f), key=lambda score: score['score'], reverse=True)[:3]

    def update(self, dt):
        if pygame.K_RETURN in self.state_machine.keysdown:
            self.state_machine.change_state("menu")

    def draw(self):
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos, 0))
        self.state_machine.screen.blit(self.state_machine.background, (self.state_machine.background_pos + self.state_machine.background.width, 0))

        self.state_machine.font.set_color(WHITE)
        self.state_machine.font.set_size(60)
        for score in range(len(self.top3)):
            self.state_machine.font.print(
                self.state_machine.screen,
                f"{self.top3[score]["initials"]}: {self.top3[score]["score"]}",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 4 + score * self.state_machine.font.get_size()
            )
            if score == 0:
                medal = pygame.image.load("assets/sprites/medals/shaded_medal1.png").convert()
            elif score == 1:
                medal = pygame.image.load("assets/sprites/medals/shaded_medal2.png").convert()
            else:
                medal = pygame.image.load("assets/sprites/medals/shaded_medal3.png").convert()
            medal = pygame.transform.scale_by(medal, 0.6)
            rect = medal.get_rect()
            rect.centery = (SCREEN_HEIGHT // 4 + score * self.state_machine.font.get_size()) - 2
            rect.centerx = (SCREEN_WIDTH // 2) - (len(f"{self.top3[score]["initials"]}:{self.top3[score]["score"]}") // 2) * self.state_machine.font.get_size()
            self.state_machine.screen.blit(medal, rect)



        self.state_machine.font.set_size(35)
        self.state_machine.font.print(
            self.state_machine.screen,
            f"Press Return to Continue",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - SCREEN_HEIGHT // 8
        )




