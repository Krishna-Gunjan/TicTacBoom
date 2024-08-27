# Tic-Tac-Toe Game with CustomTkinter

## Overview

This project is a graphical Tic-Tac-Toe game built using the `customtkinter` (CTk) library in Python. The game features a simple interface that allows two players to play Tic-Tac-Toe against each other. It includes various functionalities such as tracking player turns, checking for wins or draws, and keeping a history of game results.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Code Explanation](#code-explanation)
  - [Interface Class](#interface-class)
  - [TicTacToeWidget Class](#tictactoewidget-class)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- `customtkinter`
- `CTkMessagebox`
- `numpy`

You can install the required Python packages using pip:

```bash
pip install customtkinter CTkMessagebox numpy
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ctk.git
   cd tic-tac-toe-ctk
   ```

2. **Run the Application:**

   You can run the game using the following command:

   ```bash
   python main.py
   ```

## Usage

Once you run the application, a Tic-Tac-Toe window will appear. Two players can play the game by clicking on the grid to place their marks (`X` or `O`). The game will automatically check for a win or draw after each move.

### Game History

The game maintains a history of the results displayed on the left side of the interface. It keeps track of the number of games played, the current player, and whether the game ended in a win or a draw.

### Game Reset

After each game, the board will automatically reset for the next round.

## Features

- **Player Turns:** Automatically switches between Player 1 (`X`) and Player 2 (`O`).
- **Win/Draw Detection:** Detects and announces when a player wins or when the game is a draw.
- **Game History:** Displays the history of all games played in the current session.
- **Dynamic Buttons:** Some buttons are randomly disabled and colored differently to add complexity to the game.
- **Mark Changer:** Randomly changes a player's mark to increase unpredictability.

## Code Explanation

### Interface Class

The `Interface` class manages the main window of the application. It sets up the screen, side panel, and player details, and integrates the Tic-Tac-Toe widget.

- **screen:** Configures the window to match the screen's dimensions.
- **side_panel:** Creates a side panel on the left side of the interface.
- **player_details:** Displays player information in the side panel.
- **history_tab:** Creates a history tab to display past game results.
- **add_game_history:** Adds a new entry to the game history after each game.

### TicTacToeWidget Class

The `TicTacToeWidget` class is responsible for the Tic-Tac-Toe game logic and UI components.

- **create_board_button:** Initializes the Tic-Tac-Toe grid with buttons.
- **create_turn_label:** Displays the current player's turn.
- **on_button_click:** Handles button clicks, updates the board, and checks for a win/draw.
- **check_win:** Checks if the current player has won.
- **check_draw:** Checks if the game is a draw.
- **reset_game:** Resets the board for a new game.
- **active_buttons:** Randomly disables a button in each row to add complexity.
- **is_possible_moves_left:** Ensures that there are still moves left on the board.
- **mark_changer:** Randomly changes a player's mark to increase unpredictability.

## Customization

- **Colors:** You can customize the colors of the buttons and labels by modifying the `fg_color`, `text_color`, and other attributes.
- **Fonts:** Change the fonts by modifying the `font` attributes in the CTk components.
- **Button Sizes:** Adjust the button size by modifying the `width` and `height` parameters in the `create_board_button` method.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Issues and feature requests are also welcome.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute this code as you see fit.

---
