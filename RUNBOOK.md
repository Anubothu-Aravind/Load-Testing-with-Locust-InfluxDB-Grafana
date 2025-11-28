# Load Test Runbook — Interpreting Results & Fixes

## Overview
This runbook helps interpret Locust test outputs and provides prioritized remediation steps for common bottlenecks.

### Key metrics to monitor
- p50/p95/p99 latency: typical and tail response times.
- Requests per second (RPS): throughput achieved.
- Error rate: percentage of failed requests (4xx and 5xx).
- Concurrent users: simulated active users.
- Server-side metrics: CPU, memory, load average, disk I/O, DB connections.

## Quick interpretation guide
1. If p95 spikes but p50 is steady: tail latency problem (e.g., slow queries, GC pauses, resource contention).
2. If error rate increases with RPS: service is overloaded — check connection pools, thread limits, timeouts.
3. If RPS plateaus while CPU is low: external dependency bottleneck (DB, cache, third-party APIs).
4. If CPU and DB I/O both high: consider sharding, read replicas, or caching.
5. If failures are mostly 429/limit responses: rate-limiting or WAF interference.

## Top 5 prioritized fixes
1. **Database connection pooling & query optimization**
   - Ensure pool size matches expected concurrency.
   - Add indexes to heavy read queries; avoid N+1 query patterns.
   - Use read replicas for heavy read workloads.

2. **Introduce caching layer**
   - Add HTTP caching (CDN) for static responses.
   - Use application-level cache (Redis) for expensive reads and computed results.

3. **Increase horizontal capacity**
   - Scale application instances behind the load balancer.
   - Ensure autoscaling triggers are set on CPU or request latency.

4. **Tune application & runtime**
   - Reduce GC pauses by tuning heap sizes and GC settings.
   - Increase thread pool sizes or worker processes where safe.

5. **Rate limiting & graceful degradation**
   - Implement per-IP or per-user rate limits.
   - Return lightweight error responses or degraded features under load.

## Troubleshooting steps
1. Reproduce the issue with a step load to identify the exact user count where metrics degrade.
2. Correlate Locust metrics with server metrics (CPU, memory, DB).
3. Capture slow query logs and flame graphs; fix hot paths.
4. Test fixes in staging with the same load profile.
5. Iterate: deploy, test, measure, repeat.

## Notes on safe testing
- Always run tests in staging unless explicit permission is provided.
- Use test accounts and idempotent operations.
- Notify providers if planning >1000 simulated users.
