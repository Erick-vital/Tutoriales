## Bloque

un bloque representa items que han sido encontrados dentro de un documento

Cada bloque tiene un tipo, que indica el tipo de contenido que contiene. Los tipos de bloque incluyen:

  - PAGE: representa una página completa del documento.
  - LINE: representa una línea de texto.
  - WORD: representa una palabra de texto.
  - TABLE: representa una tabla de información estructurada.
  - CELL: representa una celda en una tabla.
  - KEY_VALUE_SET: representa un par clave-valor.

El tipo de un bloque en AWS Textract se determina según el contenido que contenga en la imagen de entrada.

Cuando AWS Textract procesa una imagen, analiza el contenido de la imagen y genera varios bloques que representan diferentes secciones del contenido de la imagen, como texto, líneas, palabras, tablas, etc. Cada bloque se asigna automáticamente a un tipo de bloque en función del contenido que contenga.
