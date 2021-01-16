# AdventureWorks-ELTL
## Objective
Create metadata driven ELTL architecture using Azure Data Factory

## Dataset
Sample AdventureworksLT database loaded to SQL database

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/adventureworkslt.png)

## Data ingestion
![](insert pipeline here)

## Data tranformation
![](insert pipeline here)

## Steps
- Get metadata from SQL database
- Copy data to Raw layer of data lake based on metadata
- Clean data in productionalized Databricks notebook 
  - create schema
  - handle nulls
  - write in parquet format to the Structured layer of the data lake
- Used data flows to denormalize the tables
- Loaded transformed data to the Curated layer of the data lake

## Data Lake Architecture
![](insert screenshot here)

- Raw_data: Data is copied from original format

- Structured_data: Schema and data types are defined, nulls are handled, unnecessary columns are removed, and format is standardized

- Curated_data: This layer is optimised for analytics so data is denormalized in star schema

![](insert data model here)
