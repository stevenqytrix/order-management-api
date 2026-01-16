# Order Management API

## Overview

Backend REST API for managing orders in an e-commerce / B2B domain.  
The system is designed as a **production-grade modular monolith**, with **strict domain boundaries**, **explicit transaction control**, and **business-first modeling**.

The primary goal is **correctness and consistency of the order lifecycle**, not framework convenience.

---

## Problem Statement

Order management is a **stateful, invariant-driven problem**:

- Order state transitions must be explicit and controlled
- Business rules must be enforced centrally and consistently
- Partial updates and inconsistent persistence must be impossible
- Infrastructure concerns must not leak into business logic

This project addresses these constraints by modeling orders as **domain aggregates** and enforcing transactional consistency through **application-level orchestration**.

---

## Architectural Principles

### Modular Monolith

The system is intentionally designed as a **modular monolith** to:

- Preserve strong domain boundaries
- Avoid premature distribution
- Enable local reasoning and refactoring safety

Modules communicate through **explicit interfaces**, not implicit framework coupling.

---

### Clean Architecture

The codebase follows Clean Architecture principles:

- **Domain**  
  Pure business rules and invariants  
  No framework, no persistence, no side effects

- **Application**  
  Use cases orchestrating domain behavior  
  Defines ports (interfaces) and policies

- **Infrastructure**  
  Technical implementations (ORM, database, persistence mapping)  
  Fully replaceable without impacting domain or application layers

Dependency direction is strictly enforced:


---

### Explicit Transaction Boundaries (Unit of Work)

Transaction management is **not implicit** and **not delegated to repositories**.

- Each use case executes inside a **Unit of Work**
- Transactions are committed or rolled back at the application boundary
- Repositories are persistence-only and side-effect free

This ensures:
- Atomic writes
- No partial state persistence
- Clear ownership of consistency guarantees

---

## Core Domain Concepts

- **Order Aggregate**  
  Encapsulates lifecycle, invariants, and state transitions

- **Explicit State Machine**


- Invalid transitions are impossible by construction

- **Value Objects**
- OrderId
- CustomerId
- OrderItem

---

## Core Features

- Create, retrieve, update, and cancel orders
- Explicit order lifecycle states:
- CREATED
- PAID
- SHIPPED
- CANCELLED
- Centralized domain validation rules
- Idempotent persistence semantics
- Consistent application-level error handling
- Transaction safety via Unit of Work

---

## Persistence Strategy

- PostgreSQL as the persistence backend
- ORM models act as **pure data representations**
- Explicit mapping between:
- Domain aggregates
- Persistence models
- No domain logic inside infrastructure code

---

## Tech Stack

- REST API
- PostgreSQL
- ORM
- Docker

---

## Design Goals (Non-Goals)

**Goals**
- Correctness over convenience
- Explicit over implicit behavior
- Replaceable infrastructure
- High signal-to-noise codebase

**Non-Goals**
- Framework-driven design
- Microservices by default
- Hidden magic or implicit side effects

---

## Summary

This project demonstrates a **business-centric, correctness-driven backend architecture**, suitable for real production systems where **data integrity and domain rules are non-negotiable**.
