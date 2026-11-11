
# =====================================
# GRAFICA 1: ERRORES POR EPOCA
# =====================================

set terminal pngcairo size 1000,600
set output "errores_por_epoca.png"

set title "Aprendizaje del perceptron"
set xlabel "Numero de epoca"
set ylabel "Cantidad de errores"

set grid
set yrange [0:*]

plot "errores.dat" using 1:2 \
with linespoints linewidth 2 pointtype 7 \
title "Errores por epoca"

set output

# =====================================
# GRAFICA 2: VARIABLE Z
# =====================================

set output "valores_z.png"

set title "Evolucion de la variable z"
set xlabel "Numero de epoca"
set ylabel "Valor de z"

set grid
set xzeroaxis

plot "z_por_epoca.dat" using 1:2 \
with linespoints linewidth 2 title "Patron 1", \
"z_por_epoca.dat" using 1:3 \
with linespoints linewidth 2 title "Patron 2", \
"z_por_epoca.dat" using 1:4 \
with linespoints linewidth 2 title "Patron 3", \
"z_por_epoca.dat" using 1:5 \
with linespoints linewidth 2 title "Patron 4"

set output
