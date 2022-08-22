# Databricks notebook source
# MAGIC %run ./includes/configuration

# COMMAND ----------

# MAGIC %run ./includes/utilities

# COMMAND ----------

dbutils.fs.rm(myPath, recurse=True)

# COMMAND ----------

display(rawDF)

# COMMAND ----------

print(dbutils.fs.head
         (dbutils.fs.ls("dbfs:FileStore/tables/movie_0.json/")[0].path)
     )

# COMMAND ----------

rawDF.printSchema()
