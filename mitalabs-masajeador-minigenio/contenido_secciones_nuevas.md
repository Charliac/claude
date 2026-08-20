# CONTENIDO SECCIONES NUEVAS — Masajeador Shiatsu MitaLabs (réplica estructura minigenio)
# Reglas aplicadas: voseo boliviano · solo claims confirmados (amasado tipo manos, calor,
# batería USB recargable, 10-15 min, cuello/hombros/espalda alta, manos libres, COD SCZ,
# envío gratis, garantía 30 días, +10.000 clientes, 4.8/5, 3.1M vistas FB) · sin "cura/elimina/sana"
# · sin specs no confirmadas (niveles, minutos de batería, temperaturas) · ancla siempre x2 ·
# CTA coherente: "Pedir ahora" (scroll al form) · paleta: #12382c / #108474 / #9edfca / #f4f7f5 / #e3ece8 / #48584f

## 1. scrolling_features_bar_mWQii9 (EDITAR mínimo)
- background_color: #000000 → #12382c (dark de la marca)
- item 3: "+10,000 CLIENTES SATISFECHOS" → "+10.000 BOLIVIANOS SATISFECHOS" (localización = confianza, patrón minigenio "Paraguayos Contentos")
- items 1-2 quedan: CALIDAD GARANTIZADA · ENVÍO GRATIS Y RÁPIDO

## 2. sticky_add_to_cart (NUEVA, "disabled": true)
- Texto botón: "Pedir ahora" + precio dinámico
- ⚠️ DESACTIVADA a propósito: el sticky del tema dispara el form NATIVO (/cart/add).
  Minigenio puede usarlo porque vende con checkout Shopify; vos vendés con EasySell.
  Activarla SOLO tras verificar que abre el form de EasySell; si no, usar el sticky
  propio de EasySell (Settings → Sticky button). Regla de la skill PY §8.

