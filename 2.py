
# required libraries and lists
import csv
my_list = []
my_list2 = []
my_list3 = []
energyfilter = ['Wind', 'Solar Thermal and Photovoltaic']
yearfilter = ['2017']
statefilter = ['TX', 'CA']
highwind = []
highsolar = []

# open csv file
with open('energy.csv', 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    # put filtered csv values into a list
    for row in reader:
        for i in row:
            if i in energyfilter:
                my_list.append(row)
    # sort the list by megawatthours, reversed
    my_list.sort(key = lambda my_list: my_list[3], reverse = True)
    for row in my_list:
        for i in row:
            if i in yearfilter:
                my_list2.append(row)
    my_list2.sort(key=lambda my_list2: my_list2[3], reverse=True)
    for row in my_list2:
        for i in row:
            if i in statefilter:
                my_list3.append(row)
    my_list3.sort(key=lambda my_list3: my_list3[3], reverse=True)
    # add list with highest wind megawatthours to highwind list
    highwind.append(my_list3[0])
    # add list with highest solar megawatthours to highsolar list
    highsolar.append(my_list3[1])

# defining __init__ w/ class
class State():    
    def __init__(self, state, energy, mwh, year):
        self.state = state
        # we want lowercase energy type
        self.energy = energy.lower()
        # shorthand for megawatthours
        self.mwh = mwh
        self.year = year

    # defining main function and print output
    def main(self):
        print('The largest producer of ' + self.energy + ' power was ' 
              + self.state + ' at ' + self.mwh + ' megawatthours in ' + self.year + '.')

# define the variables for wind and solar
wind = State(highwind[0][1], highwind[0][2], highwind[0][3], highwind[0][0])
# the example in the instructions only had 'solar' printed in the result instead of
#'Solar Thermal and Photovoltaic,' so I will be inputting 'solar' as its own string
# for the solar variable
solar = State(highsolar[0][1], 'solar', highsolar[0][3], highsolar[0][0])

# run the main function given the defined variables
if __name__ == '__main__':
    wind.main()
    solar.main()
    
# end of code for Homework 2
