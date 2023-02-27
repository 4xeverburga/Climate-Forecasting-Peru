import pandas as pd
""" Transforming the data from .txt to .csv """
file = pd.read_csv('C:/Users/ASUS/Documents/proyectos/Climate-Forecasting-Peru/src/data/data_precipitaciones/UCAYALI_ELMARONAL.txt', sep='\s+',header=None)
file_csv=file.to_csv('C:/Users/ASUS/Documents/proyectos/Climate-Forecasting-Peru/src/data/data_precipitaciones/UCAYALI_ELMARONAL.csv',header=None)

""" This was done with each of the regions of Peru """
""" The result of this is in the folder data_precipitaciones """