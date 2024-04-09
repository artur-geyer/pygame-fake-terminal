import sys

import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Fake Terminal")

# Set up fonts
font = pygame.font.Font(None, 32)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Terminal variables
cursorX = 10
cursorY = 10
inputText = ""

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                inputText = inputText[:-1]
            elif event.key == pygame.K_RETURN:
                # Handle input
                print("User input:", inputText)
                inputText = ""
            else:
                inputText += event.unicode

    # Clear the screen
    screen.fill(black)

    # Draw fake terminal window
    pygame.draw.rect(screen, white, (10, 10, screenWidth - 20, screenHeight - 20), 2)

    # Draw input text
    inputSurface = font.render("> " + inputText, True, white)
    screen.blit(inputSurface, (cursorX, cursorY))

    # Draw cursor
    cursorSurface = font.render("_", True, white)
    cursorPosition = font.size("> " + inputText)[:2]
    screen.blit(cursorSurface, (cursorX + cursorPosition[0], cursorY))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
