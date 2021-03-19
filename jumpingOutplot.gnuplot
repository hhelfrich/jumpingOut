set term pdfcairo color enhanced font "Times-New-Roman,14" size 5,3
set output "jumpingOutPlotGNU.pdf"

set xlabel "{/Times-New-Roman-Italic Time}"
set ylabel "{/Times-New-Roman-Italic Position}"

plot "jumpingOut.txt" using 1:2 title 'No Parachute' with lines lw 2

unset output

set output "jumpingOutPlotParaGNU.pdf"

plot "jumpingOutPara.txt" using 1:2 title 'Parachute at 1200m' with lines lw 2

unset output