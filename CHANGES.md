# CHANGES.md

## 🔧 Major Issues Identified in Original Code

1. **SQL Injection Vulnerabilities**
   -  Used string interpolation in SQL queries.
   -  Replaced with parameterized queries using SQLite placeholders.

2. **Monolithic Code Structure**
   -  All logic bundled in `app.py`.
   -  Refactored into:
     - `routes/` → Flask Blueprints
     - `utils/` → JWT, password security, validation
     - `db.py`, `config.py` → modular responsibilities

3. **No Input Validation**
   -  APIs accepted arbitrary JSON.
   -  Added `pydantic` schemas for clean request validation and error messaging.

4. **Plaintext Password Storage**
   -  Stored passwords in plain text.
   -  Implemented secure password hashing using `bcrypt`.

5. **No Authentication Mechanism**
   -  All routes were open to unauthenticated access.
   -  Integrated **JWT authentication** with token expiration and protected routes.

6. **Hardcoded Configuration**
   -  Secrets and settings were hardcoded.
   -  Migrated to `.env` using `python-dotenv` for environment-based configuration.

7. **Inconsistent API Responses**
   -  Returned strings and unclear messages.
   -  Standardized all responses using `jsonify()` and appropriate HTTP status codes.

8. **Missing Error Handling**
   -  No error structure or handling strategy.
   -  Unified 400/401/404/500 responses with meaningful messages.

---

##  Security Improvements

- Issued **JWT tokens** upon login with a 1-hour expiration.
- Implemented `@require_auth` decorator to protect user-related routes.
- Handled invalid or expired tokens with clear 401 responses.
- Stored `JWT_SECRET` and sensitive values securely in `.env`.

---

##  Architectural Decisions

- Modular Flask app using Blueprints for scalability.
- Stateless authentication via JWT.
- Centralized decorators and utilities for clean logic reuse.
- `.env` + `config.py` to isolate sensitive data and settings.
- Utility layer for password hashing and token encoding/decoding.

---


##  AI Usage Disclosure

- **Tool Used**: ChatGPT-4
- **Used For**:
  - Identifying key architectural and security issues
  - Writing modular Flask + JWT logic
  - Structuring and drafting this changelog
- **Review**: All generated code was verified, tested, and modified by me.

---
Runs via `python app.py` as expected.
