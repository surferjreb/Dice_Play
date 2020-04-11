from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


class VisualDie:

    def __init__(self, num_sides):
        self.die = Die(num_sides)
        self.start_index = 0
        self.max_index = self.die.num_sides+1
        self.frequency = 0
        self.x_values = list()
        self.results = []
        self.data = 0.0
        self.frequencies = []
        self.my_layout = 0

    def set_x_values(self):

        if self.start_index >= 0 and self.max_index > 0:
            self.x_values = (list(range(1, self.max_index+1)))
        else:
            print("Invalid input")

    def set_my_layout(self, x_config, y_config):
        self.my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_config, yaxis=y_config)

    def set_results(self, num_rolls=1000):

        for roll_num in range(num_rolls):
            result = self.die.roll()
            self.results.append(result)

    def set_frequency(self):

        for value in range(1, self.max_index):
            self.frequency = self.results.count(value)
            self.frequencies.append(self.frequency)

    def set_data(self):
        self.data = [Bar(x=self.x_values, y=self.frequencies)]


class VDieController:
    def __init__(self, num_of_dice=1, num_of_sides=6):
        self.num_of_dice = num_of_dice
        self.num_of_sides = num_of_sides
        self.dice = []
        self.combined_results = []
        self.combined_frequencies = 0
        self.combined_max_index = 0

    def create_dice(self):
        for i in range(self.num_of_dice):
            die = VisualDie(self.num_of_sides)
            self.dice.append(die)

    def combine_dice_values(self):
        pass

    def set_die_values(self):
        for i in range(self.num_of_dice):
            self.dice[i].set_results()
            self.dice[i].set_frequency()
            self.dice[i].set_x_values()
            self.dice[i].set_data()
            x_axis_config = {'title': 'Result'}
            y_axis_config = {'title': 'Frequency of Result'}
            self.dice[i].set_my_layout(x_axis_config, y_axis_config)

    def add_dice_results(self):
        pass

    def combine_dice_frequencies(self):
        pass

    def combine_dice_info(self, results, frequencies, x_values, data):
        pass

    def create_dice_plot(self, filename):
        for i in range(self.num_of_dice):
            data = self.dice[i].data
            my_layout = self.dice[i].my_layout

            offline.plot({'data': data, 'layout': my_layout}, filename)


# create a D6
v_die = VDieController(1, 6)

v_die.create_dice()

v_die.set_die_values()


v_die.create_dice_plot('d6.html')





# if __name__ == '__main__':
#     # Make a game instance, and run the game
