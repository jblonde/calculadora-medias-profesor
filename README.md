# 🧮 Calculadora de Medias para Profesores

Aplicación desarrollada en Python para calcular rápidamente la media de las notas de los alumnos.

## Características

- Interfaz gráfica sencilla.
- Introducción de notas separadas por comas.
- Soporte para números enteros y decimales.
- Cálculo instantáneo de la media.
- Posibilidad de pulsar **Enter** para agilizar la corrección.
- Preparada para generar un ejecutable `.exe` para Windows.

## Ejemplo de uso

Introducir:

```text
7.5, 8, 6.25, 9
```

Resultado:

```text
Media: 7.69
```

## Requisitos

- Python 3.x

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/calculadora-medias-profesor.git
```

Acceder al directorio:

```bash
cd calculadora-medias-profesor
```

Ejecutar:

```bash
python media_notas.py
```

## Crear ejecutable (.exe)

Instalar PyInstaller:

```bash
pip install pyinstaller
```

Generar el ejecutable:

```bash
pyinstaller --onefile --windowed media_notas.py
```

El archivo ejecutable se generará en:

```text
dist/media_notas.exe
```

## Tecnologías utilizadas

- Python
- Tkinter
- PyInstaller

## Captura de pantalla

<img width="375" height="209" alt="image" src="https://github.com/user-attachments/assets/f5e62d39-e75b-4ed4-b3dd-3cf03e286a7e" />



## Autor

Joaquim Rubio Fernández

## Licencia

Proyecto de uso libre para fines 
