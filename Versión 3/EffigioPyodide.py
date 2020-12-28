import os, sys
import io, base64
from zipfile import ZipFile
import js
from Effigio_v4 import *

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
    	fileContent = f.read()
    	return fileContent

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
    argv = int(argv)
    valores = balance(argv)
    lst_of_lst = division(valores, lst_view)  
    OBS_generator(lst_view, lst_of_lst)
    LaTeX(lst)
    volcado_csv(lst_view)

# this will work only online. Replace with a number assignment to make experiments
invitaciones = js.document.getElementById('invites').value

main(invitaciones,0)

zipObj = ZipFile('event.zip', 'w')
zipObj.write('OBStudio_carrusel_complutense.json')
zipObj.write('url_invitaciones.csv')
zipObj.write('InvitacionesLatex.tex')
zipObj.close()


eventBytes=bytes_from_file('event.zip')


