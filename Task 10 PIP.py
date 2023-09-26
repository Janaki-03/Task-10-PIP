import requests
import re

url = "https://raw.githubusercontent.com/rvsp/typescript-oops/master/Practice/music-player.md"

try:
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    # Define a regular expression pattern to match PlantUML diagrams
    pattern = r'```plantuml([\s\S]*?)```'

    # Search for and print all PlantUML diagrams in the content
    diagrams = re.findall(pattern, content)
    for i, diagram in enumerate(diagrams):
        print(f"UML Diagram {i + 1}:")
        print(diagram)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")