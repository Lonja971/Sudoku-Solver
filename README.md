# Sudoku Solver

Dit is een geanimeerde oplosser voor klassieke 9x9 Sudoku puzzels geschreven in Python met colorma voor kleurenuitvoer. Het algoritme gebruikt stap-voor-stap backtracking, met visualisatie van het oplossingsproces in de terminal.

## De opmaak van het sudoku-veld

Het veld wordt doorgegeven als een lijst van woordenboeken, waarbij elk woordenboek één bekende waarde beschrijft:

```python
[
    { "row": 0, "col": 0, "num": 5 },
    { "row": 0, "col": 1, "num": 3 },
    { "row": 0, "col": 4, "num": 7 },
    ...
]
```

Velden:

- **row** - rij-index (0-8)
- **col** - kolomindex (0-8)
- **num** - beginnummer (1-9)