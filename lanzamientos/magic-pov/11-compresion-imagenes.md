# 11 — Compresión de imágenes (v5)

> Fecha: 2026-06-07 · Objetivo: bajar el peso de la página (velocidad = conversión).

## Resultado de compresión (Pillow → WebP)
| Imagen | Antes | Después |
|---|---|---|
| s1 (PNG hero specs) | 507 KB | **34 KB** |
| s2 | 223 KB | 116 KB |
| s3–s8 | ~100–127 KB c/u | 44–54 KB |
| 0001-b (uso) | 242 KB | 124 KB |
| rs3 | 142 KB | 86 KB |
| avatar Daniel (jpg) | 97 KB | 6 KB |
| **GIF demo** | **2.622 KB** | **107 KB (cuadro estático webp)** |
| **Total set** | ~4 MB+ | **~0,8 MB** |

## Qué se subió y reemplazó en la página (en vivo)
- **`pov-s1.webp` (34 KB)** → reemplaza el PNG de 507 KB en la sección Especificaciones.
- **`pov-demo.webp` (107 KB)** → reemplaza el **GIF de 2,6 MB** en la sección Solución.
- Subidas vía `stagedUploadsCreate` → POST GCS → `fileCreate` → CDN de Shopify.

## Por qué solo esos dos archivos
- El resto de imágenes ya son **WebP** y **Shopify CDN las sirve auto-comprimidas (WebP/AVIF + resize)** en la entrega. Re-subirlas daba ganancia marginal con alto riesgo (firmas de carga).
- Los dos pesos reales eran el **GIF (no se auto-optimiza)** y el **PNG**. Esos se reemplazaron.

## Pendiente recomendado
- El gif quedó como **imagen estática**. Para movimiento real y liviano: convertir a **MP4** (no había ffmpeg en el entorno) y subirlo como video de Shopify.
- Si querés, puedo subir también las versiones comprimidas de s2/s6/0001-b/rs3 (ya generadas en /tmp) para minimizar aún más el archivo fuente.

## Otros puntos de la sesión
- Bundles ×1/×2/×3: se gestionan en **EasySell** (variante única en Shopify a Bs 279).
- Contador de reseñas (+9.389): lo ajusta el cliente en su app de reseñas.
- Botón de compra: se usa el de **EasySell** (color del tema no aplica).
- Reseña #1 "Daniel R.": es hombre → nombre + foto coinciden.
