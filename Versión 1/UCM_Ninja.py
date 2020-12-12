import os, sys, getopt
import codecs


def volcado_csv(lst_view):
    with open("vistas_csv.csv", "w") as outfile:
        for entries in lst_view:
            outfile.write(entries)
            outfile.write("\n")

def LaTeX(lst):
    for i in lst:
        name_str = str(i).split('UCM')
        latex = codecs.open(str(name_str[1]) + '.tex', "w", "utf-8")
        latex.write("\\documentclass[border=0.2cm,varwidth, 12pt]{standalone}")
        latex.write("\\usepackage[utf8]{inputenc}")
        latex.write("\\usepackage{graphicx}")
        latex.write("\\usepackage{booktabs}")
        latex.write("\\usepackage{siunitx}")
        latex.write("\\usepackage{multirow}")
        latex.write("\\usepackage{hyperref}")
        latex.write("\\usepackage{url}")
        latex.write("\\usepackage[dvipsnames]{xcolor}")
        latex.write("\\definecolor{UCM_color}{HTML}{990033}")
        latex.write("\\begin{document}")
        latex.write("\\centering")
        latex.write("\\textbf{Enlace: }\\textcolor{UCM_color}{\\url{" + str(i) + "}}\\\\")
        latex.write("\\vspace{0.25cm}")
        latex.write("Pulsar \\textbf{``Share your camera''}, configurar al gusto y pulsar \\textcolor{ForestGreen}{\\textbf{``START''}}\\\\")
        latex.write("\\centering")
        latex.write("\\includegraphics[width=5cm]{1.jpg}")
        latex.write("\\end{document}")
        latex.close()
        compiler = str(name_str[1]) + '.tex'
        os.system("pdflatex " + compiler)
        os.remove(str(name_str[1]) + '.tex')
        os.remove(str(name_str[1]) + '.aux')
        os.remove(str(name_str[1]) + '.log')
        os.remove(str(name_str[1]) + '.out')

