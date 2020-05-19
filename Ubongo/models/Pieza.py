from models import Componente

class Pieza(Componente):
    def __init__(self, x, y, width, height, forma, tipoPieza):
        
        Componente.__init__(self, x, y, width, height)

        self.forma = forma
        self.tipoPieza = tipoPieza

    
