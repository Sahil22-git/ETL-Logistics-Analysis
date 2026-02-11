#  E-commerce ETL Pipeline & Logistics Analytics

##  Project Overview

This project builds an complete **ETL pipeline** using Python and MySQL to analyze e-commerce logistics performance.

The pipeline extracts raw datasets, transforms and cleans the data and loads it into a MySQL database for business analytics.

The goal is to simulate a real world data analyst workflow and generate insights about delivery performance and customer behavior.

---

## Tools & Technologies

* Python (Pandas, SQLAlchemy)
* MySQL
* VS Code
* Git & GitHub

---

##  ETL Pipeline Architecture

Raw CSV Files → Extract → Transform → Load → MySQL Database

###  Extract

* Reads multiple raw datasets
* Structured folder organization

###  Transform

* Missing value analysis
* Duplicate removal
* Date conversion
* Dataset merging

###  Load

* Cleaned data loaded into MySQL
* Ready for SQL analytics

---

##  Business Analytics Performed

Using SQL queries to answer real-world questions:

* Monthly order growth trends
* Delivery performance analysis
* City wise logistics performance
* Order status distribution
* Time based analytics

---

##  Project Structure

```
ETL_projects/
│
├── Data/
│   └── Raw/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
└── README.md
```

---

##  How to Run the Project

1. Install dependencies:

```
pip install pandas sqlalchemy pymysql
```

2. Create MySQL database:

```
CREATE DATABASE etl_project;
```

3. Run pipeline:

```
python main.py
```

---

##  Key Skills Demonstrated

* ETL pipeline design
* Data cleaning & transformation
* SQL analytics
* Database integration
* Project structuring

---

