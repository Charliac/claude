#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Merge: estructura del masajeador FINAL (pulido por el usuario) + contenido de la munequera.
import json, re, os, copy

BASE = os.path.dirname(os.path.abspath(__file__))
FR = json.load(open(os.path.join(BASE, 'svg_fragments.json')))
SVG_X = FR['SVG_X']; SVG_FLAG = FR['SVG_FLAG']; SVG_COMP = FR['SVG_COMP_CHECK']
SVG_CIRCLE = '<svg viewbox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="currentColor" opacity="0.1"></circle><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="2" fill="none"></path></svg>'
SVG_BCHECK = '<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg>'
SVG_BADGE1 = '<svg viewbox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none" stroke=""><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill="#ffffff" d="M8 3a5 5 0 100 10A5 5 0 008 3z"></path></g></svg>'
SVG_ARROW = '<svg width="24" height="24" viewbox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="currentColor"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"></path></svg>'
SC_SHIELD = '<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"></path></svg>'
SC_TRUCK = '<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zm-6 0H5V6h9v2zm-9 11.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm12 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"></path></svg>'
SC_CHECK = '<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>'

def cr(name, text, avatar):
    return {'type': 'customer_review', 'settings': {
        'reviewer_name': name, 'review_text': text, 'rating': 5,
        'avatar_url': f'shopify://shop_images/{avatar}', 'show_avatar': True, 'use_theme_colors': False,
        'background_color_start': '#ffffff', 'background_color_end': '#ffffff', 'text_color': '#12382c',
        'border_color': '#e3ece8', 'border_radius': 6, 'border_style': 'dashed', 'show_shadow': True,
        'star_color': '#f4c637', 'reviewer_name_size': 16, 'review_text_size': 14, 'star_size': 16,
        'avatar_size_desktop': 75, 'avatar_size_mobile': 65, 'margin_top': 15, 'margin_right': 0,
        'margin_bottom': 15, 'margin_left': 0, 'verified_icon_color': '#108474',
        'review_text_color': '#48584f', 'enable_carousel': True, 'show_navigation': True,
        'pagination_dot_color': '#e3ece8', 'pagination_dot_active_color': '#108474', 'show_active_shadow': True}}

def vid(f):
    return {'type': 'carousel_default_video', 'settings': {'video': f'shopify://files/videos/{f}',
            'enable_autoplay': True, 'margin_top': 0, 'margin_bottom': 0}}

def frow(name, v1, v2, v3):
    t = {'yes': 'Sí', 'no': 'No'}
    return {'type': 'feature_row', 'name': '1', 'settings': {
        'feature_name': name, 'show_icon': False, 'feature_icon': SVG_COMP, 'value_type': 'checkmark',
        'value_1': v1, 'text_value_1': t[v1], 'value_2': v2, 'text_value_2': t[v2], 'value_3': v3, 'text_value_3': t[v3]}}

S = {}

