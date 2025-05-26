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



