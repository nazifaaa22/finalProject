import sys
import skincare_dataset 
import pandas as pd

class Skincare:
    """A class for determining which skincare products work best for user.
    Attributes:

    Methods:
    
    """
    def __init__(self, path):
        """Initializes a skincare object.
        Args:
        Returns:
        """
        self = pd.read_csv(path)

    def userQuestions(self, skintype, targetConcern, budget):
        """Asks the user questions about their skin, including their skin type, their skincare concern, and their budget.

        Returns:
            None
        """
        skintype = input("What is your skinstype?")
        targetConcern = input("From the list provided, what is your top skin concern? Dryness, Acne, Dull SKin, Sun Protection")
        budget = input("What is your budget?")

        return skintype, targetConcern, budget 

class SkincareRecommender:
    """_summary_
    """
    def __init__(self, dataset_path):
        """ Initializes the Skincare Recommender object. 
        """
        self.products_df = pd.read_csv(dataset_path)

    def userQuestions():
        """ asks the user questions about their skin 
        """
        skintype = input("What is your skinstype?")
        targetConcern = input("What is your skin concern?")

class Moisturizer:
    def __init__():
        """ Initializes a Moisturizer object. 
        """
        moisturizer = ("What is your skintype? (Choose 1-5, 1: Combo, 2: Dry, 3: Normal, 4: Oily, 5: Sensitive)")
        skin_types = ["Combo", "Dry", "Normal", "Oily", "Sensitive"]
        budget = ("What is your budget?")

        for skin_type in skin_types:
            print(skin_type) 

        return  
class Cleanser: 
    def __init__(): 
        """ Initializes a Cleanser object.  
        """
class Treatment:   
    def __init__():
        """ Initializes a Treatment object.
        """
        if targetConcern = acne 
            return "salicylic acid"
        elif targetConcern = anti aging 
            return "retinol" 
class Face_Mask:
    def __init__():
        """ Initializes a Face Mask object.
        """
        face_mask = ("What is your skintype? (Choose 1-4, 1: Combo, 2: Dry, 3: Normal, 4: Oily, 5: Sensitive)")

        if "skincare_dataset" ==  

class Eye_Cream:
    def __init__(): 
        """ Initializes an Eye Cream object.
        """
        eye_cream = 
class Sun_Protection:
    def __init__(): 
        """ Initializes a Sun Protection object. 
        """

def main (path): 
    dataset_path = 'skincare_dataset.csv'
    recommender = SkincareRecommender(dataset_path)
    skintype, targetConcern = userQuestions()

    skincarerecommender = []
    with open(path, 'r') as file:
        newfile = file.readlines()

    return "The best moisturizer is" brand "with" price


if __name__ == "__main__":
    main("skincare_dataset.txt") 



 

