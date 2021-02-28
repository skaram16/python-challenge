#import my dependencies
import os
import csv


#create a file path for the data
budget_data_path = os.path.join("../PyBank/Resources/budget_data.csv")


#open and read the data path
with open(budget_data_path) as budget_data_file:
    reader = csv.reader(budget_data_file)
