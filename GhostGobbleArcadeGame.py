class PacMan:
    def eat_ghost(self, has_a_power, is_touching_a_ghost):
        if is_touching_a_ghost and has_a_power:
            return True
        else:
            return False

    def score(self, touching_a_power, touching_a_dot):
        if touching_a_power and touching_a_dot:
            return True
        else:
            return False

    def lose(self, has_a_power, is_touching_a_ghost):
        if has_a_power and not is_touching_a_ghost:
            return True
        else:
            return False

    def win(self, eaten_all_of_the_dots, is_touching_a_ghost, has_a_power):
        if eaten_all_of_the_dots and not self.lose(is_touching_a_ghost, has_a_power):
            return True
        else:
            return False


man = PacMan()
man.eat_ghost(True, True)
man.score(True, True)
man.lose(False, True)
print(man.win(True, True, True))
