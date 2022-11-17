import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_FEBio_disp_mag = pd.read_csv('FEBio_disp_mag.txt', delim_whitespace = True)
df_FEBio_pressure = pd.read_csv('FEBio_pressure.txt', delim_whitespace = True)
#df_FEBio_stress = pd.read_csv('FEBio_stress_BFCubeV2.txt', delim_whitespace = True)

FEBio_time = []
FEBio_disp_mag = []
FEBio_pressure = []
#FEBio_stress = []


for i in range (len(df_FEBio_disp_mag)) :

    FEBio_time.append(df_FEBio_disp_mag.iloc[i][0])
    FEBio_disp_mag.append(df_FEBio_disp_mag.iloc[i][1])
    FEBio_pressure.append(df_FEBio_pressure.iloc[i][1])
#    FEBio_stress.append(df_FEBio_stress.iloc[i][1])


df_CEOS_disp_mag = pd.read_csv('CEOS_disp_mag.dat', delim_whitespace = True)
df_CEOS_pressure = pd.read_csv('CEOS_pressure.dat', delim_whitespace = True)
#df_CEOS_disp_mag_dt_005 = pd.read_csv('DispMag_dt_0.05.dat', delim_whitespace = True)
#df_CEOS_pressure_dt_005 = pd.read_csv('Pressure_dt_0.05.dat', delim_whitespace = True)

CEOS_time = []
CEOS_disp_mag = []
CEOS_pressure= []

for i in range(len(df_CEOS_disp_mag)):

    CEOS_time.append(df_CEOS_disp_mag.iloc[i][0])
    CEOS_disp_mag.append(df_CEOS_disp_mag.iloc[i][1])
    CEOS_pressure.append(df_CEOS_pressure.iloc[i][1])

for i in range ( len(CEOS_time) ) :

    CEOS_time[i] = float(CEOS_time[i])



print(' CEOS time = ', CEOS_time)
print(' FEBio time = ', FEBio_time)

print(' CEOS disp_mag = ', CEOS_disp_mag)
print(' FEBio disp_mag = ', FEBio_disp_mag)

print(' CEOS pressure = ', CEOS_pressure)
print(' FEBio pressure = ', FEBio_pressure)



plt.plot(CEOS_time, CEOS_disp_mag, 'r', label='CEOS', marker = '*')
plt.plot(FEBio_time, FEBio_disp_mag, 'b', label='FEBio', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()

plt.plot(CEOS_time, CEOS_pressure, 'r', label='CEOS', marker = '*')
plt.plot(FEBio_time, FEBio_pressure, 'b', label='FEBio', marker = '.')
plt.title('pressão efetiva nodal x tempo')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()