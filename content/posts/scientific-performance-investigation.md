+++
title = 'Web App Performance Investigation'
date = 2024-05-18T21:35:30-06:00

draft = false
+++

## Problem

 A Django web application is experiencing performance issues. Baseline tests show that the average latency to access an authenticated page is approximately 1500 milliseconds. This is not acceptable performance for a user interface[^nielsen-1993].

## Approach

When faced with an engineering problem, a great place to start is by formulating tests that bisect the problem space. This allows one to apply binary search[^binary-search] to the space, which is the same method that `git bisect`[^git-bisect] uses to assist a programmer in identifying the commit that introduced a bug.

### Problem Space

The developer believes that one of the following are the primary contributor to the high latency of the application:

- web server
- `nginx` reverse proxy
- `postgres` database

The first round of testing was focused around answering the following question: 

*Does the database configuration contribute significantly to application latency?*

The decision to target the database was driven by an observation that latency seemed to have increased significantly after a code commit which added authentication. The auth implementation required new queries of the auth database each time a page was loaded, to determine whether a user is permitted to see a page. It appears that these additional queries were slowing down the performance of the application.

### What to measure

The problem is specific to web page loading. Modern browsers offer a suite of developer tools for profiling and analyzing website performance. The `Network` tab in Firefox was chosen as the measurement tool, with the `Timings` column chosen to calculate the dependent variable in each test.

### Parameters

All tests were run under the same fixed conditions - from within a Docker container created from an image that was built off the same commit. The Docker container was run from the developer's local machine. The version of the database was held constant as well (Postgres 16).

The Django application is hosted on a cloud provider (AWS, GCP, etc...). The cloud provider allows the following parameters for the database to be modified:

- CPU + disk type (Shared SSD, Shared AMD + NVMe, Shared Intel + NVMe)
- Storage (10 GB, 15 GB, 20 GB...)
- RAM (1 GB, 2 GB, 4 GB, ...)
- datacenter location (NYC, SFO)
- web server location (NYC, SFO)

To minimize the number of tests which needed to be run, values for storage and RAM were selected which allowed the dependent variable (latency) to be interpolated at multiple points. In other words, these values were selected near the edges of the response surface.

Thus, the following tests were developed:

| Test Name | CPU + disk type | Storage | RAM |
| - | - | - | - |
| Test 1 (baseline) | Shared Regular + SSD | 10 GB | 1 GB |
| Test 2 | Shared Regular + SSD | 40 GB | 2 GB |
| Test 3 | Shared AMD + NVMe | 10 GB | 1 GB |
| Test 4 | Shared AMD + NVMe | 40 GB | 2 GB |
| Test 5 | Shared Intel + NVMe | 10 GB | 1 GB |
| Test 6 | Shared Intel + NVMe | 40 GB | 2 GB |

## Results

> The best-laid schemes o' mice an' men
  Gang aft agley

*To A Mouse*, Robert Burns (1785)

Unbeknownst to the developer, the cloud provider does not permit a database to be "down-provisioned" - the storage capacity can only be increased, not decreased. As a result, the tests could not be executed in the order planned. 

After several tests with minimal impact on latency, the developer made a key observation: the database server and application server did not reside in the same location. The database resided in the `NYC3` datacenter, while the app server resided in the `SFO3` datacenter. These locations are separated by nearly 3000 miles. Any time the app server needed to make a database query, a request was sent west-to-east across the country, and the response traveled east-to-west.

The developer decided to pivot, and investigate a different parameter of the database - the location of the server. Thus, the following tests were run:

| Test Name | CPU + disk type | Storage | RAM | database location | web server location | 
| - | - | - | - | - | - |
| Baseline 1 | Shared Regular + SSD | 10 GB | 1 GB | NYC3 | Colorado |
| Baseline 2 | Shared AMD + NVMe | 45 GB | 1 GB | NYC3 | SFO3 |
| Test 1 | Shared Regular + SSD | 40 GB | 2 GB | NYC3 | Colorado |
| Test 2 | Shared AMD + NVMe | 45 GB | 1 GB | NYC3 | Colorado |
| Test 3 | Shared AMD + NVMe | 45 GB | 1 GB | SFO3 | Colorado |
| Test 4 | Shared AMD + NVMe | 45 GB | 1 GB | SFO3 | SFO3 |

