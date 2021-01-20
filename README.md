# AdventureWorks-ELTL
## Objective
Create metadata driven ELTL architecture using Azure Data Factory. 
- Connected to OLTP database, performed lookup on the metadata, ingested the data by extracting tables from database based on metadata then copying it to the raw layer of data lake, cleaned the data and wrote it to the structured layer of the data lake, then denormalized the data and wrote it to the curated layer of data lake.

## Dataset
Sample AdventureworksLT database loaded to SQL database

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/adventureworkslt.png)

## Data ingestion and tranformation

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/DataIngestion.png)

- Set up linked service for SQL database
- Created a dataset for SQL database
- Created Lookup activity for list of tables using query
- Set up linked service for Azure Data Lake Storage Gen 2
- Created a dataset for SQL database with parameters 
- Created a dataset for Azure Data Lake Storage with parameters that pass values from Lookup activity
- Set up For Each activity that exports SQL database tables to Raw layer of data lake
- Set up For Each activity for Databricks notebooks with parameters
- Registered Databricks in Azure Acitve Directory
- Set up linked service for Azure Databricks
- Cleaned data in productionalized Databricks notebook 
  - configured connection to Azure Data Lake Storage Gen 2
  - created schema
  - removed rows that contain all NULLs
  - wrote in parquet format to the Structured layer of the data lake
- Created Data Flow activity to denormalize the tables using joins
- Loaded transformed data to the Curated layer of the data lake

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/DataTransform.png)


## Data Lake Architecture

- raw_data: Data is copied from original format

- structured_data: Schema and data types are defined, NULLs are handled, and format is standardized

- curated_data: This layer is optimised for analytics so data is denormalized in star schema

![](https://github.com/smithashley/Adventureworks-ELTL/blob/main/images/datamodeldiagram.png)
