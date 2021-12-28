import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5 ,6 ]

# heights of bars
height = [3 , 2, 153 , 185 ,579 , 447, ]

# labels for bars
tick_label = ['10.ja', '10.py', '1k.ja', '1k.py', '10k.ja','10k.py']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
		width = 0.6, color = ['green', 'yellow'])

# naming the x-axis
# plt.xlabel('x - sec')
# naming the y-axis
plt.ylabel(' mili- sec')
# plot title
plt.title('Performance comparison getGraph java vs python')

# function to show the plot
plt.show()
