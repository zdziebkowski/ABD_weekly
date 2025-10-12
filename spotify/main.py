from typing import Dict, List, Tuple
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import StructType

def create_spark_session(app_name: str = "SpotifyDataProcessing") -> SparkSession:
    """Create and return a Spark session."""
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.executor.memory", "2g")
        .getOrCreate()
    )

    print(f"Spark session created: {app_name}")

    return spark

def load_data(spark: SparkSession, file_path : str) -> DataFrame:
    """Load data from a CSV file into a Spark DataFrame."""
    df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(file_path)
    )

    print(f"Data loaded from {file_path}")

    return df