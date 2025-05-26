# Why system design interviews

## Purpose
- How the hell you can design Twitter in one hour?
- Good news: that's not what is expected
- Bad news: it is challenging by design

## What it is for?
- To evaluate your skills and experience as developer
    - If you did participate in complex project it usually is more or less obvious
- To evaluate how you will navigate UNKNOWN situation
- To evaluate how you are likely to interact with the interviewer

## TL/DR
- It is about HOW you approach the design
- Not the end design
    - perfect design does not matter if the "way" was bad


# "TestingCoder" approach to system design

## What is special about it?
- this is influenced by videos, practice and "System Design Interview - Insiders guide" book
- tailored for me, but hopefully helpful for you

## Design interview steps
1. Identify requirements
    - functional requirements (use cases)
    - non functional requirements (usage patterns, throughput, availability, latency,etc)
1. Go through each use-case one by one
    - start by generic and "naive" implementation
        - for example, drow single "DB" w/o specifying any details, sharding, etc
    - work for each of identified and "scoped in" use case
        - your design will mostlikely evolve
            - some stuff will be added
            - some stuff will be changed/replaces - that's OK!
1. Identify if your system can support non-functional requirements
    - That's where you can consider adding cache, specifying or breaking DB, etc
    - Your goal is not to build "bullet proof" system, but to see if you design CAN REASONABLY support intended usage/load patterns
    - Again, design will change and evolve, that's OK

## Gotchas and Tips
1. Use "building block" as Lego (will be discussed later)
1. Have some "go to" technologies
    - any reasonable developer with some experience worked at least with some:
        - RDBMS
        - Cloud provider
        - NoSQL database
        - Cache
        - Queue
    - so you are SUPPOSED to know at least some (I will specify my go-tos later too)
1. It is OK to avoid calling out particular technology/tool if it is not your area of expertise
    - you don't really want to say "Redis" and know literally nothing about it
    - Just say something "For this element I can't think of the right concrete tool/technology, some additional research may be needed. We will consider what is available in the company, if it fits the pattern and do the decision later"
1. Don't talk all the time, SLOW DOWN, PAUSE
    - that will allow interviewer to ask questions, add suggestions
    - remember, making them HAPPY about working with you is more important than having perfect diagram on the whiteboard
    - so pause, talk slow, listen, and respond

# Building blocks
- These are the "legos"
- List probablye is not exhaustive, but probably good enough for most cases

## App server
- This is where your code will be deployed and accessed
- Does some back end stuff (could be a microservice)
- And could also serve front end stuff
    - if front end very complex - it may be considered as separate building block
        - or if it is a mobile app :)

## Caching
- Caching designed to make frequently accessible data available
- Usually "in memory" for speed
- Cache is less useful if data changes often
- Works the best with imbalanced usage patterns
- Common cache invalidation strategies:
    - Least recently used
    - Least freqeuently used
    - FIFO

## Scaling

### Vertical
- Adding more/better resources (CPU, RAM) to the existing server
- No built-in redundancy
- But could be good for servers with predictable evenly distributed or small loads

### Horizontal
- Adding more servers with the App Code
- Redundancy out of the box
- Good with stateless apps, not so good with stateful (CAP theorem)
- Load balancer required

## Load Balancer
- Balances the load between several servers
- Can take unhealthy servers out of rotation
- Usually provided by your cloud provider these days

## Content Delivery Network (CDN)
- Like distributed network of S3s
- Puts content closer to the consumer
- Could be
    - "push" (all data shared accross all CDN nodes eventually)
    - "pull" (only required data, important for this region gets pulled)
        - so also act like slow cache



## Database
### RDBMS
- Old School SQL
- ACID transactions:
    - Atomic
    - Consistent
    - Independent
    - Durable
- Has cool joins :)
- Has indexing
- Usually not as fast as NoSql, but
    - Could be sharded (broken down into several databases based on some keys)
    - Can have one write - several read nodes pattern

### NoSQL
- Usually DBs that drops some of the ACID requirments, often consistency
- Many types: Key-Value, Document, etc
- No normalization needed! :)
- Good choice when:
    - unstructured data
    - huge amount of data
    - super low lateny
    - no need to do complex joins/relations

## Queues
- Systems for asyncrhrounous messages delivery
    - so used in asyncrhonous flows
- Could be simple queues, or with bells and wistles


## Other
- Don't forget about analytics, logging, authentication, deployment/Terraform, etc

# Go-to technologies
- These are technologies I either worked with or know at least basic minimum to bring them into the interview setting
- Use your tech stack, though the one here is super safe bet
- Don't commit or mention technology/tool if you don't need to!
- You could probably print it?

| **Component**         | **Type**                 | **Example Tech**         | **Notes** |
|-----------------------|--------------------------|---------------------------|-----------|
| **Relational DB**     | SQL, strong consistency  | PostgreSQL                | Super safe choice, de-facto standard for big DBs  |
| **NoSQL DB**          | Document store           | MongoDB                   | Flexible schema, very fast, evential consistency  |
|                       | Key-value store          | Redis                     | Caching, counters, sessions (in-memory, fast)     |
|                       | Key-value store          | Casandra                  | Slower, but with fault tolerance                  |
| **Cache**             | In-memory store          | Redis / Memcached         | Distributed in-memory cache                       |
| **Queue**             | Pub-sub or message bus   | Rabbit MQ / Amazon SQS    | Pick whatever you have, I guess                   |
| **Search**            | Full-text search engine  | Elasticsearch             | Useful for logs, product search, analytics        |
| **CDN**               | Static content delivery  | S3 + CloudFront           | S3 stores assets, CloudFront distributes globally |
| **Infra (MVP)**       | Containerization         | Docker                    | Docker.. Docker is everywhere!                    |
|                       | Container orchestration  | Kubernetes / AWS ECS      | Scaling, deployment, service discovery            |
| **Logging/Analytics** | Analytics                | Logstash/Graphana/Kibana  | Visibility, alerts, analysis                      |

# Back of the envelope estimation
- It is a fast way to do some very rough calculations of scale
- Some latency numbers could be helpful:
    - Disk Seek: 10 ms
    - Read 1MB from Disk: 30 ms
    - to be continued, I guess? (Pull requests welcome :)

# CAP theorem
- Consistency
- Availability
- Partition tolerance (ability to operate if network messages dropped/delayed)
- Any distributed system can have only two of these

