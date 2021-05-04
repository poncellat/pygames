from snake_mod import *


def main():

    # screen initialization
    screen = screen_init()

    # initial position for snake with food
    x1y1, x2y2, snake_len, snake_cur_dir, snake_scale_positions = snake_initial_position(screen)
    print(x1y1, x2y2, snake_len, snake_cur_dir)

    # once any arrow key pressed, start the game
    game_on, snake_speed, key_pressed = start_game()
    print(game_on, snake_speed, key_pressed)

    clock = pygame.time.Clock()

    # while game is on
    while game_on:
        clock.tick(snake_speed)

        # move the snake
        x1y1, x2y2, snake_cur_dir,\
        snake_scale_positions = move_snake(snake_speed, key_pressed,
                                           snake_cur_dir, x1y1, x2y2,
                                           screen, snake_len,
                                           snake_scale_positions)
        key_pressed = ""
        print("#", x1y1, x2y2)

        # check if it has hit the wall
        # if yes, end game
        hit_wall = did_hit_wall(x1y1, x2y2)
        if hit_wall:
            game_on = False

        # check if it has hit its own body
        # if yes, end game
        bite_itself = did_bite_itself(snake_scale_positions)
        if bite_itself:
        	game_on = False

        for event in pygame.event.get():
            # if user clicks exit button
            if event.type == pygame.QUIT:
                sys.exit()

            # check if the user pressed any arrow key
                # if yes, turn accordingly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    key_pressed = "right"
                elif event.key == pygame.K_LEFT:
                    key_pressed = "left"
                elif event.key == pygame.K_UP:
                    key_pressed = "up"
                elif event.key == pygame.K_DOWN:
                    key_pressed = "down"

            # check if it has ate the food
                # if yes, add score,
                # grow the snake,
                # create new food

    # update score board


if __name__ == "__main__":
    main()
