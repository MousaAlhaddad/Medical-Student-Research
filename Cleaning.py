# Load the needed packages 
import numpy as np
import pandas as pd

# Added on 2019-04-16
# Define a new method that is useful for going from a continuous variable to a categorical variable (very close to pandas.cut)
def cut(Value, CutPoints = [1,2,3]):
    for x in range(1,len(CutPoints)):
        if Value <= CutPoints[x]:
                return ">{} & <={}".format(CutPoints[x-1],CutPoints[x])
    if Value > CutPoints[-1]:
        return ">%s" %x

# Load the data as a pandas DataFrame with the exclusion of the unneeded columns
File = '2019-04-16 Original Data.xlsx'
Columns = ['PMID', 'Journal Title', 'Journal ISO','Journal Country', 'Journal Impact Factor',
       'Impact Factor Without Journal Self Cites', 'Five Year Impact Factor',
       'Publication Year', 'Article Title', 'Research Type',
       'Paper Country', 'Citation Counts','Number of Authors', 'Number of Student Authors',
       'Percentage of Students', 'Is 1st Author a Student', 'Solely by students']
df = pd.read_excel(File,usecols=Columns)

# Remove the "Not Available" values from the "Five Year Impact Factor" column
df["Five Year Impact Factor"] = [x if x != "Not Available" else np.NAN for x in df["Five Year Impact Factor"]]

# Rename the the columns' names to enable method chaining
df.columns=[x.replace(" ", "_") for x in list(df.columns)]
