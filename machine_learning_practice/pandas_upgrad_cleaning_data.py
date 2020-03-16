import pandas as pd
marks = pd.read_csv('https://query.data.world/s/HqjNNadqEnwSq1qnoV_JqyRJkc7o6O')

marks = marks.isnull().sum()
print(marks)