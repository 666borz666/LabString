################################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 12/09/2023 Hora: 11:00
#Fecha de finalización: 12/09/2023 Hora:
#Última versión:
################################################################################
#Listas
tipo=[1, 2, 3]
area=[1, 2, 3, 4]
piso=[1, 2, 3, 4, 5, 6, 7, 8, 9]
pasillo=list(range(1,100))
fila= list(range(1,100))
columna=list(range(1,100))
lado=["i","d"]
buscarTipo= ["libro", "revista", "folleto"]
def decoficarCodigo (codigo):
    """
    """
    dividir=codigo.split("-")
    tipoBiblio = buscarTipo[int(partes[0][0])]
    if tipoBiblio==
    areaBiblio = area[int(partes[0][1]) - 1]
    pisoBiblio = piso[int(partes[1][0]) - 1]
    pasilloBiblio = int(partes[1][1:])
    filaBiblio = int(partes[2][:2])
    columnaBiblio = int(partes[2][2:])
    ladoBiblio = "Izquierda" if partes[3] == "i" else "Derecha"

codigo=input("Digíte el código de su material bibliográfico: ")

