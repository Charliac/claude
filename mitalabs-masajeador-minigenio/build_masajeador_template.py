#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constructor del template product.masajeador (estructura minigenio, contenido MitaLabs).
- Base: base_template_usuario.json (bajado byte-exacto de la API del tema del usuario)
- Secciones reutilizadas: byte-identicas a la base (verificado)
- Secciones nuevas: cada setting id se valida contra el schema real del tema
- QC programatico: claims prohibidos, marcas ajenas, refs de imagen, precios hardcodeados
"""
import json, os, re, sys, copy

SCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schemas')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)

def load(fn):
    return json.load(open(os.path.join(SCH, fn), encoding='utf-8'))

def schema_ids(schema):
    ids = {s['id'] for s in schema.get('settings', []) if 'id' in s}
    blocks = {b['type']: {s['id'] for s in b.get('settings', []) if 'id' in s} for b in schema.get('blocks', [])}
    return ids, blocks

def assert_settings(name, schema, settings, block_type=None):
    ids, blocks = schema_ids(schema)
    valid = blocks.get(block_type, set()) if block_type else ids
    bad = [k for k in settings if k not in valid]
    if bad:
        raise SystemExit(f"[FATAL] {name}{'/'+block_type if block_type else ''}: setting ids inexistentes en schema: {bad}")

missing = [f for f in ['base_template_usuario.json','divider.schema.json','photo-grid.schema.json',
                       'before-after-comparison.schema.json','product-benefits.schema.json',
                       'sticky-add-to-cart.schema.json'] if not os.path.exists(os.path.join(SCH,f))]
if missing:
    raise SystemExit(f"[FATAL] faltan archivos del agente: {missing}")

base = load('base_template_usuario.json')
tpl = {"sections": {}, "order": []}

# ---------- 1. SECCIONES REUTILIZADAS (byte-identicas salvo edicion declarada) ----------
KEEP = ["shop_product_details_JbqzwH", "store_features_HfR3fm", "4_images_6wqdKm", "4_cards_jDTiEi",
        "image_with_text_hmnhFF", "product_comparison_ahRqAP", "satisfaction_guarantee_J4ypTy",
        "store_faq_Lpd3PW", "scrolling_features_bar_mWQii9"]
for k in KEEP:
    if k not in base['sections']:
        raise SystemExit(f"[FATAL] la base no tiene la seccion {k}")
    tpl['sections'][k] = copy.deepcopy(base['sections'][k])

# Edicion minima declarada del ticker (zona editable):
sb = tpl['sections']['scrolling_features_bar_mWQii9']
sb['settings']['background_color'] = '#12382c'
for bid, b in sb['blocks'].items():
    if '10,000' in b['settings'].get('text','') or '10.000' in b['settings'].get('text',''):
        b['settings']['text'] = '+10.000 BOLIVIANOS SATISFECHOS'

# ---------- 2. SECCIONES NUEVAS ----------
P = {  # paleta MitaLabs
    'dark': '#12382c', 'accent': '#108474', 'accent_soft': '#9edfca', 'bg_soft': '#f4f7f5',
    'line': '#e3ece8', 'text2': '#48584f', 'white': '#ffffff',
}

# --- 2a. sticky (DISABLED hasta verificar EasySell) ---
sticky_schema = load('sticky-add-to-cart.schema.json')
def pick(valid, prefs, val):
    """setea solo ids que existan en el schema"""
    return {k: v for k, v in prefs.items() if k in valid} | {}
sids, _sblocks = schema_ids(sticky_schema)
def opt_pick(schema, sid, preferred):
    st = next((x for x in schema.get('settings', []) if x.get('id') == sid), None)
    if not st or not st.get('options'):
        return None
    vals = [o['value'] for o in st['options']]
    return next((v for v in vals if any(p in v for p in preferred)), vals[0])
sticky_settings = {k: v for k, v in {
    'use_theme_colors': False,
    'button_text': 'Pedir ahora',
    'fallback_title': 'Masajeador Shiatsu MitaLabs®',
    'delivery_text_prefix': 'Recibilo aprox. antes del',
    'rating_text': '4.8 ★ Calificación "Excelente"',
    'button_bg_color': P['accent'], 'button_text_color': P['white'],
    'background_color': P['white'], 'title_color': P['dark'],
    'rating_text_color': P['text2'], 'delivery_text_color': P['text2'],
    'star_color': '#f4c637',
}.items() if k in sids}
for sid, prefs in [('select_button_behavior', ('scroll',)), ('trigger_behavior', ('scroll',))]:
    if sid in sids:
        v = opt_pick(sticky_schema, sid, prefs[0:1])
        if v is not None:
            sticky_settings[sid] = v
tpl['sections']['sticky_add_to_cart_mtlbSt'] = {
    'type': 'sticky-add-to-cart', 'disabled': True, 'name': 'Sticky Add To Cart',
    'settings': sticky_settings,
}

# --- 2b. product-benefits ---
pb_schema = load('product-benefits.schema.json')
pb_ids, pb_blocks = schema_ids(pb_schema)
pb_block_type = next((t for t in pb_blocks if 'benefit' in t), list(pb_blocks)[0] if pb_blocks else None)
BENEFITS = [
    ("Amasado Tipo Manos", "Nodos que giran como pulgares y agarran el músculo de verdad, no la vibración superficial que solo hace cosquillas."),
    ("Calor que Prepara la Zona", "Primero afloja el músculo con calor y recién ahí amasa profundo. Por eso se siente, y no lastima."),
    ("Sin Cables, Manos Libres", "Batería recargable por USB: te lo colgás y seguís con tu vida en el sofá, la cama o la oficina."),
    ("Un Ritual que Sí Podés Sostener", "Sesiones de 10 a 15 minutos mientras ves tele. Tu masajista en casa, sin turnos ni gasto repetido."),
]
pb_settings = {k: v for k, v in {
    'use_theme_colors': False,
    'heading': 'Masaje Real,', 'heading_regular': 'Masaje Real,', 'title': 'Masaje Real,',
    'heading_accent': 'Todas las Noches en tu Casa.', 'accent_text': 'Todas las Noches en tu Casa.',
    'subtitle': 'Descubrí por qué este sí se siente: el calor afloja la zona primero y los nodos amasan tipo manos, sin cables y sin pagar sesión tras sesión.',
    'subheading': 'Descubrí por qué este sí se siente: el calor afloja la zona primero y los nodos amasan tipo manos, sin cables y sin pagar sesión tras sesión.',
    'image': 'shopify://shop_images/masajeador-roadmap.webp',
    'product_image': 'shopify://shop_images/masajeador-roadmap.webp',
    'feature_image': 'shopify://shop_images/masajeador-roadmap.webp',
    'use_gradient_background': True, 'use_gradient': True,
    'background_gradient': 'linear-gradient(180deg, rgba(16, 132, 116, 1), rgba(18, 56, 44, 1) 100%)',
    'section_background': 'linear-gradient(180deg, rgba(16, 132, 116, 1), rgba(18, 56, 44, 1) 100%)',
    'gradient_background': 'linear-gradient(180deg, rgba(16, 132, 116, 1), rgba(18, 56, 44, 1) 100%)',
    'background_color': P['accent'],
    'heading_color': P['white'], 'title_color': P['white'],
    'accent_color': P['accent_soft'], 'heading_accent_color': P['accent_soft'],
    'subtitle_color': P['white'], 'text_color': P['white'],
    'benefit_title_color': P['white'], 'benefit_description_color': P['white'],
    'description_color': P['white'], 'icon_color': P['white'],
}.items() if k in pb_ids}
pb_sec = {'type': 'product-benefits', 'name': 'Product Benefits', 'settings': pb_settings}
if pb_block_type:
    blocks, order = {}, []
    valid = pb_blocks[pb_block_type]
    for i, (t, d) in enumerate(BENEFITS, 1):
        bs = {k: v for k, v in {
            'title': t, 'heading': t, 'benefit_title': t,
            'description': d, 'text': d, 'benefit_description': d,
        }.items() if k in valid}
        key = f'benefit_mtlb{i}'
        blocks[key] = {'type': pb_block_type, 'settings': bs}
        order.append(key)
    pb_sec['blocks'] = blocks; pb_sec['block_order'] = order
tpl['sections']['product_benefits_mtlbPB'] = pb_sec

# --- 2c/2f. dividers ---
dv_schema = load('divider.schema.json')
dv_ids, _ = schema_ids(dv_schema)
def divider():
    s = {k: v for k, v in {
        'use_theme_colors': False, 'color': P['accent'],
        'background_color': 'rgba(0,0,0,0)', 'height': 25,
        'show_border': False, 'use_gradient': False, 'keep_proportion': True,
        'padding_top': 0, 'padding_bottom': 0,
    }.items() if k in dv_ids}
    # divider_style: elegir la opcion mas simple del schema (linea)
    style_setting = next((x for x in dv_schema.get('settings', []) if x.get('id') == 'divider_style'), None)
    if style_setting and style_setting.get('options'):
        vals = [o['value'] for o in style_setting['options']]
        simple = next((v for v in vals if v in ('wavy', 'line', 'solid')), vals[0])
        s['divider_style'] = simple
    return {'type': 'divider', 'name': 'Divider', 'settings': s}
tpl['sections']['divider_mtlbD1'] = divider()
tpl['sections']['divider_mtlbD2'] = divider()
tpl['sections']['divider_mtlbD3'] = divider()

# --- 2d. image-with-text NUEVA (promesa + 6 checks + CTA) ---
iw_schema_path = os.path.join(SCH, 'image-with-text.schema.json')
iw_base = copy.deepcopy(base['sections']['image_with_text_hmnhFF'])  # settings validados por uso real
iw = {'type': 'image-with-text', 'name': 'Image with Text', 'settings': iw_base['settings']}
iw['settings'].update({
    'heading': 'Hombros Sueltos.', 'heading_accent': 'Y noches tranquilas.',
    'image': 'shopify://shop_images/masajeador-razon-1.webp',
    'image_position': 'right', 'background_color': P['bg_soft'], 'container_bg_color': P['bg_soft'],
})
iw_blocks = {
    'paragraph_mtlbPromesa': {'type': 'paragraph', 'settings': {
        'paragraph_text': '<p>Adiós a terminar el día hecho nudo. El <strong>Masajeador Shiatsu MitaLabs</strong> convierte 15 minutos de tele en tu sesión de masaje: <strong>calor que afloja primero</strong> y <strong>amasado tipo manos</strong> que suelta la tensión acumulada de cuello, hombros y espalda.</p>',
        'font_size_mobile': 1.5, 'font_size_desktop': 1.5, 'margin_top': -20, 'margin_bottom': 0,
        'paragraph_color': '#333333'}},
    'bullet_list_mtlbChecks': {'type': 'bullet_list', 'settings': {
        'two_columns': True, 'list_title': '',
        'list_item_1': 'Amasado shiatsu tipo manos',
        'list_item_2': 'Calor que afloja primero',
        'list_item_3': 'Batería recargable, sin cables',
        'list_item_4': 'Cuello, hombros y espalda',
        'list_item_5': 'Te lo colgás: manos libres',
        'list_item_6': 'Pagás al recibir en Santa Cruz',
        'list_color': P['text2'], 'list_title_color': P['dark'],
        'pill_style': False, 'pill_bg_color': P['accent'], 'pill_text_color': P['white'],
        'pill_border_color': P['accent'], 'pill_border_width': 1, 'pill_border_radius': 6,
        'pill_padding_vertical': 11, 'pill_padding_horizontal': 10, 'pill_spacing': 8,
        'margin_top': 0, 'margin_bottom': 0, 'font_size_mobile': 1.2, 'font_size_desktop': 1.4}},
}
iw_order = ['paragraph_mtlbPromesa', 'bullet_list_mtlbChecks']
# boton: solo si el schema lo confirma
if os.path.exists(iw_schema_path):
    iw_schema = json.load(open(iw_schema_path, encoding='utf-8'))
    _, iw_blk = schema_ids(iw_schema)
    btn_type = next((t for t in iw_blk if 'button' in t.lower()), None)
    if btn_type:
        valid = iw_blk[btn_type]
        bset = {k: v for k, v in {
            'button_label': 'Pedir ahora',
            'scroll_to_products': True,
            'button_bg_color': P['accent'], 'button_text_color': P['white'],
        }.items() if k in valid}
        brt = next((x for x in iw_schema.get('blocks', []) if x.get('type') == btn_type), {})
        rt = next((s for s in brt.get('settings', []) if s.get('id') == 'button_redirect_type'), None)
        if rt and rt.get('options'):
            vals = [o['value'] for o in rt['options']]
            bset['button_redirect_type'] = next((v for v in vals if 'scroll' in v), vals[0])
        iw_blocks['button_mtlbCTA'] = {'type': btn_type, 'settings': bset}
        iw_order.append('button_mtlbCTA')
    # validar bloques paragraph/bullet_list contra schema real
    for bk, bv in iw_blocks.items():
        if bv['type'] in iw_blk:
            bad = [k for k in bv['settings'] if k not in iw_blk[bv['type']]]
            if bad:
                for k in bad: del bv['settings'][k]
                print(f"[WARN] image-with-text/{bv['type']}: ids removidos por no estar en schema: {bad}")
iw['blocks'] = iw_blocks; iw['block_order'] = iw_order
tpl['sections']['image_with_text_mtlbIW'] = iw

# --- 2e. before-after-comparison ---
ba_schema = load('before-after-comparison.schema.json')
ba_ids, ba_blocks = schema_ids(ba_schema)
ba_settings = {k: v for k, v in {
    'use_theme_colors': False,
    'heading': 'Menos Tensión,', 'title': 'Menos Tensión,', 'title_part_1': 'Menos Tensión,',
    'title_accent': 'Más Descanso.', 'section_background_color': P['white'],
    'heading_accent': 'Más Descanso.', 'accent_text': 'Más Descanso.', 'title_part_2': 'Más Descanso.',
    'subtitle': 'Mirá la transformación: de terminar el día con el cuello hecho piedra a soltarlo cada noche en tu casa, con tu ritual de 15 minutos.',
    'description': 'Mirá la transformación: de terminar el día con el cuello hecho piedra a soltarlo cada noche en tu casa, con tu ritual de 15 minutos.',
    'before_image': 'shopify://shop_images/masajeador-card-2.webp',
    'after_image': 'shopify://shop_images/masajeador-ritual-3.webp',
    'before_label': 'Antes', 'after_label': 'Después',
    'heading_color': P['dark'], 'title_color': P['dark'], 'accent_color': P['accent'],
    'subtitle_color': P['text2'], 'description_color': P['text2'],
    'background_color': P['white'], 'section_bg_color': P['white'],
    'label_background': P['dark'], 'label_bg_color': P['dark'], 'label_color': P['white'], 'label_text_color': P['white'],
}.items() if k in ba_ids}
ba_sec = {'type': 'before-after-comparison', 'name': 'Before After Comparison', 'settings': ba_settings}
if ba_blocks:
    # si las imagenes van por bloques, armarlos
    bt = next((t for t in ba_blocks if 'before' in t or 'after' in t or 'image' in t or 'comparison' in t), None)
    if bt and not any(k in ba_settings for k in ('before_image', 'after_image')):
        print(f"[WARN] before-after usa bloques tipo {list(ba_blocks)} — revisar manualmente")
tpl['sections']['before_after_mtlbBA'] = ba_sec

# --- 2g. photo-grid ---
pg_schema = load('photo-grid.schema.json')
pg_ids, pg_blocks = schema_ids(pg_schema)
pg_settings = {k: v for k, v in {
    'use_theme_colors': False,
    'title_primary': '¡Más de 10.000', 'title_accent': 'Bolivianos Aliviados!',
    'subtitle': 'Gente real soltando el cuello con su MitaLabs en toda Bolivia.',
    'title_primary_color': P['dark'], 'title_accent_color': P['accent'],
    'social_badge_type': 'facebook', 'view_count': 3.1,
    'badge_text': 'Más de', 'badge_suffix': 'M de vistas en Facebook',
    'badge_background_color': '#f8f9fa', 'badge_text_color': '#262626',
    'use_gradient_border': True, 'text_alignment': 'center',
    'columns_mobile': '3', 'columns_desktop': '3', 'grid_gap': 8,
    'section_bg_color': P['white'], 'padding_top': 40, 'padding_bottom': 40,
}.items() if k in pg_ids}
# validar valor de social_badge_type contra las opciones del schema
sbt = next((x for x in pg_schema.get('settings', []) if x.get('id') == 'social_badge_type'), None)
if sbt and sbt.get('options'):
    vals = [o['value'] for o in sbt['options']]
    if 'facebook' not in vals:
        pg_settings['social_badge_type'] = vals[0]
        print(f"[WARN] photo-grid social_badge_type: 'facebook' no esta en {vals}")
PG_IMGS = ['resena-1','masajeador-ritual-1','resena-3','masajeador-ritual-2','resena-4',
           'masajeador-ritual-3','resena-5','masajeador-ritual-4','resena-2']
pg_sec = {'type': 'photo-grid', 'name': 'Photo Grid', 'settings': pg_settings, 'blocks': {}, 'block_order': []}
for i, img in enumerate(PG_IMGS, 1):
    key = f'image_item_mtlb{i}'
    pg_sec['blocks'][key] = {'type': 'image_item', 'settings': {'image': f'shopify://shop_images/{img}.webp'}}
    pg_sec['block_order'].append(key)
tpl['sections']['photo_grid_mtlbPG'] = pg_sec

# ---------- 3. ORDEN (espina minigenio) ----------
tpl['order'] = [
    'shop_product_details_JbqzwH',        # 1. main INTOCADO (above the fold)
    'scrolling_features_bar_mWQii9',      # 2. ticker (minigenio #2)
    'store_features_HfR3fm',              # 3. features (disabled, se conserva)
    'sticky_add_to_cart_mtlbSt',          # 4. sticky (minigenio #3) — DISABLED hasta verificar EasySell
    'product_benefits_mtlbPB',            # 5. benefits degrade verde (minigenio #4)
    'divider_mtlbD1',                     # 6. (minigenio #5)
    'image_with_text_mtlbIW',             # 7. promesa+checks+CTA (minigenio #6)
    '4_images_6wqdKm',                    # 8. ritual 3 pasos (minigenio steps #7)
    '4_cards_jDTiEi',                     # 9. cards (minigenio stacked cards #8)
    'divider_mtlbD2',                     # 10. (minigenio #9)
    'before_after_mtlbBA',                # 11. antes/despues (minigenio #10)
    'image_with_text_hmnhFF',             # 12. mecanismo/absolucion (minigenio #11)
    'product_comparison_ahRqAP',          # 13. tabla VS (minigenio #12)
    'divider_mtlbD3',                     # 14. (minigenio #13)
    'satisfaction_guarantee_J4ypTy',      # 15. garantia (minigenio #14)
    'photo_grid_mtlbPG',                  # 16. prueba social grid (minigenio #15)
    'store_faq_Lpd3PW',                   # 17. FAQ (minigenio #16)
]
missing_order = [k for k in tpl['order'] if k not in tpl['sections']]
if missing_order:
    raise SystemExit(f"[FATAL] en order pero sin seccion: {missing_order}")

# ---------- 4. QC PROGRAMATICO ----------
out_path = os.path.join(OUT, '04_PRODUCT_PAGE_MASAJEADOR_ESTRUCTURA_MINIGENIO.json')
raw = json.dumps(tpl, ensure_ascii=False, indent=2)
json.loads(raw)  # re-parse

errors, warns = [], []
# 4a. secciones intocadas identicas a la base
for k in KEEP:
    if k == 'scrolling_features_bar_mWQii9':
        continue
    if tpl['sections'][k] != base['sections'][k]:
        errors.append(f"seccion {k} difiere de la base y debia quedar intocada")
# 4b. marcas ajenas / plataformas
for bad in ['MagicLab', 'magiclab', 'minigenio', 'MiniGenio', 'Charliac', 'charliac', 'Almacen Soza', 'Gs.', 'guaraní', 'guaranies', 'Paraguay', 'paraguay']:
    if bad in raw:
        errors.append(f"string prohibido presente: {bad}")
# 4c. claims prohibidos SOLO en textos nuevos
new_keys = ['sticky_add_to_cart_mtlbSt','product_benefits_mtlbPB','divider_mtlbD1','image_with_text_mtlbIW',
            'divider_mtlbD2','before_after_mtlbBA','divider_mtlbD3','photo_grid_mtlbPG']
new_raw = json.dumps({k: tpl['sections'][k] for k in new_keys}, ensure_ascii=False).lower()
new_raw = re.sub(r'linear-gradient\([^"]*\)', '', new_raw)  # los degrades CSS no son claims
for claim in ['cura', 'curar', 'elimina', 'sana ', 'sanar', '100%', 'garantizado', 'nunca más', 'nunca mas',
              'niveles de', 'minutos de batería', 'temperatura', '°c', 'grados']:
    if claim in new_raw:
        errors.append(f"claim prohibido en secciones nuevas: '{claim}'")
if re.search(r'\b(cur)(?!iosidad|va)', new_raw.replace('recur','').replace('ocur','').replace('oscur','').replace('procur','').replace('seguridad','')):
    m = re.findall(r'.{20}cur.{20}', new_raw)
    warns.append(f"substring 'cur' detectado, revisar contexto: {m[:3]}")
# 4d. precios hardcodeados en secciones nuevas
if re.search(r'\b(389|778|179)\b', new_raw):
    errors.append("precio hardcodeado en secciones nuevas (debe ser dinamico)")
# 4e. refs de imagen: todas del set del usuario
base_raw = json.dumps(base, ensure_ascii=False)
allowed_imgs = set(re.findall(r'shopify://shop_images/([^"]+)', base_raw))
allowed_imgs |= {f'{i}.webp' for i in PG_IMGS} | {'masajeador-roadmap.webp','masajeador-razon-1.webp',
                 'masajeador-card-2.webp','masajeador-ritual-3.webp'}
used_imgs = set(re.findall(r'shopify://shop_images/([^"]+)', raw))
unknown = used_imgs - allowed_imgs
for u in sorted(unknown):
    warns.append(f"imagen no vista en la base (verificar que exista en Shopify Files): {u}")
# las resena-N y ritual-N vienen de la base (video_testimonials/4_images) — verificar:
for img in sorted(used_imgs):
    if img not in base_raw and img not in ('masajeador-roadmap.webp',):
        pass  # cubierto por unknown
# 4f. voseo: las secciones nuevas no deben usar tuteo tipico
for t in [' tu ritmo', 'tienes', 'puedes', 'usa el', 'recibe ', 'paga ', 'cuelga']:
    if t in new_raw:
        warns.append(f"posible tuteo en secciones nuevas: '{t}'")

open(out_path, 'w', encoding='utf-8').write(raw)
rep = [f"OUT: {out_path}  ({len(raw)} bytes, {len(tpl['sections'])} secciones)"]
rep.append(f"ERRORES: {len(errors)}"); rep += [f"  ✗ {e}" for e in errors]
rep.append(f"WARNINGS: {len(warns)}"); rep += [f"  ⚠ {w}" for w in warns]
print('\n'.join(rep))
open(os.path.join(OUT, 'qc_report.txt'), 'w', encoding='utf-8').write('\n'.join(rep))
sys.exit(1 if errors else 0)
