from die import Die
import pygal
#Create a d6
die_1 = Die()
die_2 = Die()

#make the rolls and store the rolls in res
res = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    res.append(result)

frequencies = []
max_res = die_1.num_sides + die_2.num_sides
for value in range(2,max_res+1):
    freq = res.count(value)
    frequencies.append(freq)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','10','11','12']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')