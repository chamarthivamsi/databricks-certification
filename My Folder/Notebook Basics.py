# Databricks notebook source
print("Hello world!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hellow world from sql"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1 
# MAGIC ## Titile 2
# MAGIC ### Title 3

# COMMAND ----------

# MAGIC %run ../demo/SecondNotebook
# MAGIC

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets/'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')
display(files)

# COMMAND ----------