# ============ 1. MAIN de la munequera — VERBATIM (above the fold intocado) ============
S['shop_product_details_JbqzwH'] = {
 'type': 'shop-product-details',
 'blocks': {
  'number_one_award_wYc38H': {'type': 'number_one_award', 'settings': {
    'badge_number': '#1', 'title_text': 'HASTA 50% OFF', 'subtitle_text': 'La mejor oferta del año',
    'gradient_start_color': '#ef4a65', 'gradient_end_color': '#ef4a65', 'background_color': '#ffffff',
    'text_color': '#000000', 'badge_width': 200, 'badge_height': 35, 'border_radius': 5,
    'margin_top': 8, 'margin_bottom': 0, 'number_badge_text_color': '#ffffff',
    'number_badge_font_size': 24, 'number_badge_font_weight': '700'}},
  'trustpilot_rating_yUMGE7': {'type': 'trustpilot_rating', 'settings': {
    'rating_text': 'Calificación 4.8 "Excelente"', 'rating_score': 'Más de +858 Reseñas',
    'text_color': '#12382c', 'star_color': '#00b67a', 'show_single_star_after_text': True,
    'font_size_desktop': 14, 'font_size_tablet': 14, 'font_size_mobile': 14, 'star_size_desktop': 18,
    'star_size_tablet': 18, 'star_size_mobile': 18, 'margin_top': 0, 'margin_bottom': 10,
    'link': 'reviews', 'enable_background': True, 'background_color': '#f4f7f5',
    'enable_background_gradient': True, 'background_gradient_start': '#ffffff',
    'background_gradient_end': '#f4f7f5', 'background_gradient_direction': 'to right',
    'border_color': '#e3ece8', 'border_width': 1, 'border_style': 'dotted', 'border_radius': 4}},
  'title_4EWLUd': {'type': 'title', 'settings': {
    'dynamic_variant_title_option': 'none', 'use_custom_title': True,
    'custom_title': 'Muñequera Térmica USB MitaLabs® — 1 Unidad Ajustable a Ambas Muñecas',
    'font_size': 24, 'margin_top': -10, 'margin_bottom': 10, 'title_color': '#12382c', 'line_height': 1}},
  'custom_text_jpmwCD': {'type': 'custom_text', 'disabled': True, 'settings': {
    'text': '<p>Muñequera térmica de <strong>calor parejo y sostenido</strong> para aflojar la rigidez y la molestia diaria de muñeca y mano —sin pastillas ni cremas. Se ajusta con velcro a <strong>cualquiera de las dos muñecas</strong> y se alimenta por USB de lo que ya tenés: cargador, laptop, power bank o el puerto del auto. <strong>El agua caliente de toda la vida, pero que no se enfría</strong> y te deja la mano libre.</p>',
    'show_description': False, 'description': '', 'description_font_size': 18, 'description_spacing': 1,
    'description_color': '#48584f', 'description_opacity': 0.8, 'show_accent_text': False,
    'accent_text': '', 'accent_text_position': 'before', 'use_accent_gradient': False,
    'accent_text_gradient': '', 'accent_text_color': '#108474', 'accent_text_font_size': 16,
    'accent_text_font_weight': 'semibold', 'accent_text_spacing': 8, 'show_icon': False,
    'custom_icon': '', 'icon_color': '#333333', 'icon_size': 20, 'icon_spacing': 8,
    'icon_alignment': 'center', 'icon_margin_left': 0, 'icon_margin_right': 8, 'use_image_icon': False,
    'show_after_icon': False, 'after_custom_icon': SVG_ARROW, 'after_icon_color': '#333333',
    'after_icon_size': 20, 'after_icon_alignment': 'center', 'after_icon_margin_left': 8,
    'after_icon_margin_right': 0, 'use_image_after_icon': False, 'text_align': 'left', 'font_size': 14,
    'text_color': '#12382c', 'link_color': '#108474', 'margin_top': -12, 'margin_bottom': -4,
    'padding_top': 0, 'padding_bottom': 0, 'use_container': True, 'container_bg_type': 'color',
    'container_bg': 'rgba(0,0,0,0)',
    'container_bg_gradient': 'linear-gradient(180deg, rgba(248, 248, 248, 1), rgba(229, 229, 229, 1) 100%)',
    'container_padding_v': 10, 'container_padding_h': 4, 'container_fit_content': False,
    'border_radius': 4, 'show_border': False, 'border_width': 1, 'border_color': '#e0e0e0',
    'show_divider': False, 'divider_color': '#e0e0e0', 'divider_height': 1, 'divider_style': 'solid',
    'divider_spacing': 12}},
  'price_wr9fm4': {'type': 'price', 'settings': {
    'multiply_price_by_quantity': True, 'apply_selected_subscription_discount': True,
    'price_color': '#000000', 'compare_price_color': '#999999', 'sale_badge_bg_color': '#ff424e',
    'sale_badge_text_color': '#ffffff', 'show_save_badge': True, 'save_badge_enable_border': False,
    'save_badge_border_color': '#000000', 'save_badge_border_width': 1, 'save_badge_border_style': 'solid',
    'price_font_size': 24, 'compare_price_font_size': 16, 'save_badge_font_size': 12,
    'price_font_weight': '600', 'price_margin_top': 5, 'price_margin_bottom': -10, 'show_save_icon': True,
    'save_icon_size_ratio': 0.9, 'save_icon_position_y': 0, 'save_badge_padding_v': 3,
    'save_badge_padding_h': 6, 'custom_save_text': 'AHORRA', 'save_badge_display_type': 'percentage',
    'custom_save_amount': ''}},
  'divider_nyDN4a': {'type': 'divider', 'settings': {
    'color': '#e0e0e0', 'style': 'solid', 'thickness': 1, 'width': '100%', 'max_width': '100%',
    'alignment': 'center', 'margin_top': 5, 'margin_bottom': 0}},
  'bullet_list_g7PBBg': {'type': 'bullet_list', 'settings': {
    'use_theme_colors': False,
    'bullet_1': 'Calor parejo que afloja la rigidez, la sesión completa',
    'bullet_2': 'Nada que tomar ni untar: calor local y listo',
    'bullet_3': 'Velcro ajustable con agarre de pulgar · ambas muñecas',
    'bullet_4': 'USB: cargador, laptop, power bank o el puerto del auto',
    'bullet_5': 'Pagás al recibir en Santa Cruz · envío gratis', 'bullet_6': '',
    'layout_style': 'horizontal', 'row_gap': 7,
    'use_custom_icon_1': False, 'custom_icon_1': '', 'use_custom_icon_2': False, 'custom_icon_2': '',
    'use_custom_icon_3': False, 'custom_icon_3': '', 'use_custom_icon_4': False, 'custom_icon_4': '',
    'use_custom_icon_5': False, 'custom_icon_5': '', 'use_custom_icon_6': False, 'custom_icon_6': '',
    'icon_color': '#108474', 'text_color': '#12382c', 'icon_size': 20, 'text_size': 14, 'spacing': 5,
    'icon_text_gap': 5, 'show_bg': False, 'bg_color': '#f4f7f5', 'border_radius': 4,
    'margin_top': 10, 'margin_bottom': 10}},
  'shipping_notice_fxXbx6': {'type': 'shipping_notice', 'settings': {
    'notice_text_before': 'Listo para enviar, recíbela aprox. antes del', 'notice_text_after': '',
    'days_ahead': 1, 'show_suffix': False, 'custom_shipping_text': '#12382c', 'custom_date_color': '#12382c',
    'custom_highlight_color_off_theme': '#108474', 'custom_bg_color_off_theme': '#f4f7f5',
    'highlight_color': '#108474', 'dot_color': '#108474', 'enable_background': True, 'bg_color': '#f4f7f5',
    'enable_border': False, 'border_color': '#e3ece8', 'border_width': 1, 'border_style': 'solid',
    'font_size': 12, 'container_margin_top': -10, 'container_margin_bottom': -5, 'enable_animation': True,
    'suffix_text': '', 'text_alignment': 'center'}},
  'easysell_cod_form_app_block_RX9DeH': {
    'type': 'shopify://apps/easysell-cod-form/blocks/app-block/7bfd0a95-6839-4f02-b2ee-896832dbe67e',
    'settings': {'product': ''}},
  'guarantee_badges_HAWQYD': {'type': 'guarantee_badges', 'settings': {
    'use_theme_colors': True, 'badge_1_show': True, 'badge_1_text': '30-Días de prueba sin riesgo',
    'badge_1_icon': 'custom_image', 'badge_1_dot_color': '#4caf50', 'badge_1_custom_icon': SVG_BADGE1,
    'badge_2_show': True, 'badge_2_text': 'Envío Gratis Incluido', 'badge_2_icon': 'custom_image',
    'badge_2_dot_color': '#4caf50', 'badge_2_custom_icon': SVG_FLAG, 'icon_color': '#108474',
    'text_color': '#12382c', 'container_margin_top': -5, 'container_margin_right': 0,
    'container_margin_bottom': 10, 'container_margin_left': 0, 'font_size': 13, 'icon_size': 13,
    'gap': 10, 'align_center': True, 'mobile_stack': False}},
  'money_back_guarantee_mtl': {'type': 'money_back_guarantee', 'settings': {
    'use_theme_colors': False, 'text_small': 'Aseguramos nuestro producto al 100%',
    'text_large': 'Si por algún motivo no te gusta nuestro producto o no funciona para ti, te reembolsamos todo lo que pagaste.',
    'badge_icon': 'shopify://shop_images/159594.webp', 'container_bg_color': '#f4f7f5',
    'border_color': '#e3ece8', 'enable_container_border': True, 'container_border_width': 1,
    'container_border_style': 'solid', 'container_border_color': '#e3ece8', 'container_border_radius': 6,
    'text_small_color': '#12382c', 'text_large_color': '#48584f', 'padding': 15, 'badge_size': 45,
    'icon_size': 30, 'text_small_size': 13, 'text_large_size': 13, 'margin_top': 5, 'margin_bottom': 0}},
  'replica_warning_wYwDwb': {'type': 'replica_warning', 'settings': {
    'warning_title': 'Cuidado con las imitaciones baratas.',
    'warning_text': 'Existen replicas de mala calidad en el mercado. Nuestro producto original solo se vende en MitaLabs Bolivia, con garantía de autenticidad y calidad asegurada.',
    'background_color': '#a40101', 'text_color': '#ffffff', 'border_color': '#ffffff',
    'icon_background_color': '#ffffff', 'icon_color': '#a40101', 'title_font_size': 20,
    'text_font_size': 14, 'border_width': 1, 'border_radius': 8, 'padding': 10,
    'margin_top': 5, 'margin_bottom': 15}},
  'customer_review_mtl1': cr('Carmen Q.', 'Años calentando agua cada mañana para que mis manos arranquen, y el agua se enfriaba al ratito. Ahora son 20 minutos con su calorcito parejo mientras tomo mi mate.', 'resena-1.webp'),
  'customer_review_mtl2': cr('Andrea V.', 'Meses poniéndole hielo porque lo vi en un video, y la sentía más dura. Con el calor es al revés: la uso enchufada a la laptop mientras trabajo.', 'resena-3.webp'),
  'customer_review_mtl3': cr('Paola F.', 'La férula me estorbaba para trabajar y la dejé a los dos días. Esta la uso de noche, después de cerrar el salón, y de día sigo con mis clientas.', 'resena-5.webp'),
  'video_carousel_standalone_cJ4iKc': {'type': 'video_carousel_standalone', 'disabled': True, 'settings': {
    'heading': 'Mírala en acción!', 'heading_size': 24, 'heading_color': '#12382c',
    'heading_letter_spacing': 'var(--letter-spacing-heading)', 'scrollbar_color': '#108474',
    'disable_sound_controls': False, 'enable_autoplay': False, 'show_sound_controls_autoplay': False,
    'play_button_size': 30, 'sound_button_size': 30, 'play_button_bg_color': '#000000',
    'play_button_bg_opacity': 35, 'sound_button_bg_color': '#000000', 'sound_button_bg_opacity': 35,
    'hide_scrollbar': False, 'video_size': 150, 'show_social_badge': False, 'social_platform': 'tiktok',
    'view_count': 56, 'badge_text': 'Over', 'badge_suffix': 'M Views On TikTok', 'use_gradient_text': False,
    'badge_background_color': '#f8f9fa', 'badge_text_color': '#262626', 'remove_badge_background': False,
    'show_divider_above_views': False, 'divider_color': '#e0e0e0', 'divider_width': 50,
    'divider_thickness': 1, 'divider_margin': 10, 'custom_badge_text': '', 'margin_top': 0, 'margin_bottom': 0}},
  'carousel_default_video_nVFMUw': vid('m1.mp4'),
  'carousel_default_video_VKUBtb': vid('m2.mp4'),
  'carousel_default_video_YK6Nzh': vid('m3.mp4'),
  'carousel_default_video_wQHnFY': vid('m4.mp4'),
  'facebook_comment_8m63hJ': {'type': 'facebook_comment', 'settings': {
    'profile_image': 'shopify://shop_images/istockphoto-1483329842-612x612.webp',
    'profile_center_color': '#4a90e2', 'author_name': 'Fabiola Suarez C.',
    'comment_text': 'A mi mamá le costaba abrir hasta el frasco de mermelada y en las mañanas se quedaba media hora sentada esperando que las manos le "arranquen". Se la puse hace dos semanas mientras tomábamos café y ahora se la pone sola todos los días. Ayer abrió el frasco sin pedirme ayuda. ¡Casi lloro!',
    'reaction_count': 12, 'time_stamp': '2d', 'author_name_font_size': 13, 'comment_text_font_size': 15,
    'meta_font_size': 13, 'use_facebook_font': False, 'block_padding': 16, 'margin_top': 16, 'margin_bottom': 16}},
  'product_tabs_hNJeCr': {'type': 'product_tabs', 'disabled': True, 'settings': {
    'block_heading': '', 'num_tabs': '4', 'block_heading_color': '#12382c', 'block_heading_size': 24,
    'block_heading_weight': '700', 'block_background': '#ffffff', 'block_margin_top': 6,
    'block_margin_bottom': 20, 'padding_top': 0, 'padding_bottom': 0, 'border_radius': 10,
    'tab_background': '#f4f7f5', 'tab_text_color': '#12382c', 'tab_font_size': 14,
    'tab_active_background': '#ffffff', 'tab_active_color': '#12382c', 'tab_border_color': '#e3ece8',
    'tab_divider_color': '#4a4a4a', 'content_text_color': '#48584f', 'content_text_size': 14,
    'tab1_title': 'Respaldo', 'tab1_author_info_gap': 4, 'tab1_star_rating': 5, 'tab1_star_color': '#f4c637',
    'tab1_star_size': 16,
    'tab1_quote': '<p>Para la rigidez y las molestias de sobreuso de muñeca y mano, en consulta casi siempre indicamos <strong>calor local</strong>: mejora el riego de la zona y la afloja. El problema de la bolsa o la compresa casera es que <strong>se enfrían a los pocos minutos</strong>, justo antes de que hagan efecto. Una fuente de <strong>calor parejo y sostenido</strong>, aplicada 15 a 20 minutos, es un gran apoyo para usar en casa.</p>',
    'tab1_author_image': 'shopify://shop_images/hombrera-fisio.webp', 'tab1_author_name': 'Lic. Mariela Justiniano',
    'tab1_author_title': 'Fisioterapeuta', 'tab1_author_title_font_size': 12, 'tab1_author_title_color': '#48584f',
    'tab1_author_title_background': 'rgba(0,0,0,0)', 'tab1_author_title_padding_v': 4,
    'tab1_author_title_padding_h': 8, 'tab1_author_title_border_radius': 4, 'tab1_author_date': 'Julio 8, 2026',
    'tab1_author_date_color': '#48584f', 'tab2_title': 'Comparación', 'tab2_show_icons': True,
    'tab2_content_layout': 'single_column', 'tab2_brand_background': '#12382c',
    'tab2_brand_name': 'Muñequera MitaLabs', 'tab2_others_label': 'Otras opciones',
    'tab2_item_1_name': 'Calor parejo toda la sesión',
    'tab2_item_1_description': 'La MitaLabs mantiene el calor de principio a fin; la bolsa de agua se enfría a los minutos.',
    'tab2_item_1_brand_has': True, 'tab2_item_1_others_has': False,
    'tab2_item_2_name': 'Afloja sin apretar en frío',
    'tab2_item_2_description': 'La MitaLabs suelta la zona con calor; la férula común aprieta e inmoviliza sin calentar nada.',
    'tab2_item_2_brand_has': True, 'tab2_item_2_others_has': False,
    'tab2_item_3_name': 'Mano libre mientras la usás',
    'tab2_item_3_description': 'Velcro con agarre de pulgar: seguís tecleando, leyendo o descansando con la muñequera puesta.',
    'tab2_item_3_brand_has': True, 'tab2_item_3_others_has': False,
    'tab2_item_4_name': 'USB universal, de lo que ya tenés',
    'tab2_item_4_description': 'Cargador, laptop, power bank o el puerto del auto: calor constante sin depender de nada más.',
    'tab2_item_4_brand_has': True, 'tab2_item_4_others_has': False, 'tab2_description_color': '#48584f',
    'tab2_description_font_size': 12, 'tab2_item_name_font_size': 14, 'tab2_column_header_font_size': 14,
    'tab2_item_name_color': '#12382c', 'tab2_brand_header_color': '#ffffff', 'tab2_others_header_color': '#12382c',
    'tab3_title': 'Cómo se usa', 'tab3_display_type': 'text', 'tab3_custom_text': '',
    'tab3_header_background': '#f8f9fa', 'tab3_column1_header': 'Detalle', 'tab3_column2_header': 'Valor',
    'tab3_num_items': 6,
    'tab3_row_1_label': 'Uso', 'tab3_row_1_sublabel': '15 a 20 min por sesión', 'tab3_row_1_value': '1 a 2 veces al día',
    'tab3_row_2_label': 'Funciones', 'tab3_row_2_sublabel': 'Calor sostenido + soporte suave', 'tab3_row_2_value': 'Control simple de un botón',
    'tab3_row_3_label': 'Energía', 'tab3_row_3_sublabel': 'Se alimenta por cable USB', 'tab3_row_3_value': 'Cargador, laptop, power bank o auto',
    'tab3_row_4_label': 'Cuidado', 'tab3_row_4_sublabel': 'Apagala y desconectala al terminar', 'tab3_row_4_value': 'Usala despierto, en sesiones cortas',
    'tab3_row_5_label': '', 'tab3_row_5_sublabel': '', 'tab3_row_5_value': '',
    'tab3_row_6_label': '', 'tab3_row_6_sublabel': '', 'tab3_row_6_value': '',
    'tab3_row_7_label': '', 'tab3_row_7_sublabel': '', 'tab3_row_7_value': '',
    'tab3_row_8_label': '', 'tab3_row_8_sublabel': '', 'tab3_row_8_value': '',
    'tab3_row_9_label': '', 'tab3_row_9_sublabel': '', 'tab3_row_9_value': '',
    'tab3_row_10_label': '', 'tab3_row_10_sublabel': '', 'tab3_row_10_value': '',
    'tab3_disclaimer_text': '', 'tab3_header_font_size': 14, 'tab3_label_font_size': 14,
    'tab3_sublabel_font_size': 12, 'tab3_value_font_size': 14, 'tab3_disclaimer_font_size': 12,
    'tab3_hide_table_borders': False, 'tab3_header_text_color': '#12382c', 'tab3_row_background_color': '#ffffff',
    'tab3_border_color': '#e5e5e5', 'tab3_label_color': '#12382c', 'tab3_sublabel_color': '#48584f',
    'tab3_value_color': '#48584f', 'tab3_disclaimer_color': '#666666', 'tab4_title': 'Beneficios',
    'tab4_content_layout': 'single_column', 'tab4_heading': 'Por qué la vas a usar todos los días',
    'tab4_heading_font_size': 20, 'tab4_benefit_font_size': 14, 'tab4_icon_size': 24,
    'tab4_heading_color': '#12382c', 'tab4_benefit_text_color': '#48584f', 'tab4_icon_bg_color': '#e5e5e5',
    'tab4_icon_check_color': '#000000', 'tab4_show_benefit_border': True,
    'tab4_benefit_1': 'Afloja la rigidez de la mañana con calor parejo, sin pastillas.',
    'tab4_benefit_2': 'Nada que tomar ni untar: calor local, y seguís con tu día.',
    'tab4_benefit_3': 'Usala en el escritorio, enchufada a la laptop, mientras trabajás.',
    'tab4_benefit_4': 'Devolvele a tu muñeca los minutos que los mil gestos del día le quitan.',
    'tab4_benefit_5': 'En invierno, el calorcito que tus manos piden apenas baja el sol.',
    'tab4_benefit_6': 'Una sola compra que sirve para ambas muñecas, cuando la necesites.',
    'tab4_benefit_7': '', 'tab4_benefit_8': ''}},
 },
 'block_order': ['number_one_award_wYc38H', 'trustpilot_rating_yUMGE7', 'title_4EWLUd', 'custom_text_jpmwCD',
  'price_wr9fm4', 'divider_nyDN4a', 'bullet_list_g7PBBg', 'shipping_notice_fxXbx6',
  'easysell_cod_form_app_block_RX9DeH', 'guarantee_badges_HAWQYD', 'money_back_guarantee_mtl',
  'replica_warning_wYwDwb', 'customer_review_mtl1', 'customer_review_mtl2', 'customer_review_mtl3',
  'video_carousel_standalone_cJ4iKc', 'carousel_default_video_nVFMUw', 'carousel_default_video_VKUBtb',
  'carousel_default_video_YK6Nzh', 'carousel_default_video_wQHnFY', 'facebook_comment_8m63hJ',
  'product_tabs_hNJeCr'],
 'custom_css': ['.custom-text-accent {font-weight: 700 !important;}',
  '.simple-variant-picker__selected-variant {opacity: 0% !important;}'],
 'name': 'Product Details',
 'settings': {
  'use_theme_colors': False, 'main_image_border_radius': 0, 'thumbnail_border_radius': 0,
  'current_product': '', 'section_bg_color': '#ffffff', 'blocks_spacing': 4, 'text_color': '#12382c',
  'accent_color': '#108474', 'divider_color': '#e3ece8', 'show_product_info': True,
  'show_product_gallery': True, 'show_product_variants': False, 'thumbnail_border_color': '#e3ece8',
  'thumbnail_active_border_color': '#108474', 'thumbnails_include_section_padding': False,
  'dots_color': '#c9d6cf', 'enable_full_width_image': False, 'enable_mobile_full_width_image': True,
  'image_aspect_ratio': '1:1', 'hide_thumbnails': False, 'dot_size': 8, 'dot_color': '#cccccc',
  'dot_active_color': '#000000', 'show_desktop_arrows': False, 'desktop_arrow_background': '#ffffff',
  'desktop_arrow_border': '#e0e0e0', 'desktop_arrow_icon': '#000000',
  'desktop_arrow_hover_background': '#f5f5f5', 'desktop_arrow_hover_border': '#d0d0d0',
  'arrow_border_radius': 50, 'arrow_opacity': 90, 'desktop_arrow_placement': 'overlaid',
  'show_mobile_arrows': True, 'mobile_arrow_placement': 'overlaid', 'mobile_thumbnails_2x2_grid': True,
  'hide_thumbnails_mobile': False, 'thumbnails_left_column_desktop': False,
  'thumbnails_fade_to_white_desktop': False, 'control_app_subscription_preselect': False,
  'seal_selling_plan_id_preselect': ''}
}

