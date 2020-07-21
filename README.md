# Gesture-Recognizer
This project incorporates the use of deep learning for accurate real time classification of hand gestures.
.
.
This is an open ended project which can be further applied and implemented for various applications like development of contactless devices and other automated applications.

Currently this model can efficiently detect four gestures namely:
1. Fist
2. L Shape
3. Palm
4. Peace

The images for first three gestures were obtained from Kaggle whereas for the fourth one I created my own dataset.
The dataset as well as the codes for preprocessing are made available for fellow developers.
Files:

Raw_dataset                        : Directory with the Kaggle dataset
processed_dataset                  : Directory with my own images addition
Preprocessor.py                    : Image processing techniques before feeding it to the network
Data_generator.py                  : Self images dataset generation (whole process was automated)
my_model2.h5                       : keras deep learning trained model which is invoked in app.py
Gesture Recognizer.ipynb           : Jupyter Notebook
App.py                             : Deployed application 

Hope this project might help any viewer for further research and learning processes.
