# 07 — Build en Shopify (lo que quedó creado)

> Fecha: 2026-06-07 · Tienda: charliac.shop (Charliac Bolivia, BOB)

## Producto creado (DRAFT)

| Campo | Valor |
|---|---|
| **Product GID** | `gid://shopify/Product/10206703485234` |
| **Título** | Soporte de Cuello Magnético POV® — Graba con las Manos Libres para TikTok y Reels |
| **Handle / URL** | `/products/soporte-cuello-magnetico-pov-manos-libres` |
| **Estado** | DRAFT (listo para revisar y publicar) |
| **Vendor** | Charliac Bolivia |
| **Tipo** | Tecnología |
| **SEO título** | Soporte de Cuello POV Magnético \| Manos Libres \| Envío Gratis |
| **SEO meta** | Graba en POV con las manos 100% libres. Soporte de cuello magnético para iPhone y Android (anillo incluido). Envío gratis a toda Bolivia y pagás al recibir. |

## Convención de nombre (auditada de tu catálogo y aplicada)

Patrón detectado: `[Producto descriptivo real] [spec/modelo]® — [Beneficio con keywords/usos]`
(ej. "Repetidor WiFi 4 Antenas 300 Mbps® — Amplificador de Señal para Toda la Casa").
→ Nombre real, descriptivo, alto CRO. Sin marca inventada.

## Variantes (opción "Cantidad") + anclaje

| Variante | SKU | Precio | Ancla (tachado) | Por unidad |
|---|---|---|---|---|
| 🎥 1 Soporte POV | POV-CUELLO-1U | Bs 279 | Bs 558 | 279 |
| 🔥 2 Soportes (Más Elegido) | POV-CUELLO-2U | Bs 502 | Bs 1.116 | 251 |
| 💰 3 Soportes (Máximo Ahorro) | POV-CUELLO-3U | Bs 711 | Bs 1.674 | 237 |

- Inventario: **no rastreado** → siempre disponible (ideal COD).
- Efecto señuelo en ×2 ("MÁS ELEGIDO"). Efecto marco en ahorro.

## Estructura del HTML (CRO, mobile-first, estilo gm4 de tu tienda)

Clase scoped `.pov`, `font-family:inherit`, responsive 640px. Secciones:
1. Hook gradiente + rating
2. Placeholder video hero
3. Tira de confianza (🇧🇴 · 🚚 · 💵 · 🛡️)
4. Problema (aversión a la pérdida) — depender de alguien
5. Agitación (3 líneas)
6. Solución (1 segundo, manos libres)
7. **Bloque Android** ("funciona en TU celular — anillo incluido") ← clave Bolivia
8. CTA bar
9. Beneficios experienciales (7)
10. Multi-uso (6 nichos)
11. Tu pedido incluye
12. 3 pasos de uso
13. Tabla VS (vs pedir ayuda / trípode / palo selfie / a pulso / solo iPhone)
14. Especificaciones (grid)
15. Reseñas estilo Facebook (3, nombres BO) + resumen 4.8★
16. Sello de garantía 30 días
17. Oferta (ancla 558 → 279, "Ahorrás Bs 279", packs, urgencia blink)
18. CTA bar
19. FAQ (Android, caída, comodidad, usos, contra entrega, envíos)
20. CTA final + WhatsApp 74171116

## ⚠️ Pendiente antes de publicar (ACTIVE)

1. **Imágenes de galería** (carrusel): no se subieron (alcance elegido = solo producto, sin IA). Subí tus fotos/render reales. La 1ª imagen = featured.
2. **Reemplazar placeholders del HTML** (`.pov-ph` y `.fbp-ph`): poné tu video hero, GIFs de uso, close-up de calidad, 3 pasos, montaje multi-uso y fotos reales de reseñas.
3. **Reseñas:** son plantillas con nombres bolivianos (siguen tu formato de tienda). Reemplazá por reseñas reales conforme lleguen clientes.
4. **Optimizaciones del tema** (suben CR, fuera del HTML):
   - Sticky add-to-cart en móvil
   - Botón "Comprar" en rojo/naranja (máximo contraste)
   - WhatsApp 74171116 visible (footer + cerca del botón)
   - App de prueba social ("X compró hace 5 min") o texto "+pedidos entregados"
   - Comprimir imágenes <500KB (TinyPNG/Squoosh)
5. **Publicar:** cambiar estado DRAFT → ACTIVE y publicar en Online Store.

## Consistencia de precio (regla de skill)

Ancla **Bs 558** y precio **Bs 279** deben ser idénticos en: ad → web → HTML → ManyChat → guion de agente. (Ya consistentes en el HTML.)
