# Polarity Game

**Polarity Game** is an exciting 2D physics-based game where players navigate through magnetic fields with changing polarities. The goal is to collect objects, avoid obstacles, and reach the end goal while switching polarities to interact with magnetic forces.

![Polarity Game Screenshot](https://raw.githubusercontent.com/prabhsharan1/RFM/main/Polarity%20Game%201592x1198.png)

## Features

- **Magnetic Forces:** Experience dynamic magnetic forces depending on the chosen polarity (positive or negative).
- **Multiple Levels:** Navigate through progressively challenging levels with increasing obstacles and collectibles.
- **Time Challenge:** A countdown timer adds urgency and increases the challenge as the game advances.
- **Collectibles:** Collect items to score points and unlock new levels.
- **Polarity Switching:** Switch between positive and negative polarity using the spacebar to interact with magnetic objects.
- **Background Music & Sound Effects:** Immersive background music and sound effects enhance gameplay.
- **Dynamic Difficulty:** Difficulty increases with faster speeds and more complex obstacles as you progress.

## Installation

To run the **Polarity Game**, you need to have **Python** and **Pygame** installed.

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/polarity-game.git
```

### Step 2: Install Dependencies

Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install pygame requests
```

### Step 3: Run the Game

Navigate to the project directory and run the game with:

```bash
python polarity_game.py
```

### Download for Mac or Linux

If you prefer a pre-built version, download the game for Mac or Linux from [Polarity Game on itch.io](https://prabhsharan1.itch.io/polarity-game).

## Game Controls

- **Arrow Keys:** Move the player up, down, left, or right.
- **Spacebar:** Switch polarity between positive and negative.
- **Objective:** Collect all collectibles, reach the goal, and avoid magnetic obstacles.

## Sound Files

The game includes the following sound files:
- **Background Music:** "party_music.mp3"
- **Victory Sound:** "victory_sound.mp3"
- **Fail Sound:** "game_fail.mp3"

These files are automatically downloaded if they do not exist in the local directory.

## Game Flow

1. The player starts at the bottom-left of the screen and must navigate through each level by collecting items and avoiding magnetic obstacles.
2. Magnetic objects (magnets) either attract or repel the player, depending on the player's current polarity.
3. Players must switch between positive and negative polarity to interact with different magnetic objects and avoid collisions.
4. Collectibles appear throughout the level. Players must collect these to score points.
5. Once all items are collected or the goal is reached, the level advances. Successfully completing all levels results in victory.

## Game Development Details

- **Libraries Used:**
  - `pygame` for handling game graphics, sound, and events.
  - `requests` for downloading sound files if not present locally.
  
- **Game Physics:** Magnetic forces are simulated by calculating the distance between the player and magnets. The closer the player is to a magnet, the stronger the force.

- **Sound Management:** Background music and sound effects (victory and failure) are played based on the game's state (win or lose).

## Contributing

Feel free to contribute to the development of this game! You can fork the repository, submit issues, or create pull requests for improvements.

### How to Contribute

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push your changes to your fork and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

