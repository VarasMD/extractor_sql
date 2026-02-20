import json
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Cargar la API Key desde el archivo .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def cargar_esquema():
    with open('esquema_db.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def enriquecer_metadatos():
    esquema_crudo = cargar_esquema()
    
    # Agrupar columnas por tabla para enviarlas juntas
    tablas = {}
    for item in esquema_crudo:
        nombre_tabla = item['tabla']
        if nombre_tabla not in tablas:
            tablas[nombre_tabla] = []
        tablas[nombre_tabla].append(f"{item['columna']} ({item['tipo']})")

    catalogo_enriquecido = []

    print(f"Iniciando enriquecimiento de {len(tablas)} tablas...")

    for nombre_tabla, columnas in tablas.items():
        print(f"--- Procesando: {nombre_tabla} ---")
        
        # El "Prompt": Las instrucciones para la IA
        prompt = f"""
        Actúa como un experto en arquitectura de datos y SQL. 
        Analiza la siguiente tabla y sus columnas de una base de datos empresarial.
        
        TABLA: {nombre_tabla}
        COLUMNAS: {', '.join(columnas)}
        
        Devuelve un objeto JSON estrictamente con este formato:
        {{
            "nombre_tecnico": "{nombre_tabla}",
            "nombre_amigable": "Nombre legible en español",
            "descripcion": "Explicación breve de para qué sirve esta tabla",
            "area": "Ventas/RRHH/Contabilidad/etc"
        }}
        Solo devuelve el JSON, nada de texto extra.
        """

        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant", # Modelo rápido y eficiente
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"} # Forzamos respuesta JSON
            )
            
            # Guardar la respuesta de la IA
            resultado = json.loads(completion.choices[0].message.content)
            catalogo_enriquecido.append(resultado)
            
        except Exception as e:
            print(f"Error procesando {nombre_tabla}: {e}")

    # Guardar el resultado final
    with open('catalogo_semantico.json', 'w', encoding='utf-8') as f:
        json.dump(catalogo_enriquecido, f, indent=4, ensure_ascii=False)
    
    print("\n ¡Catálogo semántico generado con éxito!")

if __name__ == "__main__":
    enriquecer_metadatos()