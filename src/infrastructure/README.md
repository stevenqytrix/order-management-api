# Infrastructure Layer

## Responsibility

This layer contains all technical implementation details that interact
with external systems and frameworks.

It provides concrete implementations for interfaces defined in the
application layer.

The infrastructure layer depends on:
- application
- domain

The domain and application layers must never depend on infrastructure.

## Included Concerns

Typical responsibilities of this layer include:
- Database persistence (PostgreSQL)
- ORM mappings
- External services integration
- Messaging systems
- Authentication providers
- Configuration and environment setup

## Architectural Rules

- Implements repository interfaces defined in application layer
- No business rules allowed
- No domain logic allowed
- Frameworks are isolated here
- Can be replaced without impacting domain or application layers

## Planned Structure

infrastructure/
├── persistence/
│   ├── postgres/
│   │   ├── postgres_order_repository.py
│   │   └── models.py
│
├── http/
│   └── api/
│
├── auth/
│
└── config/
