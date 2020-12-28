import os, sys, getopt
import codecs


def volcado_csv(lst_view):
    with open("url_invitaciones.csv", "w") as outfile:
        for entries in lst_view:
            outfile.write(entries)
            outfile.write("\n")


def LaTeX(lst):
    latex = codecs.open('InvitacionesLatex.tex', "w", "utf-8")
    latex.write("\\documentclass[border=0.2cm,varwidth, 12pt, multi=my,crop]{standalone}")
    latex.write("\\usepackage[utf8]{inputenc}")
    latex.write("\\usepackage{graphicx}")
    latex.write("\\usepackage{booktabs}")
    latex.write("\\usepackage{siunitx}")
    latex.write("\\usepackage{multirow}")
    latex.write("\\usepackage{hyperref}")
    latex.write("\\usepackage{luaimageembed}")
    
    latex.write("\\usepackage{url}")
    latex.write("\\usepackage[dvipsnames]{xcolor}")
    latex.write("\\definecolor{UCM_color}{HTML}{990033}")
    latex.write("\\begin{document}")
    for i in lst:
        latex.write("\\begin{my}")
        latex.write("\\centering")
        latex.write("\\textbf{Enlace: }\\textcolor{UCM_color}{\\url{" + str(i) + "}}\\\\")
        latex.write("\\vspace{0.25cm}")
        latex.write(
            "Pulsar \\textbf{``Share your camera''}, configurar al gusto y pulsar \\textcolor{ForestGreen}{\\textbf{``START''}}\\\\")
        latex.write("\\centering")
        latex.write("\\includegraphicsembedded[width=4cm]{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}")

        latex.write("\\end{my}")
    latex.write("\\end{document}")
    latex.close()
  

