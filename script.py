import pandas as pd
from pymongo import MongoClient

# Conexión a la base de datos de MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.tenisAPT
collection = db.matches

# Leer el archivo CSV
archivo_csv = 'atp_tennis.csv'
df = pd.read_csv(archivo_csv)

# Convertir el DataFrame a una lista de diccionarios para insertar en MongoDB
data = df.to_dict(orient='records')

# Insertar datos en la colección
collection.insert_many(data)

print("Datos ingresados")

# Consulta en la colección de MongoDB
def consulta_mongodb():
    query = collection.find().limit(5)  # Limitado a los primeros 5 documentos por temas de vizualizacion
    for record in query:                # se puede retirar el limit y cargarias todos los datos.
        print(record)

# Llamar a la función de consulta para mostrar los resultados en la consola
consulta_mongodb()
