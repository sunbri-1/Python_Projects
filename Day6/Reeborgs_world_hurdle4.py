def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() and front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
