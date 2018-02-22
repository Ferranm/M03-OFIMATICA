# coding: utf8
# Ferran March Azañero
# 21/02/2018

Cajon1="movil"
Cajon2="bocadillo"
Cajon3="boli"
Cajon4="bebida"

print ""
print "Antes"
print "Cajon1->", Cajon1
print "Cajon2->", Cajon2
print "Cajon3->", Cajon3
print "Cajon4->", Cajon4

mesa_extra=Cajon1
Cajon1=Cajon3
Cajon3=mesa_extra
mesa_extra=Cajon4
Cajon4=Cajon2
Cajon2=mesa_extra

print ""
print "Después"
print "Cajon1->", Cajon1
print "Cajon2->", Cajon2
print "Cajon3->", Cajon3
print "Cajon4->", Cajon4
