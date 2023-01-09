import pyarrow as pa
import pyarrow.parquet as pq

# Load the iris dataset from a parquet file
iris_dataset = pq.read_table("iris.parquet")

# Get the metadata for the dataset
schema = iris_dataset.schema

schema = pa.schema(
    [
        pa.field(
            "sepal_length",
            "double",
            metadata={"description": "The length of the sepal in centimeters"},
        ),
        pa.field(
            "sepal_width",
            "double",
            metadata={"description": "The width of the sepal in centimeters"},
        ),
        pa.field(
            "petal_length",
            "double",
            metadata={"description": "The length of the petal in centimeters"},
        ),
        pa.field(
            "petal_width",
            "double",
            metadata={"description": "The width of the petal in centimeters"},
        ),
        pa.field(
            "species",
            "string",
            metadata={"description": "The species of the iris plant"},
        ),
    ],
    metadata={"Dataset Description": "The iris dataset"},
)

iris_dataset = iris_dataset.cast(schema)
pq.write_table(iris_dataset, "iris_with_metadata.parquet")


iris_dataset_md = pq.read_table("iris_with_metadata.parquet")
iris_dataset_md.schema
