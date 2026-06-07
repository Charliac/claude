# 09 — Auditoría de imágenes/gifs + acomodo (v3)

> Fecha: 2026-06-07 · El cliente subió fotos a las reseñas + un bloque de imágenes/gifs al final.
> Se auditaron visualmente y se reubicaron por impacto en conversión.

## A. Reseñas (arregladas)

Problema: avatares mal puestos (uno dentro de la foto de reseña, dos dentro de la fila de "me gusta"), reseñas con texto placeholder viejo, divs vacíos.

Solución: cada reseña ahora con `img.fbp-av` (avatar circular) + `img.fbp-img` (foto full-width) limpios.

| Reseña | Avatar | Foto de reseña |
|---|---|---|
| Daniela R. (recetas) | 2_16 (mujer) | rs3 (producto en mano) |
| Marco T. (moto/firmeza) | ezgif (hombre) | rs2 (puesto en el pecho) |
| Gabriela P. (Android/Reels) | Diseno_15 (mujer) | rs1 (unboxing) |
| Rodrigo V. (gym/comodidad) | inicial "R" | — (solo texto) |
| Andrea S. (multi-compra) | inicial "A" | — (solo texto) |

> 3 avatares + 3 fotos reales disponibles → asignados a 3 reseñas (avatar+foto); las otras 2 quedan con inicial (look auténtico, mezcla real).

## B. Imágenes en el cuerpo (cada una en su sección de máxima conversión)

| Imagen | Contenido | Ubicación |
|---|---|---|
| **s6** | Lifestyle "Innovación y Practicidad" | HERO (arriba) |
| **giphy_977c3d61.gif** | Demo en movimiento | SOLUCIÓN ("1 segundo") |
| **s4** | "Compatible con tu mundo" iPhone/Android | bloque Android |
| **s7** | "Imán potente, agarre seguro" V/H | sección "¿se cae?" |
| **s8** | "Rotación 360°" | después de Beneficios |
| **s2** | "Tomas POV inmersivas" (6 usos) | "mil formas de usarlo" |
| **0001-b** | "Crea contenido en primera persona" (4 usos) | "Para quién es" |
| **s5** | "Liberación rápida — un clic" | "3 pasos" |
| **s3** | "Magic POV vs Otros" | antes de la tabla VS |
| **s1** | Producto (3 paneles) | Especificaciones |
| **rs1/rs2/rs3** | Fotos reales de uso | dentro de reseñas |

## C. NO usadas (y por qué) — recomendación

- **giphy_1.gif (4 MB)**: demasiado pesada, ni carga; mataría la velocidad en móvil. → Convertir a MP4 o comprimir <1 MB antes de usar.
- **gempages.webp (2.2 MB) y el gif usado (2.6 MB)**: muestran logos de **otras marcas (TELESIN/REYGEAK)**. El gif se dejó solo en 1 lugar (motion vende), pero conviene **recortar el logo** o reemplazar por un gif propio. gempages quedó fuera por peso + marca.

## D. Pendientes de optimización (velocidad = conversión)
- Comprimir TODAS las imágenes a <300–500 KB (s1 PNG pesa 519 KB → pasar a WebP).
- Convertir el gif a MP4 (90% menos peso).
- Verificar en móvil que ninguna imagen empuje el botón de compra demasiado abajo (sticky cart recomendado).