def OBS_generator(lst, lst_of_lst):
    with open('OBStudio_carrusel_complutense.json', 'w') as f:
        inicial = lst_of_lst[0]
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
                        '"volume": 0.38048261404037476 }, "current_program_scene": "C_' + str(
            len(inicial)) + '_Complutense_1", '
                            '"current_scene": "C_' + str(
            len(inicial)) + '_Complutense_1", "current_transition": "Desvanecimiento", "groups": [], '
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
        number = int(0)
        for i in lst_of_lst:
            f.write('{  "name": "C_' + str(len(i)) + '_Complutense_' + str(number) + '')
            number += 1
            if i != lst_of_lst[len(lst_of_lst) - 1]:
                f.write('" },\n')
            else:
                f.write('" } ], \n"sources": [')
        #########
        number = int(0)
        for i in lst_of_lst:
            cabecera_cam = ['\n{ "balance": 0.5, "deinterlace_field_order": 0, "deinterlace_mode": 0, "enabled": true, '
                            '"flags": 0, "hotkeys": {}, "id": "image_source", "mixers": 0, "monitoring_type": 0, '
                            '"muted": false, "name": "C_' + str(
                len(i)) + '_OVERLAY", "prev_ver": 436207618, "private_settings": {}, '
                          '"push-to-mute": false, "push-to-mute-delay": 0, "push-to-talk": false, '
                          '"push-to-talk-delay": 0, '
                          '"settings": { "file": "E:/OTEA - Clases y Talleres/Carrusel Complutense/C' + str(
                len(i)) + '.png" }, '
                          '"sync": 0, "versioned_id": "image_source", "volume": 1.0 }, { "balance": 0.5, "deinterlace_field_order": 0,'
                          '"deinterlace_mode": 0, "enabled": true, "flags": 0, "hotkeys": { "OBSBasic.SelectScene": [],']
            f.writelines(cabecera_cam)
            f.write('"libobs.hide_scene_item.C_' + str(len(i)) + '_OVERLAY": [],')
            for j in i:
                spliteado = j.split("=")
                f.write('"libobs.hide_scene_item.WEBCAM_' + str(spliteado[1]) + '": [],')
            f.write('"libobs.show_scene_item.C_' + str(len(i)) + '_OVERLAY": [],')
            for j in i:
                spliteado = j.split("=")
                f.write('"libobs.show_scene_item.WEBCAM_' + str(spliteado[1]) + '": []')
                if j != i[len(i) - 1]:
                    f.write(', ')
            ##########
            f.write("},")

            f.write('"id": "scene", "mixers": 0, "monitoring_type": 0, "muted": false, "name": "C_' + str(
                len(i)) + '_Complutense_' + str(number) + '", '
                                                          '"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, "push-to-mute-delay": 0, '
                                                          '"push-to-talk": false, "push-to-talk-delay": 0, "settings": ')
            number += 1
            if len(i) == 1:
                for j in i:
                    spliteado = j.split("=")
                    f.write('{ "custom_size": false, "id_counter": 2, "items": [ { "align": 5, "bounds":'
                            ' { "x": 1432.0, "y": 1620.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, '
                            '"crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 2, '
                            '"locked": true, "name": "WEBCAM_' + str(spliteado[1]) + '", "pos": { "x": 1504.0, "y": 271.0 }, '
                                        '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                        '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                        '"bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, "bounds_type": 0, '
                                        '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                        ' "id": 1, "locked": true, "name": "C_1_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, '
                                        '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": '
                                        '"disable", "visible": true } ] }, "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 2:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "align": 5, "bounds": { "x": 1333.0, "y": 1461.0 }, "bounds_align": 0, "bounds_type": 1,'
                        ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                        '"group_item_backup": false, "id": 2, "locked": true, "name": '
                        '"WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 1498.0, "y": 879.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 1378.0, "y": 1481.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 3, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", '
                                      '"pos": { "x": 1471.0, "y": -183.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, "bounds_type": 0, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 1, "locked": true, "name": "C_2_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true } ] }, "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 3:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 4, "items": [ { "align": 5, '
                        '"bounds": { "x": 985.0, "y": 1097.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0,'
                        ' "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 2, '
                        '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 2522.0, "y": 1215.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 1031.0, "y": 1109.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 3,'
                                      ' "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", "pos": { "x": 1491.0, "y": 512.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 1004.0, "y": 1132.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                      '"crop_top": 0, "group_item_backup": false, "id": 4, "locked": true, '
                                      '"name": "WEBCAM_' + str(
                    lst_listado[2]) + '", "pos": { "x": 487.0, "y": -182.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, "bounds_type": 0, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 1, "locked": true, '
                                      '"name": "C_3_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true } ] }, '
                                      '"sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 4:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 5, "items": [ { "align": 5, '
                        '"bounds": { "x": 1065.0, "y": 1175.0 }, "bounds_align": 0, "bounds_type": 1, '
                        '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                        '"group_item_backup": false, "id": 2, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '", '
                                      '"pos": { "x": 2422.0, "y": -114.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 1059.0, "y": 1173.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 3, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '", '
                                      '"pos": { "x": 2408.0, "y": 1092.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 1054.0, "y": 1192.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                      '"crop_top": 0, "group_item_backup": false, "id": 4, "locked": true, "name": '
                                      '"WEBCAM_' + str(
                    lst_listado[0]) + '", "pos": { "x": 1209.0, "y": 1093.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 1083.0, "y": 1182.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 5, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '", '
                                      '"pos": { "x": 1200.0, "y": -116.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, "bounds_type": 0, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 1, "locked": true, "name": "C_4_OVERLAY", '
                                      '"pos": { "x": 0.0, "y": 0.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true } ] },'
                                      ' "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 5:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 6, "items": [ { "align": 5, '
                        '"bounds": { "x": 971.0, "y": 1070.0 }, "bounds_align": 0, "bounds_type": 1, '
                        '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                        ' "id": 2, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '", "pos": { "x": 1509.0, "y": 548.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", '
                                      '"visible": true }, { "align": 5, "bounds": { "x": 976.0, "y": 1099.0 }, "bounds_align": 0,'
                                      ' "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 3, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '", '
                                      '"pos": { "x": 533.0, "y": 1205.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 971.0, "y": 1073.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 4, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 533.0, "y": -145.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 966.0, "y": 1067.0 }, "bounds_align": 0,'
                                      ' "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 5, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", '
                                      '"pos": { "x": 2492.0, "y": -131.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 964.0, "y": 1088.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 6, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[4]) + '", '
                                      '"pos": { "x": 2490.0, "y": 1195.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 0.0, "y": 0.0 },'
                                      ' "bounds_align": 0, "bounds_type": 0, "crop_bottom": 0, "crop_left": 0,'
                                      ' "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 1, '
                                      '"locked": true, "name": "C_5_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true } ] },')

            if len(i) == 6:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado)
                f.write('{ "custom_size": false, "id_counter": 15, "items": [ { "align": 5, '
                        '"bounds": { "x": 910.0, "y": 1059.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, '
                        '"crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, '
                        '"id": 2, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[5]) + '", "pos": { "x": 439.0, "y": -158.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 1027.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 3, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[4]) + '", "pos": { "x": 438.0, "y": 1252.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                      ' "scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 1038.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 4, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '", "pos": { "x": 2322.0, "y": 857.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 910.0, "y": 1034.0 }, "bounds_align": 0, "bounds_type": 1, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 5, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '", '
                                      '"pos": { "x": 1379.0, "y": 859.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 910.0, "y": 1011.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 6, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 2322.0, "y": 162.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 910.0, "y": 1044.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                      '"crop_top": 0, "group_item_backup": false, "id": 7, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", "pos": { "x": 1390.0, "y": 136.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, "bounds_type": 0, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 9, "locked": true, "name": "C_6_OVERLAY", '
                                      '"pos": { "x": 0.0, "y": 0.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true } ] }, '
                                      '"sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 7:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write(
                    '{ "custom_size": false, "id_counter": 9, "items": [ { "align": 5, "bounds": { "x": 927.0, "y": 1013.0 },'
                    ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                    '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 2, "locked": true, '
                    '"name": "WEBCAM_' + str(
                        lst_listado[6]) + '", "pos": { "x": 99.0, "y": -116.0 }, "private_settings": {}, '
                                          '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                          ' { "align": 5, "bounds": { "x": 910.0, "y": 1003.0 }, "bounds_align": 0, '
                                          '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                          '"group_item_backup": false, "id": 3, "locked": true, "name": "WEBCAM_' + str(
                        lst_listado[5]) + '", "pos": { "x": 1962.0, "y": 1157.0 },'
                                          ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                          '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 1001.0 },'
                                          ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                          '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 4, '
                                          '"locked": true, "name": "WEBCAM_' + str(
                        lst_listado[4]) + '", "pos": { "x": 1024.0, "y": 1159.0 },'
                                          ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                          '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                          '"bounds": { "x": 910.0, "y": 1000.0 }, "bounds_align": 0,'
                                          ' "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                          ' "group_item_backup": false, "id": 5, "locked": true, "name": "WEBCAM_' + str(
                        lst_listado[3]) + '",'
                                          ' "pos": { "x": 89.0, "y": 1241.0 }, "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                          ' "scale_filter": "disable", "visible": true }, { "align": 5, '
                                          '"bounds": { "x": 910.0, "y": 992.0 }, "bounds_align": 0, "bounds_type": 1,'
                                          ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                          '"group_item_backup": false, "id": 6, "locked": true, "name": "WEBCAM_' + str(
                        lst_listado[3]) + '", '
                                          '"pos": { "x": 2872.0, "y": 596.0 }, "private_settings": {}, "rot": 0.0, '
                                          '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                          ' { "align": 5, "bounds": { "x": 910.0, "y": 994.0 }, "bounds_align": 0,'
                                          ' "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                          '"crop_top": 0, "group_item_backup": false, "id": 7, "locked": true, '
                                          '"name": "WEBCAM_' + str(
                        lst_listado[1]) + '", "pos": { "x": 1962.0, "y": -24.0 }, '
                                          '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                          ' "scale_filter": "disable", "visible": true }, '
                                          '{ "align": 5, "bounds": { "x": 910.0, "y": 1012.0 }, "bounds_align": 0, '
                                          '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                          ' "group_item_backup": false, "id": 8, "locked": true, "name": "WEBCAM_' + str(
                        lst_listado[0]) + '", '
                                          '"pos": { "x": 1026.0, "y": -42.0 }, "private_settings": {}, "rot": 0.0, '
                                          '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                          ' { "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, '
                                          '"bounds_type": 0, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                          '"crop_top": 0, "group_item_backup": false, "id": 1, "locked": true, '
                                          '"name": "C_7_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, "private_settings": {}, '
                                          '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true } ] },'
                                          ' "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 8:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 9, "items": [ { "align": 5, '
                        '"bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0,'
                        ' "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 2, '
                        '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[6]) + '", "pos": { "x": 116.0, "y": -88.0 }, "private_settings": {},'
                                      ' "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, '
                                      '"id": 3, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[5]) + '", "pos": { "x": 2366.0, "y": 1258.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 970.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                                      ' "crop_top": 0, "group_item_backup": false, "id": 4, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[4]) + '",'
                                      ' "pos": { "x": 1042.0, "y": 1259.0 }, "private_settings": {}, "rot": 0.0,'
                                      ' "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 5, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '", "pos": { "x": 2837.0, "y": 590.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 970.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                                      ' "crop_top": 0, "group_item_backup": false, "id": 6, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '",'
                                      ' "pos": { "x": 1894.0, "y": 586.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 910.0, "y": 983.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 7, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '",'
                                      ' "pos": { "x": 132.0, "y": 1254.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 8, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", '
                                      '"pos": { "x": 2348.0, "y": -92.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 9, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[7]) + '", '
                                      '"pos": { "x": 1026.0, "y": -84.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, "bounds_align": 0, '
                                      '"bounds_type": 0, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                      '"crop_top": 0, "group_item_backup": false, "id": 1, "locked": true, '
                                      '"name": "C_8_OVERLAY", "pos": { "x": 0.0, "y": 0.0 }, "private_settings": {},'
                                      ' "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", '
                                      '"visible": true } ] }, "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 9:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 10, "items": [ { "align": 5, '
                        '"bounds": { "x": 910.0, "y": 1001.0 }, "bounds_align": 0, "bounds_type": 1, '
                        '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                        '"group_item_backup": false, "id": 10, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[8]) + '",'
                                      ' "pos": { "x": 2869.0, "y": 1229.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 2, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[7]) + '", "pos": { "x": 1910.0, "y": 1247.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, '
                                      '"bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                                      ' "crop_top": 0, "group_item_backup": false, "id": 3, "locked": true, '
                                      '"name": "WEBCAM_' + str(
                    lst_listado[6]) + '", "pos": { "x": 1000.0, "y": 1246.0 }, "private_settings": {},'
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", '
                                      '"visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, '
                                      '"bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0,'
                                      ' "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 4, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[5]) + '", "pos": { "x": 90.0, "y": 1243.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 910.0,'
                                      ' "y": 970.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0,'
                                      ' "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 5, "locked": true,'
                                      ' "name": "WEBCAM_' + str(
                    lst_listado[4]) + '", "pos": { "x": 1459.0, "y": 584.0 }, "private_settings": {},'
                                      ' "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 6, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '", "pos": { "x": 2846.0, "y": -101.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 910.0, "y": 970.0 }, '
                                      '"bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0,'
                                      ' "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 7, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '", "pos": { "x": 1936.0, "y": -93.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { '
                                      '"x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 8, "locked": true, '
                                      '"name": "WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 1026.0, "y": -88.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                      ' "scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 9, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '",'
                                      ' "pos": { "x": 116.0, "y": -88.0 }, "private_settings": {},'
                                      ' "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 0.0, "y": 0.0 }, '
                                      '"bounds_align": 0, "bounds_type": 0, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 1,'
                                      ' "locked": true, "name": "C_9_OVERLAY", "pos": { "x": 0.0, "y": 0.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                      ' "scale_filter": "disable", "visible": true } ] }, "sync": 0, '
                                      '"versioned_id": "scene", "volume": 1.0 },')

            if len(i) == 10:
                lst_listado = list()
                for j in i:
                    spliteado = j.split("=")
                    lst_listado.append(spliteado[1])
                f.write('{ "custom_size": false, "id_counter": 11, "items": [ { "align": 5, "bounds": '
                        '{ "x": 851.0, "y": 972.0 }, "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0,'
                        ' "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 11,'
                        ' "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[9]) + '", "pos": { "x": 2844.0, "y": 1254.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": '
                                      '"disable", "visible": true }, { "align": 5, "bounds": { "x": 850.0, "y": 981.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0,'
                                      ' "crop_top": 0, "group_item_backup": false, "id": 10, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[8]) + '",'
                                      ' "pos": { "x": 1948.0, "y": 1252.0 }, "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                      ' "scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 846.0, "y": 976.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 9, "locked": true,'
                                      ' "name": "WEBCAM_' + str(
                    lst_listado[7]) + '", "pos": { "x": 1053.0, "y": 1250.0 }, "private_settings": {}, '
                                      '"rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 855.0, "y": 974.0 }, "bounds_align": 0, "bounds_type": 1,'
                                      ' "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 8, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[6]) + '", "pos": { "x": 149.0, "y": 1254.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable",'
                                      ' "visible": true }, { "align": 5, "bounds": { "x": 854.0, "y": 976.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 7, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[5]) + '", '
                                      '"pos": { "x": 1947.0, "y": 581.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 848.0, "y": 980.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0,'
                                      ' "group_item_backup": false, "id": 6, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[4]) + '",'
                                      ' "pos": { "x": 1051.0, "y": 581.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true }, '
                                      '{ "align": 5, "bounds": { "x": 918.0, "y": 978.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, '
                                      '"group_item_backup": false, "id": 5, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[3]) + '",'
                                      ' "pos": { "x": 2844.0, "y": -90.0 }, "private_settings": {}, "rot": 0.0, '
                                      '"scale": { "x": 1.0, "y": 1.0 }, "scale_filter": "disable", "visible": true },'
                                      ' { "align": 5, "bounds": { "x": 864.0, "y": 980.0 }, "bounds_align": 0, "bounds_type": 1, '
                                      '"crop_bottom": 0, "crop_left": 0, "crop_right": 0, "crop_top": 0, "group_item_backup": false,'
                                      ' "id": 4, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[2]) + '", "pos": { "x": 1950.0, "y": -90.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, "bounds": { "x": 849.0, "y": 978.0 },'
                                      ' "bounds_align": 0, "bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, "id": 3, '
                                      '"locked": true, "name": "WEBCAM_' + str(
                    lst_listado[1]) + '", "pos": { "x": 1050.0, "y": -92.0 }, '
                                      '"private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 910.0, "y": 970.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, '
                                      '"crop_right": 0, "crop_top": 0, "group_item_backup": false, '
                                      '"id": 2, "locked": true, "name": "WEBCAM_' + str(
                    lst_listado[0]) + '", "pos": { "x": 116.0, "y": -88.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 }, '
                                      '"scale_filter": "disable", "visible": true }, { "align": 5, '
                                      '"bounds": { "x": 3874.0, "y": 2160.0 }, "bounds_align": 0, '
                                      '"bounds_type": 1, "crop_bottom": 0, "crop_left": 0, "crop_right": 0, '
                                      '"crop_top": 0, "group_item_backup": false, "id": 1, '
                                      '"locked": true, "name": "C_10_OVERLAY", "pos": { "x": -28.0, "y": 0.0 },'
                                      ' "private_settings": {}, "rot": 0.0, "scale": { "x": 1.0, "y": 1.0 },'
                                      ' "scale_filter": "disable", "visible": true } ] }, "sync": 0, "versioned_id": "scene", "volume": 1.0 },')

        for i in lst_of_lst:
            for j in i:
                spliteado = j.split("=")
                f.write('{ "balance": 0.5, "deinterlace_field_order": 0, "deinterlace_mode": 0,'
                        ' "enabled": true, "flags": 0, "hotkeys": { "libobs.mute": [], "libobs.push-to-mute": [],'
                        ' "libobs.push-to-talk": [], "libobs.unmute": [] }, "id": "browser_source", '
                        '"mixers": 255, "monitoring_type": 0, "muted": false, "name": "WEBCAM_' + str(
                    spliteado[1]) + '", '
                                    '"prev_ver": 436207618, "private_settings": {}, "push-to-mute": false, '
                                    '"push-to-mute-delay": 0, "push-to-talk": false, "push-to-talk-delay": 0, '
                                    '"settings": { "height": 800, "url": "' + str(j) + '", "width": 900 },'
                                                                                       ' "sync": 0, "versioned_id": "browser_source", "volume": 1.0 ')
                if j == i[len(i) - 1] and i == lst_of_lst[len(lst_of_lst) - 1]:
                    f.write('}')
                else:
                    f.write('},')
        f.write('], "transition_duration": 300, "transitions": [ { "id": "obs_stinger_transition", '
                '"name": "Stinger", "settings": { "audio_fade_style": 0, '
                '"path": "E:/OTEA - Clases y Talleres/Material General/FINAL RENDER.mov", '
                '"tp_type": 1, "transition_point": 30 } } ] }')


