# PFDA-project

***

Author: Galal Abdelaziz

## This README document is part of the __Programming For Data Analytics__ project 2024/2025, at [ATU](https://www.atu.ie/).

The project presents a straightforward implementation of a data analytics tool using Python, aimed at analyzing the Divvy bike-sharing system in the Chicagoland area.

***

![readme](img/readme.jpg)

***

## Table of Contents
- [Technologies](#Technologies)
- [Libraries](#Libraries)
- [Introduction](#introduction)
- [Repository Contents](#repository-contents)
- [Analysis Objectives](#analysis-objectives)
- [Running the Program](#running-the-program)
- [Resources](#resources)
- [Disclaimer](#disclaimer)

***

## Technologies

* Python 3.11.5 ([Download](https://www.anaconda.com/download)) - Selected for its powerful libraries and widespread use in data analytics.
* Visual Studio Code ([Download](https://code.visualstudio.com/)) - Chosen for its versatility and robust support for Python development.
* Jupyter Notebook ([Installation Guide](https://jupyter.org/install)) - Utilized for its interactive environment that integrates code, visuals, and narrative text for seamless data analysis and presentation.

***

## Libraries

- [**pandas**](https://pandas.pydata.org/) for data manipulation - Essential for handling large datasets and performing efficient data transformations.
- [**matplotlib.pyplot**](https://matplotlib.org/stable/api/pyplot_api.html) for visualization - Used to create static, interactive, and animated visualizations.
- [**numpy**](https://numpy.org/) for numerical computations - Provides support for handling arrays and performing complex mathematical operations.
- [**seaborn**](https://seaborn.pydata.org/) for statistical data visualization - Offers high-level interface for drawing attractive statistical graphics.
- [**sqlite3**](https://docs.python.org/3/library/sqlite3.html) for database management - Allows efficient storage and retrieval of structured data.
- [**scikit-learn**](https://scikit-learn.org/stable/) for machine learning algorithms - Facilitates the implementation of clustering, regression, and classification models.
- [**plotly.express**](https://plotly.com/python/plotly-express/) for interactive visualizations - Enables the creation of dynamic and interactive plots for better insights.

***

## Introduction

**Divvy Bikes** is a popular bicycle-sharing system in the **Chicagoland** area, providing an affordable, convenient, and flexible transportation option for short-distance travel. It operates a network of durable bikes stationed throughout Chicago and Evanston, accessible to users through **Annual Memberships** or **Passes** via the Divvy App or kiosks.

Divvy is available **24/7**, **365 days a year**, offering an ideal solution for activities such as commuting, running errands, or leisurely exploring the city. Riders can unlock and return bikes at any station within the network, providing freedom and flexibility across the extensive system.

For more details, visit [Divvy Bikes Website](https://divvybikes.com/about).

***

## Repository Contents:

- **datasets**: This folder contains the .CSV dataset files used for this analysis.
- **img**: This folder contains all images used in this project.
- **.gitignore**: Specifies which files and directories should be ignored by Git when committing changes to a repository.
- [**project.ipynb**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/project.ipynb): This notebook contains the full analysis, including data cleaning, data visualization, and data analysis.
- [**analysis.ipynb**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/analysis.ipynb): This notebook contains the data analysis portion of the project.
- [**divvy_trips.db**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/divvy_trips.db): This SQLite database file contains a table with Q1 data as a sample. A full-year database is generated when the project notebook is executed, due to GitHub's size limitations.
- [**splitlargefile.py**](https://github.com/Galal-Abdelaziz/PFDA-project/blob/main/splitlargefile.py): This file contains the script I used to split large CSV files into smaller ones due to the limitations of GitHub.
- **README.md**: Contains information about the repository, including its purpose, structure, and usage instructions.
- **requirements.txt**: Specifies the Python packages required to run the project.

***

## Analysis Objectives

This project aims to analyze the Divvy trip data to gain insights into city-wide biking trends. The following objectives will be addressed:

1. **Determine total trips**: Calculate the total number of Divvy trips that occurred.
2. **Bike utilization**: Identify the number of bikes utilized during the period.
3. **Frequent usage**: Determine which bikes were most frequently used for trips.
4. **Trip duration**: Calculate the average trip duration based on user types (e.g., customers and subscribers).
5. **Popular stations**: Identify the most popular start and end stations for Divvy trips and analyze the most popular routes taken by Divvy Bikes users.
6. **Least popular stations**: Identify the least popular start and end stations for Divvy trips and analyze the least popular routes taken by Divvy Bikes users.
7. **User division**: Examine how Divvy Bikes usage is divided between customers and subscribers.
8. **Gender usage**: Determine whether Divvy Bikes are used more by female or male users.
9. **Age demographics**: Analyze the age distribution of Divvy Bikes users.
10. **Peak usage**: Identify the peak times during which Divvy Bikes are most frequently used.
11. **Weekly patterns**: Analyze Divvy Bikes usage patterns by day of the week.
12. **Monthly trends**: Analyze the number of riders per month by quarter for the year 2019.

By addressing these questions, the project seeks to provide actionable insights to optimize and enhance the bike-sharing system's services and infrastructure.

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

## Running the program:

1. Clone the repository using the following command: `git clone https://github.com/Galal-Abdelaziz/PFDA-project.git`
2. Navigate into the project directory: `cd PFDA-project`
3. Install the required packages by running `pip install -r requirements.txt` in the terminal.
4. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```
5. Launch Jupyter Notebook or Visual Studio Code:
    - To launch Jupyter Notebook, run `jupyter notebook` in the terminal. This will open a new tab in your web browser showing the available notebooks.
    - To use Visual Studio Code, ensure the Python and Jupyter extensions are installed. Then, open the project folder in VS Code (`code .` in the terminal), and open the `.ipynb` files for interactive editing.
6. Open and run `project.ipynb` to generate the full database file and perform comprehensive data analysis, including:
   - Data cleaning, inspection, and visualization
   - Coding and analysis
7. Open `analysis.ipynb` to view the plots and summary of the data analysis.
8. Ensure you have SQLite installed to connect to the `divvy_trips.db` database. You can use SQLite or any other compatible database viewer to interact with the database file.

***

## Resources:

**Weekly Lectures**

**Understanding the Dataset:**
- [**Divvy Trip Data**](https://divvy-tripdata.s3.amazonaws.com/index.html)
- [**Divvy Kaggle Dataset**](https://www.kaggle.com/datasets/mdmasumomarjashim/divvy-trips-data-20192020)
- [**Divvy Data Cleaning and Analysis Blog**](https://medium.com/@gbemuduazubuike/)
- [**Divvy Data Cleaning with R**](divvy-bikes-an-exercise-on-data-cleaning-and-analysis-of-cycling-data-using-r-programming-language-c38e8a4521ef)

**Data Preparation:**
- [**Date Formatting with Pandas**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
- [**Setting DataFrame Index**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
- [**Handling Missing Values in Python**](https://community.sisense.com/t5/knowledge-base/dealing-with-missing-values-in-python/ta-p/9376)

**Calculations:**
- [**Pandas Resampling**](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#resampling)
- [**Calculating Mean with Pandas**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)
- [**Calculating Max with Pandas**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html)
- [**DataFrame Filtering/Indexing**](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing)
- [**Handling DateTime Index**](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset)

**Plotting:**
- [**Matplotlib Figure Creation**](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
- [**Matplotlib Plot Function**](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [**Matplotlib Axes API**](https://matplotlib.org/stable/api/axes_api.html)

**Handling Multiple Datasets:**
- [**Combining Datasets**](https://stackoverflow.com/questions/77532900/concatenating-multiple-data-frames-in-python)
- [**Splitting Large Datasets**](https://dev.to/benjaminrancourt/how-to-split-a-large-csv-file-based-on-the-number-of-rows-312o)

**Database:**
- [**SQLite Python Tutorial**](https://www.sqlitetutorial.net/sqlite-python/)
- [**Python SQLite3 Documentation**](https://docs.python.org/3/library/sqlite3.html)
- [**SQL Basics**](https://www.w3schools.com/sql/)

**SciKit-Learn (Machine Learning):**
- [**StandardScaler for Feature Scaling**](https://scikit-learn.org/0.24/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [**KMeans Clustering**](https://scikit-learn.org/0.19/modules/generated/sklearn.cluster.KMeans.html)
- [**Principal Component Analysis (PCA)**](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.PCA.html)


## Disclaimer:

This repository includes content created with the assistance of an AI chat assistant. While the AI has provided valuable insights, code, and text generation, all content has been reviewed, modified, and verified by the repository's author to ensure accuracy and relevance.

***

## End