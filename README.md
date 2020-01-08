
# Pixel Art Generator

A python script that can be used to pixilate most jpeg, jpg, png images according to the user specified pixel dimensions.
## Getting Started
### Prerequisites
The script uses the following python libraries:
* [NumPy](https://numpy.org/)
* [Pillow](https://pypi.org/project/Pillow/)
* [matplotlib](https://matplotlib.org/) 
* [scipy](http://www.dropwizard.io/1.0.2/docs/) 
* [PIL](http://www.dropwizard.io/1.0.2/docs/)

### Installing

In the terminal, execute the following commands after cloning the project on your local machine:
* Installing pip3:
`
sudo apt-get -y install python3-pip
`

* Installing NumPy  
`sudo pip3 install numpy`

* Install Pillow
`sudo pip3 install Pillow==2.2.1`

* Install PIL
`sudo pip3 install pil`

* Install scipy
`pip install git+https://github.com/scipy/scipy.git`
## Running

Execute `python3 main.py` in the project directory to run the script.
##### The script may take some time to pixilate the images that are relatively larger in size.
##### Also it is advised to not try to pixilate full HD or 4K images as these may cause overflow errors.

## Contributing
To raise issues, request a feature or contribute, visit [here](https://github.com/masterchief01/Pixel_art_generator).
