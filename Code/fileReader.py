import csv
import numpy as np
population_2010 = []
value_errors = ['--', 'NA']
country_exceptions = ['North America', 'Eurasia', 'Middle East', 'Europe', 'World',
'Country', 'Asia & Oceania', 'Africa', 'Central & South America']

with open("D:\Escuela\Semestre_3\IoT_Repositories\A01028470_Databases\TextFiles\populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
         if row[-1] not in value_errors and row[0] not in country_exceptions:
               population_2010.append([float(row[-1]), row[0]])

greenhouse_2010 = np.array([],[])
wrong_years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1998',
                '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
                '2011','2012','2013','2014']
with open("D:\Escuela\Semestre_3\IoT_Repositories\A01028470_Databases\TextFiles\greenhouse_gas_inventory_data_data.csv") as csvFile2:
    reader2 = csv.reader(csvFile2)
    for row in reader2:
        if row==1:
            row=row+1 
            continue
        if row[1] not in wrong_years and row[0] not in greenhouse_2010:
            greenhouse_2010[row]=[row[0], row[2]]


population_2010.sort(reverse=True)
print(population_2010[:5])


#The most contaminant countries are China, India, United States, Indonesia, and Brazil
