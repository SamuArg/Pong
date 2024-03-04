import pygame

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

def draw(player1,player2):
    WIN.fill("black")
    pygame.draw.rect(WIN, PLAYERS_COLOR, player1)
    pygame.draw.rect(WIN,PLAYERS_COLOR, player2)
    pygame.draw.circle(WIN, BALL_COLOR, (WIDTH//2,HEIGHT//2), radius=BALL_WIDTH)
    pygame.display.update()

def main():
    run = True
    player1 = pygame.Rect(0,HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    player2 = pygame.Rect(WIDTH-PLAYERS_WIDTH, HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    draw(player1, player2)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
main()