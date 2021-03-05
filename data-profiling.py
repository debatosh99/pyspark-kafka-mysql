#!/usr/bin/env python
# coding: utf-8

import os
os.environ['SPARK_HOME'] = 'G:\softwares\spark-3.0.1\spark-3.0.1-bin-hadoop2.7'
import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()



spark_df = spark.read.format("csv").option("header", "true").load("G:\projects\pandas-master\pokemon_data.csv")

spark_df.show(10)


spark_df.describe()


pandas_df1 = df.toPandas()

pandas_df1.columns

pandas_df1.describe()

pandas_df2 = pandas_df1.describe()

print(type(pandas_df2))

pandas_df2

pandas_df2.info()

pandas_df3 = pandas_df2.transpose()

pandas_df3

pandas_df4 = pandas_df3.iloc[1:]

pandas_df4

pandas_df4['col_names'] = pandas_df4.index
pandas_df4

pandas_df5 = pandas_df4.reset_index()

pandas_df6 = pandas_df5.drop(['index'], axis=1)

pandas_df6

pandas_df6.info()

pandas_df6.to_csv("G:\projects\pandas-master\output.csv")

from pyspark.sql.types import *

custom_schema = StructType([
     StructField("count",StringType(),True),
     StructField("unique",StringType(),True),
	 StructField("top",StringType(),True),
     StructField("freq",StringType(),True),
     StructField("col_names",StringType(),True)
])


from pyspark.sql import SQLContext

spark.createDataFrame(pandas_df6, schema=custom_schema).show(10)

spark_df6 = SQLContext.createDataFrame(data=pandas_df6, schema=custom_schema)

print(type(spark_df6))




