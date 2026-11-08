# Hi, I'm Zaid Mushtaq

**Software Developer** · Bengaluru, India · [OneBill Software Private Limited](https://github.com/zaid-mushtaq-software-engineer)

Software Developer | Backend Engineering | AI Enthusiast

---

## About Me

I'm a Software Developer interested in building reliable backend applications and scalable systems. My primary interests include Java, Spring Boot, database technologies, backend architecture, and distributed systems.

I'm also exploring AI engineering, LLMs, Model Context Protocol (MCP), and Agentic AI, with a focus on integrating AI into modern software applications.

---

## Technical Skills

### Programming

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### Backend Development

![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white)
![Hibernate](https://img.shields.io/badge/Hibernate-59666C?style=flat-square&logo=hibernate&logoColor=white)
![REST API](https://img.shields.io/badge/REST_API-02569B?style=flat-square&logo=rest&logoColor=white)

### Databases

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

### Messaging

![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)

### System Design

High-Level Design (HLD) · Low-Level Design (LLD) · Distributed Systems

### Tools

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

### AI

Large Language Models (LLMs) · Model Context Protocol (MCP) · AI Agents · Agentic AI

---

## Engineering Interests

- Backend Architecture
- Distributed Systems
- Scalability and Performance
- Database Design
- AI-powered Applications

---

## Featured Projects

### [KINNOTE](https://github.com/zaid-mushtaq-software-engineer/KINNOTE)

**Family Story Archive** — a private platform to preserve family memories through photos, stories, and personal connections.

| | |
|---|---|
| **Problem** | Centralize family memories with controlled sharing (followers and private groups) instead of scattered chats and albums. |
| **Stack** | Java 21, Spring Boot 3, MySQL, Redis, RabbitMQ, React, TypeScript, Vite |
| **Status** | Active development (private repository) |

**Implemented highlights (verified in-repo):**

- Split **`api`** and **`worker`** Spring profiles (REST + security vs. outbox relay and RabbitMQ consumers)
- Flyway-backed MySQL schema, Redis for caching/session patterns, object storage via MinIO in local dev
- React + Vite frontend with `/rest/v1` API proxy

**Architecture:** Modular Spring Boot backend with transactional outbox, async consumers, and a React SPA. See repository docs for flow and API reference.

---

### [Redis Engineering Lab](https://github.com/zaid-mushtaq-software-engineer/redis-engineering-lab)

A **hands-on Redis laboratory** on a Product & Inventory domain—MySQL as source of truth, Redis as an optional performance layer.

| | |
|---|---|
| **Problem** | Learn production-style caching, invalidation, and rate limiting with measurable failure modes. |
| **Stack** | Java 21, Spring Boot 3.5, MySQL 8, Redis 7.2, Docker Compose, Flyway, Testcontainers |
| **Status** | Phase 1 complete (documented baseline); Phase 2 planning in roadmap |

**Implemented highlights (verified in-repo):**

- **13** business HTTP endpoints (product & inventory admin + public reads)
- Cache-aside for product detail, paginated lists, and inventory (TTL + invalidation after commit)
- Per-IP **token-bucket rate limiting** (Lua in Redis) on public GETs
- Integration tests with Testcontainers; dev-only Redis sandbox behind admin key

**Architecture:** Layered Spring Boot services, explicit cache services, `SCAN`-based list eviction (no `KEYS`), fail-open when Redis is unavailable.

---

## GitHub Statistics

### Most Used Languages

*Distribution reflects **aggregated code volume** across repositories I own (public and private), not skill level. Updated automatically—see [workflow setup](docs/GH_STATS_SETUP.md).*

![Language distribution](assets/language-distribution.svg)

### Contribution Activity

![GitHub contribution activity](https://github.com/users/zaid-mushtaq-software-engineer/contributions)

### GitHub Statistics

![GitHub stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=zaid-mushtaq-software-engineer&theme=github_dark)

### Contribution Streak

![GitHub streak](https://streak-stats.demolab.com/?user=zaid-mushtaq-software-engineer&theme=github-dark&hide_border=true)

---

## Currently Exploring

*Learning focus—not all items below appear in shipped projects yet.*

- Advanced Java and Spring Boot
- System Design
- Redis and Distributed Systems
- RabbitMQ and Apache Kafka
- AI Engineering
- LLMs, MCP, and Agentic AI

---

## Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-zaid--mushtaq--software--engineer-181717?style=flat-square&logo=github)](https://github.com/zaid-mushtaq-software-engineer)
[![Portfolio](https://img.shields.io/badge/Portfolio-live-0A0A0A?style=flat-square&logo=githubpages&logoColor=white)](https://zaid-mushtaq-software-engineer.github.io/My_Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Zaid_Mushtaq-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/zaid-mushtaq-software-engineer/)
[![Email](https://img.shields.io/badge/Email-mushtaqzaid589@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mushtaqzaid589@gmail.com)
