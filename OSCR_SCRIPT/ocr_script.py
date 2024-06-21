from PIL import Image
import pytesseract

# Establecer la ruta al ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar la imagen
img_path = r"C:\Users\Deivid\Desktop\Text_To_Spech\imagen\python script1.webp"
print(f"Cargando imagen desde: {img_path}")

try:
    img = Image.open(img_path)
    print("Imagen cargada exitosamente.")
except FileNotFoundError:
    print("Error: No se encontró el archivo de imagen especificado.")
    exit()

# Realizar OCR para extraer texto de la imagen
try:
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
    print("OCR completado exitosamente.")
except Exception as e:
    print(f"Error durante el OCR: {e}")
    exit()

# Imprimir el texto extraído
print("Texto extraído:")
print(text)

# Guardar el texto extraído en un archivo
output_file = r"C:\Users\Deivid\Desktop\Text_To_Spech\Texto_Extraido.txt"
try:
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Texto guardado exitosamente en {output_file}")
except Exception as e:
    print(f"Error al guardar el texto en el archivo: {e}")
