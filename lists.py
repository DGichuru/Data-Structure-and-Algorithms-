def locate_card(cards, query):
    position = 0

    while True:
        if cards[position] == query:

            return position
        position += 1

        if position == len(cards):
            return -1

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo  = mid + 1

    return -1

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

#linear serach 
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
    