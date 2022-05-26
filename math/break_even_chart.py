import numpy
import matplotlib.pyplot as plt

# Imagine you have a product that you can 100 units of that
# costs you $3 per unit and $20 shipping handling.
#
# You can take this product and re-sell it for $5 a unit.
# Let's create a graph to see how many units you would
# need to sell to break even.

fig, ax = plt.subplots()

x = numpy.arange(0.0, 100.0, 1.0)
sales = 5*x
costs = numpy.repeat(100 * 3 + 25, 100) # Cost per unit plus shipping
costs_line, = ax.plot(x, costs, label='Costs')
sales_line, = ax.plot(x, sales, label='Sales')

ax.annotate('Break even point', xy=(65, 325), xytext=(75, 260),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.set_ylim(0, 500)
plt.title('Break Even Analysis')
plt.xlabel('Units')
plt.ylabel('Dollars')
plt.legend(loc = 'upper right')
plt.grid()
plt.savefig('break_even.png')