import pandas as pd

df = pd.read_excel(r'C:\Users\dou\PycharmProjects\dress\Attribute DataSet.xlsx')


for index, row in df.iterrows():
    print(row['Dress_ID'],row['Style'],row['Price'],row['Rating'],row['Size'],row['Season'],row['NeckLine'],row['SleeveLength'],row['waiseline'],row['Material'],row['FabricType'],row['Decoration'],row['Pattern Type'],row['Recommendation'])