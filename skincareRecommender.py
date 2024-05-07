import sys
import skincare_dataset 
import pandas as pd

class Skincare:
    """A class for determining which skincare products work best for user.
    Attributes:

    Methods:
    
    """
<<<<<<< HEAD
    def __init__(self, path):
        """Initializes a skincare object.
=======
    def __init__(self):
        """ Initializes a Skincare object.

>>>>>>> 62fa8fbb4a23a8b8eb8a89cc1a3554d4ddfc64e8
        Args:
        Returns:
        """
        self = pd.read_csv(path)

    def userQuestions(self, skinType, targetConcern, budget):
        """Asks the user questions about their skin, including their skin type, their skincare concern, and their budget.

        Returns:
            None
        """
        skinType = input("What is your skinstype?")
        targetConcern = input("What is your skin concern?")
        budget = input("What is your budget?")

<<<<<<< HEAD
        return skinType, targetConcern, budget 
=======
def userQuestions():
    """ Asks the user questions about their skin, including their skin type, their skincare concern, and their budget.

    Returns:
        None
    """
    skintype = input("What is your skinstype?")
    targetConcern = input("What is your skin concern?")
    budget = input("What is your budget?")
>>>>>>> 62fa8fbb4a23a8b8eb8a89cc1a3554d4ddfc64e8

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

    def recommendations():
        """ gives recommendations based on user's answers regarding skin type, target concern and budget
        """

class Moisturizer:
    def __init__():
        """ Initializes a Moisturizer object. 
        """
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
class Eye_Cream:
    def __init__(): 
        """ Initializes an Eye Cream object.
        """
class Sun_Protection:
    def __init__(): 
        """ Initializes a Sun Protection object. 
        """

def main (): 
    dataset_path = 'skincare_dataset.csv'
    recommender = SkincareRecommender(dataset_path)
    skinType, targetConcern, budget = userQuestions()

if __name__ == "__main__":
    main() 



 

