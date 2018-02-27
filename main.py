import random

class Fila(object):
    """Clase base de fila"""

    def __init__(self):
         """constructor de la clase Fila """
         self.enfila= 0  # Cantidad de clientes en la fila
         self.fila = []
         
class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila += 1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
        
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if self.enfila > maxenfila:
            filanueva = FilaGeneral() # Abro fila nueva, va a ser del tipo FilaGeneral
            return filanueva
        
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila += 1
        self.fila.append(cliente)
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila -= 1
        self.fila.pop(0)
        pass      

    

class Cliente(object):
     """clase cliente """
     def __init__(self,dni):
         """ constructor de la clase cliente """
         self.dni = dni
         self.categoria = None
     def modificarcategoria(self, categoria):
         """modifica el atributo categoria del cliente """
         self.categoria = categoria
         pass
     def __repr__(self):
         text = '(DNI: {} | CAT: {})'
         return text.format(self.dni,self.categoria)
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    fila_general = FilaGeneral()
    fila_preferencial = FilaPreferencial()
    # Array de clientes
    lista_dni = [random.randint(10000000,99999999) for x in range(10)]
    clientes_arr = []
    # Armo lista de clientes y asigno al azar Generales y Preferenciales
    # Uso 80% Generales y 20% Preferenciales
    proba_gen = 0.8
    for dni in lista_dni:
        cl = Cliente(dni)
        moneda = random.uniform(0,1)
        if moneda < proba_gen:
            cl.modificarcategoria('General')
        else:
            cl.modificarcategoria('Preferencial')
        clientes_arr.append(cl)
    print(clientes_arr)
    cl_1 = Cliente('37786375')
    cl_1.modificarcategoria('General')
    print('Cliente: %s | Categoria: %s ' % (cl_1.dni,cl_1.categoria))
    print(cl_1)
    # Una Fila general
    fila_gral_1 = FilaGeneral() 
    fila_gral_1.insertar(cl_1)
    print('Fila General: Cantidad de Personas: %d' % (fila_gral_1.enfila))
    print('Lista de personas: %s' % (fila_gral_1.fila))
    pass
