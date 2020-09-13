def showPlayers(game):
    for i in range(2):
        print("player" + game.getPlayer(i).getName())
        print("deck: " + game.getPlayer(i).getDeck().getName())
        print("damage: " + str(game.getPlayer(i).getDamage()))
        print("hand: ")

        for j in range(len(game.getPlayer(i).getHand().getCards())):
            print(game.getPlayer(i).getHand().getCards()[j])
        print()
    return
