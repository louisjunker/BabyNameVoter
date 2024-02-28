#This script is used to import the Danish names.
#The data is downloaded here: 
#And consist of three .xlsx datasets containing names for boys, girls and boths.
import pandas as pd

def import_data():
    #Importing Excel Data
    df_name1 = pd.read_excel("data/beggedele.xlsx")
    df_name2 = pd.read_excel("data/drengenavne.xlsx")
    df_name3 = pd.read_excel("data/pigenavne.xlsx")
    #Appending to one dataframe
    df_name = pd.concat([df_name1, df_name2, df_name3], ignore_index=True)
    # Replacing dummy text with numbers.
    df_name.replace({'Ja': 1, 'Nej': 0}, inplace=True)
    # Renaming to English.
    df_name = df_name.rename(columns={'Navn' : 'Name', 'Drengenavn' : 'Male', 'Pigenavn':'Female'})
    # Saving the file.
    df_name.to_csv('data/Names_officialVersion.csv') #Be careful changing this!!!
