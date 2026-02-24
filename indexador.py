import chromadb
import json
import os
import shutil

# 1. OPCIONAL: Borrar base anterior para evitar duplicados cada vez que pruebes
if os.path.exists("./db_vectorial"):
    shutil.rmtree("./db_vectorial")

client = chromadb.PersistentClient(path="./db_vectorial")
# Creamos la colección
collection = client.get_or_create_collection(name="metadatos_sql")

def indexar_catalogo():
    with open('catalogo_semantico.json', 'r', encoding='utf-8') as f:
        catalogo = json.load(f)

    # Preparamos las listas para insertar todo en un solo bloque (más eficiente)
    documentos = []
    metadatos = []
    ids = []

    for i, tabla in enumerate(catalogo):
        texto = f"Tabla: {tabla['nombre_amigable']}. Descripción: {tabla['descripcion']}. Área: {tabla['area']}"
        documentos.append(texto)
        metadatos.append({"nombre_tecnico": tabla['nombre_tecnico']})
        ids.append(f"id_{i}")
    
    # Insertamos todo el bloque
    collection.add(
        documents=documentos,
        metadatas=metadatos,
        ids=ids
    )
    
    print(f"Se han indexado {len(catalogo)} tablas.")
    print(f"Total actual en la base: {collection.count()}")

def buscar_tabla(query):
    # Verificamos si hay algo antes de buscar
    if collection.count() == 0:
        print("La base está vacía. Revisa el archivo JSON.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=1
    )
    
    if results['metadatas'][0]:
        print(f"\n Buscando: '{query}'")
        print(f"Tabla sugerida: {results['metadatas'][0][0]['nombre_tecnico']}")
        print(f"Contexto encontrado: {results['documents'][0][0]}")
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    indexar_catalogo()
    buscar_tabla("¿Dónde puedo ver las ventas?")