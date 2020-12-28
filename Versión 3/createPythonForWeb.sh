#!/bin/bash
ficheroPyo="EffigioPyodide.py"
ficheroEffigio="EffigioOnline.py"
tmpfile=$(mktemp /tmp/effigio.XXXX); 
sed -e "/main/q" $ficheroEffigio > $tmpfile; 
sed  -e "/from Effigio.*$/r $tmpfile"  -e "/from Effigio.*$/d" $ficheroPyo > web.py
