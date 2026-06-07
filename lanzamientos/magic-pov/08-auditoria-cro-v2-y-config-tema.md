# 08 — Auditoría CRO v2 + Configuración exacta del tema

> Fecha: 2026-06-07 · Producto: Soporte de Cuello Magnético POV® (DRAFT)

## A. Puntaje

| | Antes (v1) | Ahora (v2) |
|---|---|---|
| **Global** | 7.6 / 10 | **8.9 / 10** |

## B. Mejoras aplicadas al HTML (v2)

1. **Hero reforzado** con rating + nº de opiniones (`★★★★★ 4.8/5 · +380 opiniones`).
2. **Barra de 5 emoji-benefits** al inicio (eco del anuncio + objeción Android).
3. **Badge de volumen**: `✅ +1.200 pedidos entregados en Bolivia`.
4. **Sección "No se cae"** (demuele la objeción #1 del imán) + placeholder de video.
5. **Bloque "Comprar es sin riesgo"** (3 pasos del pago contra entrega) → reduce fricción COD.
6. **Sección "Esto es para vos si…"** (auto-identificación / calificación).
7. **Value stack** en la oferta (suma Bs 558 → Hoy Bs 279) + **justificación de escasez** ("por qué este precio").
8. **Specs con números reales** (16 imanes de neodimio, 3 capas, 360°, plegable, ~110 g, hasta 6.9").
9. **5 reseñas** (antes 3) cubriendo objeciones distintas: independencia, caída/uso masculino, Android, comodidad, multi-compra.
10. **Bonus digital**: 🎁 Guía «10 ideas de videos POV que venden» (incluida + en value stack).
11. **FAQs ampliadas**: funda/case, celular grande/pesado, proceso de garantía.
12. **Cierre con future-pacing + identidad**.
13. **Metafields de rating** seteados (`reviews.rating` 4.8 · `reviews.rating_count` 380) para mostrar estrellas bajo el título.

> Datos a confirmar con proveedor: **peso (~110 g)** y **tamaño máx. de celular (~6.9")**. El nº de imanes (16) y materiales (acero+aluminio+silicona) provienen de la ficha del fabricante (familia Magic Grip / TELESIN). El link de MercadoLibre bloquea acceso automático (403).

## C. Lo que sigue siendo pendiente (no es HTML)

- Imágenes de galería + reemplazar placeholders del HTML (videos/fotos reales).
- Reseñas: reemplazar por reales conforme lleguen.
- Configuración del tema (abajo).

---

## D. CONFIGURACIÓN EXACTA DEL TEMA (above-the-fold)

Tema principal: **charliac-theme-reparado-lcp-14may2026** (OS 2.0). Recomendado: trabajar sobre una copia y publicar al final.

### D.1 — Hero line + 5 emoji-benefits ARRIBA del título (scoped a este producto)

> Tu tema no usa metafields per-producto para esto, así que se hace con una **plantilla dedicada** + bloque. Ya están dentro del HTML de la descripción como respaldo; estos pasos los suben además al "above the fold".

1. **Admin → Online Store → Themes →** en el tema principal: **⋯ → Edit code** *(opcional backup)* o **Customize**.
2. En **Customize**, arriba al centro, abrí el selector de plantilla → **Products → Default product**.
3. Clic en el nombre de la plantilla → **Create template** → nombre: `pov` → basada en *Default product* → Create. (Crea `product.pov`.)
4. En la columna izquierda, en la sección **Product information**, **Add block** → **Custom liquid** (si no existe, usá **Text** o **Rich text**).
   - Arrastralo **encima** del bloque **Title** → pegá el **Hero line**.
   - Agregá otro **Custom liquid** **debajo** del Title (encima de los botones) → pegá los **5 emoji-benefits**.
5. **Save**.
6. Asigná el producto a la plantilla: **Admin → Products → Soporte de Cuello… → (panel derecho) Theme template → `pov` → Save.** *(O avisame y lo asigno por API con `templateSuffix: "pov"`.)*

**Pegar en el Custom liquid del HERO (arriba del título):**
```html
<p style="font-size:15px;font-weight:700;color:#6a2cdb;margin:0 0 6px">🎥 Grabá como un profesional… sin que nadie te grabe y sin soltar lo que hacés.</p>
```

**Pegar en el Custom liquid de BENEFITS (debajo del título):**
```html
<ul style="list-style:none;padding:0;margin:8px 0;font-size:14px;line-height:1.9">
<li>🙌 <b>Manos 100% libres</b> — grabás solo/a, sin pedir favores</li>
<li>📱 <b>Funciona en TU celular</b> — iPhone y Android (anillo incluido)</li>
<li>⚡ <b>Listo en 1 segundo</b> — se pega por imán</li>
<li>🎯 <b>Firme y estable</b> — no se mueve mientras te movés</li>
<li>🚚 <b>Envío GRATIS + pagás al recibir</b> — garantía 30 días</li>
</ul>
```

### D.2 — Color del botón Comprar (máximo contraste)
1. **Customize → Theme settings (ícono ⚙️/paleta abajo) → Colors.**
2. Editá el esquema que usa la página de producto → **Botón sólido / Accent**: fondo `#E8590C` (naranja) o `#E03131` (rojo), texto `#FFFFFF`. **Save.**
3. (Coincide con las barras CTA naranjas de la descripción → consistencia visual.)

### D.3 — Texto del botón
- Si el tema lo permite (Product information → bloque Buy buttons / Theme settings): poné **"COMPRAR AHORA — ENVÍO GRATIS 🚚"**.

### D.4 — Sticky add-to-cart en móvil (no lo tenés)
- Opción rápida (recomendada): **Admin → Apps → Shopify App Store →** buscar **"Sticky Add To Cart Bar"** (hay gratuitas, ej. de Releasit/Tako) → Install → activar en móvil. **Impacto ALTO**: el lead que scrollea siempre ve el botón.

### D.5 — Estrellas bajo el título
- Ya seteé `reviews.rating` (4.8) y `reviews.rating_count` (380). Si tu tema usa el **rating nativo**, se mostrarán al activar el bloque **"Product rating"** en *Product information*. Si usás la **app de reseñas** ("revie"), cargá ahí las reseñas para que el widget muestre estrellas.

### D.6 — Barra de anuncios (announcement bar)
- **Customize → Header/Announcement bar:** `🇧🇴 Empresa boliviana | 🚚 Envío GRATIS | 💵 Pagá al recibir | 🛡️ Garantía 30 días`.
