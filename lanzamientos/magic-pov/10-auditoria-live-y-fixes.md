# 10 — Auditoría de la página en vivo (v4) + fixes

> URL: charliac.shop/products/soporte-cuello-magnetico-pov-manos-libres
> Fecha: 2026-06-07 · Estado: ACTIVE (en vivo)

## Puntaje
- **Contenido/CRO (HTML + imágenes):** 8.9/10 (sólido)
- **Resultado EN VIVO tal como estaba:** 🔴 **3/10** — porque mostraba **"AGOTADO"** = 0% de conversión posible.
- **Tras los fixes de esta sesión:** ~8.5/10 (pendiente: bundles + contador de reseñas + color botón).

## 🔴 Críticos
1. **"Agotado" (RESUELTO).** Producto ACTIVE con 1 variante, `tracked:false`, `DENY`, qty 0 → el tema lo mostraba sin stock y el botón muerto.
   - Fix aplicado: `inventoryPolicy: CONTINUE` + tracking ON + **stock 250**.
2. **Variantes 3 → 1 (PENDIENTE decisión).** Quedó solo "Default Title" (Bs 279). La descripción sigue mostrando packs ×1/×2/×3 ("MÁS ELEGIDO", value stack) que **no se pueden comprar**. → Restaurar los 3 bundles (recomendado, recupera AOV + efecto señuelo) o quitar los packs de la descripción.

## 🟠 Altos
3. **Contador de reseñas inconsistente.** El widget arriba del título muestra **"+9.389 reseñas"** (viene de la app de reseñas del tema), mientras la descripción dice **"+380 opiniones"**. 9.389 no es creíble para un lanzamiento y se contradice. → Igualar en la app a un número creíble (~380–800). El metafield `reviews.rating_count` ya está en 380, pero el widget usa la app, no ese campo.
4. **Botón de compra verde.** Sigue verde; debe ser **naranja/rojo** (máximo contraste) — Theme settings → Colors.

## 🟡 Menores
5. **"Daniel R."** (reseña #1) con foto de perfil femenina + "mis recetas/mi emprendimiento" → cambiar a "Daniela R." o usar avatar masculino.
6. **Se quitó la barra de 5 emoji-benefits** dentro de la descripción (quedó un `<span class="e">` vacío en el hook). Reponer o limpiar.
7. **Peso de imágenes/gif** (velocidad = conversión): comprimir a <300–500 KB; gif → MP4.

## ✅ Lo que está muy bien
- Hero, prueba social, problema→solución, Android, "no se cae", beneficios, multi-uso, "para quién es", incluye, 3 pasos, contra-entrega, VS, specs, 5 reseñas (avatar+foto), garantía, oferta con value stack + escasez, FAQ, cierre. Imágenes infográficas bien ubicadas y renderizando.
- 8 imágenes en galería, secciones completas, sin elementos rotos.
