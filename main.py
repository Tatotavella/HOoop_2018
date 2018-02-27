import random
import matplotlib.pyplot as plt

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
            filanueva = FilaPreferencial() # Abro fila nueva preferencial
            return filanueva
        else:
            return 0
        
    
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
    # Array de clientes
    # Total de clientes disponibles
    tot_clientes = 60
    lista_dni = [random.randint(10000000,99999999) for x in range(tot_clientes)]
    clientes_arr = []
    # Armo lista de clientes y asigno al azar Generales y Preferenciales
    # Probabilidad de generar clientes de categoria General
    # 1 - proba_gen es la probabilidad de generarl clientes de categoria Preferencial
    proba_gen = 0.5
    #print('Lista de Clientes:')
    for dni in lista_dni:
        cl = Cliente(dni)
        moneda = random.uniform(0,1)
        if moneda < proba_gen:
            cl.modificarcategoria('General')
        else:
            cl.modificarcategoria('Preferencial')
        clientes_arr.append(cl)
        #print(cl)
    # Inicializacion de filas
    fila_general = FilaGeneral()
    fila_preferencial = FilaPreferencial()
    fila_nueva = FilaGeneral()
    # Serie temporal de gente en cada fila
    gen_data = []
    pref_data = []
    # Tiempo de atencion fila general
    t_aten_gen = 7
    # Tiempo de atencion fila preferencial
    t_aten_pref = 5
    # Pasos totales de simulacion
    N = 100
    # Cantidad maxima de clientes en fila Preferencial
    maxenfila = 5
    # Tiempo de entrada a fila - A cada paso (por ahora)
    step = 1
    t_gen = 1
    t_pref = 1
    indice_cliente = 0
    while(step < N):
        # Ingreso a la fila si hay clientes disponibles
        if indice_cliente < tot_clientes:
            cl = clientes_arr[indice_cliente]
            cat = cl.categoria
            if cat == 'General':
                # Fila general
                fila_general.insertar(cl)
            elif cat == 'Preferencial':
                # Fila preferencial
                fila_preferencial.insertar(cl)
        # Egreso de la fila si hay clientes en la fila
        # General
        if fila_general.enfila > 0:
            if t_gen > t_aten_gen:
                fila_general.atender()
                t_gen = 1
            else:
                t_gen += 1
        # Preferencial
        if fila_preferencial.enfila > 0:
            if t_pref > t_aten_pref:
                fila_preferencial.atender()
                t_pref = 1
            else:
                t_pref += 1

        # Fila nueva
        fila_nueva = fila_preferencial.abrircajanueva(maxenfila,fila_nueva)
        if fila_nueva != 0:
            # Ingresos y egresos de fila nueva
            pass
        else:
            pass

        # Guardo data
        gen_data.append(fila_general.enfila)
        pref_data.append(fila_preferencial.enfila)
        indice_cliente += 1
        step += 1
       
    plt.plot(gen_data,'o', label = 'Gente en fila general')
    plt.plot(pref_data,'o', label = 'Gente en fila preferencial')
    plt.legend()
    plt.show()
    '''
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
    '''
