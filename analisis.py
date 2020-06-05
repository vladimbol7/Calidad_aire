#!/home/programacion1/.linuxbrew/bin/python3
#PBS -N Datos
#PBS -e Datos.err
#PBS -o Datos.out
#PBS -l nodes=4:ppn=16
#PBS -M vladimirimbol83117@correo.itm.edu.co
#PBS -m b

import pandas as pd
import glob

vector = ['/home/programacion1/Data/estacion_data_calidadaire_12_20190101_20190131.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190201_20190228.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190301_20190331.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190401_20190430.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190501_20190531.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190601_20190630.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190701_20190731.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190801_20190831.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20190901_20190930.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20191001_20191031.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20191101_20191130.csv',
          '/home/programacion1/Data/estacion_data_calidadaire_12_20191201_20191231.csv']

for i in range(12):
    df = pd.read_csv(vector[i])
    print(df.info())
    df2 = df[(df['calidad_pm25'] < 2.6) & (df['calidad_pm10'] < 2.6)]
    df3 = df2.iloc[:, 0:6]
    df3.columns = ['Fecha', 'codigoSerial', 'pm2.5', 'calidad_pm2.5', 'pm10', 'calidad_pm10']
    if i == 0: path = 'enero'
    if i == 1: path = 'febrero'
    if i == 2: path = 'marzo'
    if i == 3: path = 'abril'
    if i == 4: path = 'mayo'
    if i == 5: path = 'junio'
    if i == 6: path = 'julio'
    if i == 7: path = 'agosto'
    if i == 8: path = 'septiembre'
    if i == 9: path = 'octubre'
    if i == 10: path = 'noviembre'
    if i == 11: path = 'diciembre'
    
    if i < 9:
        camino = '/home/programacion1/Data/BaseDatos/_0' + str(i+1) + '_estacion_data_calidadaire_12_' + path + '.csv'
    else:
        camino = '/home/programacion1/Data/BaseDatos/_' + str(i+1) + '_estacion_data_calidadaire_12_' + path + '.csv'
    df3.to_csv(camino)
    print('\n\n')
    print(df3.head(1))
    print(df3.info())

    
filenames = glob.glob('/home/programacion1/Data/BaseDatos/*.csv')
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)
big_frame.columns = ['N', 'Fecha', 'codigoSerial', 'pm2.5', 'calidad_pm2.5', 'pm10', 'calidad_pm10']
big_frame.to_csv('/home/programacion1/Data/BaseDatos/_00_estacion_data_calidadaire_12_anual.csv')
