# Data Modeling

<!-- topics 
3rd nf vs star schema
surrogate keys or no surrogate keys
index
-->

## Gather Business Requirements and Data Realities
Understand needs of business and realities of underlying source data. 
Uncover requirements of key performance indicators, compelling business issues, decision-mkaing processes and analytics needs.

## Four-Step Dimensional Design Process
1. Select the business process
2. Declare the grain
3. Identity the dimensions - "who, what, where, when, why, how"
4. Identify the facts - observable event

## Fact Tables
A fact table contains the numeric measures produced by an operational measurement event in the real world. At the lowest grain, a fact table row corresponds to a
measurement event and vice versa. 

Nulls should be avoid in a fact table's foreign keys.

### Conformed Facts
Identical measurement across different fact tables. If business calculation is same, then conformed facts should be named the same.

### Transaction Fact Tables
A row in a transaction fact table corresponds to a measurement event at a point in
space and time. 

### Periodic Snapshot Fact Tables
A row in a periodic snapshot fact table summarizes many measurement events occurring over a standard period, such as a day, a week, or a month. The grain is the period, not the individual transaction.

### Accumulating Snapshot Fact Tables
A row in an accumulating snapshot fact table summarizes the measurement events occurring at predictable steps between the beginning and the end of a process. 

|                     | Transaction                               | Periodic Snapshot                                     | Accumulating Snapshot                                  |
|---------------------|-------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| Periodicity         | Discrete transaction point in time        | Recurring snapshots at regular, predictable intervals | Indeterminate time span for evolving pipeline/workflow |
| Grain               | 1 row per transaction or transaction line | 1 row per snapshot period plus other dimensions       | 1 row per pipeline occurrence                          |
| Date dimension(s)   | Transaction date                          | Snapshot date                                         | Multiple dates for pipeline’s key milestones           |
| Facts               | Transaction performance                   | Cumulative performance for time interval              | Performance for pipeline occurrence                    |
| Fact table sparsity | Sparse or dense, depending on activity    | Predictably dense                                     | Sparse or dense, depending on pipeline occurrence      |
| Fact table updates  | No updates, unless erorr correction       | No updates, unless error correction                   | Updated whenever pipeline activity occurs              |

### Factless Fact Tables
A factless fact table is a fact table that does not have any measures. It is essentially an intersection of dimensions (it contains nothing but dimensional keys). There are two types of factless tables: One is for capturing an event, and one is for describing conditions.

## Dimension Tables
Stores attributes, or dimensions, that describe the objects in a fact table.

### Surrogate Keys
Primary key of dimension table, and is embedded as a foregin key in associated fact table

* Buffer the data warehouse from operational changes.
* Integrate multiple source systems.
* Improve performance.
* Handle null or unknown conditions.
* Support dimension attribute change tracking.

### Degenerate Dimension (DD)
Key in fact table without related dimension. Provides grouping and business meaning.

### Null Attributes in Dimensions
Null-valued dimension attributes result when a given dimension row has not been
fully populated, or when there are attributes that are not applicable to all the dimension’s rows. In both cases, we recommend substituting a descriptive string, such as
Unknown or Not Applicable in place of the null value. Nulls in dimension attributes
should be avoided because diff erent databases handle grouping and constraining
on nulls inconsistently

### Role-Playing Dimensions
A single physical dimension can be referenced multiple times in a fact table, with
each reference linking to a logically distinct role for the dimension. For instance, a
fact table can have several dates, each of which is represented by a foreign key to the
date dimension.