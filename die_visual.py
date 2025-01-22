from die import Die
import pygal
#Create a d6
die = Die()

#make the rolls and store the rolls in res
res = []
for roll_num in range(10):
    result = die.roll()
    res.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
    freq = res.count(value)
    frequencies.append(freq)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')