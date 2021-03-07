#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:49:29 2021

@author: simonec
"""

import pandas as pd
import os
path1='/Users/simonec/Desktop/Mach_Lear_exercises/Exercises-redone-by-me-from-the-book/'
datapath = os.path.join(path1, "datasets", "lifesat", "")

oecd_bli = pd.read_csv(datapath + 'oecd_bli_2015.csv', thousands=',')
#Se tu gaurdi la tabella, cosi' come e' importata (puoi anche aprire questo file con excel se vuoi visualizzarlo tutto), vedrai che 
#i valori 'Value' sono tutti a destra e le gli stati si ripetono per ogni categoria 
#(per esempio 'Labor market insecurity'): prendi la colonna INEQUALITY 
# e vedi che c'e' 'TOT, poi MN (MEN) e poi WMN (WOMEN) , poi'High' , poi 'Low' .

#NOTA: se scarichi dal sit0 (https://stats.oecd.org/index.aspx?DataSetCode=BLI#),: il file excel (xls) vedrai la tabella come sul sito e quindi con diversa formattazione . Dal sito puoi scegliere dalla tendina, se vuoi "TOTAL", ""MEN", etc... 

#Prendi dunque solo i valori 'TOT' della colonna INEQUALITY (e' una scelta)
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=='TOT'] #come vedi in questo modo hai tolto molto righe dalla tabella

#Creiamo una tabella 'derivata' dall'originale utilazzando la funzione 'pivot', avendo come indici gli Stati, come colonne gli Indicatori (che adesso invece di essere sulle righe saranno i nomi delle colonne), e come valori la colnna 'Values' (l'unica dove ci sono i valori)
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")  

#To check the first 5 rows only of the 'Life satisfaction' column:
oecd_bli["Life satisfaction"].head()

#Now we retrieve the data for the GDP pro capita from : https://www.imf.org/en/Publications/SPROLLs/world-economic-outlook-databases#sort=%40imfdate%20descending (you have to choose 2016 in this case, and follow the steps and choose what you want. Download the report and then you save the file with .csv extension.)
