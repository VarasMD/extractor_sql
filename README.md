# 🧠 SQL Semantic Search
### Buscador Inteligente de Tablas con IA

Este proyecto utiliza **Inteligencia Artificial** y una **Base de Datos Vectorial (ChromaDB)** para encontrar tablas en una base de datos SQL Server mediante lenguaje natural. En lugar de buscar por palabras clave exactas, el sistema entiende el **contexto y la intención** detrás de la consulta.

---

## 🚀 Características

* **Indexación Semántica:** Transforma descripciones técnicas en vectores de significado (embeddings).
* **Búsqueda Natural:** Responde a preguntas como *"¿Dónde están los saldos de los usuarios?"* identificando la tabla técnica correcta.
* **Eficiencia Local:** Basado en `ChromaDB`, lo que permite búsquedas instantáneas sin llamadas constantes a APIs externas.
* **Modelo de Lenguaje:** Utiliza el modelo `all-MiniLM-L6-v2` para un procesamiento ligero y preciso.



---

## 🛠️ Tecnologías

* **Lenguaje:** Python 3.10+
* **IA:** ChromaDB & Sentence-Transformers.
* **Formato de Datos:** JSON para el catálogo maestro.

---

## 📂 Estructura del Proyecto

```text
├── db_vectorial/          # Base de datos vectorial (local)
├── indexador.py           # Script para cargar/actualizar el catálogo
├── consulta.py            # Interfaz de búsqueda interactiva
├── catalogo_semantico.json # Diccionario de metadatos de SQL
├── .gitignore             # Archivos excluidos de Git
└── README.md              # Documentación
