import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://dayz.fandom.com/wiki/List_of_ranged_weapons"

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontrar todos los elementos que contienen los nombres de las armas
    weapon_elements = soup.find_all("li", class_="gallerybox")
    
    # Extraer los nombres de las armas y guardarlos en un archivo
    with open("ranged_weapons.txt", "w") as file:
        for weapon_element in weapon_elements:
            name = weapon_element.find("div", class_="gallerytext").text.strip()
            file.write(name + "\n")
    print("Los nombres de las armas de fuego han sido guardados en 'ranged_weapons.txt'.")
else:
    print("No se pudo acceder a la página.")