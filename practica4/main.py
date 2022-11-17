import functions as f
from os import path

file= path.join(path.dirname(path.abspath('cuento.txt')), 'cuento.txt')
def main():
    f.count_line(file)

if __name__ == '__main__':
    main()


