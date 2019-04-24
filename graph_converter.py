import pandas as pd
import numpy as np
import datetime



class data_model():
    series = None 

    def __init__(self, data):
        self.series = pd.read_csv('/home/domdom/Desktop/downloads/TechCrunchcontinentalUSA.csv')
    
    def find_max_money(self):
        company_money = self.series[['company', 'raisedAmt']]
        max_money = company_money[ company_money['raisedAmt'] == company_money['raisedAmt'].max()]
        return max_money
