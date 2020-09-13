import model.gameModel as gm
import model.cardModel as cm


def createRoyal(player):
    newDeck = gm.Deck(player, "Royal Paladin Trial Deck", [])

    for i in range(4):
        newCard = cm.Card("Alfred Early", 3, gm.Gift.FORCE, gm.Trigger.NONE,
                          13000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HUMAN, "placeholder",
                          False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Stardrive Dragon", 3, gm.Gift.FORCE,
                          gm.Trigger.NONE, 13000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.COSMODRAGON,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Knight of Silence, Gallatin", 2, gm.Gift.NONE,
                          gm.Trigger.NONE, 10000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HUMAN, "placeholder",
                          False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Blaster Blade", 2, gm.Gift.FORCE, gm.Trigger.NONE,
                          10000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.GIANT, "placeholder",
                          False)
        newDeck.cards.append(newCard)

    for i in range(3):
        newCard = cm.Card("Sage of the Arts, Jauron", 2, gm.Gift.NONE,
                          gm.Trigger.NONE, 10000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HUMAN, "placeholder",
                          False)
        newDeck.cards.append(newCard)

    for i in range(3):
        newCard = cm.Card("Wingal", 1, gm.Gift.NONE,
                          gm.Trigger.NONE, 8000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HIGHBEAST,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Knight Squire, Allen", 1, gm.Gift.NONE,
                          gm.Trigger.NONE, 8000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HUMAN,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Strong Knight, Rounoria", 1, gm.Gift.NONE,
                          gm.Trigger.NONE, 8000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HUMAN, "placeholder",
                          False)
        newDeck.cards.append(newCard)

    for i in range(3):
        newCard = cm.Card("Auspice Falcon", 1, gm.Gift.NONE,
                          gm.Trigger.NONE, 6000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HIGHBEAST,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(1):
        newCard = cm.Card("Glyme", 0, gm.Gift.NONE,
                          gm.Trigger.NONE, 6000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HIGHBEAST,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Bringer of Good Luck, Epona", 0, gm.Gift.NONE,
                          gm.Trigger.CRITICAL, 5000, 1,
                          gm.Nation.UNITEDSANCTUARY, gm.Clan.ROYALPALADIN,
                          gm.Race.SYLPH, "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Flogal", 0, gm.Gift.NONE,
                          gm.Trigger.CRITICAL, 5000, 1,
                          gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HIGHBEAST,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Margal", 0, gm.Gift.NONE,
                          gm.Trigger.DRAW, 5000, 1, gm.Nation.UNITEDSANCTUARY,
                          gm.Clan.ROYALPALADIN, gm.Race.HIGHBEAST,
                          "placeholder", False)
        newDeck.cards.append(newCard)

    for i in range(4):
        newCard = cm.Card("Yggdrasil Maiden, Elaine", 0, gm.Gift.NONE,
                          gm.Trigger.HEAL, 5000, 1,
                          gm.Nation.UNITEDSANCTUARY, gm.Clan.ROYALPALADIN,
                          gm.Race.ELF, "placeholder", False)
        newDeck.cards.append(newCard)

    return newDeck


def initializePlayer(id, name, deck, hand):
    return gm.Player(id, name, deck, hand)


def initializeSide(player):
    side = []

    for i in range(6):
        side.append(initializeZone(player, i))

    return side


def initializeZone(player, position):
    return gm.Zone(player, position, [])


def initializeGame():
    players = []
    players.append(initializePlayer(0, "Abel", createRoyal(0), []))
    players.append(initializePlayer(1, "Cain", createRoyal(1), []))

    field = []
    field.append(initializeSide(0))
    field.append(initializeSide(1))

    return gm.Game(0, players, field)
