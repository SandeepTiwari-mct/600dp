# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d9e3def0-8f4e-44d3-a2f3-89dec515f0b9",
# META       "default_lakehouse_name": "lkh1",
# META       "default_lakehouse_workspace_id": "c259803c-057e-48c2-8ec1-9686119c1ab7",
# META       "known_lakehouses": [
# META         {
# META           "id": "d9e3def0-8f4e-44d3-a2f3-89dec515f0b9"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/orders.csv")
# df now is a Spark DataFrame containing CSV data from "Files/orders.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

null

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
