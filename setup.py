def create_files():
    readme_content = """# Projektname

## Beschreibung
Dies ist eine Platzhalter-Beschreibung für dein Projekt.

## Installation
```sh
pip install -r requirements.txt
```

## Nutzung
```sh
python main.py
```

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
"""
    
    main_content = """# main.py

if __name__ == "__main__":
    print("Hello, World! Dies ist ein Platzhalter-Code.")
"""
    
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)
    
    with open("main.py", "w", encoding="utf-8") as main_file:
        main_file.write(main_content)
    
    print("README.md und main.py wurden erfolgreich erstellt.")

if __name__ == "__main__":
    create_files()
