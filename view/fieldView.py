def showField(game):
    print("showing field")
    print()

    field0 = game.getField(0)
    field1 = game.getField(1)

    print("player 1 field:")
    for i in range(6):
        if isinstance(field0[i].getTop(), str):
            print(field0[i].getTop())
        else:
            print(field0[i].getTop().cardName())

    print("player 2 field:")
    for i in range(6):
        if isinstance(field1[i].getTop(), str):
            print(field1[i].getTop())
        else:
            print(field1[i].getTop().cardName())

    print()
