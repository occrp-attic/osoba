# Osoba

DESCRIPTION

## Technology Stack
 * Django
 * Django REST Framework

## User Roles
 * User
 * Staff [Exists as is_staff in User Profile]

## Core concepts
 * Entity
 * Person
 * Company

## General requirements
 * An entity

## User Stories
 * ...

## Cross-functional Requirements
 * Fully unit tested (using Django's unit test framework)
 * Fully integration tested
 * All core logic in models or separate classes, not in views or templates
 * No unit composition in units

## REST Endpoints

### Entity (collection)
 * POST /entity/                - Create new entity
 * GET /entity/                 - Get list of entities matching a search term

### Entity (member)
 * GET /entity/<eid>/            - Get entity <eid>
 * DELETE /entity/<eid>/         - Delete entity <eid>
 * PUT /entity/<eid>/            - Alter the entity properties
