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
        df(DataFrame): contains skincare products

    Methods:
        userQuestions: asks users questions about their skincare needs/budget.
    
    """
    def __init__(self, path):
        """Initializes a skincare object.
        
        Args:
            path: provides the path
        
        """

        self.df = pd.read_csv(path)

    def userQuestions(self, skintype, targetConcern, budget):
        """Asks the user questions about their skin, including their skin type, their skincare concern, and their budget.

        Args:
            skintype(str): the user's type of skin
            targetConcern(str): the user's main target concern for their skin
            budget(float): the user's budget

        Returns:
            None
        """
        skintype = input("What is your skinstype?")
        targetConcern = input("From the list provided, what is your top skin concern? Dryness, Acne, Dull Skin, Sun Protection ")
        budget = float(input("What is your budget?"))

        return skintype, targetConcern, budget 

class SkincareRecommender:
    """The skincare recommender based on input.

    Attributes:
        dataset_path: provides a path
        skintype(str): the user's type of skin
        targetConcern(str): the user's main target concern
    """
    def __init__(self, dataset_path):
        """ Initializes the Skincare Recommender object.

        Args:
            dataset_path: provides a path to the dataset
        """
        self.products_df = pd.read_csv(dataset_path)

    def userQuestions(self):
        """ Asks the user questions about their skin.

       """
        skintype = input("What is your skinstype?")
        targetConcern = input("What is your skin concern?")

    def recommend_products(self, skintype, targetConcern):
        """Recommends products to user.

        Args:
            skintype(str): the user's skintype
            targetConcern(str): the user's main concern regarding their skincare
        """
        pass 

class Moisturizer:
    """A class that focuses on the moisturizer products.

    Attributes:
        list(list): provides a list of moisturizers
        brand(str): provides the different brands of moisturizers
        price(float): provides the different prices
    """
    def __init__(self, list, brand, price):
        """ Initializes a Moisturizer object.

        Args:
            list(list): provides a list of moisturizers
            brand(str): provides the different brands of moisturizers
            price(float): provides the different prices
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
        """Reads the dataset and outputs a message if match is found.

        Args:
            path(str): provides a file path to products
        
        Returns:
            product_list(list): list containing the products
        """
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
    """Class for cleanser products.
    
    """
    def __init__(self, rank): 
        """ Initializes a Cleanser object. 
        
        """
        if list legnth > i = 
            reset = {cleanser} with the biggest rating 
class Treatment:
    """Class for treatment products.
    
    """
    def __init__():
        """ Initializes a Treatment object.
        """
        if targetConcern == "acne": 
            return "salicylic acid"
        elif targetConcern == "anti aging": 
            return "retinol" 
        
class Face_Mask:
    """Class for face mask products.
    
    """
    def __init__():
        """ Initializes a Face Mask object.
        """
        face_mask = ("What is your skintype? (Choose 1-4, 1: Combo, 2: Dry, 3: Normal, 4: Oily, 5: Sensitive)")

        if "skincare_dataset" ==  

class Eye_Cream:
    """Class for eye cream products
    """
    
    def __init__(): 
        """ Initializes an Eye Cream object.
        """
        eye_cream = 
class Sun_Protection:
    """Class for products that provide sun protection.
    """
    def __init__(): 
        """ Initializes a Sun Protection object. 
        """

def main (path): 
    """Runs the skincare recommendation
    """
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
