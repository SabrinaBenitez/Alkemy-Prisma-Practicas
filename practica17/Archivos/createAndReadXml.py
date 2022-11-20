#coding=utf-8
import xml.dom.minidom
import xml.etree.cElementTree as ET

def GenerateXml():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'CONFIG_LIST', None)
    root = dom.documentElement
    employee = dom.createElement('COMP')
    root.appendChild(employee)
    nameE = dom.createElement('path')
    nameE.setAttribute ("valor", "aaaaaaaaaaa") # Agregar atributo
    nameT = dom.createTextNode('linux')
    nameE.appendChild(nameT)
    employee.appendChild(nameE)
    f = open('config_new.xml', 'a')
    dom.writexml(f, addindent=' ', newl='\n')
    f.close()

GenerateXml()

tree = ET.parse("config_new.xml")
root = tree.getroot()
COMP = root.findall ('COMP') [0]
print("Tag:", COMP.tag, "Attributes:", COMP.attrib, "Text:",COMP.text.strip(), "Tail:", COMP.tail)
ruta = COMP.findall ("ruta") [0]
print("Tag:", path.tag, "Attributes:", path.attrib, "Text:", path.text.strip(),"Tail:", path.tail)
