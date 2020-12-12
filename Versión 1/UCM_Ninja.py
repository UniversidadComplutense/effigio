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
    LaTeX(lst)
    volcado_csv(lst_view)
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Error de argumetos, se necesita un único entero (int) seguido de la posición de comienzo (int) \nEjemplo: ./script 5 0")

