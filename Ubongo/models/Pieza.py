from models import componente


class Pieza(componente):
    def __init__(self, x, y, width, height, forma, tipoPieza):

         componente.__init__(self, x, y, width, height)
         self.forma = forma
         self.tipoPieza = tipoPieza

    
