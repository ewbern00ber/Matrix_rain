import random
import math

# Matrix characters pool
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+-=[]{}|;:,.<>?/"

# Configuration
COLUMN_WIDTH = 8
NUM_COLUMNS = screen.width // COLUMN_WIDTH  # 40 columns on 320px width
CHAR_HEIGHT = 8
MAX_TRAIL_LENGTH = 25

# Matrix green colors - various intensities
BRIGHT_GREEN = color.rgb(200, 255, 200)
GREEN_1 = color.rgb(150, 255, 150)
GREEN_2 = color.rgb(100, 200, 100)
GREEN_3 = color.rgb(50, 150, 50)
GREEN_4 = color.rgb(25, 100, 25)
GREEN_5 = color.rgb(10, 50, 10)
BLACK = color.rgb(0, 0, 0)

# Rain drop class
class RainDrop:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-20, 0)
        self.speed = random.uniform(0.5, 2.0)
        self.trail_length = random.randint(10, MAX_TRAIL_LENGTH)
        self.chars = [random.choice(CHARS) for _ in range(self.trail_length)]
        self.change_interval = random.randint(5, 15)
        self.frame_count = 0
        
    def update(self):
        self.y += self.speed
        self.frame_count += 1
        
        # Randomly change characters in the trail
        if self.frame_count >= self.change_interval:
            self.frame_count = 0
            # Change a few random characters
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(self.chars) - 1)
                self.chars[idx] = random.choice(CHARS)
        
        # Reset when off screen
        if self.y > screen.height + (self.trail_length * CHAR_HEIGHT):
            self.y = random.randint(-50, -10)
            self.speed = random.uniform(0.5, 2.0)
            self.trail_length = random.randint(10, MAX_TRAIL_LENGTH)
            self.chars = [random.choice(CHARS) for _ in range(self.trail_length)]
    
    def draw(self):
        for i in range(len(self.chars)):
            char_y = int(self.y - (i * CHAR_HEIGHT))
            
            # Only draw if on screen
            if 0 <= char_y < screen.height:
                # Color gradient - brightest at head, fading to dark at tail
                if i == 0:
                    screen.pen = BRIGHT_GREEN  # Brightest white-green at head
                elif i == 1:
                    screen.pen = GREEN_1
                elif i <= 3:
                    screen.pen = GREEN_2
                elif i <= 6:
                    screen.pen = GREEN_3
                elif i <= 10:
                    screen.pen = GREEN_4
                else:
                    screen.pen = GREEN_5
                
                screen.text(self.chars[i], self.x * COLUMN_WIDTH + 1, char_y)

# Initialize raindrops
raindrops = []

# Settings for different modes
current_mode = 0
MODES = ["Classic", "Intense", "Slow Mo", "Chaos"]
mode_colors = [
    color.rgb(0, 255, 0),    # Classic green
    color.rgb(255, 0, 0),    # Intense red
    color.rgb(0, 150, 255),  # Slow cyan
    color.rgb(255, 0, 255)   # Chaos purple
]

def init():
    global raindrops
    # Create initial raindrops for each column
    raindrops = []
    for col in range(NUM_COLUMNS):
        drop = RainDrop(col)
        drop.y = random.randint(-screen.height, 0)  # Stagger initial positions
        raindrops.append(drop)
    
    # Set font
    screen.font = rom_font.nope

def update():
    global current_mode
    
    # Mode switching with A button
    if io.BUTTON_A in io.pressed:
        current_mode = (current_mode + 1) % len(MODES)
    
    # Apply mode-specific settings
    if current_mode == 0:  # Classic
        fade_amount = 40
        spawn_chance = 0
    elif current_mode == 1:  # Intense
        fade_amount = 20
        spawn_chance = 5
    elif current_mode == 2:  # Slow Mo
        fade_amount = 60
        spawn_chance = 0
    else:  # Chaos
        fade_amount = 10
        spawn_chance = 10
    
    # Fade effect - creates the trailing effect
    screen.pen = color.rgb(0, 0, 0, fade_amount)
    screen.rectangle(0, 0, screen.width, screen.height)
    
    # Update and draw all raindrops
    for drop in raindrops:
        # Apply mode speed multiplier
        original_speed = drop.speed
        if current_mode == 1:  # Intense
            drop.speed *= 1.5
        elif current_mode == 2:  # Slow Mo
            drop.speed *= 0.3
        elif current_mode == 3:  # Chaos
            drop.speed *= random.uniform(0.5, 2.5)
        
        drop.update()
        drop.draw()
        drop.speed = original_speed  # Reset for next frame
    
    # Spawn extra drops in intense/chaos modes
    if random.randint(0, 100) < spawn_chance:
        col = random.randint(0, NUM_COLUMNS - 1)
        if random.randint(0, 1):  # 50% chance
            raindrops.append(RainDrop(col))
    
    # Mode indicator removed for clean Matrix experience
    # You can still cycle modes with Button A
    
    # Add some random "glitches" in chaos mode
    if current_mode == 3 and random.randint(0, 100) < 5:
        glitch_y = random.randint(0, screen.height - 10)
        screen.pen = color.rgb(255, 0, 255, 100)
        screen.rectangle(0, glitch_y, screen.width, 2)

def on_exit():
    # Clean up
    pass
