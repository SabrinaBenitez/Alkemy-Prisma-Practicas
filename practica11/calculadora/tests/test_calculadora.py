import unittest
import sys,os
import funciones.funciones as f
from pathlib  import Path
import datetime
sys.path.append('')

from docs_from_tests.instrument_call_hierarchy import (instrument_and_import_package, 
                                                        instrument_and_import_module, 
                                                        initialise_call_hierarchy, 
                                                        finalise_call_hierarchy
                                                       )

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(),
                              '..', 'funciones'), 'funciones'
                            )

class TestCalculadora(unittest.TestCase):
    initialise_call_hierarchy('start')
    def test_suma(self):
        self.assertEqual(f.obtener_suma(2,5),7)
        self.assertTrue(f.obtener_suma(2,2),4)  
        self.assertIsNotNone(f.obtener_suma(9,2),'Se esperaba que no fuera cero')  

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
        show_private_functions=False,
        excluded_functions=[])

        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..',
                                                 'doc', 'diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)  

    def test_resta(self):
       self.assertIsInstance(f.obtener_resta(3,5),int)   
       self.assertNotEqual(f.obtener_resta(2,1),2)  
       self.assertGreater(f.obtener_resta(9,1),7)

    def test_multiplicacion(self): 
        self.assertLess(f.obtener_multiplicacion(9,5),50)  
        self.assertGreaterEqual(f.obtener_multiplicacion(3,2),5)   
        self.assertLessEqual(f.obtener_multiplicacion(3,2),10)

    def test_division(self):
        self.assertIsNot(f.obtener_division(4,2),3)
        self.assertNotEqual(f.obtener_division(7,2),3)
        self.assertIsNotNone(f.obtener_division(2,2),"No es cero")         