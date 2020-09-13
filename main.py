import creator as cr
import controller.gameController as gc


def main():
    game = cr.initializeGame()
    gc.start(game)


if __name__ == "__main__":
    main()
