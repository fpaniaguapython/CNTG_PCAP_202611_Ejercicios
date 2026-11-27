# Proyecto Calculadora

Estructura básica de un proyecto Python con un módulo de operaciones
aritméticas (`calculadora`) y tests unitarios.

## Estructura

```
Proyecto_Calculadora/
├── pyproject.toml
├── README.md
├── calculadora/
│   ├── __init__.py
│   └── operaciones.py      # sumar, restar, multiplicar, dividir
└── tests/
    ├── __init__.py
    └── test_operaciones.py # tests unittest
```

## Tests

```bash
python -m unittest discover -s tests
# o bien
pytest
```

Estado: **estructura y firmas creadas; implementación pendiente.**
