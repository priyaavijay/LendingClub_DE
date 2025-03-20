# Lending Club Data Engineering Project Using PySpark
![Alt Text](https://github.com/priyaavijay/LendingClub_DE/blob/main/Workflow%20Diagram.png)

# Overview

This project focuses on analyzing and transforming Lending Club data using PySpark. It includes data cleaning, processing, and risk assessment to support financial decision-making.


# Data Engineering Workflow

# Data Sources:

**Customers Data:** Member details (e.g., income, employment, credit status).

**Loans Data:** Loan-related information.

**Loan Repayments:** Payment history.

**Loan Defaulters:** Risk assessment metrics.

# Data Cleaning & Processing:

Convert data types.

Rename columns.

Handle missing values.

Normalize address fields.

Deduplicate records.

Store cleaned data in HDFS.
Store cleaned data in Parquet format with Snappy compression for efficient storage and retrieval.
The output data is written in data/output/results.parquet, ensuring optimized performance.

# PySpark Environment Setup

**Environment Management:**
Use Pipenv to manage dependencies:

pipenv shell  # Activate environment
pipenv install  # Install dependencies
pipenv uninstall <package>  # Uninstall a package
pipenv --rm  # Remove the environment

PyEnv for managing Python versions.
ConfigReader.py -- Loads configuration settings.
DataReader.py -- Handles data ingestion.

# Unit Testing

Used pytest for unit tests.

Logging in Apache Spark

Used Log4j for efficient logging instead of print statements.

Log levels: DEBUG < INFO < WARN < ERROR < FATAL

log4j.properties

log4j.rootLogger=WARN, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n
