# Data Engineer Interview Cheat Sheet

Contains curated list of questions and topic relating to a Data Engineer Interview

# Table of Contents
- [Data Warehousing](data-warehousing)

# <a id="data-warehousing"></a>Data Warehousing

## OLTP vs OLAP

### OLTP - Online Transaction Processing
* Day to day operation of an application.
* One thing at a time.
* Optimized for inserts and updates.
* Uses just the current state.

### OLAP - Online Analytical Processing
* Online query and analsis of business entities. 
* Aggregations and questioning of many things at a time.
* Optimized for heavy reads.
* Needs history to track business progression over time.

## Star Schema

### Dimension
* "By" what we measure things?
* The who, what when, where of things.
* Examples: Dates, Products, Countries

#### Slowly Changing Dimension
* Type 1: Override the data. Doesn't track dimension history.
* Type 2: Add new record for the new data, mark the old one inactive with inactivation date.
* Type 3: Maintain multiple columns of of changed values.

### Fact
* An observation or event.
* Something to bemeasured.
* Examples: Customer Payment, User Logins, Product Orders.

### Grain
* Determines what each fact row contains and in what detail.

### Surrogate  Key
* The dimensions PK should be in control of the OLAP system.
* Dimensions may come from multiple sources, synchronizing the PK system is an unnecessary headache.
* Decouple OLTP system from OLAP system.
