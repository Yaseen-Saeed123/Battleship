# Battleship (Python – Terminal)

### A simple Battleship game played in the terminal using Python.

## How the Game Works

- The game uses a 10×10 grid

- Enemy ships are hidden

- The player fires by entering coordinates like <mark>A1</mark> , <mark>B5</mark>, <mark>J10</mark>

- Hits and misses are shown on the board

- When all enemy ships are destroyed, the player wins

## Board Symbols

- <strong>~</strong> --> water / unknown

- <strong>X</strong> --> hit

- <strong>O</strong> --> miss

## Ships

### The game includes 5 ships:

- Carrier (5)

- Battleship (4)

- Cruiser (3)

- Submarine (3)

- Destroyer (2)

<b> Each ship is stored as a list of coordinates.
When the list becomes empty, the ship is sunk.</b>

## AI

- AI never fires at the same coordinate twice

- AI selects only valid positions

## Win Condition

- The game ends when all enemy ship lists are empty.

## Goal

- Sink all enemy ships to win the game.
