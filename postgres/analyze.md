# Collecting statistics about your database with `ANALYZE` 

## Links 

- [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html)

## Notes 

From the docs: 

> ANALYZE collects statistics about the contents of tables in the database, and stores the results in the pg_statistic system catalog. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries.

> **Without a table_and_columns list, ANALYZE processes every table and materialized view in the current database** that the current user has permission to analyze. With a list, ANALYZE processes only those table(s). It is further possible to give a list of column names for a table, in which case only the statistics for those columns are collected. (_emphasis added_)

> When the option list is surrounded by parentheses, the options can be written in any order. The parenthesized syntax was added in PostgreSQL 11; the unparenthesized syntax is deprecated.

```
ANALYZE [ ( option [, ...] ) ] [ table_and_columns [, ...] ]
ANALYZE [ VERBOSE ] [ table_and_columns [, ...] ]

where option can be one of:

    VERBOSE [ boolean ]
    SKIP_LOCKED [ boolean ]
    BUFFER_USAGE_LIMIT size

and table_and_columns is:

    table_name [ ( column_name [, ...] ) ]

```

Apparently, it was once a best practice to run ANALYZE after indexing the database, but in general that's not necessary due to updates in Postgres. 

I've never used this myself, but learned about it in passing and wanted to document it. 
