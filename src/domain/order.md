# Order Domain Model

## Purpose
Represents a customer order and encapsulates all business rules related
to order lifecycle and validity.

## Core Attributes
- OrderId
- CustomerId
- OrderStatus
- OrderItems
- TotalAmount
- CreatedAt
- UpdatedAt

## Order Status
An order can be in one of the following states:
- CREATED
- PAID
- SHIPPED
- CANCELLED

## Business Rules
- An order must contain at least one order item
- Total amount must be greater than zero
- An order cannot be shipped unless it has been paid
- A cancelled order cannot change state
- Order state transitions must be explicit and controlled

## State Transitions
- CREATED → PAID
- PAID → SHIPPED
- CREATED → CANCELLED
- PAID → CANCELLED

Transitions not listed above are invalid.

## Invariants
- OrderId is immutable
- OrderStatus changes only through domain rules
- TotalAmount is derived from order items
