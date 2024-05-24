# Attendance
This repository contains a Python-based attendance system that uses face recognition to identify individuals and mark their attendance. The project leverages OpenCV for video capture, face_recognition library for detecting and recognizing faces, and Pandas for updating attendance records in an Excel sheet.

# Features

Real-time face detection and recognition using a webcam.
Automatic marking of attendance for recognized individuals.
Stores attendance records in an Excel sheet.
Efficiently handles new and existing entries in the attendance sheet.

# Requirements
Python 3.x

OpenCV

face_recognition

numpy

pandas

openpyxl

# Installation

1.Clone this repository to your local machine:

git clone https://github.com/manishaaasini/attendance
cd attendance

2.Install the required Python packages:

pip install opencv-python face_recognition numpy pandas openpyxl

3.Please create a image folder and place your reference images in a folder  within the project directory. Each image file name should be the person's name (e.g., john_doe.jpg).

# Usage
Ensure your webcam is connected and working.

# Run the main script to start the attendance system:

python main_video.py
