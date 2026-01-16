# Infrastructure Layer

## Responsibility

The Infrastructure layer contains all **technical implementation details**
that interact with external systems and frameworks.

It provides **concrete implementations** for interfaces defined in the
application layer and acts as the outermost boundary of the system.

This layer is responsible for *how* things are done, never *what* or *why*.

## Dependencies

The Infrastructure layer depends on:
- application
- domain

The domain and application layers **must never depend on infrastructure**.

All dependencies point inward.

## Included Concerns

Typical responsibilities of this layer include:

- Database persistence (PostgreSQL)
- ORM mappings
- Read and write repository implementations
- External services integration
- Messaging systems
- Authentication providers
- Configuration and environment setup

## Architectural Rules

- Implements repository interfaces defined in the application layer
- No business rules allowed
- No domain logic allowed
- No transaction boundaries defined here  
  (handled externally via Unit of Work)
- Frameworks and libraries are isolated in this layer
- Can be replaced without impacting domain or application layers

## CQRS (Light) — Infrastructure Perspective

This project applies a **CQRS light** approach at the system level.

From the infrastructure point of view:

- **Write-side repositories** persist full domain aggregates  
  and are used exclusively within transactional boundaries
- **Read-side repositories** expose optimized, read-only projections  
  mapped directly to read models (DTOs)

Infrastructure implementations strictly follow the contracts defined
by the application layer, without leaking framework or persistence
details upward.

## Planned Structure

infrastructure/
├── persistence/
│ ├── models/
│ │ └── order_model.py
│ ├── postgres_order_repository.py
│ └── postgres_order_read_repository.py
│
├── http/
│ └── api/
│
├── auth/
│
└── config/


Each submodule is replaceable and isolated, ensuring long-term
maintainability and evolvability of the system.

