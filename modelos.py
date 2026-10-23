class Libro:
    def __init__(self, titulo, autor, editorial, genero, precio, stock):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.genero=genero
        self.__precio=precio #Atributo privado
        self.stock=stock
        
    def mostrar_info(self,):
        print(f"""
              INFORMACIÓN DEL LIBRO 
              {self.titulo}:
              Autor: {self.autor}
              Editorial: {self.editorial}
              Genero: {self.genero}
              Precio: ${self.__precio}
              Unidades disponibles: {self.stock}
              """)