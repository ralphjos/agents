# Birst JDBC Connection Pool

## Summary
Ralph Arroyo introduced a JDBC connection pool at Birst. The pool supplies database connections used to query customer data warehouses and populate Birst dashboards. Dashboard queries are frequent, so reusing connections avoids the cost of repeatedly creating and destroying database connections and improves dashboard load performance.

## Proposal and decision
Ralph originally proposed adopting an existing connection pool, such as HikariCP, as risk mitigation. He was concerned that a custom pool might miss edge cases and block customers from querying their data. The engineering team backed that proposal. When Ralph and the engineering team presented it to the CEO, the CEO asked him to build a custom implementation instead, because packaging additional software such as HikariCP would add bloat.

## Custom implementation
Ralph implemented a thread-safe pool of reusable JDBC connections. Calling `.close()` on a connection does not actually close it. The connection is returned to the pool so it can be reused.

## Production problems
The custom pool later had production issues. Connections were leaked and never returned to the pool, which blocked customers from querying their data. The leaks came from unhandled errors that could occur while a database connection was in use.

## Outcome and lesson
Ralph eventually replaced the custom pool with HikariCP. After that change, the pool itself caused no further production issues. The custom implementation could have been better. The lesson was that, in cases like this, it can be a worthy tradeoff to trust an existing implementation that has already withstood the test of time, rather than trying to handle every potential edge case in-house.
