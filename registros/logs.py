from datetime import datetime
from os.path import exists
from os import system
import sys
class log:
      def registro(self,parametro):

          """
          Funcion para ejecutar todas las demas funciones
          """
          
          inicio = datetime.now()
          log_str = inicio.strftime('%Y%m%d_%H%M%S')
          archivo_log = 'log.log'
          if not exists('registros/logRegistros'):
                system('mkdir registros/logRegistros')
                        
          if parametro=="e":
                with open(f'registros/logRegistros/{archivo_log}','a') as log:
                      log.write(f'{datetime.now()}: El registro fue ingresado correctamente\n')
          else:
                with open(f'registros/logRegistros/{archivo_log}','a') as log:
                      log.write(f'{datetime.now()}: El registro no fue ingresado\n')
