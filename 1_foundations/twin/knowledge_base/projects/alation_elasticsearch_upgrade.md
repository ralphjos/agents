# Alation Elasticsearch Upgrade from 1.x to 7.x

## Summary
At Alation, Ralph Arroyo was responsible for upgrading the Elasticsearch version used in the codebase from 1.x to 7.x. He made extensive changes around querying Elasticsearch and installing it.

## Why the upgrade happened
The upgrade was prompted primarily by security concerns raised by larger customers. Those customers wanted the security enhancements introduced since Elasticsearch 1.x so they could stay compliant inside their organizations. The large version jump also made it easier for the Search team to introduce vector search in Alation later, because a future move to Elasticsearch 8.x would be a much smoother transition.

## What changed
The work primarily included:

- Updating the Python Elasticsearch client.
- Adapting queries to the updated Elasticsearch query DSL.
- For the beta only, letting customers configure whether they wanted Elasticsearch 1.x or 7.x.

To support that beta choice, Ralph introduced a compatibility shim. The shim preserved legacy 1.x behavior for customers who ran into issues with 7.x, and it gave Alation a fallback if any customer had trouble migrating to 7.x.
