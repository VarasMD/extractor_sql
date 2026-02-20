# SQL-AI Metadata Bridge 🔗🤖

Este proyecto es el primer componente de un sistema **Text-to-SQL**. Permite extraer el esquema de una base de datos SQL Server y enriquecerlo semánticamente utilizando Inteligencia Artificial (Llama 3.1) para facilitar la interacción en lenguaje natural.

## 🚀 Características
- **Extracción Automática:** Obtiene tablas, columnas y tipos de datos mediante `pyodbc`.
- **Enriquecimiento Semántico:** Utiliza LLMs (vía Groq) para traducir nombres de tablas crípticos a conceptos de negocio.
- **Formato Interoperable:** Genera un catálogo en JSON listo para ser consumido por aplicaciones .NET, Angular o Motores de Búsqueda Vectorial.

## 🛠️ Tecnologías
- **Lenguaje:** Python 3.x
- **DB:** SQL Server
- **IA:** Groq Cloud (Llama 3.1 8b)
- **Librerías:** `pyodbc`, `python-dotenv`, `groq`

## 📋 Estructura del Proyecto
- `extractor.py`: Conecta a SQL Server y genera `esquema_db.json`.
- `enriquecedor.py`: Toma el esquema y genera `catalogo_semantico.json` con descripciones de IA.
- `.env`: Configuración de credenciales (Server, DB, API Key).

## ⏭️ Próximos Pasos
- Implementación de **ChromaDB** para búsqueda semántica de tablas.
- Integración con Backend .NET para generación dinámica de Queries SQL.
