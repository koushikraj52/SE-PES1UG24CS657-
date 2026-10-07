# Lab 4 - VibeCoding

**Name:** B Koushikraj  
**SRN:** PES1UG24CS657

## Objective

To use Vibe Coding with an LLM to identify, fix, and improve an existing Whack-a-Mole game by implementing the required features.

## Project

**Project:** Whack-a-Mole Game

The project is a graphical Whack-a-Mole game developed using Python and Pygame. The game contains a 3x3 grid of holes where moles appear randomly and the player scores points by clicking active moles.

## Tasks Completed

### Task 1 - Refine Collision Detection

Improved the click-hit handling so that a single mouse click cannot award multiple points when neighboring mole hit-boxes overlap. The game stops checking after the first successful whack.

### Task 2 - Game Over Condition

Added a graphical Game Over screen that displays the final score when the round timer reaches zero. The game waits for the player to choose the next action instead of only printing the final score in the console.

### Task 3 - Replay Option

Added a replay system after Game Over with three difficulty levels:

- Easy
- Medium
- Hard

Each difficulty has a different mole spawn rate and mole visibility duration. The game state is reset when starting a new round. An exit option is also provided.

### Task 4 - Sound Feedback

Added sound effects for:

- Successful mole whack
- Missed click
- Game Over

## Technologies Used

- Python
- Pygame
- Git
- GitHub
- LLM / Vibe Coding

## Project Structure

```text
Lab-4/
├── 48_whack-a-mole/
│   ├── game/
│   │   ├── game_engine.py
│   │   ├── hole.py
│   │   ├── create_sounds.py
│   │   └── sounds/
│   │       ├── whack.wav
│   │       ├── miss.wav
│   │       └── game_over.wav
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
├── Before_Video.mp4
├── After_Video.mp4
├── Chatgpt Link
└── README.md