# ============ 2. TICKER — estructura del masajeador FINAL ============
S['scrolling_features_bar_mWQii9'] = {
 'type': 'scrolling-features-bar',
 'blocks': {
  'feature_item_c3mYCR': {'type': 'feature_item', 'settings': {'text': 'CALIDAD GARANTIZADA', 'icon_type': 'svg', 'icon': SC_SHIELD}},
  'feature_item_edritJ': {'type': 'feature_item', 'settings': {'text': 'ENVÍO GRATIS Y RÁPIDO', 'icon_type': 'svg', 'icon': SC_TRUCK}},
  'feature_item_dGdNVg': {'type': 'feature_item', 'settings': {'text': '+10.000 BOLIVIANOS SATISFECHOS', 'icon_type': 'svg', 'icon': SC_CHECK}},
 },
 'block_order': ['feature_item_c3mYCR', 'feature_item_edritJ', 'feature_item_dGdNVg'],
 'name': 'Scrolling Features Bar',
 'settings': {
  'theme_color_mode': 'custom', 'vertical_padding': 15, 'item_gap': 60, 'mobile_item_gap': 30,
  'font_size': 14, 'mobile_font_size': 12, 'letter_spacing': 1, 'uppercase_text': True,
  'override_bold': False, 'icon_size': 20, 'mobile_icon_size': 16, 'icon_spacing': 10,
  'slider_direction': 'left', 'scrolling_velocity': 45, 'pause_on_hover': True,
  'background_color': '#12382c', 'text_color': '#ffffff', 'icon_color': '#fffcfc',
  'use_gradient_background': False, 'background_gradient': '', 'enable_top_border': False,
  'top_border_width': 1, 'top_border_style': 'solid', 'top_border_color': '#e5e5e5',
  'enable_bottom_border': False, 'bottom_border_width': 1, 'bottom_border_style': 'solid',
  'bottom_border_color': '#e5e5e5'}
}

# ============ 3. STORE FEATURES munequera (disabled, verbatim) ============
S['store_features_HfR3fm'] = {
 'type': 'store-features',
 'blocks': {
  'feature_YtK7EJ': {'type': 'feature', 'settings': {'icon': 'shopify://shop_images/hombrera-icon-calor.svg',
    'title': 'Esta vez sí vas a sentir el calor',
    'description': 'La bolsa se enfría y la crema se evapora; esta mantiene el calor parejo la sesión completa, justo en la zona'}},
  'feature_Dem9Wd': {'type': 'feature', 'settings': {'icon': 'shopify://shop_images/02-pago-contra-entrega.svg',
    'title': 'Probala sin arriesgar tu plata',
    'description': 'En Santa Cruz recibís y recién pagás en tu puerta; en otras ciudades, por QR o transferencia'}},
  'feature_wfgLTr': {'type': 'feature', 'settings': {'icon': 'shopify://shop_images/hombrera-icon-sin-cables.svg',
    'title': 'Se alimenta de lo que ya tenés',
    'description': 'USB: cargador, laptop, power bank o el puerto del auto — calor constante que no se apaga a mitad de sesión'}},
  'feature_3ERnjc': {'type': 'feature', 'settings': {'icon': 'shopify://shop_images/04-registro-anvisa.svg',
    'title': 'Un ritual fácil de sostener',
    'description': 'Sesiones de 15 a 20 minutos que controlás vos: te la ajustás, la conectás y seguís con lo tuyo'}},
 },
 'block_order': ['feature_YtK7EJ', 'feature_Dem9Wd', 'feature_wfgLTr', 'feature_3ERnjc'],
 'disabled': True, 'name': 'Features',
 'settings': {
  'padding_top': 0, 'padding_bottom': 20, 'desktop_margin_top': 0, 'desktop_margin_bottom': 0,
  'mobile_margin_top': 0, 'mobile_margin_bottom': 0, 'mobile_section_padding_left': 20,
  'mobile_section_padding_right': 20, 'max_width': 1200, 'section_background_color': '#f4f7f5',
  'gap': 20, 'desktop_layout_gap': 40, 'mobile_layout_gap': 30, 'icon_size': 50,
  'desktop_icon_margin_bottom': 16, 'mobile_icon_size': 55, 'mobile_icon_gap': 0,
  'container_background_type': 'color',
  'container_background_color_desktop': 'linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(244, 247, 245, 1) 100%)',
  'container_background_color_mobile': 'linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(244, 247, 245, 1) 100%)',
  'border_radius': 6, 'enable_container_border': True, 'container_border_width': 1,
  'container_border_style': 'solid', 'container_border_color': '#e0e0e0', 'container_padding_top': 40,
  'container_padding_bottom': 40, 'container_padding_left': 20, 'container_padding_right': 20,
  'heading': '', 'heading_size_desktop': 36, 'heading_size_mobile': 30, 'feature_title_size_desktop': 18,
  'feature_title_size_mobile': 13, 'feature_desc_size_desktop': 13, 'feature_desc_size_mobile': 12,
  'heading_line_height': 1.2, 'sub_line_height': 1.2, 'body_line_height': 1.5,
  'heading_alignment': 'center', 'text_alignment': 'center', 'icon_alignment': 'center',
  'heading_color': '#12382c', 'title_color': '#12382c', 'desc_color': '#48584f', 'desktop_columns': 4,
  'tablet_columns': 4, 'mobile_columns': '2', 'tablet_breakpoint': 1024, 'mobile_breakpoint': 768}
}

# ============ 4. STICKY (masajeador final, adaptado en 2 textos, disabled) ============
S['sticky_add_to_cart_mtlbSt'] = {
 'type': 'sticky-add-to-cart', 'disabled': True, 'name': 'Sticky Add To Cart',
 'settings': {
  'trigger_behavior': 'scroll_percentage', 'scroll_percentage_trigger': 25,
  'select_button_behavior': 'scroll_to_section', 'show_section_numbers': False, 'scroll_offset': 0,
  'scroll_to_percentage': 50, 'button_link': '', 'fallback_title': 'Muñequera Térmica USB MitaLabs®',
  'button_text': 'Pedir ahora', 'rating_text': 'Calificación 4.8 "Excelente"',
  'satc_toggle_variant': False, 'turn_off_delivery_date': False, 'delivery_days': 5,
  'delivery_text_prefix': 'Recibila aprox. antes del', 'delivery_date_display_format': 'weekday_month_day',
  'use_theme_colors': False, 'background_color': '#ffffff', 'star_color': '#f4c637',
  'mobile_style': 'default', 'z_index': 9900, 'title_color': '#12382c', 'title_desktop_font_size': 16,
  'title_mobile_font_size': 14, 'title_letter_spacing': 0, 'use_global_button_styling': True,
  'custom_button_padding_y': 15, 'custom_button_font_size': 14, 'button_bg_color': '#108474',
  'button_hover_color': '#7bdbf1', 'button_text_color': '#ffffff', 'border_radius': 6,
  'rating_text_color': '#48584f', 'rating_text_font_weight': 'var(--font-weight-regular)',
  'rating_text_desktop_font_size': 14, 'rating_text_mobile_font_size': 14, 'rating_text_letter_spacing': 0,
  'delivery_text_color': '#48584f', 'delivery_text_font_weight': 'var(--font-weight-regular)',
  'delivery_text_desktop_font_size': 14, 'delivery_text_mobile_font_size': 11, 'delivery_text_letter_spacing': 0}
}

