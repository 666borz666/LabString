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
listaLado=["i","d"]
code=str("0201-34-i0506")
#funcion separar código
def separarCódigo(code):
    """
    F:
    E:
    S:
    """
    tipo=str(code[1:2])
    area=str(code[3:4])
    piso=str(code[5:6])
    pasillo=str(code[6:8])
    lado=str(code[9:10])
    fila=str(code[10:12])
    columna=str(code[12:14])
    return tipo, area, piso, pasillo, lado, fila, columna

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

#Decodificar el tipo y pasillo
def decodificarPyP(code):
    """
    F:
    E:
    S:
    """
    piso=int(code[5:6])
    pasillo=int(code[6:8])
    if piso in listaPiso and pasillo in listaPasillo:
        return print("El material bibliográfico está en el piso",piso,"y el pasillo",pasillo)

#Decodificar el tipo y pasillo
def decodificarLyFyC(code):
    """
    F:
    E:
    S:
    """
    lado=str(code[8:9])
    fila=int(code[9:11])
    columna=int(code[11:13])
    if lado in listaLado and fila in listaFila and columna in listaColumna:
        if lado == "i":
            lado ="izquierdo"
        if lado == "d":
            lado ="derecho"
    return print("El material bibliográfico está en: \nLado",lado,"\nFila",fila,"\nColumna",columna)

decodificarLyFyC(code)