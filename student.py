#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -- Facial Recognition System --


# create an object for a student
class Student:
    def __init__(self, name):
        """set the name and default attendance of a new student in code"""
        self._name = name 
        self._attendance = 0 

    # Getter for name 
    @property
    def name(self):
        """First name and last name of the student"""
        return self._name

    # Getter for attendance
    @property
    def attendance(self):
        """attendance as a sum of classes"""
        return self._attendance

    # Setter for attendance
    @attendance.setter
    def attendance(self, value):
        """set attendance"""
        if value < 0:
            raise ValueError("Attendance cannot be negative")
        self._attendance = value


# Create a class for facial recongition
class FacialRecongition():
    def __init__(self):
        ImageStack = []
    
    def QueueImages(self, images):
        """Add images captured from video at regular intervals to the self.imagestack"""
        pass

    def _ExecuteQueue(self):
        """Itterates over the image stack and attempts to detect faces and then discards the img frame"""
        pass
    
    def _CheckStudent(self):
        """Identifies the student name and if they are present"""
        pass



        