## 3. product_benefits (NUEVA — degradé verde, imagen + 4 beneficios en tarjeta glass)
- heading_regular: "Masaje Real,"
- heading_accent (itálica clara #9edfca): "Todas las Noches en tu Casa."
- subtitle: "Descubrí por qué este sí se siente: el calor afloja la zona primero y los nodos amasan tipo manos, sin cables y sin pagar sesión tras sesión."
- imagen: shopify://shop_images/masajeador-roadmap.webp  [REEMPLAZAR por GIF del amasado en movimiento — minigenio usa GIF acá; el movimiento vende el mecanismo]
- gradiente sección: linear-gradient(180deg, rgba(16,132,116,1), rgba(18,56,44,1) 100%)
- Beneficios (título + texto):
  1. "Amasado Tipo Manos" — "Nodos que giran como pulgares y agarran el músculo de verdad, no la vibración superficial que solo hace cosquillas."
  2. "Calor que Prepara la Zona" — "Primero afloja el músculo con calor y recién ahí amasa profundo. Por eso se siente, y no lastima."
  3. "Sin Cables, Manos Libres" — "Batería recargable por USB: te lo colgás y seguís con tu vida en el sofá, la cama o la oficina."
  4. "Un Ritual que Sí Podés Sostener" — "Sesiones de 10 a 15 minutos mientras ves tele. Tu masajista en casa, sin turnos ni gasto repetido."

## 4. divider ×3 (NUEVAS) — color #108474, fondo transparente, patrón minigenio

## 5. image_with_text NUEVA (slot "promesa + checks + CTA", espejo de "Caligrafía Perfecta. Y sin peleas.")
- heading: "Hombros Sueltos." / heading_accent: "Y noches tranquilas."
- párrafo: "Adiós a terminar el día hecho nudo. El Masajeador Shiatsu MitaLabs convierte 15 minutos de tele en tu sesión de masaje: calor que afloja primero y amasado tipo manos que suelta la tensión acumulada de cuello, hombros y espalda."
- bullet_list (two_columns: true, estilo check — NO pill):
  1. "Amasado shiatsu tipo manos"
  2. "Calor que afloja primero"
  3. "Batería recargable, sin cables"
  4. "Cuello, hombros y espalda"
  5. "Te lo colgás: manos libres"
  6. "Pagás al recibir en Santa Cruz"   ← última = mata objeción (regla skill)
- botón: "Pedir ahora" (scroll arriba, bg #108474, texto blanco)
- imagen: shopify://shop_images/masajeador-razon-1.webp  [ideal: GIF en movimiento]
- fondo sección: #f4f7f5 (espejo del gris claro de minigenio, en tu paleta)

## 6. 4_images_6wqdKm — SIN CAMBIOS (tu ritual en 3 pasos = slot "steps" de minigenio)
## 7. 4_cards_jDTiEi — SIN CAMBIOS (slot "stacked cards")

## 8. before_after_comparison (NUEVA)
- heading: "Menos Tensión," / accent: "Más Descanso."
- subtitle: "Mirá la transformación: de terminar el día con el cuello hecho piedra a soltarlo cada noche en tu casa, con tu ritual de 15 minutos."
- label antes: "Antes" · label después: "Después" (con tilde — minigenio lo tiene mal)
- imagen ANTES: shopify://shop_images/masajeador-card-2.webp   [PLACEHOLDER]
- imagen DESPUÉS: shopify://shop_images/masajeador-ritual-3.webp [PLACEHOLDER]
- [GENERAR PAR REAL en Higgsfield: misma mujer/misma sala — antes: mano en el cuello,
  gesto cargado frente a la laptop · después: masajeador puesto, hombros bajos, luz cálida.
  Sin claims médicos visuales, es estado emocional, no "resultado clínico".]

## 9. image_with_text_hmnhFF — SIN CAMBIOS (tu mecanismo/absolución = slot "desafíos" de minigenio)
## 10. product_comparison_ahRqAP — SIN CAMBIOS (misma sección que usa minigenio, ya validada)
## 11. satisfaction_guarantee_J4ypTy — SIN CAMBIOS (slot garantía)

## 12. photo_grid (NUEVA — prueba social con contador)
- heading: "¡Más de 10.000" / accent: "Bolivianos Aliviados!"
  (mismo número que tu ticker — consistencia; minigenio se contradice: 5.000 acá, 10.000 en ticker)
- subtitle: "Gente real soltando el cuello con su MitaLabs en toda Bolivia."
- pill social: Facebook · "Más de 3.1M de vistas" (MISMO claim que tu bloque de videos del main;
  minigenio se contradice: 4.4M en main vs 6M acá — no repetir su bug)
- 9 fotos [PLACEHOLDERS hasta tener UGC real]: resena-1, ritual-1, resena-2, ritual-2,
  resena-3, ritual-3, resena-4, ritual-4, resena-5 (.webp, shopify://shop_images/)

## 13. store_faq_Lpd3PW — SIN CAMBIOS (tus 7 FAQ ya superan las 5 de minigenio)

## FUERA de la nueva plantilla (quedan en tu template actual, no se pierden):
rich_text_Cdzprk (hero oscuro) · video_testimonials_deTydM · roadmap_cCJcRP ·
testimonials_LLc4fa · statistics_grid_rCpmYM · steps_eK6Lpb ("4 razones") ·
store_features_HfR3fm queda en el archivo pero disabled (como está hoy).
Si el test contra tu página actual pierde en CPA, lo primero a reinyectar:
video_testimonials (tu prueba social más fuerte, minigenio no tiene equivalente).

## NO SE COPIA de minigenio (viola tus reglas de skill):
- Countdown evergreen "La oferta termina en 24 HRS" (timer falso → prohibido; tu urgencia
  válida: "Precio promocional por stock limitado" que YA tenés en el main)
- Avatares con fotos del producto y foto de stock (istockphoto) como perfil de reseña
- Su inconsistencia de números (4.4M vs 6M · 5.000 vs 10.000)
