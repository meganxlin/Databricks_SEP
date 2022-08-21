# Databricks notebook source
# MAGIC %run ./includes/configuration

# COMMAND ----------

display(dbutils.fs.ls(rawPath))

# COMMAND ----------

dbutils.fs.rm(bronzePath, recurse=True)

# COMMAND ----------

rawDF = ingest_batch_raw(rawData).cache()

# COMMAND ----------


