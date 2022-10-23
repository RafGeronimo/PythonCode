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


plt.plot(FEBio_time, FEBio_disp_mag, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time, CEOS_disp_mag, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo ')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()



df_FEBio_disp_mag_perm1 = pd.read_csv('FEBio_Disp_mag_Perm_1.txt', delim_whitespace = True)
df_FEBio_pressure_perm1 = pd.read_csv('FEBio_Pressure_Perm_1.txt', delim_whitespace = True)

FEBio_time_perm1 = []
FEBio_disp_mag_perm1 = []
FEBio_pressure_perm1 = []



for i in range (len(df_FEBio_disp_mag_perm1)) :

    FEBio_time_perm1.append(df_FEBio_disp_mag_perm1.iloc[i][0])
    FEBio_disp_mag_perm1.append(df_FEBio_disp_mag_perm1.iloc[i][1])
    FEBio_pressure_perm1.append(df_FEBio_pressure_perm1.iloc[i][1])



df_CEOS_disp_mag_perm1 = pd.read_csv('CEOS_Disp_Mag_Perm_1.dat', delim_whitespace = True)
df_CEOS_pressure_perm1 = pd.read_csv('CEOS_Pressure_Perm_1.dat', delim_whitespace = True)

CEOS_time_perm1 = []
CEOS_disp_mag_perm1 = []
CEOS_pressure_perm1 = []

for i in range(len(df_CEOS_disp_mag_perm1)):

    CEOS_time_perm1.append(df_CEOS_disp_mag_perm1.iloc[i][0])
    CEOS_disp_mag_perm1.append(df_CEOS_disp_mag_perm1.iloc[i][1])
    CEOS_pressure_perm1.append(df_CEOS_pressure_perm1.iloc[i][1])


for i in range ( len(CEOS_time_perm1) ) :

    CEOS_time_perm1[i] = float(CEOS_time_perm1[i])

print('================================================================')
print('PERMEABILIDADE k = 1')
print('FEBio_time = ', FEBio_time_perm1)
print('CEOS_time = ', CEOS_time_perm1)
print('CEOS_disp_mag = ', CEOS_disp_mag_perm1)
print('FEBio_disp_mag = ', FEBio_disp_mag_perm1)
print('CEOS_pressure = ', CEOS_pressure_perm1)
print('FEBio_pressure = ', FEBio_pressure_perm1)
print('================================================================')

plt.plot(FEBio_time_perm1, FEBio_disp_mag_perm1, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_perm1, CEOS_disp_mag_perm1, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo (PERMEABILIDADE k=1)')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()

plt.plot(FEBio_time_perm1, FEBio_pressure_perm1, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_perm1, CEOS_pressure_perm1, 'r', label = 'CEOS', marker = '.')
plt.title('Pressão nodal x tempo (PERMEABILIDADE k=1)')
plt.xlabel('Tempo')
plt.ylabel('Pressão Efetiva')
plt.legend()
plt.show()




df_FEBio_disp_mag_perm10 = pd.read_csv('FEBio_Disp_mag_Perm_10.txt', delim_whitespace = True)
df_FEBio_pressure_perm10 = pd.read_csv('FEBio_Pressure_Perm_10.txt', delim_whitespace = True)

FEBio_time_perm10 = []
FEBio_disp_mag_perm10 = []
FEBio_pressure_perm10 = []



for i in range (len(df_FEBio_disp_mag_perm10)) :

    FEBio_time_perm10.append(df_FEBio_disp_mag_perm10.iloc[i][0])
    FEBio_disp_mag_perm10.append(df_FEBio_disp_mag_perm10.iloc[i][1])
    FEBio_pressure_perm10.append(df_FEBio_pressure_perm10.iloc[i][1])



df_CEOS_disp_mag_perm10 = pd.read_csv('CEOS_Disp_Mag_Perm_10.dat', delim_whitespace = True)
df_CEOS_pressure_perm10 = pd.read_csv('CEOS_Pressure_Perm_10.dat', delim_whitespace = True)

CEOS_time_perm10 = []
CEOS_disp_mag_perm10 = []
CEOS_pressure_perm10 = []

for i in range(len(df_CEOS_disp_mag_perm10)):

    CEOS_time_perm10.append(df_CEOS_disp_mag_perm10.iloc[i][0])
    CEOS_disp_mag_perm10.append(df_CEOS_disp_mag_perm10.iloc[i][1])
    CEOS_pressure_perm10.append(df_CEOS_pressure_perm10.iloc[i][1])


for i in range ( len(CEOS_time_perm10) ) :

    CEOS_time_perm10[i] = float(CEOS_time_perm10[i])

print('================================================================')
print('PERMEABILIDADE k = 10')
print('FEBio_time = ', FEBio_time_perm10)
print('CEOS_time = ', CEOS_time_perm10)
print('CEOS_disp_mag = ', CEOS_disp_mag_perm10)
print('FEBio_disp_mag = ', FEBio_disp_mag_perm10)
print('CEOS_pressure = ', CEOS_pressure_perm10)
print('FEBio_pressure = ', FEBio_pressure_perm10)
print('================================================================')

plt.plot(FEBio_time_perm10, FEBio_disp_mag_perm10, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_perm10, CEOS_disp_mag_perm10, 'r', label = 'CEOS', marker = '.')
plt.title('Magnitude do deslocamento do Nó x tempo (PERMEABILIDADE k=10)')
plt.xlabel('Tempo')
plt.ylabel('Magnitude do deslocamento')
plt.legend()
plt.show()

plt.plot(FEBio_time_perm10, FEBio_pressure_perm10, 'b', label='FEBio', marker = '*')
plt.plot(CEOS_time_perm10, CEOS_pressure_perm10, 'r', label = 'CEOS', marker = '.')
plt.title('Pressão nodal x tempo (PERMEABILIDADE k=10)')
plt.xlabel('Tempo')
plt.ylabel('Pressão Efetiva')
plt.legend()
plt.show()




