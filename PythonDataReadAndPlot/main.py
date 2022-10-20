import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#with open('DispMag FEBio.txt', 'r', encoding = 'utf-8') as FEBioData:
    #FEBio_vec = FEBioData.readlines()

#print(FEBio_vec)

#print(FEBio_vec[5])


df_FEBio = pd.read_csv('DispMag FEBio.txt', delim_whitespace = True)
#print(df_FEBio.head())
#print(df_FEBio.info())
#print(df_FEBio.iloc[3][1])

FEBio_time = []
FEBio_disp_mag = []

for i in range (len(df_FEBio)) :

    FEBio_time.append(df_FEBio.iloc[i][0])
    FEBio_disp_mag.append(df_FEBio.iloc[i][1])



df1_CEOS = pd.read_csv('DispMag node42 CEOS-Osmotic step1.dat', delim_whitespace = True)

CEOS_time = []
CEOS_disp_mag = []

for i in range(len(df1_CEOS) - 1):

    CEOS_time.append(df1_CEOS.iloc[i][0])
    CEOS_disp_mag.append(df1_CEOS.iloc[i][1])


df2_CEOS = pd.read_csv('DispMag node42 CEOS-Osmotic.dat', delim_whitespace = True)

for i in range(len(df2_CEOS) - 1):

    CEOS_time.append(df2_CEOS.iloc[i][0])
    CEOS_disp_mag.append(df2_CEOS.iloc[i][1])


for i in range ( len(CEOS_time) ) :

    CEOS_time[i] = float(CEOS_time[i])

print('FEBio_time = ', FEBio_time)
print('CEOS_time = ', CEOS_time)
print('CEOS_disp_mag = ', CEOS_disp_mag)
print('FEBio_disp_mag = ', FEBio_disp_mag)

#CEOS_time[-1] = float(CEOS_time[-1])
#print('CEOS_time = ', CEOS_time)


plt.plot(FEBio_time, FEBio_disp_mag, 'b', label='FEBio')
plt.plot(CEOS_time, CEOS_disp_mag, 'r', label = 'CEOS')
plt.title('Magnitude do deslocamento do Nó x tempo ')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()





