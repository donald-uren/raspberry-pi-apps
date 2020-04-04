# RMIT IoT Sem1 2020 - Assignment 1

## Overview
The project has 3 sub-tasks, as listed below. Task 1 and 2 utilise the same main.py file which monitors for a joystick press to halt the program.

## Tasks
1. [Emoji display](https://github.com/donald-uren/a1_iot/tree/master/emoji):
A simple program which displays a series of emoji faces. Can also optionally load emoji patterns from a .json file.

2. [Temperature display](https://github.com/donald-uren/a1_iot/tree/master/temperature):
A simple program which detects and displays the current temperature as a solid colour based on customisable range values (loaded from a .json file)

3. [Electronic dice game](https://github.com/donald-uren/a1_iot/tree/master/dice_game):
A multi-player dice game, where players take turns shaking the raspberry to simulate the act of rolling dice. Whoever gets 30 points first wins the game, which will then export winner name and score to a .csv file.

## Requirements
Tasks have been tested and implemented on Raspberry Pi 3 Model B with SenseHAT, using Python 3.6

### How to run:
Tasks 1 and 2 can be run using:
```
python3 main.py [emoji|temperature] [config.json]
```

Task 3 can be run using:
```
python3 dice_game/main.py
```

## Contributors
1. [Donald U'Ren](https://github.com/donald-uren)
2. [Daniel Dao](https://github.com/DanDanDao)
