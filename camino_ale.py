from borracho import BorrachoTradicional,Borracho
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, pasos, tipo_de_borracho):

    borracho = tipo_de_borracho(nombre='Andy')
    origen = Coordenada(0, 0)
    campo.anadir_borracho(borracho, origen)

    coordenadas_x=[]
    coordenadas_y=[]

    coordenadas_x.append(origen.x)
    coordenadas_y.append(origen.y)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        coordenadas_x.append(campo.obtener_coordenada(borracho).x)
        coordenadas_y.append(campo.obtener_coordenada(borracho).y)

    return (coordenadas_x, coordenadas_y)

def graficar(x, y,pasos):
    grafica = figure(title='Random Walks',x_axis_label='x axis', y_axis_label='y axis')
    grafica.line(x, y, legend_label='walk', color='yellowgreen',name='juan') #recorrido

    # gráfica la línea inicial de movimiento porque no se puede graficar un punto
    grafica.line(x[0:2],y[0:2],color='black',line_width=10)
    grafica.line(x[-3:-1],y[-3:-1],color='red',line_width=10) #punto final y final-1
    grafica.line(x[0:-1:pasos-1],y[0:-1:pasos-1]) #linea de punto inicial a punto final
    show(grafica)

def main(pasos, tipo_de_borracho):

    campo=Campo()
    coordenadas_x, coordenadas_y = caminata(campo, pasos, tipo_de_borracho)
    graficar(coordenadas_x, coordenadas_y,pasos)

if __name__ == '__main__':

    pasos = 10000
    main(pasos, Borracho)