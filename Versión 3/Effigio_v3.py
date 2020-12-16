import os, sys, getopt
import codecs
from PyPDF2 import PdfFileWriter, PdfFileReader


def volcado_csv(lst_view):
    with open("vistas_csv.csv", "w") as outfile:
        for entries in lst_view:
            outfile.write(entries)
            outfile.write("\n")


def LaTeX(lst):
    latex = codecs.open('BD_ALL.tex', "w", "utf-8")
    latex.write("\\documentclass[border=0.2cm,varwidth, 12pt, multi=my,crop]{standalone}")
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
    for i in lst:
        latex.write("\\begin{my}")
        latex.write("\\centering")
        latex.write("\\textbf{Enlace: }\\textcolor{UCM_color}{\\url{" + str(i) + "}}\\\\")
        latex.write("\\vspace{0.25cm}")
        latex.write(
            "Pulsar \\textbf{``Share your camera''}, configurar al gusto y pulsar \\textcolor{ForestGreen}{\\textbf{``START''}}\\\\")
        latex.write("\\centering")
        latex.write("\\includegraphics[width=5cm]{1.jpg}")
        latex.write("\\end{my}")
    latex.write("\\end{document}")
    latex.close()
    compiler = 'BD_ALL.tex'
    os.system("pdflatex -quiet " + compiler)
    os.remove('BD_ALL.tex')
    os.remove('BD_ALL' + '.aux')
    os.remove('BD_ALL' + '.log')
    os.remove('BD_ALL' + '.out')


def OBS_generator(lst, lst_of_lst):
    with open('carrusel_complutense.json', 'w') as f:
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


def PDF_split():
    pdf_document = "BD_ALL.pdf"
    file_base_name = pdf_document.replace('.pdf', '')

    pdf = PdfFileReader(pdf_document)

    for page_num in range(pdf.numPages):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page_num))
        with open('Complutense_CAM_Visitante_{1}.pdf'.format(file_base_name, page_num + 1), 'wb') as f:
            pdfWriter.write(f)
            f.close()


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
    print("Invitaciones creadas...")
    PDF_split()
    volcado_csv(lst_view)
    print("Proceso finalizado, datos completos...")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print(
            "Error de argumetos, se necesita un único entero (int) seguido de la posición de comienzo (int) \nEjemplo: ./script 5 0")
