\# Detector de homoglifos v1.0



Herramienta de consola en Python que detecta caracteres no ASCII

(homoglifos) en el dominio de un mail o una URL. Un homoglifo es un

carácter de otro alfabeto que se ve igual a una letra latina, y se usa

en ataques de phishing (por ejemplo, la "а" cirílica en vez de la "a").



\## Requisitos

\- Python 3

\- Sin dependencias externas (solo librería estándar)



\## Uso

```

python detector_homoglifos.py

```

El menú permite analizar un mail, una URL o salir.



\## Ejemplo

Entrada: `usuario@раураl.com`



```

Dominio:  раураl.com

SOSPECHOSO

Posicion 0 : р CYRILLIC SMALL LETTER ER se parece a: p

Posicion 1 : а CYRILLIC SMALL LETTER A se parece a: a

Posicion 2 : у CYRILLIC SMALL LETTER U se parece a: y

Posicion 3 : р CYRILLIC SMALL LETTER ER se parece a: p

Posicion 4 : а CYRILLIC SMALL LETTER A se parece a: a

```



\## Qué hace

\- Extrae el dominio de un mail o de una URL.

\- Marca cada carácter fuera del ASCII, con su posición y nombre Unicode.

\- Indica a qué letra latina se parece (tabla limitada).



\## Limitaciones

\- No detecta dominios que usan solo ASCII, como `paypa1.com`

&#x20; o `rnicrosoft.com`.

\- Las vocales con tilde (á, é...) se consideran válidas.

\- La tabla de equivalencias es pequeña (3 caracteres).

\- Rechaza URLs que contienen `@`.



\## Mejoras previstas

\- Ampliar la tabla de equivalencias.

\- Detectar sustituciones ASCII como `1` por `l`.

