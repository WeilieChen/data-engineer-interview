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

### Nulls should be avoid in a fact table's foreign keys.

### Conformed Facts
Identical measurement across different fact tables. If business calculation is same, then conformed facts should be named the same.