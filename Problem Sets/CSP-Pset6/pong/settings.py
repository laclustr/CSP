import pygame
pygame.mixer.init()

# BALL
BALL_SIZE      = 12
BALL_SPEED_X   = 0.2
BALL_SPEED_Y   = 0.2
BALL_RAND_SPEED_X = 0.12
BALL_RAND_SPEED_Y = 0.2
SPEED_INCREASE = 0.05
MAX_BALL_SPEED = 3
WIN_POINTS = 5

# AI
AI_THRESHOLD = 2
AI_SMOOTHER = 0.7

# SOUNDS
PADDLE_SOUND = pygame.Sound("sounds/paddle_hit.wav")
SCORE_SOUND  = pygame.Sound("sounds/score.wav")
WALL_SOUND   = pygame.Sound("sounds/wall_hit.wav")

# COLORS
GRAY  = (44, 44, 44)
WHITE = (255, 255, 255)
BLUE  = (120, 120, 255)

# FONT
SM_FONT_SIZE  = 12
MED_FONT_SIZE = 24
LG_FONT_SIZE  = 64

# PADDLE
PADDLE_WIDTH  = 12
PADDLE_HEIGHT = 84
PADDLE_SPEED  = 0.75

# SCREEN
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600