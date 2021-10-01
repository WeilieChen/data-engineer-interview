What is the difference between partition key, primary key, foreign key?
* Primary Key is one or more columns used to identiy a row.
* Partition Key is reponsible for data distribution across nodes. It determines which node will store a given row.
* Foreign Key is a column or set of columns in a table whose values correspond to the values of the primary key in another table.

What is the difference between a Type 1 and Type 2 dimension?
* Type 1: Update the column to newest record.
* Type 2: Insert a new row to identiy new record.

Which is more efficient, UNION or UNION ALL?
* Union All, because it doesn't remove duplicate records. Avoids an expensive distinct sort.

What is indexing?
A database index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index data structure.

View vs Materialized View?
* Views are virtual only and run the query definition each they are accessed.
* Materialized Views are disk based and are updated periodically based upon the query definition.