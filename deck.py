

class Card(object):
    def __init__(self, id):
        self.id = id
        self.above = None
        self.below = None
        

class Deck(object):
    def __init__(self, card_count):
        self.bottom = None
        self.top = None

        if card_count != 0:
            first_card = Card(0)
            self.bottom = self.top = first_card  
            for i in range(1,card_count):
                card = Card(i)
                card.below = self.top
                self.top.above = card
                self.top = card

    def to_top(self, card):
        card.below = self.top
        self.top = card
        self.top.above = None
        if self.bottom == None:
            self.bottom = card
    
    def top_to(self, deck):
        if self.top != None:
            newtop = self.top.below
            
            deck.to_top(self.top)

            self.top = newtop
            if self.top != None:
                self.top.above = None
    
    def top_to_bottom(self):
        if self.top != None:
            self.bottom.below = self.top
            self.bottom = self.top
            self.top = self.top.below
            self.top.above = None
            self.bottom.below = None
        



    def display(self):
        if self.top != None:
            print(self.top.id, '\n')
            to_disp = self.top.below
            while to_disp != None:
                print(to_disp.id, '\n')
                to_disp = to_disp.below
    



