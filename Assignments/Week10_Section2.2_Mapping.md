# Week 10: Mapping<!-- omit in toc -->
This week we are starting are going to work with spatial vector data and explore mapping with Python.
____
## Table of Contents:<!-- omit in toc -->
- [To Do List](#to-do-list)
- [Resources](#resources)
    - [Geopandas documentation](#geopandas-documentation)
    - [Spatial Datasets:](#spatial-datasets)
- [Required Training Activities](#required-training-activities)
- [Optional but Highly Recommended Activities](#optional-but-highly-recommended-activities)
- [Assignment 9: Map our watershed!](#assignment-9-map-our-watershed)
  - [Part 1: Forecast](#part-1-forecast)
    - [Forecast Rules for this week:](#forecast-rules-for-this-week)
    - [Submission Instructions](#submission-instructions)
  - [Part 2: Mapping](#part-2-mapping)
    - [Requirements:](#requirements)
    - [Submission Instructions](#submission-instructions-1)
  - [Part 3: Pandas Cheat Sheet](#part-3-pandas-cheat-sheet)
    - [Notes on Cheat Sheet formatting](#notes-on-cheat-sheet-formatting)

___
## To Do List
1. Save the portion of your script from last week that downloads and formats your data to  `class_scripts/data_downloading` folder in the `Forecasting21` repo **before Thursday**

2. Complete the required training activities **before next Tuesday**
   
3. Complete the [Pandas Cheat Sheet](#part-3-pandas-cheat-sheet) by the end of the day **Thursday**

4. Complete your [forecast](#part-1-forecast) and submit your script to your `Forecast_Submissions` folder in your `homework repo` by **noon on Monday**.
   
5. Submit your [mapping script](#part-2-mapping) to the `class_scripts/mapping` folder in the `Forecasting21` repo **noon on Monday**

6. Submit your map to the google slides [here](https://docs.google.com/presentation/d/1jAU9PtItwcw3LbqZx6HlZEDVyuQ6_oo6iFLnWykQ6KY/edit?usp=sharing) and add your mapping script to the forecast folder by **noon on Monday**

___
## Resources
#### Geopandas documentation
- [GeoPandas official documentation](https://geopandas.org/)
- [GeoPandas Examples Gallery](https://geopandas.org/gallery/index.html)

#### Spatial Datasets:
- [USGS Stream Gauges](https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder)
- [USGS Spatial Resources Site](https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products)
- [USGS Mapping Viewer](https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View)
___
## Required Training Activities
1. Chapter 2 of Intermediate to Earth Data Science: Vector Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/): GIS in Python: Introduction to Vector Format Spatial Data - Points, Lines and Polygons
 - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/intro-to-coordinate-reference-systems-python/): Introduction to Coordinate Reference Systems
 - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/geographic-vs-projected-coordinate-reference-systems-python/): Geographic vs projected coordinate reference systems - GIS in Python

## Optional but Highly Recommended Activities
1. Chapter 3 of Intermediate to Earth Data Science: Processing Spatial Vector Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/reproject-vector-data-in-python/): Reproject Vector Data
 - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/clip-vector-data-in-python-geopandas-shapely/): Clip Vector Data
 - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/dissolve-polygons-in-python-geopandas-shapely/): Dissolve Polygons
  - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/spatial-joins-in-python-geopandas-shapely/): Spatial Joins
  - [Lesson 4](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/missing-data-vector-data-in-python/): Missing Spatial Data

___
## Assignment 9: Map our watershed! 
This week you will still make a forecast as usual but we won't really be advancing our forecasting approach (you are of course welcome to if you would like though). Rather we are going to focus on making a spatial map of the watershed. As such the assignment has two parts:
 1. Submitting your forecast to the competition as usual and putting the python script you used to generate it in your `Forecast_submissions` folder of your `homework` repo
 2. Creating a map and submitting this to (1) our class gallery and (2) the folder of scripts in the `Forecasting21` repo.

 NOTE: **There is no markdown file required this week**. Also note that your mapping script should be completely separate from your forecast script and will be submitted separately in the `Forecasting21` repo.  

### Part 1: Forecast
Note this part should be really fast for you. Just run your forecast as you have been doing and submit to the competition.

#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis.

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission Instructions
This week you should submit 2 things in your `submission` folder
  1. Submit your forecast to the forecast repo as normal
  2. submit the script you used to generate your forecast to the submission folder of your repo `Latname_HW10.py`

### Part 2: Mapping
This is the part I would like for you to focus your efforts on. Your assignment is to make the **most visually appealing and informative map** you can of our watershed. Its completely up to you what layers you include and what the spatial extent of your map will be.

#### Requirements:
At a minimum you map must include:
- At least 4 layers
- A minimum of two vector data types (i.e. point, line, polygon)
- A legend

#### Submission Instructions
1.  Add your final map to our map gallery and describe it [here](https://docs.google.com/presentation/d/1jAU9PtItwcw3LbqZx6HlZEDVyuQ6_oo6iFLnWykQ6KY/edit?usp=sharing) follow the instructions slide to see what you should include on your slide.
2. Submit the script you used to make your map to the `Forecasting21` repo: `class_scripts/mapping`
  - Your script should be named `lastname_map.py`
  - Your script should be well commented, follow pep8 standards and be easy to follow.
  - **Do not** upload the datasets for your map to the repo. Its okay if your script won't run from the forecast repo because its pointing to files you have locally.
  - For each file you use include a comment with a link for where you got it.
  - This script should include only what is necessary to generate the map you submitted to the gallery. Don't include your forecast analysis here.

### Part 3: Pandas Cheat Sheet 
1. Create a cheet sheet on Pandas basics that covers the following: 
   - Summarize Pandas
     - What are they and how are they different from the other object types we have worked with so far
     - How to make a pandas dataframe from scratch & by reading in a csv
     - How to slice pandas dataframes -- both using loc and iloc
     - What is the index of a pandas dataframe -- why is is different than other columns and how can you work with it? 
     - Key methods associated with pandas dataframes
     - Key attributes associated with pandas dataframes
   - Summarize any additional functions you have found helpful for working with dataframes 
2. Submit your cheat sheet to me in the `cheat_sheets` folder of your `homework-githubname` repo. Name your file `lastname_CS4_Pandas`

  #### Notes on Cheat Sheet formatting
   - Reminder: it is entirely up to you what your cheet sheet should look like, and note that you already have the ones provided in the content folder you so it doesn't need to be a duplicate of that. The point is for you to have a concise guide in your own words that will be helpful to you and that you can refer back to.
   - This might take the form of a word document, a powerpoint slide, or even a hand written or drawn diagram, a jupyter notebook or pythhon script (when we get to those) or something more creative that I'm not thinking of yet :)
   - In general I'm looking for something the equivalent of 1-2 pages long.
   - All Cheat Sheet assignments will be graded pass/fail. If I determine yours needs work you will be able to resubmit the following Tuesday with a revised version.