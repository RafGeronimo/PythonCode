import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_FEBio_disp_mag_CF0_50 = pd.read_csv('DISP_MAG_FEBio_CF0_50.txt', delim_whitespace = True)

FEBio_time_CF0_50 = []
FEBio_disp_mag_CF0_50 = []


for i in range (len(df_FEBio_disp_mag_CF0_50 )) :

    FEBio_time_CF0_50.append(df_FEBio_disp_mag_CF0_50.iloc[i][0])
    FEBio_disp_mag_CF0_50.append(df_FEBio_disp_mag_CF0_50.iloc[i][1])



df_CEOS_disp_mag_CF0_50 = pd.read_csv('DISP_MAG_CEOS_CF0_50.dat', delim_whitespace = True)

CEOS_time_CF0_50 = []
CEOS_disp_mag_CF0_50 = []

for i in range(len(df_CEOS_disp_mag_CF0_50)):

    CEOS_time_CF0_50.append(df_CEOS_disp_mag_CF0_50.iloc[i][0])
    CEOS_disp_mag_CF0_50.append(df_CEOS_disp_mag_CF0_50.iloc[i][1])


for i in range ( len(CEOS_time_CF0_50) ) :

    CEOS_time_CF0_50[i] = float(CEOS_time_CF0_50[i])


plt.plot(FEBio_time_CF0_50, FEBio_disp_mag_CF0_50, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_CF0_50, CEOS_disp_mag_CF0_50, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo (CF0 = 50 mM)')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
#plt.legend()
#plt.show()



df_FEBio_disp_mag_CF0_25 = pd.read_csv('DISP_MAG_FEBio_CF0_25.txt', delim_whitespace = True)

FEBio_time_CF0_25 = []
FEBio_disp_mag_CF0_25 = []


for i in range (len(df_FEBio_disp_mag_CF0_25 )) :

    FEBio_time_CF0_25.append(df_FEBio_disp_mag_CF0_25.iloc[i][0])
    FEBio_disp_mag_CF0_25.append(df_FEBio_disp_mag_CF0_25.iloc[i][1])



df_CEOS_disp_mag_CF0_25 = pd.read_csv('DISP_MAG_CEOS_CF0_25.dat', delim_whitespace = True)

CEOS_time_CF0_25 = []
CEOS_disp_mag_CF0_25 = []

for i in range(len(df_CEOS_disp_mag_CF0_25)):

    CEOS_time_CF0_25.append(df_CEOS_disp_mag_CF0_25.iloc[i][0])
    CEOS_disp_mag_CF0_25.append(df_CEOS_disp_mag_CF0_25.iloc[i][1])


for i in range ( len(CEOS_time_CF0_25) ) :

    CEOS_time_CF0_25[i] = float(CEOS_time_CF0_25[i])


plt.plot(FEBio_time_CF0_25, FEBio_disp_mag_CF0_25, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_CF0_25, CEOS_disp_mag_CF0_25, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo (CF0 = 25 mM)')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()