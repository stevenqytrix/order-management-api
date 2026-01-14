# Order Management API

## Overview
Backend REST API for managing orders in an e-commerce / B2B domain.
Designed with clean architecture and production-oriented patterns.

## Problem Statement
Order management requires strict control over order lifecycle,
business validation rules, and data consistency.

## Architecture
- Modular monolith
- Clean Architecture
- Separation between domain, application, and infrastructure layers

## Core Features
- Create, read, update, and cancel orders
- Order lifecycle states: CREATED, PAID, SHIPPED, CANCELLED
- Domain validation rules
- Idempotent order creation
- Standardized error handling

## Tech Stack
- REST API
- PostgreSQL
- ORM
- Docker
