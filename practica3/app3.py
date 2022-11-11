from log import my_log

logger = my_log(__name__)

fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]

for f in fruits:
    
    try:
        logger.info(f'Conversion Exitosa : {f} ---> {f.lower()} ')
    except:
        logger.error(f'Conversion Fallida :{f}')