# ============ 5. PRODUCT BENEFITS (estructura masajeador final + contenido munequera) ============
def ben(t, d):
    return {'type': 'benefit', 'settings': {'title': t, 'description': d, 'benefit_color': '',
            'benefit_description_color': '', 'icon_size': 24, 'use_image': False, 'preset_icon': 'check',
            'use_custom_icon': False, 'custom_icon_svg': SVG_BCHECK}}
S['product_benefits_mtlbPB'] = {
 'type': 'product-benefits',
 'blocks': {
  'benefit_mtlb1': ben('Calor Parejo la Sesión Completa', 'Calor que se mantiene de principio a fin, no como la bolsa de agua que se enfría a los cinco minutos.'),
  'benefit_mtlb2': ben('Afloja Sin Apretar en Frío', 'Se ajusta suave con velcro y calienta la zona: nada que ver con la férula que inmoviliza tu mano.'),
  'benefit_mtlb3': ben('USB de lo que Ya Tenés', 'Cargador, laptop, power bank o el puerto del auto: calor constante sin depender de nada más.'),
  'benefit_mtlb4': ben('Un Ritual que Sí Podés Sostener', 'Sesiones de 15 a 20 minutos mientras trabajás o ves tele. Nada que tomar ni untar.'),
 },
 'block_order': ['benefit_mtlb1', 'benefit_mtlb2', 'benefit_mtlb3', 'benefit_mtlb4'],
 'name': 'Product Benefits',
 'settings': {
  'padding_top': 50, 'padding_bottom': 50, 'padding_left': 25, 'padding_right': 25,
  'image_position_desktop': 'right', 'heading_size_mobile': 34, 'heading_size_desktop': 35,
  'heading_line_height_mobile': 1.1, 'heading_line_height_desktop': 1.1, 'subtitle_size_mobile': 13,
  'subtitle_size_desktop': 13, 'benefit_title_size_mobile': 14, 'benefit_title_size_desktop': 14,
  'benefit_description_size_mobile': 12, 'benefit_description_size_desktop': 12,
  'accent_color': '#44977C', 'use_theme_colors': False, 'title_below_icon': False,
  'override_global_accent': False, 'accent_font_family': 'inherit', 'accent_font_style': 'normal',
  'accent_font_weight': 'inherit', 'use_accent_gradient': False,
  'accent_text_gradient': 'linear-gradient(45deg, rgba(239, 74, 101, 1), rgba(255, 107, 157, 1) 100%)',
  'accent_text_margin_left': 0,
  'list_background': 'linear-gradient(180deg, rgba(255, 255, 255, 1), rgba(240, 240, 240, 1) 100%)',
  'list_border_radius': 20, 'benefits_list_max_width': 450, 'border_color': '#e0e0e0',
  'heading_accent': 'Todos los Días en tu Casa.', 'heading_regular': 'Calor Real,',
  'subtitle': 'Descubrí por qué esta sí se siente: calor parejo que no se muere a mitad de sesión, con tu mano libre y sin pagar cremas mes tras mes.',
  'show_image': True, 'media_type': 'image', 'feature_image': 'shopify://shop_images/munequera-roadmap.webp',
  'image_alt': 'Feature product image', 'video_autoplay': True, 'video_muted': True, 'video_loop': True,
  'video_controls': False, 'mobile_image_full_width': False, 'hide_media_on_desktop': False,
  'image_column_full_height': False, 'image_margin_top': 0, 'image_margin_bottom': 20,
  'enable_image_border': False, 'image_border_width': 1, 'image_border_style': 'solid',
  'image_border_color': '#000000', 'image_border_radius': 8, 'heading_color': '#FFFCFC',
  'subtitle_color': '#FFFFFF', 'description_color': '#000000',
  'section_background': 'linear-gradient(180deg, rgba(16, 132, 116, 1), rgba(18, 56, 44, 1) 100%)',
  'use_background_image': False, 'background_image_size': 'cover', 'background_image_position_mode': 'preset',
  'background_image_position': 'center center', 'background_focal_point_x': 50, 'background_focal_point_y': 50,
  'background_image_attachment': 'scroll', 'background_overlay_enable': False,
  'background_overlay_color': '#0000004d', 'background_overlay_opacity': 30, 'enable_top_border': False,
  'top_border_width': 1, 'top_border_style': 'solid', 'top_border_color': '#e5e5e5',
  'enable_bottom_border': False, 'bottom_border_width': 1, 'bottom_border_style': 'solid',
  'bottom_border_color': '#e5e5e5'}
}

# ============ 6/10/14. DIVIDERS (masajeador final verbatim) ============
def dv(flip, color, disabled=False):
    d = {'type': 'divider', 'name': 'Divider', 'settings': {
        'use_theme_colors': True, 'divider_style': 'wavy', 'background_color': 'rgba(0,0,0,0)',
        'flip_direction': flip, 'keep_proportion': False, 'color': color, 'height': 25,
        'show_border': False, 'border_color': '#e0e0e0', 'border_width': 1, 'border_style': 'solid',
        'use_gradient': False,
        'gradient_background': 'linear-gradient(135deg, rgba(102, 126, 234, 1), rgba(118, 75, 162, 1) 100%)',
        'padding_top': 0, 'padding_bottom': 0}}
    if disabled: d['disabled'] = True
    return d
S['divider_mtlbD1'] = dv(True, '#44977C')
S['divider_mtlbD2'] = dv(False, '#108474', disabled=True)
S['divider_mtlbD3'] = dv(False, '#108474')

# ============ 7. IMAGE WITH TEXT nueva (estructura masajeador final + contenido munequera) ============
iw_checks = {'type': 'bullet_list', 'settings': {
  'two_columns': True, 'list_title': '',
  'list_item_1': 'Calor parejo la sesión completa', 'list_item_1_svg': SVG_CIRCLE,
  'list_item_2': 'Afloja sin apretar en frío', 'list_item_2_svg': SVG_CIRCLE,
  'list_item_3': 'USB: de lo que ya tenés', 'list_item_3_svg': SVG_CIRCLE,
  'list_item_4': 'Sirve en ambas muñecas', 'list_item_4_svg': SVG_CIRCLE,
  'list_item_5': 'Mano libre mientras la usás', 'list_item_5_svg': SVG_CIRCLE,
  'list_item_6': 'Pagás al recibir en Santa Cruz', 'list_item_6_svg': SVG_CIRCLE,
  'list_color': '#48584f', 'list_title_color': '#12382c', 'pill_style': False, 'pill_bg_color': '#108474',
  'pill_text_color': '#ffffff', 'pill_border_color': '#108474', 'pill_border_width': 1,
  'pill_border_radius': 6, 'pill_padding_vertical': 11, 'pill_padding_horizontal': 10, 'pill_spacing': 8,
  'margin_top': 0, 'margin_bottom': 0, 'font_size_mobile': 1.2, 'font_size_desktop': 1.4}}
S['image_with_text_mtlbIW'] = {
 'type': 'image-with-text',
 'blocks': {
  'paragraph_mtlbPromesa': {'type': 'paragraph', 'settings': {
    'paragraph_text': '<p>Adiós a esperar que las manos arranquen. La <strong>Muñequera Térmica MitaLabs</strong> convierte 15 a 20 minutos de tu día en tu sesión de calor: <strong>calor parejo que no se corta</strong> y va soltando la rigidez acumulada de muñeca y mano.</p>',
    'font_size_mobile': 1.5, 'font_size_desktop': 1.5, 'margin_top': -20, 'margin_bottom': 0,
    'paragraph_color': '#333333'}},
  'bullet_list_mtlbChecks': iw_checks,
  'button_mtlbCTA': {'type': 'button', 'settings': {
    'button_label': 'Pedir ahora', 'button_redirect_type': 'scroll_to_top', 'button_link': '',
    'redirect_product': '', 'redirect_collection': '', 'redirect_page': '', 'custom_url': '',
    'scroll_to_products': True, 'button_bg_color': '#108474', 'button_text_color': '#ffffff',
    'margin_top': 0, 'margin_bottom': 0, 'button_text_size': 18, 'button_border_radius': 4,
    'full_width_mobile': False, 'disable_global_button_styling': False}},
 },
 'block_order': ['paragraph_mtlbPromesa', 'bullet_list_mtlbChecks', 'button_mtlbCTA'],
 'name': 'Image with Text',
 'settings': {
  'use_theme_colors': False, 'inverse_theme_colors': False, 'image_position': 'right',
  'image_position_mobile': 'top', 'heading_above_image_mobile': False, 'text_align': 'left',
  'center_align_with_media': False, 'text_column_width': 50, 'margin_top_mobile': 0,
  'margin_bottom_mobile': 20, 'margin_top_desktop': 0, 'margin_bottom_desktop': 0,
  'padding_top_mobile': 40, 'padding_bottom_mobile': 40, 'container_padding_mobile': 20,
  'padding_top_desktop': 60, 'padding_bottom_desktop': 60, 'container_padding_desktop': 80,
  'content_spacing': 30, 'mobile_full_width_gap': 0, 'desktop_content_spacing': 40,
  'section_border_radius': 0, 'section_max_width': 1200, 'contain_section': False,
  'container_max_width': 1200, 'container_bg_color': '#f4f7f5', 'enable_container_gradient': False,
  'container_gradient_background': 'linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(248, 248, 248, 1) 100%)',
  'container_padding_vertical': 40, 'container_padding_horizontal': 100,
  'container_padding_vertical_mobile': 30, 'container_padding_horizontal_mobile': 20,
  'container_margin_top': 0, 'container_margin_bottom': 0, 'container_margin_left': 0,
  'container_margin_right': 0, 'container_margin_top_mobile': 0, 'container_margin_bottom_mobile': 0,
  'container_margin_left_mobile': 0, 'container_margin_right_mobile': 0, 'enable_border': False,
  'border_width': 1, 'border_style': 'solid', 'border_color': '#e5e7eb', 'border_radius': 8,
  'enable_shadow': False, 'heading': 'Manos Sueltas.', 'heading_accent': 'Y mañanas tranquilas.',
  'image': 'shopify://shop_images/munequera-razon-1.webp', 'enable_image_fade_mask': False,
  'video_autoplay': True, 'video_loop': True, 'video_muted': True, 'video_controls': False,
  'text_font_size_mobile': 1.1, 'text_font_size_desktop': 1.2, 'content_elements_spacing': 15,
  'desktop_content_elements_spacing': 20, 'mobile_heading_bottom_margin': 20,
  'desktop_heading_bottom_margin': 25, 'text_bottom_margin': 25, 'desktop_text_bottom_margin': 25,
  'text_padding_vertical': 0, 'text_padding_left': 0, 'text_padding_right': 0,
  'mobile_text_padding_vertical': 0, 'mobile_text_padding_horizontal': 0, 'button_padding_vertical': 12,
  'button_padding_horizontal': 24, 'button_border_radius': 4, 'background_color': '#f4f7f5',
  'background_gradient': '', 'heading_color': '#12382c', 'accent_color': '#108474',
  'text_color': '#48584f', 'button_bg_color': '#ef4a65', 'button_text_color': '#ffffff',
  'image_max_width': 800, 'image_max_height': 0, 'image_border_radius': 8, 'image_padding': 0,
  'mobile_image_full_width': False, 'desktop_image_full_height': False, 'full_height_section_height': 100,
  'use_background_image': False, 'background_image_position': 'center center',
  'background_image_size': 'cover', 'enable_top_border': False, 'top_border_width': 1,
  'top_border_color': '#000000', 'enable_bottom_border': False, 'bottom_border_width': 1,
  'bottom_border_color': '#000000', 'heading_size_desktop': 48, 'subtitle_size_mobile': 18,
  'override_global_accent': False, 'accent_font_family': 'inherit', 'accent_font_style': 'inherit',
  'accent_font_weight': 'inherit', 'use_accent_gradient': False, 'accent_text_gradient': '',
  'accent_text_margin_left': 0}
}

