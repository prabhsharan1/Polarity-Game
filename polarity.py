import pygame
import sys
import random
import requests
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polarity Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
GOLD = (255, 215, 0)
BG_COLOR = (30, 30, 60)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Player setup
player_size = 50
player = pygame.Rect(100, HEIGHT - 100, player_size, player_size)
player_color = BLUE
player_speed = 5
player_polarity = "positive"

# Magnetic object setup
magnet_size = 50
magnets = []

# Collectibles setup
collectibles = []

# Goal setup
goal = pygame.Rect(WIDTH - 100, HEIGHT - 100, player_size, player_size)

# Game variables
running = True
won = False
score = 0
level = 1
max_level = 3
level_timer = 30  # Timer in seconds
start_ticks = pygame.time.get_ticks()  # To track elapsed time

# Download music and sound files from GitHub if not present locally
base_url = "https://raw.githubusercontent.com/prabhsharan1/RFM/main/"
files = {
    "party_music.mp3": "RFM%20No%20Copyright%20Party%20Song.mp3",
    "victory_sound.mp3": "Victory%20Sound%20Effect%20Version%20230553.mp3",
    "game_fail.mp3": "8%20Bit%20Game%20Fail%20Version%202.mp3",
}

for local_name, remote_name in files.items():
    if not os.path.exists(local_name):
        print(f"Downloading {local_name}...")
        response = requests.get(base_url + remote_name)
        with open(local_name, "wb") as file:
            file.write(response.content)

# Music and sounds
pygame.mixer.init()
try:
    # Load sounds
    pygame.mixer.music.load("party_music.mp3")  # Background music
    win_sound = pygame.mixer.Sound("victory_sound.mp3")  # Winning sound
    lose_sound = pygame.mixer.Sound("game_fail.mp3")  # Losing sound

    # Start background music (looping)
    pygame.mixer.music.play(loops=-1)
except pygame.error as e:
    print(f"Error loading music/sound: {e}")

def draw_text(text, x, y, color):
    """Helper function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def handle_magnetics(player, magnets, polarity):
    """Handle attraction and repulsion between the player and magnetic objects."""
    for magnet in magnets:
        magnet_rect = magnet["rect"]
        magnet_polarity = magnet["polarity"]

        # Calculate the direction of the force
        dx = magnet_rect.centerx - player.centerx
        dy = magnet_rect.centery - player.centery
        distance = max((dx**2 + dy**2)**0.5, 1)  # Avoid division by zero
        force = 5 / distance  # Force decreases with distance

        # Apply attraction or repulsion
        if magnet_polarity == polarity:
            player.x -= int(force * dx)
            player.y -= int(force * dy)
        else:
            player.x += int(force * dx)
            player.y += int(force * dy)

def initialize_level(level):
    """Initialize magnets and collectibles for the current level."""
    global magnets, collectibles, player_speed, level_timer
    magnets = [
        {"rect": pygame.Rect(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), magnet_size, magnet_size),
         "polarity": random.choice(["positive", "negative"])}
        for _ in range(level * 3)  # Increase magnets with each level
    ]
    collectibles = [
        pygame.Rect(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), 20, 20)
        for _ in range(5 + level * 2)  # More collectibles with each level
    ]
    player_speed = 5 + level  # Increase speed as levels progress
    level_timer = 30 - (level * 5)  # Decrease time as levels progress

# Initialize the first level
initialize_level(level)

# Main game loop
while running:
    screen.fill(BG_COLOR)

    # Calculate remaining time
    seconds = level_timer - (pygame.time.get_ticks() - start_ticks) // 1000

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Switch polarity
    if keys[pygame.K_SPACE]:
        if player_polarity == "positive":
            player_polarity = "negative"
            player_color = RED
        else:
            player_polarity = "positive"
            player_color = BLUE

    # Handle magnetic forces
    handle_magnetics(player, magnets, player_polarity)

    # Check for victory
    if player.colliderect(goal) and not collectibles:
        if level < max_level:
            level += 1
            start_ticks = pygame.time.get_ticks()  # Reset timer
            initialize_level(level)  # Load next level
        else:
            won = True
            running = False

    # Collect collectibles
    for collectible in collectibles[:]:
        if player.colliderect(collectible):
            collectibles.remove(collectible)
            score += 10

    # Draw background elements
    pygame.draw.rect(screen, GRAY, goal)

    # Draw magnets
    for magnet in magnets:
        color = RED if magnet["polarity"] == "positive" else BLUE
        pygame.draw.rect(screen, color, magnet["rect"])

    # Draw collectibles
    for collectible in collectibles:
        pygame.draw.circle(screen, GOLD, collectible.center, collectible.width // 2)

    # Draw player
    pygame.draw.rect(screen, player_color, player)

    # Draw UI
    draw_text(f"Score: {score}", 10, 10, WHITE)
    draw_text(f"Polarity: {player_polarity.capitalize()}", 10, 40, WHITE)
    draw_text(f"Level: {level}", 10, 70, WHITE)
    draw_text(f"Time Left: {seconds}s", 10, 100, WHITE)

    # Check if time is up
    if seconds <= 0:
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# End screen
pygame.mixer.music.stop()  # Stop background music
if won:
    win_sound.play()  # Play winning sound
    screen.fill(BG_COLOR)
    draw_text("You Win!", WIDTH // 2 - 50, HEIGHT // 2 - 20, WHITE)
else:
    lose_sound.play()  # Play losing sound
    screen.fill(BG_COLOR)
    draw_text("Time's Up! Game Over!", WIDTH // 2 - 120, HEIGHT // 2 - 20, RED)
draw_text(f"Final Score: {score}", WIDTH // 2 - 70, HEIGHT // 2 + 20, WHITE)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()