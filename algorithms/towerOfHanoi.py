def peek_ring(tower):
    if len(tower) == 0:
        return None

    ring = tower.pop()
    tower.append(ring)
    return ring


def can_move_to(from_tower, to_tower):
    if len(from_tower) == 0:
        return False

    if len(to_tower) == 0:
        return True
    else:
        from_item = peek_ring(from_tower)
        to_item = peek_ring(to_tower)
        if from_item < to_item:
            return True
    return False


def move_ring(from_tower, to_tower):
    if can_move_to(from_tower, to_tower):
        ring = from_tower.pop()
        to_tower.append(ring)
        return ring
    return None


def get_tower_with_bigger_ring(tower_one, tower_two):
    if len(tower_one) > 0:
        one_item = peek_ring(tower_one)
    else:
        one_item = None

    if len(tower_two) > 0:
        two_item = peek_ring(tower_two)
    else:
        two_item = None

    if one_item is None and two_item is None:
        return None
    if one_item is None:
        return tower_two
    if two_item is None:
        return tower_one

    return tower_one if one_item > two_item else tower_two


def get_tower_with_smaller_ring(tower_one, tower_two):
    if len(tower_one) > 0:
        one_item = peek_ring(tower_one)
    else:
        one_item = None

    if len(tower_two) > 0:
        two_item = peek_ring(tower_two)
    else:
        two_item = None

    if one_item is None and two_item is None:
        return None
    if one_item is None:
        return tower_two
    if two_item is None:
        return tower_one

    return tower_one if one_item < two_item else tower_two


def get_movable_len(from_tower, target_ring):
    from_len = len(from_tower)
    if target_ring is None:
        return from_len

    movable_len = 0
    for i in from_tower:
        if i < target_ring:
            movable_len += 1
    return movable_len


def move_rings_recur(from_tower_given, middle_tower_given, to_tower_given):
    print("In : ", from_tower_given, middle_tower_given, to_tower_given)
    move_count = 0
    if len(from_tower_given)==0:
        return move_count
    from_tower = from_tower_given
    to_tower = to_tower_given
    middle_tower = middle_tower_given

    to_tower_ring = peek_ring(to_tower_given)
    target_ring = to_tower_ring
    if to_tower_ring is None:
        target_ring == peek_ring(from_tower)
    movable_len = get_movable_len(from_tower, to_tower_ring)
    if (movable_len % 2) == 0:
        to_tower = middle_tower_given
        middle_tower = to_tower_given
    else:
        to_tower = to_tower_given
        middle_tower = middle_tower_given

    while len(from_tower) > 0:

        if peek_ring(from_tower) is None:
            return move_count

        if target_ring is not None:
            if peek_ring(from_tower) > target_ring:
                return move_count

        top_ring = move_ring(from_tower, to_tower)
        if top_ring is not None:
            move_count += 1
        next_ring = move_ring(from_tower, middle_tower)
        if next_ring is not None:
            move_count += 1

        if top_ring is not None and next_ring is not None :
            quick_ring = move_ring(to_tower, middle_tower)
            if quick_ring is not None:
                move_count += 1

        if top_ring is None and next_ring is None :
            tower_with_big_ring = get_tower_with_bigger_ring(to_tower, middle_tower)
            tower_with_small_ring = get_tower_with_smaller_ring(to_tower, middle_tower)
            # print("Move : ", from_tower_given, middle_tower_given, to_tower_given)
            if peek_ring(tower_with_small_ring) < peek_ring(tower_with_big_ring):
                move_count += move_rings_recur(tower_with_small_ring, from_tower, tower_with_big_ring)
            else:
                move_count += move_rings_recur(tower_with_big_ring, from_tower, tower_with_small_ring)
            # print("Back : ", from_tower_given, middle_tower_given, to_tower_given)
        else:
            continue
    return move_count


def move_rings_cycle(from_tower, middle_tower, to_tower):
    print("In Cycle: ", from_tower, middle_tower, to_tower)
    move_count = 0

    while len(from_tower) > 0 or len(middle_tower) > 0:
        if len(from_tower) > 0:
            # print("Next Cycle From: ", from_tower, middle_tower, to_tower)
            move_count += move_rings_recur(from_tower, middle_tower, to_tower)
        if len(middle_tower) > 0:
            # print("Next Cycle Middle: ", from_tower, middle_tower, to_tower)
            move_count += move_rings_recur(middle_tower, from_tower, to_tower)
    return move_count


def main():
    # from_tower = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    from_tower = [6, 5, 4, 3, 2, 1]
    to_tower = []
    middle_tower = []
    print(from_tower)
    print(middle_tower)
    print(to_tower)
    from_tower_len = len(from_tower)
    projected_count = 2**from_tower_len - 1
    move_count = move_rings_cycle(from_tower, middle_tower, to_tower)
    print(from_tower)
    print(middle_tower)
    print(to_tower)
    print("Move count. Projected : ", projected_count, ", Actual :", move_count)

if __name__ == "__main__":
    main()
'''
[6, 5, 4, 3, 2, 1]
[]
[]
In Cycle:  [6, 5, 4, 3, 2, 1] [] []
In :  [6, 5, 4, 3, 2, 1] [] []
In :  [2, 1] [6, 5, 4] [3]
In :  [3, 2, 1] [6, 5] [4]
In :  [4, 3, 2, 1] [6] [5]
In :  [5, 2, 1] [4] [6, 3]
In :  [2, 1] [6] [5, 4, 3]
In :  [5, 4, 3, 2, 1] [] [6]
In :  [2, 1] [5, 4] [6, 3]
In :  [6, 3, 2, 1] [5] [4]
In :  [4, 3, 2, 1] [] [6, 5]
In :  [6, 5, 2, 1] [4] [3]
In :  [3, 2, 1] [] [6, 5, 4]
In :  [2, 1] [] [6, 5, 4, 3]
[]
[]
[6, 5, 4, 3, 2, 1]
Move count. Projected :  63 , Actual : 63
'''