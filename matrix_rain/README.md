# Matrix Rain App for Tufty Badge

A full-color Matrix-style digital rain animation with multiple visual modes.

## Features

- **Full-color cascading characters** - Beautiful green matrix rain effect
- **4 Different Modes:**
  - **Classic** - Traditional Matrix rain (green)
  - **Intense** - Faster drops with red accents, more density
  - **Slow Mo** - Slow, meditative cyan rain
  - **Chaos** - Random speeds, purple theme with glitch effects

- **Smooth animations** - Takes advantage of Tufty's 320x240 display
- **Dynamic character changes** - Characters morph as they fall
- **Fade trails** - Authentic trailing effect

## Controls

- **Button A** - Cycle through modes (no on-screen indicator - just feel the vibe change!)
- **HOME Button** - Return to menu

## Installation

1. Copy the entire `matrix_rain` folder to `/apps/` on your Tufty badge
2. Restart or return to home menu
3. Select "Matrix Rain" from the apps menu

## Technical Details

- 40 columns of falling characters
- Variable speed drops (0.5x to 2.0x speed)
- 10-25 character trail lengths
- Alpha blending for smooth fading
- Random character mutation during fall

## Customization

You can edit `__init__.py` to customize:
- `COLUMN_WIDTH` - Spacing between columns
- `MAX_TRAIL_LENGTH` - Maximum length of character trails
- `CHARS` - Pool of characters to display
- Mode colors and speeds

Enjoy the digital rain! 🟢⚡
