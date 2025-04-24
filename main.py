import sys
from pathlib import Path

# Agregar la carpeta 'src' al path para poder importar los módulos
src_path = Path(__file__).parent / 'src'
sys.path.append(str(src_path))

# Importar las funciones principales desde cada script
from src.camara import cam
from src.cifar_classification import main as cifar_main
from src.dataset_creation import main as dataset_main

def main():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar cámara")
    print("2. Ejecutar clasificación CIFAR")
    print("3. Crear dataset con webcam")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        cam()
    elif opcion == '2':
        cifar_main()
    elif opcion == '3':
        dataset_main()
    elif opcion == '4':
        print("👋 Saliendo del programa.")
    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")

if __name__ == '__main__':
    main()

