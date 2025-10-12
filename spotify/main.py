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
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("encoding", "UTF-8")
        .csv(file_path)
    )

    print(f"Data loaded from {file_path}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"Columns: {df.columns}")

    return df

def explore_data(df: DataFrame, num_rows: int = 5) -> None:
    """Display the schema and a few rows of the DataFrame. Display description."""
    df.printSchema()
    df.show(num_rows, truncate=False)
    numeric_cols = ["skip_rate", "songs_played_per_day", "listening_time", "age"]
    df.select(numeric_cols).describe().show()

def get_subscription_distribution(df: DataFrame, subscription_column: str = "subscription_type") -> DataFrame:
    """Get the distribution of users by subscription type."""
    total_users = df.count()

    distribution = (
        df.groupBy(subscription_column)
        .agg(
            F.count("*").alias("count")
        )
        .withColumn("percentage", F.round((F.col("count") / total_users) * 100, 2))
        .orderBy(F.col("count").desc())
    )
    
    return distribution

def compare_by_subscription(df: DataFrame, subscription_col: str, metric_columns: List[str]) -> DataFrame:
    """Compare average, median, min, max, and stddev of specified metrics by subscription type."""
    agg_expressions = []
    
    for metric in metric_columns:
        agg_expressions.extend([
            F.avg(metric).alias(f"{metric}_avg"),
            F.expr(f"percentile_approx({metric}, 0.5)").alias(f"{metric}_median"),
            F.min(metric).alias(f"{metric}_min"),
            F.max(metric).alias(f"{metric}_max"),
            F.stddev(metric).alias(f"{metric}_stddev")
        ])
    
    comparison = (
        df.groupBy(subscription_col)
        .agg(*agg_expressions)
    )
    
    return comparison

def calculate_skip_rate(df: DataFrame, skips_col: str, songs_col: str) -> DataFrame:
    """Calculate the skip rate as a percentage of skipped songs to total songs."""
    df_with_skip_rate = df.withColumn(
        "skip_rate",
        F.round((F.col(skips_col) / F.col(songs_col)) * 100, 2)
    )
    
    return df_with_skip_rate

def main() -> None:
    """Main function to execute the data processing and analysis."""
    spark = create_spark_session("Spotify_Analysis")
    
    file_path = "csv/spotify_churn_dataset.csv"
    df = load_data(spark, file_path)
    
    explore_data(df, num_rows=10)
    
    dist_df = get_subscription_distribution(df, subscription_column="subscription_type")
    dist_df.show(truncate=False)
     
    metrics = ["skip_rate", "songs_played_per_day", "listening_time"]
    comparison = compare_by_subscription(
        df, 
        subscription_col="subscription_type", 
        metric_columns=metrics
    )
    comparison.show(truncate=False)
    
    spark.stop()


if __name__ == "__main__":
    main()