def OBS_generator(lst):
    with open('carrusel_complutense.json', 'w') as f:
        web_browsers = ['{ "AuxAudioDevice1": { "balance": 0.5, "deinterlace_field_order": 0, "deinterlace_mode": 0, '
                        '"enabled": true, "filters": [ { "balance": 0.5, "deinterlace_field_order": 0, '
                        '"deinterlace_mode": 0, "enabled": true, "flags": 0, "hotkeys": {}, "id": "noise_gate_filter", '
                        '"mixers": 255, "monitoring_type": 0, "muted": false, "name": "Puerta anti-ruidos", '
                        '"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, "push-to-mute-delay": 0, '
                        '"push-to-talk": false, "push-to-talk-delay": 0, "settings": { "attack_time": 15, '
                        '"close_threshold": -60.0, "open_threshold": -42.0, "release_time": 100 }, "sync": 0, '
                        '"versioned_id": "noise_gate_filter", "volume": 1.0 }, { "balance": 0.5, '
                        '"deinterlace_field_order": 0, "deinterlace_mode": 0, "enabled": true, "flags": 0, '
                        '"hotkeys": {}, "id": "compressor_filter", "mixers": 255, "monitoring_type": 0, "muted": false, '
                        '"name": "Compresor", "prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, '
                        '"push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, "settings": { '
                        '"attack_time": 1, "output_gain": 9.0, "ratio": 3.0, "release_time": 50, "threshold": -20.0}, '
                        '"sync": 0, "versioned_id": "compressor_filter", "volume": 1.0 } ], "flags": 0, "hotkeys": { '
                        ' "libobs.mute": [], "libobs.push-to-mute": [], "libobs.push-to-talk": [], "libobs.unmute": [] '
                        '}, "id": "wasapi_input_capture", "mixers": 255, "monitoring_type": 0, "muted": true, '
                        '"name": "Mic/Aux", "prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, '
                        '"push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, "settings": { '
                        '"device_id": "{0.0.1.00000000}.{8d4e9a7b-02f1-4174-a018-614de348b4b6}" }, "sync": 0, '
                        '"versioned_id": "wasapi_input_capture", "volume": 0.51179677248001099 }, '
                        '"DesktopAudioDevice2": { "balance": 0.5, "deinterlace_field_order": 0,  "deinterlace_mode": 0, '
                        '"enabled": true, "filters": [ { "balance": 0.5, "deinterlace_field_order": 0, '
                        '"deinterlace_mode": 0,  "enabled": true, "flags": 0, "hotkeys": {}, "id": "noise_gate_filter", '
                        '"mixers": 255, "monitoring_type": 0, "muted": false, "name": "Puerta anti-ruidos", '
                        '"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, "push-to-mute-delay": 0, '
                        '"push-to-talk": false, "push-to-talk-delay": 0, "settings": { "attack_time": 15, '
                        '"close_threshold": -60.0, "open_threshold": -42.0, "release_time": 100 }, "sync": 0, '
                        '"versioned_id": "noise_gate_filter", "volume": 1.0 }, { "balance": 0.5, '
                        '"deinterlace_field_order": 0, "deinterlace_mode": 0, "enabled": true, "flags": 0, "hotkeys": {},  '
                        '"id": "compressor_filter", "mixers": 255, "monitoring_type": 0, "muted": false, '
                        '"name": "Compresor", "prev_ver": 436207618, "private_settings": {}, "push-to-mute": false,'
                        '"push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, "settings": { '
                        '"attack_time": 1, "output_gain": 9.0, "ratio": 3.0, "release_time": 50, "threshold": -20.0}, '
                        '"sync": 0, "versioned_id": "compressor_filter", "volume": 1.0 } ], "flags": 0, "hotkeys": { '
                        '"libobs.mute": [], "libobs.push-to-mute": [], "libobs.push-to-talk": [], "libobs.unmute": []}, '
                        '"id": "wasapi_output_capture", "mixers": 255, "monitoring_type": 0, "muted": true, "name": '
                        '"Audio del escritorio 2", "prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, '
                        '"push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, "settings": { '
                        '"device_id": "default" }, "sync": 0, "versioned_id": "wasapi_output_capture", '
                        '"volume": 0.38048261404037476 }, "current_program_scene": "C_9_Complutense_0", '
                        '"current_scene": "C_9_Complutense_0", "current_transition": "Desvanecimiento", "groups": [], '
                        '"modules": { "auto-scene-switcher": { "active": false, "interval": 300, "non_matching_scene": "",'
                        ' "switch_if_not_matching": false, "switches": [] }, "captions": {"enabled": false, "lang_id": 3082, '
                        '"provider": "mssapi", "source": "" }, "output-timer": { "autoStartRecordTimer": false, '
                        '"autoStartStreamTimer": false, "pauseRecordTimer": true, "recordTimerHours": 0, '
                        '"recordTimerMinutes": 0, "recordTimerSeconds": 30, "streamTimerHours": 0, "streamTimerMinutes": 0, '
                        '"streamTimerSeconds": 30 }, "scripts-tool": [] }, "name": "Sin Título", "preview_locked": false, '
                        '"quick_transitions": [ { "duration": 300, "fade_to_black": false, "hotkeys": [], "id": 1, '
                        '"name": "Corte" }, { "duration": 300, "fade_to_black": false, "hotkeys": [], "id": 2, '
                        '"name": "Desvanecimiento" },{ "duration": 300, "fade_to_black": true, "hotkeys": [], "id": 3, '
                        '"name": "Desvanecimiento" }, { "duration": 500, "fade_to_black": false, "hotkeys": [], "id": 4, '
                        '"name": "Stinger" } ], "saved_projectors": [], "scaling_enabled": false, "scaling_level": 0, '
                        '"scaling_off_x": 0.0, "scaling_off_y": 0.0,'
                        ]
        f.writelines(web_browsers)
        f.write('\n\n  "scene_order": [ ')
        for i in range(0, 10):
            f.write('{  "name": "C_9_Complutense_' + str(i))
            if i != 9:
                f.write('" },\n')
            else:
                f.write('" }\n')
        f.write('  ],\n "sources": [ ')
        cabecera_cam = ['\n{"balance": 0.5,"deinterlace_field_order": 0,"deinterlace_mode": 0,"enabled": true,'
                        '"flags": 0,"hotkeys": { "libobs.mute": [], "libobs.push-to-mute": [], "libobs.push-to-talk": [], '
                        '"libobs.unmute": [] }, "id": "browser_source", "mixers": 255, "monitoring_type": 0, '
                        '"muted": false,'
                        ]
        medio_cam = ['\n"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, "push-to-mute-delay": 0,'
                     '"push-to-talk": false, "push-to-talk-delay": 0, "settings": {"height": 800,'
                     ]
        fin_cam = ['\n"width": 900 }, "sync": 0, "versioned_id": "browser_source", "volume": 1.0 },'
                   ]
        number = int(0)

        for i in lst:
            f.writelines(cabecera_cam)
            f.write(' "name": "WEBCAM_' + str(number) + '", ')
            f.writelines(medio_cam)
            f.write('"url": "' + str(i) + '",')
            f.writelines(fin_cam)
            number += int(1)

        overlay_sin_loc = [' { "balance": 0.5, "deinterlace_field_order": 0, "deinterlace_mode": 0, "enabled": true, '
                           '"flags": 0, "hotkeys": {}, "id": "image_source", "mixers": 0, "monitoring_type": 0, '
                           '"muted": false, "name": "C_9_OVERLAY", "prev_ver": 436207618, "private_settings": {}, '
                           '"push-to-mute": false, "push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, '
                           '"settings": { "file": "~/C9.png" }, "sync": 0, "versioned_id": "image_source", "volume": 1.0 },'
                           ]
        f.writelines(overlay_sin_loc)

        cabecera_escenatica = ['\n   {"balance": 0.5, "deinterlace_field_order": 0,  "deinterlace_mode": 0, "enabled": '
                               'true, "flags": 0, "hotkeys": { "OBSBasic.SelectScene": [], \n"libobs.hide_scene_item.C_9_OVERLAY": [],'
                               ]

        number = int(0)
        f.writelines(cabecera_escenatica)
        for i in lst:
            f.write('\n "libobs.hide_scene_item.WEBCAM_'+ str(number) +'": [],')
            number += int(1)
        f.write('\n"libobs.show_scene_item.C_9_OVERLAY": [],')
        number = int(0)
        for i in lst:
            f.write('\n "libobs.show_scene_item.WEBCAM_' + str(number) + '": []')
            if number != int(len(lst) - 1):
                f.write(' ,')
            else:
                f.write(' },')
            number += int(1)
        medio_escenatica = [' "id": "scene","mixers": 0,"monitoring_type": 0,"muted": false,']
        f.writelines(medio_escenatica)
        f.write('"name": "C_9_Complutense_0",')

        escenas_finales = ['"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, "push-to-mute-delay": 0, '
                           '"push-to-talk": false, "push-to-talk-delay": 0, "settings": { "custom_size": false, '
                           '"id_counter": 11, "items": [ { "align": 5, "bounds": { "x": 851.0, "y": 972.0 }, "bounds_align": 0, '
                           '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 11, "locked": true, "name": "WEBCAM_9",  "pos": { '
                           '"x": 2844.0, "y": 1254.0 }, "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                           '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 850.0, "y": 981.0 }, '
                           '"bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 10, "locked": true, "name": "WEBCAM_8", "pos": { "x": 1948.0, '
                           '"y": 1252.0 }, "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                           '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 846.0, "y": 976.0 }, '
                           '"bounds_align": 0, "bounds_type": 1,  "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 9, "locked": true, "name": "WEBCAM_7", "pos": { "x": 1053.0, '
                           '"y": 1250.0 }, "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", '
                           '"visible": true }, { "align": 5, "bounds": { "x": 855.0, "y": 974.0 }, "bounds_align": 0, '
                           '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 8, "locked": true, "name": "WEBCAM_6", "pos": { "x": 149.0, "y": 1254.0 },'
                           ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                           '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 854.0, "y": 976.0 },'
                           ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                           ' "group_item_backup": false, "id": 7, "locked": true, "name": "WEBCAM_5",'
                           ' "pos": { "x": 1947.0, "y": 581.0 }, "private_settings": {}, "rot": 0.0, '
                           '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                           '{ "align": 5, "bounds": { "x": 848.0, "y": 980.0 }, "bounds_align": 0,'
                           '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                           ' "crop_top": 0, "group_item_backup": false, "id": 6, "locked": true, '
                           '"name": "WEBCAM_4", "pos": { "x": 1051.0, "y": 581.0 }, "private_settings": {},'
                           ' "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                           ' { "align": 5, "bounds": { "x": 849.0, "y": 978.0 }, "bounds_align": 0,'
                           ' "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                           '"crop_top": 0, "group_item_backup": false, "id": 5, "locked": true, '
                           '"name": "WEBCAM_3", "pos": { "x": 2844.0, "y": -90.0 }, '
                           '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                           ' "scale_filter": "disable", "visible": true }, { "align": 5, '
                           '"bounds": { "x": 848.0, "y": 980.0 }, '
                           '"bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                           ' "crop_top": 0, "group_item_backup": false, "id": 4, "locked": true, '
                           '"name": "WEBCAM_2", "pos": { "x": 1950.0, "y": -90.0 }, "private_settings": {}, "rot": 0.0,'
                           ' "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                           ' { "align": 5, "bounds": { "x": 849.0, "y": 978.0 }, "bounds_align": 0, '
                           '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 3, "locked": true, "name": "WEBCAM_1", '
                           '"pos": { "x": 1050.0, "y": -92.0 }, "private_settings": {}, '
                           '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                           ' { "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, '
                           '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                           '"group_item_backup": false, "id": 2, "locked": true, "name": "WEBCAM_0", '
                           '"pos": { "x": 116.0, "y": -88.0 }, "private_settings": {}, "rot": 0.0, '
                           '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                           ' { "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, '
                           '"bounds_type": 0, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                           '"crop_top": 0, "group_item_backup": false, "id": 1, '
                           '"locked": true, "name": "C_9_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, '
                           '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                           '"scale_filter": "disable", "visible": true } ] }, '
                           '"sync": 0, "versioned_id": "scene", "volume": 1.0 }], "transition_duration": 300,'
                           '"transitions": []}'
                           ]
        f.writelines(escenas_finales)

def main(argv, argv_d):
    url = 'https://obs.ninja/?push=UCM'
    url_view = 'https://obs.ninja/?view=UCM'
    hex_ucm_code = hex(0X00000c22)  # 3106 direcciones reservadas
    hex_ucm_code = hex(int(hex_ucm_code, 16) + int(argv_d))
    lst = list()
    lst_view = list()
    for i in range(0, int(argv)):
        hex_ucm_code = hex(int(hex_ucm_code, 16) + 1)
        lst.append(url + str(hex_ucm_code))
        lst_view.append(url_view + str(hex_ucm_code))
    OBS_generator(lst_view)
    LaTeX(lst)
    volcado_csv(lst_view)
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Error de argumetos, se necesita un único entero (int) seguido de la posición de comienzo (int) \nEjemplo: ./script 5 0")

