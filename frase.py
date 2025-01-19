import requests # type: ignore
import urllib3 # type: ignore
import subprocess
import textwrap

# Desactivar advertencias de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get("https://api.quotable.io/random", verify=False)
if response.status_code == 200:
    data = response.json()
    phrase = data['content']
    author = data['author']

    # Usar translate-shell para traducir
    command = f"trans :es \"{phrase}\""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    lines = result.stdout.splitlines()
    
    # Verificar si hay suficientes líneas para evitar errores
    if len(lines) >= 3:
        translated_phrase = lines[2]  # Obtener la tercera línea
    else:
        translated_phrase = "No se pudo traducir la frase."

    # Formatear el texto con sangría
    indent = " " * 2  # Espacios de sangría (2 en este caso)        

    # Imprimir la frase traducida con formato
    translated_block = textwrap.fill(f"{translated_phrase}", width=60)
    translated_block = textwrap.indent(translated_block, indent)
    
    print("\nLa frase de hoy es:\n")
    print(translated_block)
    print(f"\n{indent}- {author}\n")
else:
    print("No se pudo obtener la frase célebre")
