import chromadb

# Conectamos a la base ya existente
client = chromadb.PersistentClient(path="./db_vectorial")
collection = client.get_collection(name="metadatos_sql")

conteo = collection.count()
print(f"--- Sistema listo. Tablas en memoria: {conteo} ---")

if conteo == 0:
    print("Error: La base de datos está vacía.")
else:
    # 1. El input debe estar vacío o pedir la pregunta al usuario
    pregunta_usuario = input("\n¿Qué quieres buscar? (Escribe aquí): ")
    
    # 2. Hacemos la consulta
    results = collection.query(
        query_texts=[pregunta_usuario], 
        n_results=1
    )
    
    # 3. Formateamos la salida para verla bien
    if results['metadatas'] and results['metadatas'][0]:
        tabla = results['metadatas'][0][0]['nombre_tecnico']
        # Accedemos al documento (la descripción que guardamos)
        descripcion = results['documents'][0][0]
        
        print("\n TABLA ENCONTRADA:")
        print(f"--- Nombre: {tabla}")
        print(f"--- Info: {descripcion}")
    else:
        print("\n No se encontraron resultados para esa búsqueda.")