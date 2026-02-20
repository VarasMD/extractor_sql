import pyodbc
import json

# --- CONFIGURACIÓN ---
# Si tu SQL es local, puedes usar 'localhost' o '.'
# Si es una instancia con nombre, usa 'SERVIDOR\\INSTANCIA'
server = '(localdb)\Local' 
database = 'CallCenter'

# Usamos el Driver 17 que confirmamos que tienes
connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

def extraer_esquema():
    # Query para traer solo tablas base del usuario (evita vistas de sistema)
    query = """
    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA = 'dbo'
    ORDER BY TABLE_NAME, ORDINAL_POSITION
    """
    
    esquema_lista = []
    
    print(f"Intentando conectar a {database}...")
    
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(query)
        
        filas = cursor.fetchall()
        
        for row in filas:
            esquema_lista.append({
                "tabla": row.TABLE_NAME,
                "columna": row.COLUMN_NAME,
                "tipo": row.DATA_TYPE
            })
            
        # Guardado en JSON
        with open('esquema_db.json', 'w', encoding='utf-8') as f:
            json.dump(esquema_lista, f, indent=4, ensure_ascii=False)
            
        print(f"¡Éxito! Se procesaron {len(filas)} columnas.")
        print("Revisa el archivo 'esquema_db.json' en tu carpeta.")
        
    except Exception as e:
        print(f"\n[ERROR] Error de conexión:")
        print(f"Mensaje: {e}")
        print("\nTip: Revisa que el nombre del servidor y la base de datos sean correctos.")

if __name__ == "__main__":
    extraer_esquema()