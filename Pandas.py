import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('2.csv')

# Filtrar por las columnas 'dirección de correo' y 'nombre completo'
df['Nombre Completo'] = df['Nombre'] + ' ' + df['Apellido Paterno'] + ' ' + df['Apellido Materno']
df_filtered = df[['Dirección de correo electrónico', 'Nombre Completo']]

# Guardar el resultado en un nuevo archivo CSV
df_filtered.to_csv('lista.csv', index=False)
print(df_filtered)