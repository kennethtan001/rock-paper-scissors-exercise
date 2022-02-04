# rock-paper-scissors-exercise

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Setup

Clone this repository onto your local computer. Then navigate to wherever you downloaded the repo.

Create a virtual environment:

```sh
conda create -n my-game-env python=3.8
```

Activate the virtual environment:

```sh
conda activate my-game-env
```

Install package dependencies within the virtual environment:

```sh
pip install -r requirements.txt
```

## Player Types

When you play the RPS game, you'll be able to select rock, paper, or scissors. 

## Usage

### Game Play

Play a game vs computer:

```sh
python game.py
```


### Game Simulation

User has choice to pass in name as environment variables:

```sh
PLAYER_NAME="Jon Snow" python game.py
```


## Testing

Run automated tests, to know whether the app is working as expected:

```sh
pytest
```
