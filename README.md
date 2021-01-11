# Building-a-webapplication

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Acknowledgements](#licensing)

## Installation <a name="installation"></a>
The code should run in Python 3 with no problems. No additional packages are needed. 

Follwoing libraries are being used:
 - flask
 - pandas
 - plotly
 - gunicorn
 
## Project Motivation<a name="motivation"></a>
The goal of this project was to build a webapplication to present data and graphs.

The analysed data contain information about the bitcoin and other crypto currencies. The data are presented on 

## File Descriptions <a name="files"></a>
To start the app, run the file "myapp.py".

#### data
The used data consists of three dataframes (allcc, market-price, total-bitcoins) and can be downloaded in the data folder. 

#### front-end
The "myapp" folder contains the "index.html" file for the frontend. For the structure Bootstrap was used. For the images plotly was used. With the help of the "render_template" they were transferred from the back-end to the frontend. 

#### data wrangle
The data for the figures are prepared in the "wrangle_data.py" file. 

#### requirements
The file "requirements.txt" is needed for the upload to the Heroku webpage to build the webapp. 

## Results<a name="results"></a>
The results can be viewed on https://webapprico.herokuapp.com/

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
The origin of the data are:
www.nomics.com
www.kaggle.com
Maybe you even have an idea for adjustments or improvements. 
