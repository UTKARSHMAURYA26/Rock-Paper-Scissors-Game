import pygame
import random
import sys

# Constants for choices
ROCK, PAPER, SCISSORS = 1, 2, 3

# Initialize pygame
pygame.init()

# Create the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Game")

# Load images (customize these)
rock_image = pygame.image.load('rock.png')
paper_image = pygame.image.load('paper.png')
scissors_image = pygame.image.load('scissors.png')

# Define player and enemy choices
player_choice = None
enemy_choice = None

# Game state variables
game_active = False
result_text = ""
score = 0

# Fonts and text
font = pygame.font.Font(None, 36)

def display_message(message):
    text = font.render(message, True, (255, 255, 255))
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)

def get_enemy_choice():
    return random.choice([ROCK, PAPER, SCISSORS])

def draw_images():
    image_dict = {ROCK: rock_image, PAPER: paper_image, SCISSORS: scissors_image}
    player_image = image_dict.get(player_choice)
    enemy_image = image_dict.get(enemy_choice)
    if player_image and enemy_image:
        window.blit(player_image, (100, 100))
        window.blit(enemy_image, (500, 100))

def main():
    global game_active, player_choice, enemy_choice, result_text, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_active:
                if 100 < event.pos[0] < 300:
                    player_choice = ROCK
                elif 300 < event.pos[0] < 500:
                    player_choice = PAPER
                elif 500 < event.pos[0] < 700:
                    player_choice = SCISSORS
                game_active = True

        if game_active:
            enemy_choice = get_enemy_choice()

            if player_choice == enemy_choice:
                result_text = "It's a tie!"
            elif (player_choice == ROCK and enemy_choice == SCISSORS) or \
                 (player_choice == PAPER and enemy_choice == ROCK) or \
                 (player_choice == SCISSORS and enemy_choice == PAPER):
                result_text = "You win!"
                score += 1
            else:
                result_text = "Computer wins!"

        window.fill((0, 0, 0))
        draw_images()
        
        if game_active:
            display_message(result_text)
            game_active = False
            player_choice = None
        else:
            display_message("Click to choose.")
        
        pygame.display.update()

if __name__ == "__main__":
    main()
