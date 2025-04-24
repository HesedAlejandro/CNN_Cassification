# Proyecto de Clasificación y Captura de Gestos con Cámara

Este proyecto permite capturar gestos con una cámara, crear datasets personalizados y realizar clasificación de imágenes (por ejemplo, tipo CIFAR) utilizando modelos entrenados previamente. Todo el código principal se organiza en la carpeta src.

## 📁 Estructura del Proyecto


├── main.py               # Menú principal para ejecutar los scripts
├── src/                  # Scripts principales
│   ├── camara.py         # Captura de video desde webcam
│   ├── cifar_classification.py  # Clasificación de imágenes tipo CIFAR
│   └── dataset_creation.py      # Creación de dataset a partir de la webcam
├── data/                 # Carpeta sugerida para almacenar datasets
│   ├── train/
│   ├── valid/
│   └── test/
├── trained_model_parameters/    # Parámetros de modelos entrenados
├── .gitignore            # Archivo para ignorar carpetas y archivos no deseados
└── README.md             # Documentación del proyecto


## ▶️ Cómo ejecutar

1. Asegúrate de tener instalado Python y las dependencias necesarias (como opencv, torch, etc).
2. Ejecuta el menú principal:
bash
python main.py

3. Elige una opción:
   - *1:* Inicia la cámara en tiempo real
   - *2:* Ejecuta la clasificación de imágenes usando un modelo
   - *3:* Crea un dataset personalizado capturando imágenes de la webcam

## 📦 Requisitos

Instala los paquetes necesarios con:
bash
pip install -r requirements.txt


(Nota: Asegúrate de tener un archivo requirements.txt con los módulos requeridos por src/)

## 📂 Carpetas importantes

- src/: Contiene toda la lógica del proyecto.
- data/: Directorios de entrenamiento, validación y prueba para el modelo.
- trained_model_parameters/: Archivos .pth o similares para modelos preentrenados.

## 📌 Notas adicionales
- Asegúrate de que cada archivo en src/ tenga definida una función main().
- Los datos en data/ no se suben al repositorio (están en .gitignore).
- Puedes adaptar la estructura a tus necesidades agregando nuevos módulos o scripts.

---

¡Listo para capturar y clasificar tus propios gestos! ✌️