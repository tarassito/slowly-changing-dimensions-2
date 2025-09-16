from pyspark.sql.types import StructType, StructField, BooleanType, StringType, IntegerType


target_table_schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("address", StringType()),
    StructField("start_date", StringType()),
    StructField("end_date", StringType()),
    StructField("is_current", BooleanType())
])

incoming_updates_schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("address", StringType()),
    StructField("start_date", StringType()),
])