# ============ 8. 4 IMAGES munequera (verbatim) ============
def item(img, t, d):
    return {'type': 'item', 'settings': {'media_type': 'image', 'step_image': f'shopify://shop_images/{img}',
            'step_title': t, 'step_description': d}}
S['4_images_6wqdKm'] = {
 'type': '4-images',
 'blocks': {
  'item_enQcqM': item('munequera-ritual-1.webp', '1. Ajustala con el velcro', 'En la muñeca que la necesite, con el pulgar en su agarre'),
  'item_LEjhgD': item('munequera-ritual-2.webp', '2. Conectala al USB', 'Cargador, laptop, power bank o el puerto del auto'),
  'item_CbkQcC': item('munequera-ritual-3.webp', '3. Relajate 15 a 20 minutos', 'El calor parejo afloja la zona mientras seguís con lo tuyo'),
  'item_Wbn6LC': item('munequera-ritual-4.webp', 'Desconectala y seguí tu día', 'Guardala o pasala a la otra muñeca cuando la necesite'),
 },
 'block_order': ['item_enQcqM', 'item_LEjhgD', 'item_CbkQcC', 'item_Wbn6LC'],
 'name': '4 Images',
 'settings': {
  'use_theme_colors': False, 'main_heading': 'Tu ritual de alivio', 'accent_text': 'en 3 pasos',
  'subtitle': 'Simple y fácil de sostener todos los días.', 'text_alignment': 'center',
  'section_padding_top': 60, 'section_padding_bottom': 60, 'section_max_width': 1600,
  'container_padding_horizontal': 20, 'desktop_columns': 4, 'tablet_columns': 2, 'mobile_columns': '1',
  'desktop_gap_vertical': 30, 'desktop_gap_horizontal': 30, 'main_heading_font_size_desktop': 48,
  'main_heading_line_height_desktop': 1.2, 'main_heading_font_size_mobile': 24,
  'main_heading_line_height_mobile': 1.2, 'subtitle_font_size_desktop': 18, 'subtitle_font_size_mobile': 12,
  'item_title_font_size': 20, 'item_title_bold': False, 'item_description_font_size': 14,
  'grid_margin_top': 10, 'main_heading_margin_top': 0, 'main_heading_margin_bottom': 10,
  'subtitle_margin_top': 0, 'subtitle_margin_bottom': 20, 'content_margin_top': 20,
  'step_title_margin_top': 0, 'step_title_margin_bottom': 8, 'step_description_margin_top': 0,
  'step_description_margin_bottom': 0, 'divider_margin_top': 16, 'divider_margin_bottom': 16,
  'section_background_color': '#ffffff', 'main_heading_color': '#12382c', 'subtitle_color': '#48584f',
  'step_title_color': '#12382c', 'step_description_color': '#48584f', 'override_global_accent': True,
  'use_accent_gradient': False, 'accent_text_gradient': '', 'accent_color': '#108474',
  'accent_text_margin_left': 0, 'show_divider': False, 'divider_width': 50, 'divider_thickness': 2,
  'divider_color': '#000000', 'divider_alignment': 'center', 'enable_card_styling': True,
  'card_background_color': '#f4f7f5', 'card_border_color': '#12382c', 'card_border_width': 1,
  'card_border_radius': 4, 'image_border_radius': 6, 'card_padding_horizontal': 18,
  'card_padding_vertical': 20, 'image_focal_point': 'center', 'placeholder_background_color': '#eef3f0',
  'placeholder_text_color': '#90a59c'}
}

# ============ 9. 4 CARDS munequera (verbatim) ============
def card(img, t, d):
    return {'type': 'card', 'settings': {'card_image': f'shopify://shop_images/{img}', 'card_title': t,
        'card_description': d, 'show_bullets': False, 'bullet_icon': '', 'bullet_points': '',
        'bullet_icon_color': '#333333', 'bullet_text_color': '#48584f', 'bullet_container': False,
        'bullet_container_bg': '#f8f9fa', 'bullet_container_border_color': '#e9ecef',
        'bullet_container_border_style': 'solid', 'bullet_container_border_width': 1,
        'bullet_container_border_radius': 4}}
S['4_cards_jDTiEi'] = {
 'type': '4-cards',
 'blocks': {
  'card_QCJgGg': card('munequera-card-1.webp', 'El agua caliente que no se enfría', 'El calor que tu cuerpo ya conoce, pero parejo la sesión completa y con las manos libres'),
  'card_3WhhLd': card('munequera-card-2.webp', 'No fallaste vos: te dieron frío y apretón', 'Férulas que aprietan en frío, hielo que endurece y cremas que se evaporan: por eso seguías igual'),
  'card_whC8LR': card('munequera-card-3.webp', 'Se enchufa a lo que ya tenés', 'Cargador, laptop, power bank o el puerto del auto: calor constante que no se apaga a mitad de sesión'),
 },
 'block_order': ['card_QCJgGg', 'card_3WhhLd', 'card_whC8LR'],
 'name': 'Cards',
 'settings': {
  'heading': 'Por qué esta vez tu muñeca', 'accent_text': 'sí va a responder',
  'subtitle': 'Por qué no es una muñequera más.', 'horizontal_layout': True, 'pyramid_layout': False,
  'hide_description': False, 'heading_alignment': 'center', 'heading_size': 52, 'heading_size_mobile': 36,
  'heading_color': '#12382c', 'subtitle_color': '#48584f', 'title_size': 22, 'title_size_mobile': 14,
  'title_color': '#12382c', 'description_size': 14, 'description_size_mobile': 12,
  'description_color': '#48584f', 'bullet_size': 13, 'bullet_size_mobile': 9, 'accent_color': '#108474',
  'use_accent_gradient': False, 'accent_text_gradient': '', 'accent_left_margin': 0,
  'override_global_accent': True, 'accent_font_family': 'inherit', 'accent_font_style': 'normal',
  'accent_font_weight': '700', 'card_background_gradient': '#f4f7f5', 'card_border_color': '#12382c',
  'card_border_style': 'solid', 'card_border_width': 1, 'card_border_radius': 12,
  'card_image_object_fit': 'cover', 'image_inside_padding': True, 'image_padding': 10,
  'image_border_radius': 8, 'card_image_height_desktop': 220, 'card_image_height_mobile': 110,
  'card_image_height_horizontal_desktop': 150, 'card_image_height_horizontal_mobile': 100,
  'card_min_height_desktop': 0, 'padding_top': 30, 'padding_bottom': 60, 'padding_left': 20,
  'padding_right': 20, 'section_background_gradient': '#ffffff'}
}

# ============ 11. BEFORE/AFTER (estructura masajeador final + contenido munequera) ============
S['before_after_mtlbBA'] = {
 'type': 'before-after-comparison', 'name': 'Before After Comparison',
 'settings': {
  'use_theme_colors': False, 'enable_two_column_layout': False, 'text_alignment': 'left',
  'mobile_text_alignment': 'center', 'column_gap': 50, 'text_column_width': 40,
  'mobile_container_padding': 16, 'tablet_container_padding': 24, 'comparison_container_padding_top': 0,
  'comparison_container_padding_right': 16, 'comparison_container_padding_bottom': 0,
  'comparison_container_padding_left': 16, 'title': 'Menos Rigidez,', 'title_accent': 'Más Soltura.',
  'override_global_accent': False, 'accent_color': '#108474', 'use_accent_gradient': False,
  'accent_text_gradient': 'linear-gradient(45deg, rgba(239, 74, 101, 1), rgba(255, 107, 157, 1) 100%)',
  'accent_font_family': 'inherit', 'accent_font_style': 'normal', 'accent_font_weight': 'inherit',
  'accent_letter_spacing': 0, 'accent_text_transform': 'none', 'accent_text_margin_left': 0,
  'description': 'Mirá la transformación: de esperar a que las manos arranquen a empezar el día con la muñeca suelta, con tu ritual de 15 a 20 minutos.',
  'additional_description': '', 'instructions_text': 'Drag the slider to see the difference',
  'before_image': 'shopify://shop_images/munequera-card-2.webp',
  'after_image': 'shopify://shop_images/munequera-ritual-3.webp',
  'before_label': 'Antes', 'after_label': 'Después', 'initial_position': 50, 'container_max_width': 600,
  'page_width': 1200, 'container_border_radius': 8, 'title_font_size': 32, 'description_font_size': 16,
  'instructions_font_size': 14, 'label_font_size': 12, 'title_font_size_mobile': 24,
  'description_font_size_mobile': 14, 'instructions_font_size_mobile': 12, 'label_font_size_mobile': 11,
  'image_aspect_ratio': '4/3', 'image_min_height': 250, 'image_max_height': 500,
  'mobile_aspect_ratio': '4/3', 'mobile_min_height': 200, 'mobile_max_height': 400,
  'mobile_container_width': 320, 'section_background_color': '#ffffff', 'title_color': '#12382c',
  'description_color': '#48584f', 'instructions_color': '', 'slider_button_bg': '',
  'slider_button_border': '', 'slider_button_icon': '', 'image_label_bg': '', 'image_label_text': '',
  'contain_section': False, 'container_padding_top': 40, 'container_padding_right': 40,
  'container_padding_bottom': 40, 'container_padding_left': 40, 'container_padding_top_mobile': 20,
  'container_padding_right_mobile': 20, 'container_padding_bottom_mobile': 20,
  'container_padding_left_mobile': 20,
  'container_background': 'linear-gradient(180deg, rgba(255, 255, 255, 1), rgba(248, 248, 248, 1) 100%)',
  'enable_border': False, 'border_width': 1, 'border_style': 'solid', 'border_color': '#e5e7eb',
  'enable_shadow': False}
}

