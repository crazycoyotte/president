class Card:
    """Card definition"""

    # instance attribut
    def __init__(self, value, color):
        """Card generation"""
        self.color = color
        self.value = value
        match value:
            case 1:
                self.name = "As"
            case 2:
                self.name = "2"
            case 3:
                self.name = "3"
            case 4:
                self.name = "4"
            case 5:
                self.name = "5"
            case 6:
                self.name = "6"
            case 7:
                self.name = "7"
            case 8:
                self.name = "8"
            case 9:
                self.name = "9"
            case 10:
                self.name = "10"
            case 11:
                self.name = "Valet"
            case 12:
                self.name = "Dame"
            case 13:
                self.name = "Roi"

    def playable(self, valueLastCardPlayed):
        """Is a card playable?
        :return Boolean
        """
        card_is_playable = False
        if self.value < valueLastCardPlayed + 3:
            card_is_playable = True
        return card_is_playable

