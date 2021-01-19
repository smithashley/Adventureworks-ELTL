# AdventureWorks-ELTL
## Objective
Create metadata driven ELTL architecture using Azure Data Factory

## Dataset
Sample AdventureworksLT database loaded to SQL database

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/adventureworkslt.png)

## Data ingestion and tranformation
![](insert pipeline here)

- Set up linked service for SQL database
- Create a dataset for SQL database
- Lookup list of table using query
- Set up linked service for Azure Data Lake Storage Gen 2
- Create a dataset for SQL database with parameters
- Create a dataset for Azure Data Lake Storage with parameters
- Set up For Each activity that exports SQL database tables to Raw layer of data lake
- Clean data in productionalized Databricks notebook 
  - create schema
  - handle nulls
  - write in parquet format to the Structured layer of the data lake
- Used data flows to denormalize the tables
- Loaded transformed data to the Curated layer of the data lake

![](insert pipeline here)


## Data Lake Architecture
![](insert screenshot here)

- Raw_data: Data is copied from original format

- Structured_data: Schema and data types are defined, nulls are handled, and format is standardized

- Curated_data: This layer is optimised for analytics so data is denormalized in star schema

![](insert data model here)