# ============ 12. IMAGE WITH TEXT hmnhFF munequera (verbatim) ============
S['image_with_text_hmnhFF'] = {
 'type': 'image-with-text',
 'blocks': {
  'paragraph_chBURf': {'type': 'paragraph', 'settings': {
    'paragraph_text': '<p>La férula común <strong>aprieta el músculo en frío</strong> y estorba para todo, por eso terminó en el cajón. La crema alivia <strong>lo que dura el olor</strong> y se evapora. Y la bolsa de agua caliente sí ayuda… <strong>cinco minutos, hasta que se enfría</strong> — justo antes de aflojar de verdad. Por eso tanta gente dice que nada le hizo nada.</p>',
    'font_size_mobile': 1.5, 'font_size_desktop': 1.5, 'margin_top': -20, 'margin_bottom': 0,
    'paragraph_color': '#333333'}},
  'bullet_list_EXq7Ba': {'type': 'bullet_list', 'settings': {
    'two_columns': True, 'list_title': '',
    'list_item_1': 'La férula aprieta en frío y estorba para trabajar', 'list_item_1_svg': SVG_X,
    'list_item_2': 'La crema se evapora y el alivio se va con ella', 'list_item_2_svg': SVG_X,
    'list_item_3': 'La bolsa de agua se enfría antes de aflojar', 'list_item_3_svg': SVG_X,
    'list_item_4': 'Lo que alivia es calor parejo, la sesión completa', 'list_item_4_svg': SVG_X,
    'list_item_5': '', 'list_item_5_svg': '', 'list_item_6': '', 'list_item_6_svg': '',
    'list_color': '#48584f', 'list_title_color': '#12382c', 'pill_style': True, 'pill_bg_color': '#108474',
    'pill_text_color': '#ffffff', 'pill_border_color': '#108474', 'pill_border_width': 1,
    'pill_border_radius': 6, 'pill_padding_vertical': 11, 'pill_padding_horizontal': 10,
    'pill_spacing': 8, 'margin_top': 0, 'margin_bottom': 0, 'font_size_mobile': 1.2, 'font_size_desktop': 1.6}},
  'paragraph_XYkPH3': {'type': 'paragraph', 'settings': {
    'paragraph_text': '<p>La <strong>Muñequera Térmica MitaLabs</strong> corrige las tres cosas: <strong>calor parejo que no se muere</strong> a mitad de sesión, <strong>ajuste con velcro que no inmoviliza</strong> tu mano, y alimentación <strong>USB de lo que ya tenés</strong> (cargador, laptop, power bank o auto). La que sí llega a aflojar.</p>',
    'font_size_mobile': 1.5, 'font_size_desktop': 1.5, 'margin_top': 0, 'margin_bottom': 0,
    'paragraph_color': '#333333'}},
 },
 'block_order': ['paragraph_chBURf', 'bullet_list_EXq7Ba', 'paragraph_XYkPH3'],
 'name': 'Image with Text',
 'settings': {
  'use_theme_colors': False, 'inverse_theme_colors': False, 'image_position': 'left',
  'image_position_mobile': 'top', 'heading_above_image_mobile': False, 'text_align': 'left',
  'center_align_with_media': False, 'text_column_width': 50, 'margin_top_mobile': 0,
  'margin_bottom_mobile': 20, 'margin_top_desktop': 0, 'margin_bottom_desktop': 0,
  'padding_top_mobile': 40, 'padding_bottom_mobile': 40, 'container_padding_mobile': 20,
  'padding_top_desktop': 60, 'padding_bottom_desktop': 60, 'container_padding_desktop': 80,
  'content_spacing': 30, 'mobile_full_width_gap': 0, 'desktop_content_spacing': 40,
  'section_border_radius': 0, 'section_max_width': 1200, 'contain_section': False,
  'container_max_width': 1200, 'container_bg_color': '#ffffff', 'enable_container_gradient': False,
  'container_gradient_background': 'linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(248, 248, 248, 1) 100%)',
  'container_padding_vertical': 40, 'container_padding_horizontal': 100,
  'container_padding_vertical_mobile': 30, 'container_padding_horizontal_mobile': 20,
  'container_margin_top': 0, 'container_margin_bottom': 0, 'container_margin_left': 0,
  'container_margin_right': 0, 'container_margin_top_mobile': 0, 'container_margin_bottom_mobile': 0,
  'container_margin_left_mobile': 0, 'container_margin_right_mobile': 0, 'enable_border': False,
  'border_width': 1, 'border_style': 'solid', 'border_color': '#e5e7eb', 'border_radius': 8,
  'enable_shadow': False, 'heading': 'Por qué lo que probaste', 'heading_accent': 'no te alivió',
  'image': 'shopify://shop_images/munequera-mecanismo.webp', 'enable_image_fade_mask': False,
  'video_autoplay': True, 'video_loop': True, 'video_muted': True, 'video_controls': False,
  'text_font_size_mobile': 1.1, 'text_font_size_desktop': 1.2, 'content_elements_spacing': 15,
  'desktop_content_elements_spacing': 20, 'mobile_heading_bottom_margin': 20,
  'desktop_heading_bottom_margin': 25, 'text_bottom_margin': 25, 'desktop_text_bottom_margin': 25,
  'text_padding_vertical': 0, 'text_padding_left': 0, 'text_padding_right': 0,
  'mobile_text_padding_vertical': 0, 'mobile_text_padding_horizontal': 0, 'button_padding_vertical': 12,
  'button_padding_horizontal': 24, 'button_border_radius': 4, 'background_color': '#ffffff',
  'background_gradient': '', 'heading_color': '#12382c', 'accent_color': '#108474',
  'text_color': '#48584f', 'button_bg_color': '#ef4a65', 'button_text_color': '#ffffff',
  'image_max_width': 800, 'image_max_height': 0, 'image_border_radius': 8, 'image_padding': 0,
  'mobile_image_full_width': False, 'desktop_image_full_height': False, 'full_height_section_height': 100,
  'use_background_image': False, 'background_image_position': 'center center',
  'background_image_size': 'cover', 'enable_top_border': False, 'top_border_width': 1,
  'top_border_color': '#000000', 'enable_bottom_border': False, 'bottom_border_width': 1,
  'bottom_border_color': '#000000', 'heading_size_desktop': 48, 'subtitle_size_mobile': 18,
  'override_global_accent': False, 'accent_font_family': 'inherit', 'accent_font_style': 'inherit',
  'accent_font_weight': 'inherit', 'use_accent_gradient': False, 'accent_text_gradient': '',
  'accent_text_margin_left': 0}
}

# ============ 13. PRODUCT COMPARISON munequera (verbatim) ============
def pcol(name, sub, highlight, img_mob):
    s = {'product_name': name, 'product_subtitle': sub, 'product_image_size': 80,
         'product_image_size_mobile': img_mob, 'subtitle_custom_icon': '', 'show_subtitle_icon': True,
         'use_subtitle_background': True}
    if highlight:
        s.update({'subtitle_border_color': '#ffffff', 'highlight_column': True, 'highlight_color': '#12382c',
                  'use_highlight_gradient': True, 'highlight_gradient_start_color': '#12382c',
                  'highlight_gradient_end_color': '#108474', 'highlight_gradient_angle': 210,
                  'subtitle_glass_color': '#ffffff', 'subtitle_icon_color': '#12382c'})
    else:
        s.update({'subtitle_border_color': '#e3ece8', 'highlight_column': False, 'highlight_color': '#f4f7f5',
                  'use_highlight_gradient': False, 'highlight_gradient_start_color': '#ef4a65',
                  'highlight_gradient_end_color': '#ef4a65', 'highlight_gradient_angle': 45,
                  'subtitle_glass_color': '#f4f7f5', 'subtitle_icon_color': '#12382c'})
    return {'type': 'product_column', 'name': 'A' if highlight else 'B', 'settings': s}
S['product_comparison_ahRqAP'] = {
 'type': 'product-comparison',
 'blocks': {
  'product_column_HQQ9kd': pcol('Muñequera Térmica MitaLabs', 'Calor parejo, mano libre', True, 75),
  'product_column_DF3TFg': pcol('Férula / muñequera común', 'Aprieta en frío, no calienta', False, 50),
  'product_column_VITAL3': pcol('Bolsa de agua / cremas', 'El alivio se muere al rato', False, 50),
  'feature_row_DrAYGc': frow('Calor parejo los 20 minutos completos', 'yes', 'no', 'no'),
  'feature_row_jVg8fd': frow('Afloja la zona sin apretarla en frío', 'yes', 'no', 'no'),
  'feature_row_jKJjfC': frow('Deja tu mano libre para seguir con lo tuyo', 'yes', 'no', 'yes'),
  'feature_row_7AHheD': frow('Sirve en ambas muñecas con un solo equipo', 'yes', 'no', 'no'),
  'feature_row_3KqcXw': frow('Nada que tomar ni untar sobre la piel', 'yes', 'yes', 'no'),
  'feature_row_RD8MMV': frow('Acompañamiento por WhatsApp y compra protegida', 'yes', 'no', 'no'),
 },
 'block_order': ['product_column_HQQ9kd', 'product_column_DF3TFg', 'product_column_VITAL3',
  'feature_row_DrAYGc', 'feature_row_jVg8fd', 'feature_row_jKJjfC', 'feature_row_7AHheD',
  'feature_row_3KqcXw', 'feature_row_RD8MMV'],
 'settings': {
  'use_theme_colors': False, 'column_count': '3', 'show_heading': True,
  'title_part_1': 'No fallaste vos: te dieron la solución incompleta',
  'title_part_2': '(por eso esta vez sí lo vas a sentir)',
  'title_part_1_color': '#12382c', 'title_part_2_color': '#108474', 'subheading': '',
  'desktop_description': '<p>El problema nunca fue tu mano. Fue <strong>la férula que aprieta en frío, la crema que se evapora y la bolsa que se enfría a los cinco minutos</strong>. La <strong>Muñequera Térmica MitaLabs</strong> lo corrige: calor parejo que dura la sesión completa, ajuste con velcro que deja tu mano libre, y USB de lo que ya tenés. Y la probás pagando al recibir.</p>',
  'show_description_on_mobile': False, 'heading_size_mobile': 36, 'heading_size_desktop': 52,
  'subheading_size': 12, 'heading_line_height': 1.1, 'subheading_color': '#48584f',
  'desktop_description_size_mobile': 12, 'desktop_description_size_desktop': 16,
  'override_global_accent': False, 'accent_text_margin_left': 12, 'use_accent_gradient': False,
  'accent_text_gradient': '', 'accent_font_family': 'inherit', 'accent_font_style': 'normal',
  'accent_font_weight': '300', 'table_column_position': 'right', 'product_header_width_desktop': 80,
  'table_column_width': 40, 'center_text_column_desktop': True, 'padding_top': 40, 'padding_bottom': 40,
  'padding_horizontal': 20, 'mobile_padding_top': 32, 'mobile_padding_bottom': 32,
  'mobile_padding_horizontal': 16, 'container_padding_vertical_desktop': 0,
  'container_padding_horizontal_desktop': 0, 'container_padding_vertical_mobile': 0,
  'container_padding_horizontal_mobile': 16, 'table_width': 1200, 'text_column_padding_mobile': 20,
  'text_column_padding_desktop': 40, 'product_title_size': 21, 'subtitle_size': 10,
  'feature_name_size': 15, 'text_value_size': 14, 'product_title_size_mobile': 16,
  'subtitle_size_mobile': 10, 'feature_name_size_mobile': 12, 'text_value_size_mobile': 10,
  'icon_size_desktop': 24, 'icon_size_mobile': 20, 'use_custom_check_icons': False,
  'use_gradient_background': True, 'background_color': '#ffffff',
  'background_gradient': 'linear-gradient(180deg, rgba(255, 255, 255, 1), rgba(244, 247, 245, 1) 100%)',
  'use_background_image': False, 'background_image_size': 'cover',
  'background_image_position': 'center center', 'background_image_repeat': 'no-repeat',
  'background_overlay_enable': False, 'background_overlay_color': '#000000',
  'background_overlay_opacity': 30, 'text_color': '#12382c', 'subtitle_color': '#48584f',
  'highlighted_text_color': '#ffffff', 'highlighted_subtitle_color': '#d6e6de',
  'highlighted_check_color': '#ffffff', 'highlighted_x_color': '#ffd0d8', 'border_color': '#e3ece8',
  'icon_color': '#12382c', 'check_color': '#108474', 'x_color': '#ef4a65', 'highlight_border_radius': 6,
  'use_highlight_border': True, 'highlight_border_color': '#108474', 'enable_highlight_shadow': True,
  'highlight_border_width': 1, 'unhighlighted_text_color': '#12382c',
  'unhighlighted_subtitle_color': '#48584f', 'unhighlighted_icon_color': '#12382c',
  'unhighlighted_check_color': '#108474', 'unhighlighted_x_color': '#ef4a65',
  'enable_section_top_border': False, 'section_top_border_width': 1, 'section_top_border_style': 'solid',
  'section_top_border_color': '#e5e5e5', 'enable_section_bottom_border': False,
  'section_bottom_border_width': 1, 'section_bottom_border_style': 'solid',
  'section_bottom_border_color': '#e5e5e5'}
}

