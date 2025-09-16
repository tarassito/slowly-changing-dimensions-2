# Slowly Changing Dimensions (SCD) Type 2

This repository contains experiments and implementations of Slowly Changing Dimensions (SCD) Type 2 using Apache Spark and Delta Lake.

## What is SCD Type 2?

SCD Type 2 is a data warehousing technique that maintains a complete history of changes to dimension data. When a dimension attribute changes, instead of updating the existing record, a new record is created with:
- The new attribute values
- A start date (when the change became effective)
- An end date (when the change was superseded)
- A flag indicating if it's the current record

## Repository Contents

- **`src/1.basic-implementation.ipynb`** - Basic SCD Type 2 implementation with Delta Lake merge operations
- **`src/helpers.py`** - Spark session initialization utilities
- **`src/schemas.py`** - Data schemas for target and incoming data

## Development Environment

This repository includes a devcontainer configuration with:
- Python 3.12.3
- Apache Spark 3.4.4
- Delta Lake 2.4.0
- OpenJDK 17
- Jupyter notebook support

The devcontainer is pre-configured to run Spark locally with Delta Lake extensions, making it easy to experiment with SCD Type 2 implementations.

## Getting Started

1. Open the repository in a devcontainer-enabled environment (VS Code with Dev Containers extension)
2. Run the notebooks in `src/` to see basic SCD Type 2 implementation
