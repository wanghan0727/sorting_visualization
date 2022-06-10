import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from func import *

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)

generator = bubble_sort(nums)
sort_name = 'Bubble Sort'

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_title(f'{sort_name} Visualization')
ax.set_xlim(0, len(nums))
ax.set_ylim(0, len(nums))
bar_rects = ax.bar(range(len(nums)), nums, align='edge')
# text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]

def update(nums, rects, iteration):
	
	for rect, val in zip(rects, nums):
		rect.set_height(val)
	iteration[0] += 1
    # text.set_text(f'operations : {iteration[0]}')


anim = FuncAnimation(fig,
					 func=update,
                     fargs=(bar_rects, iteration),
                     frames=generator,
                     interval=1000,
                     repeat=False)

plt.show()
