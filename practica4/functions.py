import logging
import logging.config

#log_file_path = path.join(path.dirname(path.abspath('log_file_config.conf')), 'log_file_config.conf')
logging.config.fileConfig('C:/Users/Sabrina/Desktop/practica4/log_config_file.conf')
logger_main = logging.getLogger('main')
logger_functions = logging.getLogger('functions')

def count_line(filename):
    count= 0
    with open(filename,'r') as fname:
        logger_main.info("Leyendo el archivo ...")
        try:
            lines = fname.readlines()
            for line in lines:
                count_words(line,count)
                count = count + 1        
            logger_main.info("Procesando el archivo ...")  
	    logger_functions.info(f"cuento.txt - Cantidad de renglones {count}")
                  
        except:            
            logger_main.error("Error al procesar el archivo ...") 
    
def count_words(word,count):
    countword=0
    for i in word.split(' '):
        countword= countword + 1
    logger_functions.info(f"Renglon {count}: {countword} Palabras")
