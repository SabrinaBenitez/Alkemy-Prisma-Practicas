import logging
import logging.config
from functions  import count_line,count_words

#logging.config.fileConfig(fname='log_config_file', disable_existing_loggers=False)
#logger = logging.getLogger('mainLogger')

def main ():
    count_line('cuento.txt')
    count_words()

if __name__ == '__main__':
    main()


