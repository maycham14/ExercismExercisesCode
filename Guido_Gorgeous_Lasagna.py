class Lasagna:
    def __init__(self):
        self.EXPECTED_BAKE_TIME = 40
        self.remaining_time = 40

    def bake_time_remaining(self, time):
        self.remaining_time -= time
        return self.remaining_time

    def preparation_time_in_minutes(self, layers):
        TIME = 2
        munites = TIME * layers
        return munites

    def elapsed_time_in_minutes(self, number_of_layers, elapsed_bake_time):
        total = self.preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
        return total


lasagna = Lasagna()
print(lasagna.bake_time_remaining(23))
output = lasagna.preparation_time_in_minutes(3)
print(output)
total = lasagna.elapsed_time_in_minutes(3,34)
print(total)