## How have the Olympics Changed? An Exploration of Data from Athens 1896 to Rio 2016
Team Members: Kevin Clark, Rebekah Rowland, Amy Dach, Poonam Goel

![alt text](https://stillmed.olympic.org/media/Images/OlympicOrg/IOC/The_Organisation/The-Olympic-Rings/Olympic_rings_TM_c_IOC_All_rights_reserved_1.jpg?interpolation=lanczos-none&resize=1400:*)

## Project Description

This project aims to create an interactive web application that showcases how the have the Olympics games have changed over 120 years. 

Our app can be accessed at: https://olympic-medalists.herokuapp.com/

## Data Source:
```
https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results 
``` 
## Description:
The dataset we found contains every male and female participant information that has competed in the Summer and Winter Olympic games since Athens 1896 up until Rio 2016. The data set is composed of two CSV files: one containing the athletes information (such as sex, age, event, year, and if they medaled) and the second containing the NOC (National Olympic Committee 3 letter code) and the country name. 

We chose this dataset because the raw data looked fairly clean and could provide many unique visualizations. We chose to investigate which countries have won the most medals over time utilizing maps and how the average dimensions of the Olympic athlete have changed using Tableau.

## Dependencies:

* Python 
* Flask 
* HTML/CSS
* JavaScript
* GeoJSON
* Leaflet 
* Mapbox
* SQLLite
* Tableau

## Usage:

1. Open site 
2. Click on buttons to explore, Tableau visualization to analyze olympian biometrics.  
3. Explore the plotly map to analyze medals by country.
4. Users can interactively explore biometrics through various filters and drop downs based on key data dimensions including sport, season, decade, and gender.
