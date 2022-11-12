import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#df_FEBio_disp_mag = pd.read_csv('FEBio_disp_mag_BFCubeV2.txt', delim_whitespace = True)
#df_FEBio_pressure = pd.read_csv('FEBio_pressure_BFCubeV2.txt', delim_whitespace = True)
#df_FEBio_stress = pd.read_csv('FEBio_stress_BFCubeV2.txt', delim_whitespace = True)

#FEBio_time = []
#FEBio_disp_mag = []
#FEBio_pressure= []
#FEBio_stress = []


#for i in range (len(df_FEBio_disp_mag)) :

#    FEBio_time.append(df_FEBio_disp_mag.iloc[i][0])
#    FEBio_disp_mag.append(df_FEBio_disp_mag.iloc[i][1])
#    FEBio_pressure.append(df_FEBio_pressure.iloc[i][1])
#    FEBio_stress.append(df_FEBio_stress.iloc[i][1])


df_CEOS_disp_mag_dt_01 = pd.read_csv('DispMag_dt_0.1.dat', delim_whitespace = True)
df_CEOS_pressure_dt_01 = pd.read_csv('Pressure_dt_0.1.dat', delim_whitespace = True)
df_CEOS_disp_mag_dt_005 = pd.read_csv('DispMag_dt_0.05.dat', delim_whitespace = True)
df_CEOS_pressure_dt_005 = pd.read_csv('Pressure_dt_0.05.dat', delim_whitespace = True)

CEOS_time_dt_01 = []
CEOS_disp_mag_dt_01 = []
CEOS_pressure_dt_01 = []
CEOS_time_dt_005 = []
CEOS_disp_mag_dt_005  = []
CEOS_pressure_dt_005 = []


for i in range(len(df_CEOS_disp_mag_dt_01)):

    CEOS_time_dt_01.append(df_CEOS_disp_mag_dt_01.iloc[i][0])
    CEOS_disp_mag_dt_01.append(df_CEOS_disp_mag_dt_01.iloc[i][1])
    CEOS_pressure_dt_01.append(df_CEOS_pressure_dt_01.iloc[i][1])

for i in range(len(df_CEOS_disp_mag_dt_005)):

    CEOS_time_dt_005.append(df_CEOS_disp_mag_dt_005.iloc[i][0])
    CEOS_disp_mag_dt_005.append(df_CEOS_disp_mag_dt_005.iloc[i][1])
    CEOS_pressure_dt_005.append(df_CEOS_pressure_dt_005.iloc[i][1])

for i in range ( len(CEOS_time_dt_01) ) :

    CEOS_time_dt_01[i] = float(CEOS_time_dt_01[i])

for i in range(len(df_CEOS_disp_mag_dt_005)):

    CEOS_time_dt_005[i] = float(CEOS_time_dt_005[i])


print(' CEOS time (dt = 0.1) = ', CEOS_time_dt_01)
print(' CEOS time (dt = 0.05) = ', CEOS_time_dt_005)

print(' CEOS disp_mag (dt = 0.1) = ', CEOS_disp_mag_dt_01)
print(' CEOS disp_mag (dt = 0.05) = ', CEOS_disp_mag_dt_005)

print(' CEOS pressure (dt = 0.1) = ', CEOS_pressure_dt_01)
print(' CEOS pressure (dt = 0.05) = ', CEOS_pressure_dt_005)

df_FEBio_disp_mag_dt_01 = pd.read_csv('Febio_DispMag_dt_0.1.txt', delim_whitespace = True)
df_FEBio_pressure_dt_01 = pd.read_csv('Febio_pressure_dt_0.1.txt', delim_whitespace = True)
df_FEBio_disp_mag_dt_005 = pd.read_csv('Febio_DispMag_dt_0.05.txt', delim_whitespace = True)
df_FEBio_pressure_dt_005 = pd.read_csv('Febio_pressure_dt_0.05.txt', delim_whitespace = True)

FEBio_time_dt_01 = []
FEBio_disp_mag_dt_01 = []
FEBio_pressure_dt_01 = []
FEBio_time_dt_005 = []
FEBio_disp_mag_dt_005 = []
FEBio_pressure_dt_005 = []


for i in range(len(df_FEBio_disp_mag_dt_01)):

    FEBio_time_dt_01.append(df_FEBio_disp_mag_dt_01.iloc[i][0])
    FEBio_disp_mag_dt_01.append(df_FEBio_disp_mag_dt_01.iloc[i][1])
    FEBio_pressure_dt_01.append(df_FEBio_pressure_dt_01.iloc[i][1])

for i in range(len(df_FEBio_disp_mag_dt_005)):

    FEBio_time_dt_005.append(df_FEBio_disp_mag_dt_005.iloc[i][0])
    FEBio_disp_mag_dt_005.append(df_FEBio_disp_mag_dt_005.iloc[i][1])
    FEBio_pressure_dt_005.append(df_FEBio_pressure_dt_005.iloc[i][1])

for i in range ( len(FEBio_time_dt_01) ) :

    FEBio_time_dt_01[i] = float(FEBio_time_dt_01[i])

for i in range(len(df_FEBio_disp_mag_dt_005)):

    FEBio_time_dt_005[i] = float(FEBio_time_dt_005[i])


print(' FEBio time (dt = 0.1) = ', FEBio_time_dt_01)
print(' time (dt = 0.05) = ', FEBio_time_dt_005)

print(' FEBio disp_mag (dt = 0.1) = ', FEBio_disp_mag_dt_01)
print(' FEBio disp_mag (dt = 0.05) = ', FEBio_disp_mag_dt_005)

print(' FEBio pressure (dt = 0.1) = ', FEBio_pressure_dt_01)
print(' FEBio pressure (dt = 0.05) = ', FEBio_pressure_dt_005)


plt.plot(CEOS_time_dt_01, CEOS_disp_mag_dt_01, 'b', label='CEOS dt = 0.1', marker = '*')
plt.plot(CEOS_time_dt_005, CEOS_disp_mag_dt_005, 'r', label = 'CEOS dt = 0.05', marker = '.')
plt.plot(FEBio_time_dt_01, FEBio_disp_mag_dt_01, 'g', label='FEBio dt = 0.1', marker = '*')
plt.plot(FEBio_time_dt_005, FEBio_disp_mag_dt_005, 'y', label = 'FEBio dt = 0.05', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo - CEOS')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()

plt.plot(CEOS_time_dt_01, CEOS_pressure_dt_01, 'b', label='CEOS dt = 0.1', marker = '*')
plt.plot(CEOS_time_dt_005, CEOS_pressure_dt_005, 'r', label = 'CEOS dt = 0.05', marker = '.')
plt.plot(FEBio_time_dt_01, FEBio_pressure_dt_01, 'g', label='FEBio dt = 0.1', marker = '*')
plt.plot(FEBio_time_dt_005, FEBio_pressure_dt_005, 'y', label = 'FEBio dt = 0.05', marker = '.')
plt.title('pressão efetiva no nó x tempo - CEOS')
plt.xlabel('Tempo')
plt.ylabel('presão efetiva no nó')
plt.legend()
plt.show()

