import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_FEBio_disp_mag = pd.read_csv('FEBio_disp_mag_BFCubeV2.txt', delim_whitespace = True)
#df_FEBio_pressure = pd.read_csv('FEBio_pressure_BFCubeV2.txt', delim_whitespace = True)
#df_FEBio_stress = pd.read_csv('FEBio_stress_BFCubeV2.txt', delim_whitespace = True)

FEBio_time = []
FEBio_disp_mag = []
FEBio_pressure= []
FEBio_stress = []


for i in range (len(df_FEBio_disp_mag)) :

    FEBio_time.append(df_FEBio_disp_mag.iloc[i][0])
    FEBio_disp_mag.append(df_FEBio_disp_mag.iloc[i][1])
    #FEBio_pressure.append(df_FEBio_pressure.iloc[i][1])
    #FEBio_stress.append(df_FEBio_stress.iloc[i][1])


df_CEOS_disp_mag = pd.read_csv('CEOS_disp_mag_BFCubeV2.dat', delim_whitespace = True)
#df_CEOS_pressure = pd.read_csv('CEOS_pressure_BFCubeV2.dat', delim_whitespace = True)
#df_CEOS_stress = pd.read_csv('CEOS_stress_BFCubeV2.dat', delim_whitespace = True)

CEOS_time = []
CEOS_disp_mag = []
CEOS_pressure = []
CEOS_stress = []

for i in range(len(df_CEOS_disp_mag)):

    CEOS_time.append(df_CEOS_disp_mag.iloc[i][0])
    CEOS_disp_mag.append(df_CEOS_disp_mag.iloc[i][1])
    #CEOS_pressure.append(df_CEOS_pressure.iloc[i][1])
    #CEOS_stress.append(df_CEOS_stress.iloc[i][1])

for i in range ( len(CEOS_time) ) :

    CEOS_time[i] = float(CEOS_time[i])



print('FEBio time = ', FEBio_time)
print('CEOS time = ', CEOS_time)

#print('FEBio pressure = ', FEBio_pressure)
#print('CEOS pressure = ', CEOS_pressure)

print('FEBio disp mag = ', FEBio_disp_mag)
print('CEOS disp mag = ', CEOS_disp_mag)

#print('FEBio stress = ', FEBio_stress)
#print('CEOS stress = ', CEOS_stress)



plt.plot(FEBio_time, FEBio_disp_mag, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time, CEOS_disp_mag, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()
