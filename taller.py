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

# Ejercicio 14
print(data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10))

# Ejercicio 15
print(data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
)

# Ejercicio 16
print(data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10))

# Ejercicio 17
print(data.groupby(['Nombre departamento', 'Nombre municipio']
                   ).size().sort_values(ascending=False))

# Ejercicio 18
print(data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']
                   ).size().sort_values(ascending=False))

# Ejercicio 19
print(data.groupby(['Nombre departamento',
      'Nombre municipio', 'Sexo']).Edad.mean())

# Ejercicio 20
print(data.groupby('Nombre del país').size().sort_values(ascending=False))

# Ejercicio 21
print(data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False))

# Ejercicio 22
mortalidad = (
    (len(data[data['Ubicación del caso'] == 'Fallecido'])) * 100) / (len(data))
recuperacion = (
    (len(data[data['Recuperado'] == 'Recuperado'])) * 100) / (len(data))

print(f'Mortalidad: {mortalidad} \n Recuperacion: {recuperacion}')

# Ejercicio 23
print('Mortalidad:')
print((data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre departamento').size() / data['ID de caso'].max())*100)
print('Recuperacion: ')
print((data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size() / data['ID de caso'].max())*100)

# Ejercicio 24
print('Mortalidad:')
print((data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre municipio').size() / data['ID de caso'].max())*100)
print('Recuperacion: ')
print((data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size() / data['ID de caso'].max())*100)

# Ejercicio 25
print(data.groupby(
    ['Nombre municipio', 'Ubicación del caso']).size().sort_values())

# Ejercicio 26
print(data.groupby(['Nombre municipio', 'Sexo']).Edad.mean())

# Ejercicio 27
# Contagiados
plt.plot(data.groupby('Fecha de diagnóstico').size().sort_values())
plt.show()
# Fallecidos
plt.plot(data[data['Ubicación del caso'] ==
              'Fallecido'].groupby('Fecha de diagnóstico').size().sort_values())
plt.show()
# Recuperados
plt.plot(data[data['Recuperado'] ==
              'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values())
plt.show()

# Ejercicio 28
# Contagiados
plt.plot(data.groupby('Nombre departamento').size(
).sort_values(ascending=False).head(10))
plt.show()
# Fallecidos
plt.plot(data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10))
plt.show()
# Recuperados
plt.plot(data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10))
plt.show()

# Ejercicio 29
plt.plot(data.groupby('Nombre municipio').size().sort_values(
    ascending=False).head(10))
plt.show()
# Fallecidos
plt.plot(data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10))
plt.show()
# Recuperados
plt.plot(data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10))
plt.show()

# Ejercicio 30
print(data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Edad').size().sort_values(ascending=False))

# Ejercicio 31
print((data.groupby('Ubicación del caso').size() /
      data['ID de caso'].max()) * 100)

# Ejercicio 32
data.groupby('Ubicación del caso').size().sort_values().plot(kind='bar')
plt.show()

# Ejercicio 33
data.groupby('Sexo').size().sort_values().plot(kind='bar')
plt.show()

# Ejercicio 34
data.groupby('Tipo de contagio').size().sort_values().plot(kind='bar')
plt.show()

# Ejercicio 35
# Contagiados
data.groupby('Fecha de diagnóstico').size().sort_values().plot(kind='bar')
plt.show()
# Fallecidos
data[data['Ubicación del caso'] == 'Fallecido'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(kind='bar')
plt.show()
# Recuperados
data[data['Recuperado'] == 'Recuperado'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot(kind='bar')
plt.show()