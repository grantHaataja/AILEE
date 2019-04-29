"""
Run the game
"""


from game import Game
from MainMenuException import MainMenuException
import funfunctions

from funfunctions import clear
import time

from computers import factory


def main():
    while True:
        # Create the game, agent, computer; and get a shell
        game = Game()
        if game.leave:
            break
        ailee = game.spawn_agent("ailee")
        comp = factory.mk_computer('ailee', game=game)

        if not game.skip_dialog:
            clear()
            time.sleep(3)
            user = comp.get_user('Administrator')
            time.sleep(5)
            funfunctions.login(user.name, user.password)
            clear()
            funfunctions.startAilee()
        ailee.login(comp)
        try:
            ailee.shells[0].start_shell_loop()
            print("Just broke out of main loop")
            time.sleep(10)
        except MainMenuException:
            pass  # So the shutdown command returns to the main menu
                  # instead of exiting


if __name__ == '__main__':
    main()
