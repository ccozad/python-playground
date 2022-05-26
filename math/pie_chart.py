import numpy
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))

activities = [
    'Fall',
    'Winter',
    'Summer',
    'Spring'
]

activity_hours = [
    30,
    15,
    20,
    35
]

def generate_label(pct, all_values):
    absolute = int(numpy.round(pct/100.*numpy.sum(all_values)))
    return "{:.1f}%".format(pct)


wedges, texts, autotexts = ax.pie(activity_hours, autopct=lambda pct: generate_label(pct, activity_hours),
                                  textprops=dict(color="w"))

ax.legend(wedges, activities,
          title='Season',
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Favorite Season")

plt.savefig('activity.png')