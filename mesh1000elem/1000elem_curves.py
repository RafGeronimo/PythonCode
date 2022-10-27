import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_FEBio_disp_mag_1000elem = pd.read_csv('FEBio_disp_mag_1000elem.txt', delim_whitespace = True)
df_FEBio_pressure_1000elem = pd.read_csv('FEBio_pressure_1000elem.txt', delim_whitespace = True)

FEBio_time_1000elem = []
FEBio_disp_mag_1000elem = []
FEBio_pressure_1000elem = []


for i in range (len(df_FEBio_disp_mag_1000elem)) :

    FEBio_time_1000elem.append(df_FEBio_disp_mag_1000elem.iloc[i][0])
    FEBio_disp_mag_1000elem.append(df_FEBio_disp_mag_1000elem.iloc[i][1])
    FEBio_pressure_1000elem.append(df_FEBio_pressure_1000elem.iloc[i][1])


df_CEOS_disp_mag_1000elem = pd.read_csv('CEOS_disp_mag_1000elem.dat', delim_whitespace = True)
df_CEOS_pressure_1000elem = pd.read_csv('CEOS_pressure_1000elem.dat', delim_whitespace = True)

CEOS_time_1000elem = []
CEOS_disp_mag_1000elem = []
CEOS_pressure_1000elem = []

for i in range(len(df_CEOS_disp_mag_1000elem)):

    CEOS_time_1000elem.append(df_CEOS_disp_mag_1000elem.iloc[i][0])
    CEOS_disp_mag_1000elem.append(df_CEOS_disp_mag_1000elem.iloc[i][1])
    CEOS_pressure_1000elem.append(df_CEOS_pressure_1000elem.iloc[i][1])


for i in range ( len(CEOS_time_1000elem) ) :

    CEOS_time_1000elem[i] = float(CEOS_time_1000elem[i])



print('FEBio time = ', FEBio_time_1000elem)
print('FEBio pressure = ', FEBio_pressure_1000elem)
print('FEBio disp mag = ', FEBio_disp_mag_1000elem)

print('CEOS time = ', CEOS_time_1000elem)
print('CEOS pressure = ', CEOS_pressure_1000elem)
print('CEOS disp mag = ', CEOS_disp_mag_1000elem)


plt.plot(FEBio_time_1000elem, FEBio_disp_mag_1000elem, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_1000elem, CEOS_disp_mag_1000elem, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()



plt.plot(FEBio_time_1000elem, FEBio_pressure_1000elem, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_1000elem, CEOS_pressure_1000elem, 'r', label = 'CEOS', marker = '.')
plt.title('pressão efetiva x tempo')
plt.xlabel('Tempo')
plt.ylabel('pressão efetiva')
plt.legend()
plt.show()