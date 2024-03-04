# Pong Game using Pygame

A simple implementation of the classic Pong game using the Pygame library.

## Table of Contents

- [Pong Game using Pygame](#pong-game-using-pygame)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Python Installation](#python-installation)
    - [Standalone Executable Installation](#standalone-executable-installation)
  - [How to Play](#how-to-play)
  - [Controls](#controls)
  - [Gameplay](#gameplay)
  - [Scoring](#scoring)
  - [Winning](#winning)
  - [Dependencies](#dependencies)
  - [Acknowledgements](#acknowledgements)

## Introduction

Welcome to the Pygame Pong game! This classic Pong implementation allows two players to compete against each other in a simple yet entertaining game of virtual table tennis.

## Installation

### Python Installation

To run this game using Python, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the Pygame library by running the following command in your terminal or command prompt:

```bash
pip install pygame
```

After installing Pygame, you can run the game script:

```bash
python pong.py
```

### Standalone Executable Installation

To play the game without Python, simply download and run the provided executable file [pong.exe](https://github.com/SamuArg/Pong/releases/download/v1.0/pong.exe) No additional installations are required.

## How to Play

- The game features two paddles and a ball.
- Players control the paddles using the keyboard to hit the ball back and forth.
- The objective is to score points by making the ball pass the opponent's paddle.

## Controls

- Player 1 (Left Paddle):

  - W: Move paddle up
  - S: Move paddle down

- Player 2 (Right Paddle):
  - Up Arrow: Move paddle up
  - Down Arrow: Move paddle down

## Gameplay

- The ball moves in the initial direction specified by its velocity.
- When the ball collides with a paddle, its direction changes, creating a dynamic and challenging game.
- The game continues until one player scores a predefined number of points.

## Scoring

- Points are scored when the ball passes the opponent's paddle and reaches the border behind it.
- The first player to reach 7 points wins the game.

## Winning

- The game ends when one of the players reaches a score of 7 points.
- A message will display the winning player's name in the center of the screen.
- The game will restart automatically after a brief delay.

## Dependencies

- Python 3.x
- Pygame library

## Acknowledgements

This Pong game was created using the Pygame library. Pygame is an open-source set of Python modules designed for writing video games. Visit the [Pygame website](https://www.pygame.org/docs/) for more information.

Enjoy the game!
