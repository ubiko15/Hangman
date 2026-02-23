# Hangman

A classic Hangman word-guessing game with a graphical user interface built using Python and Tkinter.

## Overview

This is a desktop implementation of the traditional Hangman game where players attempt to guess a word by suggesting letters within a limited number of attempts. The game features multiple playing modes, customizable word lists, and visual feedback through animated gallows graphics.

## Features

### Game Modes

- **Own Word Mode**: Enter a custom word for another player to guess (with optional show/hide toggle)
- **Word from List Mode**: Play with randomly selected words from:
    - Your own custom word list
    - A pre-prepared word list
    - Both lists combined

### Core Functionality

- **Interactive Letter Selection**: Click on letter buttons to make guesses
- **Visual Feedback**: Animated gallows graphic that updates with each incorrect guess
- **Word List Management**: Add, view, and delete words from your custom word list
- **Game Statistics**: Track guessed letters and time taken to complete each game
- **Rules Display**: Built-in rules explanation
- **Special Graphics**: Rare alternative gallows graphics (1 in 42 chance)

### User Interface

- Clean, intuitive navigation with dedicated return and close buttons
- Multiple themed screens (main menu, game selection, running game, end screen)
- Custom color scheme and typography for enhanced readability
- Real-time word display showing guessed letters and remaining blanks

## How It Works

### Game Mechanics

1. **Word Selection**: Choose a game mode and provide/select a word to guess
2. **Guessing Process**: Click letter buttons to guess one letter at a time
3. **Feedback System**:
    - Correct guesses reveal the letter(s) in the word
    - Incorrect guesses add a stroke to the gallows (maximum 9 failures)
4. **Win/Lose Conditions**:
    - Win: Guess all letters before the gallows is complete
    - Lose: Reach 9 incorrect guesses and complete the gallows
5. **Statistics**: View guessed letters and completion time after each game

### Technical Implementation

- **Framework**: Python with Tkinter for GUI
- **Graphics**: PNG images for visual elements (gallows states, icons, buttons)
- **Data Storage**: Text files for word lists (`own_list.txt`, `prepared_list.txt`)
- **Word Validation**: Accepts letters (a-z), hyphens, and spaces; word length 1-30 characters
- **Dynamic UI**: Letter buttons and labels are programmatically generated based on word length
- **State Management**: Frame-based navigation system for different game screens

### Word List Management

- Words are stored in plaintext files in the `Lists/` directory
- Custom words can be added or removed through the in-game editor
- Listbox interface with multi-selection for batch deletion
- Automatic validation to ensure only valid words are stored

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Graphics files in `Graphics/` directory:
    - Gallows state images (`Galgen_States/`, `Galgen_States_A/`)
    - UI icons (`Icons/`)

## Running the Game

Execute the main Python file:

```bash
python Hangman.py
```

Or use the provided batch file on Windows:

```bash
run.bat
```

## Author

- **Author**: ubiko
- **Version**: 0.0.1
- **Release Date**: May 2, 2022
