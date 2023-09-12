################################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 12/09/2023 Hora: 11:00
#Fecha de finalización: 12/09/2023 Hora:
#Última versión:
################################################################################

#formato codigo: 0201-304-i0506

#listas
listaTipo=[1, 2, 3]
listaArea=[1, 2, 3, 4]
listaPiso=[1, 2, 3, 4, 5, 6, 7, 8, 9]
listaPasillo=list(range(1,100))
listaFila= list(range(1,100))
listaColumna=list(range(1,100))
code=str("0201-304-i0506")

#Decodificar el área y el tipo
def decodificarAyT(code):
    """
    F:
    E:
    S:
    """
    tipo=int(code[1:2])
    area=int(code[3:4])
    if tipo in listaTipo:
        if tipo==1:
            tipo=str("libro")
        elif tipo==2:
            tipo=str("revista")
        elif tipo==3:
            tipo=str("folleto")
    if area in listaArea:
        if area==1:
            area=str("científica")
        elif area==2:
            area=str("tecnológica")
        elif area==3:
            area=str("legislativa")
        elif area==4:
            area=str("médica")
    return print("El material bibliográfico es de tipo",tipo,"del área",area)

decodificarAyT(code)