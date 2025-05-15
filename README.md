# Sudoku Solver

Dit project is een sudokupuzzeloplosser. Het programma stelt je in staat om automatisch het sudoku-veld in te vullen en biedt ook de mogelijkheid om parameters zoals de snelheid van oplossen te configureren. Het ondersteunt ook het laden en opslaan van configuraties, inclusief het instellen van uitvoerkleuren.

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
3. Selecteer in het opdrachtblad `start`.
4. Kies een bord uit de weergegeven lijst.
5. Het geselecteerde Sudoku-bord wordt getoond en opgelost in realtime.


## JSON-formaat

Een geldig Sudoku-bordbestand moet een lijst zijn van objecten met rijnummer, kolomnummer en het getal:

```json
[
    { "row": 0, "col": 0, "num": 5 },
    { "row": 0, "col": 1, "num": 3 },
    { "row": 0, "col": 4, "num": 7 }
]
```

- `row`: Rij-index (0 t/m 8)
- `col`: Kolom-index (0 t/m 8)
- `num`: Ingevuld getal (1 t/m 9)