import matplotlib.pyplot as plt


def generate_pie_char():
  labels = ['A', 'B', 'C']
  values = [20, 30, 40]

  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)

  plt.savefig('graph.png')
  plt.close()
