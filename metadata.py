import pyarrow as pa
import pyarrow.parquet as pq

# Load the iris dataset from a parquet file
iris_dataset = pq.read_table("iris.parquet")

# Get the metadata for the dataset
schema = iris_dataset.schema


# Add descriptions for each column in the dataset
schema[0].with_metadata({"description": "The length of the sepal in centimeters"})
schema[1].with_metadata({"description": "The width of the sepal in centimeters"})
schema[2].with_metadata({"description": "The length of the petal in centimeters"})
schema[3].with_metadata({"description": "The width of the petal in centimeters"})
schema[4].with_metadata({"description": "The species of the iris plant"})

# Save the updated dataset to a new parquet file
pq.write_table(iris_dataset, "iris_with_metadata.parquet")