def uno(f, ):
    f.write('')




def balance(argv):
    if int(argv) > 10:
        lst_elem = list()
        lst_ceros = list()
        final = list()
        for i in range(2, 11):
            modl = int(argv % i)
            divs = int(argv / i)
            lst_a = [i, modl, divs]
            lst_elem.append(lst_a)
            if modl == 0 and int(i) > 6:
                lst_ceros.append([0, i, divs])
        if len(lst_ceros) == 0:
            amont_lst = list()
            op_abs = argv
            lst_b = list()
            for i in lst_elem:
                amont_lst = i
                aux = abs(amont_lst[1] - amont_lst[2])
                if int(aux) < int(op_abs) and aux != 0:
                    op_abs = aux
                    final = i
            final = [final[1], final[0], final[2]]
        else:
            final = min(lst_ceros)
    else:
        final = [argv, argv, 0]
    return final


def division(valores, lst):
    repeticiones = valores[2]
    canva_principal = valores[1]
    canva_secundario = valores[0]
    contador_repeticiones = 0
    contador_total = 0
    lst_of_lst = list()
    lst_canva_auxiliar = list()
    lst_aux = list()
    for i in lst:
        if contador_total < int(canva_principal * repeticiones):
            if contador_repeticiones == canva_principal:
                contador_repeticiones = 0
                lst_of_lst.append(lst_aux)
                lst_aux = list()
            contador_repeticiones += 1
            lst_aux.append(i)
            contador_total += 1
        else:
            lst_canva_auxiliar.append(i)
    if len(lst_canva_auxiliar) != 0:
        lst_of_lst.append(lst_canva_auxiliar)

    return (lst_of_lst)

#main

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
    print("Enlaces generados...")
    argv = int(argv)
    valores = balance(argv)
    print("Valores generados...")
    lst_of_lst = division(valores, lst_view)
    print("Canvas seleccionados...")
    OBS_generator(lst_view, lst_of_lst)
    print("overlays generados...")
    LaTeX(lst)
    volcado_csv(lst_view)
    print("Proceso finalizado, datos completos...")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print(
            "Error de argumetos, se necesita un único entero (int) seguido de la posición de comienzo (int) \nEjemplo: ./script 5 0")