# ============ 15. SATISFACTION munequera (verbatim) ============
S['satisfaction_guarantee_J4ypTy'] = {
 'type': 'satisfaction-guarantee',
 'custom_css': ['.accent-text {color: white !important;}'],
 'settings': {
  'use_theme_colors': False, 'show_photos': False, 'allow_overflow': False, 'icon_style': 'custom',
  'custom_svg_code': '', 'icon_color': '#9edfca', 'icon_margin_bottom': 10,
  'accent_text': 'Compra sin riesgo',
  'heading_text': 'Recibí primero, pagá tranquilo cuando ya la tenés en tus manos',
  'description_text': '<p>Sabemos que ya te decepcionaron antes: la férula que <strong>estorbaba</strong>, la crema que se evaporaba, la bolsa que se enfriaba. Por eso no te pedimos que confíes a ciegas. En <strong>Santa Cruz</strong> comprás con <strong>pago contra entrega</strong>: recibís tu Muñequera Térmica MitaLabs en tu puerta y recién ahí, con el producto en tus manos, pagás en efectivo. En el resto de Bolivia el pago es anticipado por QR o transferencia, siempre con <strong>30 días de garantía</strong> y cambio si llega dañada.</p>',
  'product_name': 'Muñequera Térmica MitaLabs', 'heading_text_color': '#ffffff',
  'description_color': '#ffffff', 'benefit_text_color': '#ffffff', 'checkmark_icon_color': '#9edfca',
  'heading_size_desktop': 44, 'heading_size_mobile': 36, 'heading_line_height': 1,
  'description_size_desktop': 14, 'description_size_mobile': 14, 'benefit_size_desktop': 14,
  'benefit_size_mobile': 14, 'description_line_height': 1.5, 'accent_color': '#9edfca',
  'accent_text_margin_left': 4, 'use_global_accent_typography': False, 'use_accent_gradient': False,
  'accent_text_gradient': '', 'accent_font_family': 'inherit', 'accent_font_style': 'normal',
  'accent_font_weight': '700', 'button_text': 'Pedir ahora', 'button_action_type': 'scroll',
  'redirect_product': '', 'custom_url': '', 'use_global_button_style': False, 'button_color': '#000000',
  'button_text_color': '#ffffff', 'button_font_size': 16, 'button_font_weight': '600',
  'button_border_radius': 8, 'button_padding_vertical': 12, 'button_padding_horizontal': 20,
  'benefit_1': 'En Santa Cruz pagás al recibir; en el resto del país, compra protegida con garantía',
  'benefit_2': 'Calor parejo garantizado: 30 días para probarla con calma',
  'benefit_3': 'Cambio asegurado si tu pedido llega dañado',
  'polaroid_size_desktop': 180, 'polaroid_size_mobile': 100, 'image_extension': 80,
  'image_vertical_offset': 0, 'content_padding_mobile': 10, 'content_padding_desktop': 70,
  'content_width_with_photos': 50, 'content_max_width_with_photos': 600,
  'content_max_width_no_photos': 450, 'padding_top': 60, 'padding_bottom': 50, 'padding_top_mobile': 40,
  'padding_bottom_mobile': 40, 'padding_top_no_photos_mobile': 15, 'padding_top_no_photos_desktop': 15,
  'section_padding_vertical': 30, 'section_padding_horizontal': 0, 'section_padding_vertical_mobile': 0,
  'section_padding_horizontal_mobile': 0, 'enable_top_border': False, 'top_border_width': 1,
  'top_border_color': '#000000', 'enable_bottom_border': False, 'bottom_border_width': 1,
  'bottom_border_color': '#000000',
  'section_background': 'linear-gradient(180deg, rgba(166, 186, 180, 1), rgba(129, 193, 173, 1) 96%)',
  'background_image_position': 'center center', 'background_image_size': 'cover',
  'background_image_repeat': 'no-repeat', 'contain_section': False, 'container_padding': 0,
  'container_background': '', 'container_bg_size': 'cover', 'container_bg_position': 'center center',
  'enable_container_bg_overlay': False, 'container_bg_overlay_color': '#000000',
  'container_bg_overlay_opacity': 30, 'enable_border': False, 'border_width': 1,
  'border_style': 'solid', 'border_color': '#108474', 'border_radius': 8, 'enable_shadow': False}
}

# ============ 16. PHOTO GRID (estructura masajeador final + imagenes munequera, badge OFF) ============
PG_IMGS = ['resena-1-carmen.webp', 'munequera-ritual-1.webp', 'resena-4-andrea.webp',
           'munequera-ritual-2.webp', 'resena-3-gabriela.webp', 'munequera-ritual-3.webp',
           'resena-2-paola.webp', 'munequera-ritual-4.webp', 'resena-5-rodrigo.webp']
pg_blocks, pg_order = {}, []
for i, img in enumerate(PG_IMGS, 1):
    k = f'image_item_mtlb{i}'
    pg_blocks[k] = {'type': 'image_item', 'settings': {'image': f'shopify://shop_images/{img}',
                    'custom_position': '', 'link': '', 'caption': ''}}
    pg_order.append(k)
S['photo_grid_mtlbPG'] = {
 'type': 'photo-grid', 'blocks': pg_blocks, 'block_order': pg_order, 'name': 'Photo Grid',
 'settings': {
  'use_theme_colors': False, 'title_primary': '¡Más de 10.000', 'title_accent': 'Bolivianos Aliviados!',
  'subtitle': 'Gente real soltando las manos con su MitaLabs en toda Bolivia.',
  'title_font_size': 36, 'title_font_size_mobile': 28, 'subtitle_font_size': 18,
  'subtitle_font_size_mobile': 16, 'title_margin_bottom': 20, 'subtitle_margin_bottom': 16,
  'text_alignment': 'center', 'title_primary_color': '#12382c', 'title_accent_color': '#108474',
  'use_global_accent_typography': False, 'use_accent_gradient': False,
  'accent_text_gradient': 'linear-gradient(45deg, #EF4A65, #FF6B9D)', 'accent_font_family': 'inherit',
  'accent_font_style': 'normal', 'accent_font_weight': 'inherit', 'social_badge_type': 'none',
  'view_count': '', 'badge_text': '', 'badge_suffix': '', 'badge_background_color': '#f8f9fa',
  'badge_text_color': '#262626', 'use_gradient_text': False, 'use_gradient_border': True,
  'badge_border_width': 1, 'badge_border_color': '#000000', 'badge_border_radius': 50,
  'tiktok_gradient_color_1': '#00f2ea', 'tiktok_gradient_color_2': '#ff0050',
  'facebook_gradient_color_1': '#1877f2', 'facebook_gradient_color_2': '#4267b2',
  'instagram_gradient_color_1': '#833ab4', 'instagram_gradient_color_2': '#fd1d1d',
  'instagram_gradient_color_3': '#fcb045', 'grid_gap': 8, 'columns_mobile': '3', 'columns_desktop': '3',
  'natural_aspect_ratio': False, 'image_position': 'center center', 'show_image_caption': False,
  'border_width': 1, 'border_color': '#dddddd', 'border_radius': 0, 'use_gradient_border_photos': False,
  'padding_top': 40, 'padding_bottom': 40, 'padding_horizontal': 30, 'section_border_radius': 0,
  'section_bg_color': '#ffffff'}
}

# ============ 17. FAQ munequera (verbatim) ============
def faq(q, a, name=None):
    b = {'type': 'faq_item', 'settings': {'question': q, 'answer': a}}
    if name: b['name'] = name
    return b
