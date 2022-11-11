import unittest
import sys,os
import funciones

sys.path.append('/mnt/c/Users/Sabrina/Desktop/Practicas/practica10/calculadora')

class TestCalculadora(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(funciones.obtener_suma(2,5),7)
        self.assertTrue(funciones.obtener_suma(2,2),4)  
        self.assertIsNotNone(funciones.obtener_suma(9,2),'Se esperaba que no fuera cero')     
   
    def test_resta(self):
       self.assertIsInstance(funciones.obtener_resta(3,5),int)   
       self.assertNotEqual(funciones.obtener_resta(2,1),2)  
       self.assertGreater(funciones.obtener_resta(9,1),7)

    def test_multiplicacion(self): 
        self.assertLess(funciones.obtener_multiplicacion(9,5),50)  
        self.assertGreaterEqual(funciones.obtener_multiplicacion(3,2),5)   
        self.assertLessEqual(funciones.obtener_multiplicacion(3,2),10)

    def test_division(self):
        self.assertIsNot(funciones.obtener_division(4,2),3)
        self.assertNotEqual(funciones.obtener_division(7,2),3)
        self.assertIsNotNone(funciones.obtener_division(2,2),"No es cero")