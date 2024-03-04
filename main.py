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

def draw(player1,player2, ball_position):
    WIN.fill("black")
    pygame.draw.rect(WIN, PLAYERS_COLOR, player1)
    pygame.draw.rect(WIN,PLAYERS_COLOR, player2)
    pygame.draw.circle(WIN, BALL_COLOR, ball_position, radius=BALL_WIDTH)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    player1 = pygame.Rect(0,HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    player2 = pygame.Rect(WIDTH-PLAYERS_WIDTH, HEIGHT//2-PLAYERS_HEIGHT//2, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    ball_position = (WIDTH//2,HEIGHT//2)
    draw(player1, player2, ball_position)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_UP] and player2.y - PLAYERS_VEL >= 0:
            player2.y -= PLAYERS_VEL
        if keys[pygame.K_DOWN] and player2.y + PLAYERS_VEL + PLAYERS_HEIGHT <= HEIGHT:
            player2.y += PLAYERS_VEL
        if keys[pygame.K_w] and player1.y - PLAYERS_VEL >= 0:
            player1.y -= PLAYERS_VEL
        if keys[pygame.K_s] and player1.y + PLAYERS_VEL + PLAYERS_HEIGHT <= HEIGHT:
            player1.y += PLAYERS_VEL
        

        draw(player1, player2, ball_position)

if __name__ == "__main__":
    main()