### Data

Each test was run 10 times each, on multiple pages in the Django application. Each page that was loaded required a user to be authenticated in to the system. For baseline 1, only data on the homepage could be collected (due to a mistake by the developer). The following is the summarized results:

#### Baseline 1

CPU: Shared Regular
Disk type: SSD
Storage: 10 GB
RAM: 1 GB RAM
Datacenters: database @ NYC3, web server @ Colorado

| Page | Load time +/- 2σ (milliseconds) |
| - | - |
| Homepage | - |
| View 1 | 1495 +/- 57 ms |
| View 2 | - |
| View 3 | - |
| View 4 | - |

#### Baseline 2

CPU: Shared AMD
Disk type: NVMe
Storage: 45 GB
RAM: 1 GB RAM
Datacenters: database @ NYC3, web server @ SFO3

| Page | Load time |
| - | - |
| Homepage | 1080 ms +/- 112 ms |
| View 1 | 1871 ms +/- 102 ms |
| View 2 | 2331 +/- 83 ms |
| View 3 | 2165 +/- 75 ms |
| View 4 | 2059 +/- 72 ms |

#### Test 1

CPU: Shared Regular
Disk type: SSD
Storage: 40 GB
RAM: 2 GB RAM
Datacenters: database @ NYC3, web server @ Colorado

| Page | Load time |
| - | - |
| Homepage | 812 +/- 22 ms |
| View 1 | 1484 +/- 104 ms |
| View 2 | 1840 +/- 42 ms |
| View 3 | 1704 +/- 93 ms |
| View 4 | 1656 +/- 76 ms |

#### Test 2

CPU: Shared AMD
Disk type: NVMe
Storage: 45 GB
RAM: 1 GB RAM
Datacenters: database @ NYC3, web server @ Colorado

| Page | Load time |
| - | - |
| Homepage | 833 +/- 72 ms |
| View 1 | 1455 +/- 31 ms |
| View 2 | 1830 +/- 61 ms |
| View 3 | 1692 +/- 30 ms |
| View 4 | 1657 +/- 69 ms |

#### Test 3

CPU: Shared AMD
Disk type: NVMe
Storage: 45 GB
RAM: 1 GB RAM
Datacenters: database @ SFO3, web server @ Colorado

| Page | Load time |
| - | - |
| Homepage | 577 +/- 25 ms |
| View 1 | 1027 +/- 72 ms |
| View 2 | 1278 +/- 39 ms |
| View 3 | 1192 +/- 50 ms |
| View 4 | 1141 +/- 33 ms |

#### Test 4

CPU: Shared AMD
Disk type: NVMe
Storage: 45 GB
RAM: 1 GB RAM
Datacenters: database @ SFO3, web server @ SFO3

| Page | Load time |
| - | - |
| Homepage | 94 +/- 27 ms |
| View 1 | 160 +/- 25 ms |
| View 2 | 193 +/- 89 ms |
| View 3 | 170 +/- 47 ms |
| View 4 | 123 +/- 33 ms |

## Conclusion

The primary determinant of page load latency was proximity of database to web server. In test 3, the database was migrated from the NYC3 datacenter to the SFO3 datacenter, which is approximately 40% closer to the web server in Colorado. The latency to load VIew 1 also declined by approximately 30%, indicating a negative correlation for distance between servers and page latency.

In test 4, latency declined by nearly an order of magnitude compared to, Baseline 1. The difference in this test is that the database server and web server were co-located in the SFO3 datacenter.  

This exercise of systematically changing factors that may contribute to database performance was productive, as it helped isolate a (monetarily) free change that could be made - which is to migrate the database to the same datacenter as the web server. It also helped confirm that with the current application setup and demands, the paid upgrades (RAM, storage, disk type) were not worth investing in at this time. Finally, this set of tests can be repeated in the future if application latency becomes an issue again.

[^nielsen-1993]: https://www.nngroup.com/articles/response-times-3-important-limits/
[^binary-search]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[^git-bisect]: https://git-scm.com/docs/git-bisect