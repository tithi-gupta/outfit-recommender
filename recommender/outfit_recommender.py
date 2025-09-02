
import pandas as pd
class OutfitRecommender:
  def __init__(self, data_path):
    self.data = pd.read_csv(data_path)

  def recommender(self, color, occasion):
    result=self.data
    if color:
      result=result[result['color'].str.lower()==color.lower()]
    if occasion:
      result=result[result['occasion'].str.lower()==occasion.lower()]
    return result['outfit'].tolist()
