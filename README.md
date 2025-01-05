# PFDA-project

***

Author: Galal Abdelaziz

## This README document is part of the __Programming For Data Analytics__ project 2024/2025, at [ATU](https://www.atu.ie/).

***

## Technologies:

* Python 3.11.5 available [here](https://www.anaconda.com/download)
* Visual Studio Code available [here](https://code.visualstudio.com/)

***

## Libraries:

- [**pandas**](https://pandas.pydata.org/) as pd
- [**matplotlib.pyplot**](https://matplotlib.org/stable/api/pyplot_api.html) as plt
- [**numpy**](https://numpy.org/) as np
- [**seaborn**](https://seaborn.pydata.org/) as sns
- [**sqlite3**](https://docs.python.org/3/library/sqlite3.html)

***

## Introduction

**Divvy Bikes** is a popular bicycle-sharing system in the **Chicagoland** area, providing an affordable, convenient, and flexible transportation option for short-distance travel. It operates a network of durable bikes stationed throughout Chicago and Evanston, accessible to users through **Annual Memberships** or **Passes** via the Divvy App or kiosks.

Divvy is available **24/7**, **365 days a year**, offering an ideal solution for activities such as commuting, running errands, or leisurely exploring the city. Riders can unlock and return bikes at any station within the network, providing freedom and flexibility across the extensive system.

For more details, visit [Divvy Bikes Website](https://divvybikes.com/about).

***

## About:

This project is a simple implementation of a data analytics tool using Python. 

***

## Contents:

- **datasets**: This folder contains the .CSV dataset files used for this analysis.
- **img**: This folder contains all images used in this project.
- **.gitignore**: Specifies which files and directories should be ignored by Git when committing changes to a repository.
- [**project.ipynb**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/project.ipynb): This notebook contains the full analysis, including data cleaning, data visualization, and data analysis.
- [**analysis.ipynb**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/analysis.ipynb): This notebook contains the data analysis part of the project.
- [**divvy_trips.db**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/divvy_trips.db): This file contains a Database table created using SQLite. 
- [**splitlargefile.py**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/splitlargefile.py): This file contains the script I used to split large CSV files into smaller ones due to the limitations of GitHub.
- **README.md**: Contains information about the repository, including its purpose, structure, and usage instructions.
- **requirements.txt**: Specifies the Python packages required to run the project.
- **requirements.txt**: Specifies the Python packages required to run the project.

***

The **Divvy Trips Q1 2019 Dataset** provides detailed information about **365,069 trips** recorded between January and March 2019. It captures key aspects of Chicago’s bike-sharing program, including trip details, user demographics, and station usage.

### Key Features:

- **Trip Information**: Includes trip ID, start and end times, trip duration, and bike ID.
- **Station Details**: Provides the start and end station names and IDs.
- **User Demographics**: Contains user type (Subscriber or Customer), gender, and birth year.

### Data Highlights:

- **Trip Patterns**: The dataset enables analyses of usage trends, station popularity, and trip durations.
- **User Insights**: Demographic information (gender and birth year) allows for user profile studies, though some data is missing:
  - **Gender**: Missing for **19,711 trips** (~5.4%).
  - **Birthyear**: Missing for **18,023 trips** (~4.9%).

### Use Cases:

This dataset is ideal for exploring:
- User behavior trends across seasons.
- Station and bike usage patterns.
- Demographic characteristics of riders.

The dataset’s completeness in trip-level details ensures robust analysis of operational aspects, while missing demographic data may slightly limit user-specific insights.

***

**Disclaimer**

This repository includes content created with the assistance of an AI chat assistant. While the AI has provided valuable insights, code, and text generation, all content has been reviewed, modified, and verified by the repository's author to ensure accuracy and relevance.

***

## Resources:

- Weekly lectures. 
- Understanding the dataset: : [1](https://divvy-tripdata.s3.amazonaws.com/index.html), [2](https://www.kaggle.com/datasets/mdmasumomarjashim/divvy-trips-data-20192020), [3](https://medium.com/@gbemuduazubuike/), [4](divvy-bikes-an-exercise-on-data-cleaning-and-analysis-of-cycling-data-using-r-programming-language-c38e8a4521ef).
- Data Preperation: [Date Formatting](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html); [Data Frame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html); [Handling Missing Values](https://community.sisense.com/t5/knowledge-base/dealing-with-missing-values-in-python/ta-p/9376).
- Calculations: [Resampling](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#resampling); [Calculating Mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html); [Calculating Max](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html); [Data Frame Filtring/Indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing); [Date Time Index](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset).
- Plotting: [1](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html), [2](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html), [3](https://matplotlib.org/stable/api/axes_api.html).  
- Database: [1](https://www.sqlitetutorial.net/sqlite-python/), [2](https://docs.python.org/3/library/sqlite3.html), [3](https://www.w3schools.com/sql/).

***

## Running the program:

1. Clone the repository using the following command: `git clone https://github.com/Galal-Abdelaziz/PFDA-project.git`
2. Install the required packages by running `pip install -r requirements.txt` in the terminal.

***

## End