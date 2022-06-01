import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data.csv')

data['Tipo de contagio'].replace(
    ['comunitaria'], ['Comunitaria'], inplace=True)
data['Nombre departamento'].replace(
    ['Tolima', 'Caldas', 'Santander', 'Cundinamarca'], ['TOLIMA', 'CALDAS', 'SANTANDER', 'CUNDINAMARCA'], inplace=True)
data.Sexo.replace(['m', 'f'], ['M', 'F'], inplace=True)
data['Ubicación del caso'].replace(
    ['CASA', 'casa'], ['Casa', 'Casa'], inplace=True)


# Ejercicio 1
print(data['ID de caso'].count())

# Ejercicio 2
print(data['Nombre municipio'].unique().size)

# Ejercicio 3
print(data['Nombre municipio'].unique())

# Ejercicio 4
print(len(data[data['Ubicación del caso'] == 'Casa']))

# Ejercicio 5
print(len(data[data['Recuperado'] == 'Recuperado']))

# Ejercicio 6
print(len(data[data['Ubicación del caso'] == 'Fallecido']))

# Ejercicio 7
print(data.groupby('Tipo de contagio').size().sort_values(ascending=False))

# Ejercicio 8
print(data['Nombre departamento'].unique().size)

# Ejercicio 9
print(data['Nombre departamento'].unique())

# Ejercicio 10
print(data.groupby('Ubicación del caso').size().sort_values(ascending=False))

# Ejercicio 11
print(data.groupby('Nombre departamento').size(
).sort_values(ascending=False).head(10))

# Ejercicio 12
print(data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10))

# Ejercicio 13
print(data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10))