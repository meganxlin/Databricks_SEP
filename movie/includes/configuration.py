# Databricks notebook source
username = 'meganxlin'

myPath = f"/dbfs/FileStore/tables/movie/"

rawPath = myPath + "raw/"
bronzePath = myPath + "bronze/"
silverPath = myPath + "silver/"
silverQuarantinePath = myPath + "silverQuarantine/"
goldPath = myPath + "gold/"

# COMMAND ----------

spark.sql(f"CREATE DATABASE IF NOT EXISTS moviebricks_{username}")
spark.sql(f"USE moviebricks_{username}")

# COMMAND ----------

# MAGIC %run ./utilities

# COMMAND ----------


