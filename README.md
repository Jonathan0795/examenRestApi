# examenRestApi

Preguntas
1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente.
   Análisis de datos: Procesar, limpiar y analizar grandes cantidad de datos.
   Big Data: Manejar y procesar grandes volúmenes de datos con herramientas como PySpark o Dask.
   Web Scraping: Extracción de datos de sitios web, usa herramientas como BeautifulSoup, selenium.
   Machine Learning e Inteligencia Artificial: Entrenar modelos predictivos y de aprendizaje profundo usando Scikit-learn, TensorFlow.
   Aplicaciones web: Creacion de apis, fronted y backend, herramientas como Django, FastApi.
2. ¿Cómo se diferencian Flask de Django? Argumentar.
   Flask es un microframework ligero, ideal para proyecto pequeños y apis , tiene una curva de aprendizaje alta.
   Django un framework más completo, su curva de aprendizaje es algo más complejam ideal para proyectos grandes.
3. ¿Qué es un API? Explicar en sus propias palabras.
   Herramientas que permiten la comunicación y el intercambio de datos entre programas. Permite que una aplicación obtenga datos de un servidor o utilice servicios de terceros, como mapas o pagos en línea.

Levantar FastApi
1. Cambiar las credenciales en la conexion a MYSQL.
2. Crear Base de datos.
3. Insertar datos de prueba.

CREATE DATABASE ALUMNOS_CIBERTEC;

INSERT INTO tb_alumnos (nombre, apellido, documento) 
VALUES 
    ('Juan', 'Perez', '78952315'),
    ('María', 'López', '42368915'),
    ('Carlos', 'García', '10698745'),
    ('Lucía', 'Martínez', '63124596');