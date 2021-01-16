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

## Data Model of Transformed data
![](insert data model here)
