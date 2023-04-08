import pygame
import game

# Set window
WIN = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
pygame.display.set_caption("Flappy Bird")

def main():
    bird = game.Bird(WIN)
    pipes = [game.Pipe(400, WIN), game.Pipe(600, WIN), game.Pipe(800, WIN)]

    clock = pygame.time.Clock()

    score = 0

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()

        for pipe in pipes:
            pipe.update()
            if pipe.offscreen():
                pipes.remove(pipe)
                pipes.append(game.Pipe(550, WIN))
            if pipe.collide_with(bird):
                run = False
        
        WIN.blit(game.background_image, (0,0))

        for pipe in pipes:
            pipe.draw(WIN)

        bird.draw(WIN)

        score += 1
        text = game.font.render("Score: " + str(score // 10), True, game.WHITE)
        WIN.blit(text, (5,5))

        pygame.display.update()

        clock.tick(60)

    if run == False:
        pygame.quit()

if __name__ == "__main__":
    main()