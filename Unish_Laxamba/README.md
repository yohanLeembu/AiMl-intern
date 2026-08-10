# Month 1

# Week 1: Python Fundamentals & File I/O

Welcome to **Week 1** of the internship/learning roadmap! This folder contains foundational Python scripts focusing on core programming concepts, control flow, functions, error handling, and simple file manipulation.

---

## Repository Structure

```text
Month_1/Week_1/
├── Text_Files/          # Folder storing input/output .txt files
├── Basic_Calculator.py  # Interactive CLI calculator with error handling
├── File_Parser.py       # Custom text file parser converting raw data to structured formats
├── Python_Basic.py      # Basic Python exercises & File I/O tasks
└── To_Do_List.py        # CLI-based task management application

```

# Task Summaries

Python_Basic.py: Exercises covering variables, loops, conditionals, and basic file read/write operations.

Basic_Calculator.py: An interactive CLI calculator with try-except error handling for safe math operations.

File_Parser.py: A custom parser that reads raw text files and converts them into structured dictionaries.

To_Do_List.py: A simple terminal-based application to add, view, and manage daily tasks.

# Week 2: Data Handling with NumPy & Pandas

## Overview

This week focused on the fundamentals of **NumPy** and **Pandas** for numerical computing and data handling in Python.

The main goal was to learn how to work with arrays and tabular datasets, clean raw data, and prepare it for analysis.

## Learning Goals

- Understand the difference between Python lists and NumPy arrays.
- Learn why NumPy is useful for numerical operations.
- Load and inspect tabular datasets using Pandas.
- Handle missing and inconsistent data.
- Filter and transform DataFrame data.
- Use `groupby()` for aggregation and analysis.
- Merge multiple datasets.
- Create pivot tables.
- Convert a messy raw dataset into an analysis-ready dataset.

## Tasks Completed

### 1. NumPy Exercises

Completed exercises covering:

- Creating NumPy arrays
- Accessing and indexing array elements
- Slicing arrays
- Performing vectorized mathematical operations
- Broadcasting
- Understanding the advantages of NumPy arrays over regular Python lists

### 2. Loading a Dataset with Pandas

Loaded a CSV dataset into a Pandas DataFrame and practiced basic data inspection, including:

- Viewing the first and last rows
- Checking the shape of the dataset
- Inspecting column names
- Checking data types
- Identifying missing values
- Generating basic descriptive statistics

### 3. Data Cleaning

Practiced preparing raw data for analysis by:

- Detecting missing values
- Handling missing values
- Removing unnecessary or duplicate records
- Correcting data types
- Renaming columns where necessary
- Creating a cleaner and more consistent DataFrame

### 4. Filtering and Transforming Data

Practiced selecting useful information from the dataset by:

- Filtering rows based on conditions
- Selecting specific columns
- Creating new columns
- Transforming existing columns
- Sorting data

### 5. GroupBy

Used Pandas `groupby()` to summarize and analyze data by categories.

Examples included calculating:

- Mean
- Count
- Sum
- Other aggregate statistics

### 6. Merging Data

Practiced combining related DataFrames using Pandas merge operations such as:

- Inner merge
- Left merge
- Right merge

This helped demonstrate how separate datasets can be combined using common columns.

### 7. Pivot Tables

Created Pandas pivot tables to summarize data across multiple categories and make patterns easier to analyze.

### 8. Data Cleaning Script

Created a cleaning workflow that converts a messy raw dataset into an analysis-ready dataset.

The workflow includes:

```text
Raw Dataset
     ↓
Load Data
     ↓
Inspect Data
     ↓
Handle Missing Values
     ↓
Remove Duplicates / Unnecessary Data
     ↓
Correct Data Types
     ↓
Filter and Transform
     ↓
Clean Dataset
     ↓
Ready for Analysis
```

## Deliverable

The completed Jupyter Notebook demonstrates the complete process:

**Raw Dataset → Data Inspection → Cleaning → Transformation → Clean Dataset**

Comments have been included throughout the notebook to explain the purpose of the major steps.

## Tools Used

- Python
- NumPy
- Pandas
- Jupyter Notebook

## Key Takeaways

By completing Week 2, I practiced the core skills required to work with numerical and tabular data in Python. I learned how NumPy can efficiently perform numerical operations and how Pandas can be used to load, clean, transform, summarize, and prepare datasets for further analysis and machine learning.

# Week 3 – Data Visualization & Statistics Basics

## Overview

Week 3 focused on **data visualization, descriptive statistics, and exploratory data analysis (EDA)** using the cleaned dataset from Week 2.

## Learning Goals

- Visualize distributions, relationships, and trends.
- Understand mean, median, mode, variance, and standard deviation.
- Understand and interpret correlation.
- Use visualizations to identify patterns in data.

## Tasks Completed

### 1. Data Visualization

Created visualizations using **Matplotlib** and **Seaborn**, including:

- Histograms to understand data distributions
- Box plots to identify spread and potential outliers
- Scatter plots to examine relationships between variables
- Heatmaps to visualize correlations between numerical features

### 2. Exploratory Data Analysis (EDA)

Performed EDA on the cleaned Week 2 dataset by:

- Inspecting important columns and their distributions
- Calculating descriptive statistics
- Examining relationships between variables
- Checking for patterns and potential outliers

### 3. Statistical Analysis

Calculated and interpreted basic statistics, including:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Correlation

### 4. Key Insights

Identified **3–5 important patterns and insights** from the dataset based on the statistical analysis and visualizations.

## Deliverable

Completed a short **EDA report/notebook** containing:

**Clean Dataset → Statistical Analysis → Visualizations → Key Insights**

The notebook includes charts and written explanations of the main findings.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Key Takeaway

This week provided practical experience in using statistics and visualizations to understand a dataset, identify relationships and trends, and communicate meaningful insights before moving on to further analysis or machine learning.
