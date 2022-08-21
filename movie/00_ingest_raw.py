# Databricks notebook source
#%run ./includes/configuration

# COMMAND ----------

#%run ./includes/utilities

# COMMAND ----------

dbutils.fs.rm(myPath, recurse=True)

# COMMAND ----------

display(dbutils.fs.ls(rawPath))

# COMMAND ----------

rawDF = ingest_batch_raw(rawData).cache()

# COMMAND ----------

display(rawDF)

# COMMAND ----------

print(dbutils.fs.head
         (dbutils.fs.ls("dbfs:/mnt/movieShop/raw")[0].path)
     )

# COMMAND ----------

rawDF.printSchema()
