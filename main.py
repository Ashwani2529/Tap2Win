import pygame
import random

def main():
    # Initialize Pygame
    pygame.init()
    # Set up the game window
    screen = pygame.display.set_mode((600, 600))
    # Create the objects to tap
    box_width = screen.get_width() // 2.2
    box_height = screen.get_height() // 2.2
    red_object_rect = pygame.Rect(screen.get_width() // 4 - box_width // 2,
                                  screen.get_height() // 4 - box_height // 2,
                                  box_width,
                                  box_height)
    red_object_color = (255, 0, 0)
    blue_object_rect = pygame.Rect(screen.get_width() // 4 - box_width // 2 + 150,
                                    screen.get_height() // 4 - box_height // 2 + 150,
                                    box_width,
                                    box_height)
    blue_object_color = (0, 0, 255)
    # Set up the game score and timer
    player1_score = 0
    player2_score = 0
    timer = 40.0
    score_font = pygame.font.SysFont("Bold", 64)

    # Create the reset button
    reset_button_rect = pygame.Rect(screen.get_width() - 88, screen.get_height() - 52, 90, 48)
    reset_button_color = (0, 255, 0)
    reset_font = pygame.font.SysFont("Bold", 40)
    reset_text = reset_font.render("Reset", True, (0, 0, 0))
    def reset_game():
        nonlocal player1_score, player2_score, timer
        player1_score = 0
        player2_score = 0
        timer = 40.0
    # Create the restart button
    restartb_rect= pygame.Rect(screen.get_width() - 101, screen.get_height() -82, 89, 28)
    restartb_color = (23,243, 165)
    restartb_font = pygame.font.SysFont("Bold", 40)
    restartb_text = reset_font.render("Restart", True, (0, 0, 50))
    def restart_game():
        pygame.display.update()
        # main()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_button_rect.collidepoint(event.pos):
                        reset_game()
                        return
                    elif restartb_rect.collidepoint(event.pos):
                        return
  # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the red object was tapped by player 1
                if red_object_rect.collidepoint(event.pos):
                    player1_score += 1
                # Check if the blue object was tapped by player 2
                elif blue_object_rect.collidepoint(event.pos):
                    player2_score += 1
                # Check if the reset button was clicked
                elif reset_button_rect.collidepoint(event.pos):
                    reset_game()
                # Check if the restart button was clicked
                elif restartb_rect.collidepoint(event.pos):
                    restart_game()

        # Update the positions of the objects every 60 frames
        if pygame.time.get_ticks() % 60 == 0:
            red_object_rect.move_ip(random.randint(-100, 100), random.randint(-100, 100))
            blue_object_rect.move_ip(random.randint(-100, 100), random.randint(-100, 100))
        # Ensure that the red and blue objects don't overlap
        if red_object_rect.colliderect(blue_object_rect):
            red_object_rect.move_ip(random.randint(50, 100), random.randint(50, 100))
            blue_object_rect.move_ip(random.randint(-100, -50), random.randint(-100, -50))
        red_object_rect.clamp_ip(screen.get_rect())
        blue_object_rect.clamp_ip(screen.get_rect())
        # Draw the objects and scores on the screen
        screen.fill((255, 215, 163))
        pygame.draw.rect(screen, red_object_color, red_object_rect)
        pygame.draw.rect(screen, blue_object_color, blue_object_rect)
        player1_score_text = score_font.render(f"RED Score: {player1_score}", True, (0, 0, 0))
        screen.blit(player1_score_text, (250, 32))
        player2_score_text = score_font.render(f"BLUE Score: {player2_score}", True, (0, 0, 0))
        screen.blit(player2_score_text, (600, 32))
        # Draw the reset button on the screen
        pygame.draw.rect(screen, reset_button_color, reset_button_rect)
        screen.blit(reset_text, (screen.get_width() - 75, screen.get_height() - 35))
        
        # Draw the restart button on the screen
        pygame.draw.rect(screen, restartb_color, restartb_rect)
        screen.blit(restartb_text, (screen.get_width() -101, screen.get_height() - 87))
    
        # Update the timer and end the game if time is up
        timer -= 1 / 60
        if timer <= 0:
            running = False
        # Update the display
        pygame.display.update()
# Display the winner
    winner = "RED" if player1_score > player2_score else "BLUE" if player2_score > player1_score else "TIE"
    winner_text = score_font.render(f"Winner: {winner}", True, (130, 43, 171))
    screen.blit(winner_text, (375, 1960))
    pygame.display.update()
    
    # Add delay and reset the game
    pygame.time.delay(5000)  # Wait for 5 seconds
    reset_game()
    
    # Loop to wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicked mouse, exit loop
                return

main()
