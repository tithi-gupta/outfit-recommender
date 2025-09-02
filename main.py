
from recommender.outfit_recommender import OutfitRecommender
def main():
  recommender = OutfitRecommender("data/outfits.csv")
  print("recommendations for color=blue and occasion=work")
  print(recommender.recommender("blue", "work"))

if __name__ == "__main__":
  main()
