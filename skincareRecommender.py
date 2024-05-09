"""
Names: Nazifa Ullah & Selam Kebede 
Assignment: Final Project - Final Project 
Date: 5/9/2024 
"""

import sys
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

        self.df = pd.read_csv(path)

    def userQuestions(self, skintype, targetConcern, budget):
        """Asks the user questions about their skin, including their skin type, their skincare concern, and their budget.

        Returns:
            None
        """
        skintype = input("What is your skinstype?")
        targetConcern = input("From the list provided, what is your top skin concern? Dryness, Acne, Dull Skin, Sun Protection ")
        budget = float(input("What is your budget?"))

        return skintype, targetConcern, budget 

class SkincareRecommender:
    """_summary_
    """
    def __init__(self, dataset_path):
        """ Initializes the Skincare Recommender object. 
        """
        self.products_df = pd.read_csv(dataset_path)

    def userQuestions(self):
        """ asks the user questions about their skin 
        """
        skintype = input("What is your skinstype?")
        targetConcern = input("What is your skin concern?")

    def recommend_products(self, skintype, targetConcern): 
        pass 

class Moisturizer:
    def __init__(self, list, brand, price):
        """ Initializes a Moisturizer object. 
        """
        self.list = list
        moisturizer_list = [] 
        obj = Moisturizer()
        obj = brand 
        obj = price
        print(obj.brand)
        print(obj.price)

        """
        moisturizer = ("What is your skintype? (Choose 1-5, 1: Combo, 2: Dry, 3: Normal, 4: Oily, 5: Sensitive)")
        skin_types = ["Combo", "Dry", "Normal", "Oily", "Sensitive"]
        """
        budget = ("What is your budget?")
        """for budget"""

        for skintype in skin_types:
            print(skin_type) 

            print("Mostuizer brand: ", moisturizer.brand)
            print("Mostuizer price: ", moisturizer.price)

    def main(path): 
        dataset_path = 'skincare_dataset.csv'
        recommender = SkincareRecommender(dataset_path)
        recommender.userQuestions()

        product_list = []
        with open(path, 'r') as file:
            for line in file:
                product_list.append(line.strip()) 

        for product in product_list: 

            if skintype in product: 
                print(f"The product{product} is suitable for your skin type.")    
        
        return product_list
          
class Cleanser: 
    def __init__(self, rank): 
        """ Initializes a Cleanser object.  
        """
        if list legnth > i = 
            reset = {cleanser} with the biggest rating 
class Treatment:   
    def __init__():
        """ Initializes a Treatment object.
        """
        if targetConcern == "acne": 
            return "salicylic acid"
        elif targetConcern == "anti aging": 
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
    skintype, targetConcern = userQuestions()

    skincarerecommender = []
    with open(path, 'r') as file:
        newfile = file.readlines()

        moisturizer = [] 
        cleanser = [] 
        treatment = []
        face_mask = []
        eye_cream = []
        sun_protection = []

        str.splitlines()




if __name__ == "__main__":
    main("skincare_dataset.txt") 
    print (Skincare) 
