from multiprocessing.sharedctypes import Value
from typing import Type
from PyQt5.QtWidgets import *
from shapes_view import Ui_MainWindow
import math

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calc_button_circle.clicked.connect(lambda : self.calculate_circle())
        self.calc_button_rectangle.clicked.connect(lambda : self.calculate_rectangle())
        self.calc_button_square.clicked.connect(lambda : self.calculate_square())
        self.calc_button_triangle.clicked.connect(lambda : self.calculate_triangle())
        self.calc_button_trapezoid.clicked.connect(lambda : self.calculate_trapezoid())
        self.calc_button_para.clicked.connect(lambda : self.calculate_para())

    def calculate_circle(self):
        '''
        Method defining area formula for circle (pi * r^2)
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")
        try:
            radius = float(self.radius_input.text())
            if radius <= 0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()
            else:
                circle_area = (math.pi * radius * radius)
                msg.setText(f'Area = {circle_area:.2f}')
                x = msg.exec_()
        except ValueError:
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()
    
        self.radius_input.setText("")
    
    def calculate_rectangle(self):
        '''
        Method for defining area formula for rectangle (A = l * w)
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")

        try:
            long_side = float(self.long_side_input.text())
            short_side = float(self.short_side_input.text())
            if short_side <= 0 or long_side <=0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()
            else:
                rectangle_area = (short_side * long_side)
                msg.setText(f'Area = {rectangle_area:.2f}')
                x = msg.exec_() 
        except ValueError:
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()

        self.long_side_input.setText("")
        self.short_side_input.setText("")

    def calculate_square(self):
        '''
        Method for defining area formula for square (A = a^2)
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")

        try:
            side = float(self.side_input.text())
            if side <= 0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()  
            else:
                square_area = (side * side)
                msg.setText(f'Area = {square_area:.2f}')
                x = msg.exec_()
        except ValueError:
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()
    
        self.side_input.setText("")

    def calculate_triangle(self):
        '''
        Method for defining area formula for right triangle (A = 1/2 * b * h)  
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")

        try:
            base = float(self.base_input.text())
            height = float(self.height_input.text())
            if base <= 0 or height <= 0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()                
            else:
                triangle_area = (0.5 * base * height)   
                msg.setText(f'Area = {triangle_area:.2f}')
                x = msg.exec_()
        except ValueError: 
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()

        self.base_input.setText("")
        self.height_input.setText("")

    def calculate_trapezoid(self):
        '''
        Method for defining area formula for trapezoid (A = 1/2 * (a + b) * h)
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")

        try:
            base_a = float(self.base_a_input.text())
            base_b = float(self.base_b_input_2.text())
            height = float(self.trap_height_input.text())
            if base_a <= 0 or base_b <= 0 or height <= 0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()                 
            else:
                trapezoid_area = (0.5 * (base_a + base_b) * height)
                msg.setText(f'Area = {trapezoid_area:.2f}')
                x = msg.exec_()    
        except ValueError:
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()
       
        self.base_a_input.setText("")
        self.base_b_input_2.setText("")
        self.trap_height_input.setText("")

    def calculate_para(self):
        '''
        Defining area formula for parallelogram (A = b * h)
        '''
        msg = QMessageBox()
        msg.setWindowTitle('Answer')

        msg_err = QMessageBox()
        msg_err.setWindowTitle("ERR")

        msg_err_2 = QMessageBox()
        msg_err_2.setWindowTitle("ERR")

        try:
            base = float(self.para_base_input.text())
            height = float(self.para_height_input.text())
            if base <= 0 or height <= 0:
                msg_err.setText(f'Input positive integers')
                y = msg_err.exec_()           
            else:
                para_area = (base * height)
                msg.setText(f'Area = {para_area:.2f}')
                x = msg.exec_()
        except ValueError:
            msg_err_2.setText(f'String input')
            z = msg_err_2.exec_()
        
        self.para_base_input.setText("")
        self.para_height_input.setText("")

    #def ellipse_area(axis_a, axis_b):
        #'''
        #Method for defining area formula for ellipse (A = pi * a * b)
        #'''
        #msg = QMessageBox()
        #msg.setWindowTitle('Answer')

        #msg_err = QMessageBox()
        #msg_err.setWindowTitle("ERR")

        #msg_err_2 = QMessageBox()
        #msg_err_2.setWindowTitle("ERR")

        #try:
            #axis_a = float(self.axis_a_input())
            #axis_b = float(self.axis_b_input.text())          
            #if axis_a <= 0 or axis_b <= 0:
                #msg_err.setText(f'Input positive integers')
                #y = msg_err.exec_() 
            #else:
                #ellipse_area = (math.pi * axis_a * axis_b)
                #msg.setText(f'Area = {ellipse_area:.2f}')
                #x = msg.exec_()
        #except ValueError:
            #msg_err_2.setText(f'String input')
            #z = msg_err_2.exec_()

        #self.axis_a_input.setText("")
        #self.axis_b_input.setText("")