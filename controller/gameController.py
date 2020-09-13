import view.fieldView as fv
import view.playerView as pv


def start(game):
    print("starting")
    gameLoop(game)


def gameLoop(game):
    while True:
        fv.showField(game)
        pv.showPlayers(game)
        input("prompting user")
