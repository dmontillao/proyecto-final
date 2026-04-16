import pandas as pd

# 1. Cargar el archivo original 

print("Leyendo datos_contratacion.csv...")
df = pd.read_csv('datos_contratacion.csv', sep=',', low_memory=False)

# 2. Convertir a Parquet (comprimido)
print("Comprimiendo a datos_secop.parquet...")
df.to_parquet('datos_secop.parquet', index=False)

print("¡Proceso terminado con éxito!")