S['store_faq_Lpd3PW'] = {
 'type': 'store-faq',
 'blocks': {
  'faq_item_appL6A': faq('¿Cómo se usa la muñequera?', '<p>Ajustala con el <strong>velcro</strong> en la muñeca que la necesite (sirve para <strong>derecha e izquierda</strong>, con el pulgar en su agarre), conectala por USB a un cargador, laptop, power bank o al puerto del auto, y encendela con su botón. Usala <strong>15 a 20 minutos</strong>, una o dos veces al día, y apagala y desconectala al terminar.</p>', '1'),
  'faq_item_KQndp9': faq('¿Por qué esta sí se siente y lo demás no me hizo nada?', '<p>Acá está la clave que casi nadie te explica. Una zona rígida es una zona a la que le llega <strong>poca sangre</strong>. La férula común la aprieta en frío, el hielo le cierra el paso todavía más y la bolsa de agua se enfría a los cinco minutos, justo antes de aflojar. No era tu mano: era la solución incompleta. La Muñequera MitaLabs mantiene <strong>calor parejo la sesión completa</strong>, que le abre la puerta al riego y va soltando la zona.</p>', '2'),
  'faq_item_FKAc3E': faq('¿Sirve para las dos manos?', '<p>Sí. Es <strong>talla única ajustable</strong> con velcro y agarre de pulgar: la usás en la muñeca derecha o izquierda, según el día. Un solo equipo para ambas.</p>', '3'),
  'faq_item_NxPPHM': faq('¿Necesita estar conectada mientras la uso?', '<p>Sí, y te lo decimos de frente porque otros lo esconden: funciona <strong>conectada por USB</strong> mientras la usás. Eso tiene una ventaja real: el calor es <strong>constante y parejo de principio a fin</strong>, sin batería que se vaya agotando a mitad de sesión. La enchufás a lo que ya tenés: cargador de pared, laptop, power bank (para usarla donde quieras) o el puerto USB del auto.</p>'),
  'faq_item_QMRATN': faq('¿Es segura? ¿Puedo usarla todos los días?', '<p>Sí, es un equipo de <strong>calor local de uso diario</strong> que funciona a bajo voltaje por USB. Usala despierto, en sesiones cortas de <strong>15 a 20 minutos</strong>, empezá suave para probar tu tolerancia y apagala al terminar. <em>Es un apoyo de calor (termoterapia); si tenés una lesión o condición, seguí también las indicaciones de tu médico o fisioterapeuta.</em></p>'),
  'faq_item_yAPqUQ': faq('¿Cómo son los envíos y el pago en Bolivia?', '<p>Depende de tu ciudad:</p><ul><li><strong>Santa Cruz:</strong> pago contra entrega — pagás en efectivo al recibir, con entrega en aproximadamente <strong>24 a 72 horas</strong>.</li><li><strong>La Paz, El Alto, Cochabamba y otras ciudades:</strong> pago anticipado por QR o transferencia, con envío por encomienda en <strong>3 a 6 días hábiles</strong>.</li></ul><p>En todos los casos te contactamos por WhatsApp para confirmar tu dirección y coordinar la entrega.</p>'),
  'faq_item_WbQwaa': faq('¿Y si no me convence o llega dañada?', '<p>Tu compra es <strong>sin riesgo</strong>. En <strong>Santa Cruz</strong>, como pagás contra entrega, podés revisar que tu muñequera llegue <strong>en buen estado antes de pagar</strong>. En el resto del país viaja protegida y, si llegara dañada, <strong>te la cambiamos sin problema</strong>. Además tenés <strong>30 días de garantía</strong> para probarla con calma.</p>'),
 },
 'block_order': ['faq_item_appL6A', 'faq_item_KQndp9', 'faq_item_FKAc3E', 'faq_item_NxPPHM',
  'faq_item_QMRATN', 'faq_item_yAPqUQ', 'faq_item_WbQwaa'],
 'settings': {
  'use_theme_colors': False, 'heading': 'Preguntas frecuentes', 'subtitle': '',
  'heading_color': '#12382c', 'subtitle_color': '#48584f', 'section_padding': 40,
  'container_padding_mobile': 15, 'container_padding_desktop': 15, 'section_bg_color': '#ffffff',
  'border_radius': 6, 'border_color': '#e3ece8', 'divider_color': '#e3ece8', 'border_style': 'full',
  'border_width': 1, 'question_color': '#12382c', 'question_bg_color': '#ffffff',
  'answer_color': '#48584f', 'answer_bg_color': '#ffffff', 'accordion_mode': True,
  'image_border_radius': 8, 'image_full_height': False, 'full_height_min_height': 600,
  'use_background_image': False, 'background_image_size': 'cover',
  'background_image_position': 'center center', 'background_image_attachment': 'scroll',
  'background_overlay_enable': False, 'background_overlay_color': '#0000004d',
  'background_overlay_opacity': 30, 'center_when_no_image': True, 'center_max_width': 1000,
  'two_column_desktop': True, 'column_gap': 10, 'faq_item_spacing': 6, 'individual_item_borders': True,
  'question_padding_top': 10, 'question_padding_bottom': 10, 'question_padding_left': 17,
  'question_padding_right': 14, 'answer_padding_top': 10, 'answer_padding_bottom': 15,
  'answer_padding_left': 20, 'answer_padding_right': 20, 'heading_font_size': 36,
  'heading_font_size_mobile': 36, 'heading_line_height': 1.2, 'subtitle_font_size': 16,
  'subtitle_font_size_mobile': 14, 'subtitle_line_height': 1.5, 'question_font_size': 16,
  'question_font_size_mobile': 14, 'answer_font_size': 14, 'answer_font_size_mobile': 13,
  'enable_section_top_border': False, 'section_top_border_width': 1,
  'section_top_border_style': 'solid', 'section_top_border_color': '#e5e5e5',
  'enable_section_bottom_border': False, 'section_bottom_border_width': 1,
  'section_bottom_border_style': 'solid', 'section_bottom_border_color': '#e5e5e5'}
}

ORDER = ['shop_product_details_JbqzwH', 'scrolling_features_bar_mWQii9', 'store_features_HfR3fm',
 'sticky_add_to_cart_mtlbSt', 'product_benefits_mtlbPB', 'divider_mtlbD1', 'image_with_text_mtlbIW',
 '4_images_6wqdKm', '4_cards_jDTiEi', 'divider_mtlbD2', 'before_after_mtlbBA', 'image_with_text_hmnhFF',
 'product_comparison_ahRqAP', 'divider_mtlbD3', 'satisfaction_guarantee_J4ypTy', 'photo_grid_mtlbPG',
 'store_faq_Lpd3PW']
tpl = {'sections': S, 'order': ORDER}

# ================= QC =================
errors, warns = [], []
assert set(ORDER) == set(S.keys()) and len(ORDER) == 17
raw = json.dumps(tpl, ensure_ascii=False, indent=2)
json.loads(raw)

# secciones de estructura/swap: no deben tener vocabulario del masajeador
swap_keys = ['sticky_add_to_cart_mtlbSt', 'product_benefits_mtlbPB', 'image_with_text_mtlbIW',
             'before_after_mtlbBA', 'photo_grid_mtlbPG', 'scrolling_features_bar_mWQii9',
             'divider_mtlbD1', 'divider_mtlbD2', 'divider_mtlbD3']
sw = json.dumps({k: S[k] for k in swap_keys}, ensure_ascii=False).lower()
sw_clean = re.sub(r'linear-gradient\([^"]*\)', '', sw)
for w in ['masaje', 'amasa', 'shiatsu', 'cuello', 'hombro', 'nodos', 'masajista', 'colg', 'sobador']:
    if w in sw_clean: errors.append(f'vocabulario del masajeador en secciones nuevas: {w}')
for claim in ['cura', 'curar', 'elimina', 'sana ', 'sanar', '100%', 'garantizado', 'nunca más',
              'temperatura de ', '°c', 'grados', 'niveles de']:
    if claim in sw_clean: errors.append(f'claim prohibido: {claim}')
if re.search(r'\b(389|778|179)\b', sw_clean): errors.append('precio hardcodeado')
for bad in ['MagicLab', 'minigenio', 'Charliac', 'Gs.', 'Paraguay', 'guaraní']:
    if bad in raw: errors.append(f'string prohibido: {bad}')

# sweep tipos/rangos contra schemas para secciones nueva-estructura
schemas = {'sticky-add-to-cart': 'sticky-add-to-cart.schema.json', 'product-benefits': 'product-benefits.schema.json',
           'divider': 'divider.schema.json', 'image-with-text': 'image-with-text.schema.json',
           'before-after-comparison': 'before-after-comparison.schema.json', 'photo-grid': 'photo-grid.schema.json',
           'scrolling-features-bar': 'scrolling-features-bar.schema.json'}
STR = {'text', 'textarea', 'richtext', 'html', 'liquid', 'url', 'color', 'color_background',
       'image_picker', 'video', 'font_picker', 'inline_richtext'}
def index(lst): return {x['id']: x for x in lst if 'id' in x}
for key in swap_keys:
    sec = S[key]
    sch = json.load(open(os.path.join(BASE, 'schemas', schemas[sec['type']])))
    sidx = index(sch.get('settings', []))
    bidx = {b['type']: index(b.get('settings', [])) for b in sch.get('blocks', [])}
    def chk(settings, idx, where):
        for sid, val in settings.items():
            m = idx.get(sid)
            if not m: continue
            t = m.get('type')
            if t in STR and not isinstance(val, str): errors.append(f'{where}.{sid}: debe ser string ({t})')
            if t == 'range':
                mn, mx, st = m.get('min', 0), m.get('max', 100), m.get('step', 1)
                if not isinstance(val, (int, float)) or isinstance(val, bool) or not (mn <= val <= mx) or round((val - mn) % st, 9) not in (0, st):
                    errors.append(f'{where}.{sid}: {val} fuera de range {mn}..{mx}/{st}')
            if t == 'checkbox' and not isinstance(val, bool): errors.append(f'{where}.{sid}: checkbox')
            if t == 'select':
                vals = [o['value'] for o in m.get('options', [])]
                if vals and val not in vals: errors.append(f'{where}.{sid}: {val!r} no en {vals}')
    chk(sec.get('settings', {}), sidx, key)
    for bk, bv in sec.get('blocks', {}).items():
        chk(bv.get('settings', {}), bidx.get(bv['type'], {}), f'{key}/{bk}')

# imagenes: solo refs de la munequera / compartidas confirmadas en su template actual
allowed = {'159594.webp', 'hombrera-fisio.webp', 'hombrera-icon-calor.svg', '02-pago-contra-entrega.svg',
           'hombrera-icon-sin-cables.svg', '04-registro-anvisa.svg', 'istockphoto-1483329842-612x612.webp',
           'resena-1.webp', 'resena-3.webp', 'resena-5.webp', 'munequera-mecanismo.webp',
           'munequera-roadmap.webp', 'munequera-razon-1.webp', 'munequera-card-1.webp',
           'munequera-card-2.webp', 'munequera-card-3.webp',
           'munequera-ritual-1.webp', 'munequera-ritual-2.webp', 'munequera-ritual-3.webp',
           'munequera-ritual-4.webp', 'resena-1-carmen.webp', 'resena-4-andrea.webp',
           'resena-3-gabriela.webp', 'resena-2-paola.webp', 'resena-5-rodrigo.webp'}
used = set(re.findall(r'shopify://shop_images/([^"\']+)', raw))
for u in sorted(used - allowed): errors.append(f'imagen fuera de whitelist: {u}')

out = os.path.join(BASE, 'out', '05_PRODUCT_PAGE_MUNEQUERA_ESTRUCTURA_MINIGENIO.json')
open(out, 'w', encoding='utf-8').write(raw)
open(os.path.join(BASE, 'out', 'munequera_paste.json'), 'w', encoding='utf-8').write(
    json.dumps(tpl, ensure_ascii=False, separators=(',', ': '), indent=0))
print(f'OUT: {out} ({len(raw)} bytes, {len(S)} secciones)')
print(f'ERRORES: {len(errors)}'); [print('  ✗', e) for e in errors]
print(f'WARNINGS: {len(warns)}'); [print('  ⚠', w) for w in warns]
raise SystemExit(1 if errors else 0)
