# Sudoku Solver

Een interactieve Sudoku-oplosser in de terminal, geschreven in Python.
Het programma leest Sudoku-borden uit `.json` bestanden in de map `boards/` en lost ze stap voor stap op met animatie.

## Vereisten

- Externe module:
  - `colorama`

Installeer afhankelijkheden via pip:

```bash
pip install colorama
```

## Gebruik

1. Zorg ervoor dat je JSON-bestanden in de map `boards/` plaatst.
2. Start het script:
```bash
python main.py
```
3. Kies een bord uit de weergegeven lijst.
4. Het geselecteerde Sudoku-bord wordt getoond en opgelost in realtime.


## JSON-formaat

Een geldig Sudoku-bordbestand moet een lijst zijn van objecten met rijnummer, kolomnummer en het getal:

```python
[
    { "row": 0, "col": 0, "num": 5 },
    { "row": 0, "col": 1, "num": 3 },
    { "row": 0, "col": 4, "num": 7 }
]
```

- `row`: Rij-index (0 t/m 8)
- `col`: Kolom-index (0 t/m 8)
- `num`: Ingevuld getal (1 t/m 9)