# Databricks notebook source
#setup the configuration for Azure Data Lake Storage Gen 2
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "f62b9429-c55e-4ba4-bb93-bdfa4c0934b3",
           "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="keyvaultscope",key="keyvaultdatabricks1"),
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/e5eaa9eb-6662-451d-ab83-b25dc3376b45/oauth2/token"}

dbutils.fs.mount(
  source = "abfss://data@adwdatalake.dfs.core.windows.net/",
  mount_point = "/mnt/adwdatalake",
  extra_configs = configs)

# COMMAND ----------

#Unmounting when finished
dbutils.fs.unmount("/mnt/adwdatalake")
