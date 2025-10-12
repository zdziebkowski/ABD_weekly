from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spotify-test").getOrCreate()

df = spark.range(0, 5).withColumnRenamed("id", "n")
df.show()

#df.write.mode("overwrite").parquet("out/parquet_demo")
print("✅ Zapisano plik Parquet do folderu 'out/parquet_demo'")

spark.stop()
