def deck_to_list(deck):
    l = []
    if deck.top != None:
        l.append(deck.top.id)
        to_append = deck.top.below
        while(to_append != None):
            l.append(to_append.id)
            to_append = to_append.below
    return l