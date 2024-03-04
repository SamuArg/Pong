import pygame
import random
pygame.font.init()

WIDTH = 1000
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

PLAYERS_HEIGHT = 100
PLAYERS_WIDTH = 10
BALL_WIDTH = 10
PLAYERS_VEL = 5
BALL_VEL = 5
PLAYERS_COLOR = "white"
BALL_COLOR = "white"
FONT = pygame.font.SysFont("comicsans", 30)
DEFAULT_SCORE = (0,0)

def draw(player1,player2, ball_position, score):
    WIN.fill("black")
    pygame.draw.rect(WIN, PLAYERS_COLOR, player1)
    pygame.draw.rect(WIN,PLAYERS_COLOR, player2)
    ball = pygame.draw.circle(WIN, BALL_COLOR,ball_position, radius=BALL_WIDTH)
    text = FONT.render(f"{score[0]} - {score[1]}", 1 , "white")
    text_width = text.get_width()
    WIN.blit(text, (WIDTH//2 - text_width//2, 10))
    pygame.display.update()
    return ball

def main():
    run = True
    ball = Ball((BALL_VEL,0))
    clock = pygame.time.Clock()
    player1 = pygame.Rect(0,HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    player2 = pygame.Rect(WIDTH-PLAYERS_WIDTH, HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    ball_position = (WIDTH//2,HEIGHT//2)
    score = DEFAULT_SCORE
    ball_rect = draw(player1, player2, ball_position, score)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        handle_border_collision(ball_rect,ball)    
        ball_position = (ball_position[0]+ball.direction[0], ball_position[1]+ball.direction[1])

        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_UP] and player2.y - PLAYERS_VEL >= 0:
            player2.y -= PLAYERS_VEL
        if keys[pygame.K_DOWN] and player2.y + PLAYERS_VEL + PLAYERS_HEIGHT <= HEIGHT:
            player2.y += PLAYERS_VEL
        if keys[pygame.K_w] and player1.y - PLAYERS_VEL >= 0:
            player1.y -= PLAYERS_VEL
        if keys[pygame.K_s] and player1.y + PLAYERS_VEL + PLAYERS_HEIGHT <= HEIGHT:
            player1.y += PLAYERS_VEL
        
        if player1.colliderect(ball_rect):
            ball.direction = (1*BALL_VEL,random.random()*BALL_VEL)
        if player2.colliderect(ball_rect):
            ball.direction = (-1*BALL_VEL, random.random()*BALL_VEL)
        
        if ball_rect.x + 2*BALL_WIDTH <= 0:
            score = (score[0], score[1] + 1)
            ball_position = (WIDTH//2, HEIGHT//2)
            ball.direction = (-BALL_VEL,0)
        if ball_rect.x >= WIDTH:
            score = (score[0] + 1, score[1])
            ball_position = (WIDTH//2, HEIGHT//2)
            ball.direction = (BALL_VEL,0)
        if score[0] == 7:
            end("Player 1")
        if score[1] == 7:
            end("Player 2")
        ball_rect = draw(player1, player2, ball_position, score)
    pygame.quit()


def handle_border_collision(ball_rect, ball):
    if ball_rect.y - BALL_VEL <= 0:
        ball_rect.y += 2*BALL_WIDTH
        ball.direction = (ball.direction[0], -ball.direction[1])
    elif ball_rect.y + 2*BALL_WIDTH + BALL_VEL >= HEIGHT:
        ball_rect.y -= 2*BALL_WIDTH
        ball.direction = (ball.direction[0], -ball.direction[1])

def end(winning_player):
    text = FONT.render(winning_player + " won !",1, "white")
    WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 -text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(4000)
    main()

class Ball:
    def __init__(self, direction):
        self.direction = direction

if __name__ == "__main__":
    main()