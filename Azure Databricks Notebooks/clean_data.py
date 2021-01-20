# Databricks notebook source
#Creating widgets for leveraging parameters to be passed from Azure Data Factory

dbutils.widgets.text("filename", "","") 
dbutils.widgets.get("filename")

# COMMAND ----------

# Read in raw data and infer schema
inputPath = "/mnt/adwdatalake/raw_data/SalesLT."+getArgument("filename")+".csv"

df = spark.read.option("header", "True").option("delimiter", ",").option("inferSchema", "True").csv(inputPath)

# COMMAND ----------

#Delete rows that are all NULLs
cleanDF=df.na.drop(how="all")

# COMMAND ----------

#Write data to Structured layer of data lake
outputPath = "/mnt/adwdatalake/structured_data/SalesLT."+getArgument("filename")

showDF=cleanDF.write.mode("overwrite").format("delta").option("header", "true").save(outputPath)
