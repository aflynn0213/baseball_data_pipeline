from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("StuffPlusModel") \
        .getOrCreate()

    # Load data from PostgreSQL
    db_properties = {
        "user": "username",
        "password": "password",
        "driver": "org.postgresql.Driver"
    }
    url = "jdbc:postgresql://localhost:5432/baseball"
    query = "(SELECT pitch_type, release_speed, release_spin_rate, pfx_x, pfx_z, run_value FROM processed_statcast WHERE run_value IS NOT NULL) as statcast_data"

    df = spark.read.jdbc(url=url, table=query, properties=db_properties)

    # Feature engineering
    assembler = VectorAssembler(
        inputCols=["release_speed", "release_spin_rate", "pfx_x", "pfx_z"],
        outputCol="features"
    )
    df = assembler.transform(df)

    # Train-Test Split
    train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

    # Train the model
    lr = LinearRegression(featuresCol="features", labelCol="run_value")
    model = lr.fit(train_data)

    # Save the model
    model.save("models/stuff_plus_model")

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()
