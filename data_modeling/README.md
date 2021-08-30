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