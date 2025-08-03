# CHANGES.md

## 🔧 Major Issues Identified in Original Code

1. **SQL Injection Vulnerabilities**
   - Used string interpolation in SQL.
   - ✅ Replaced with parameterized queries.

2. **Poor Structure**
   - All routes, DB logic, and config in `app.py`.
   - ✅ Split into `routes/`, `db.py`, `utils/`, `config.py`.

3. **No Input Validation**
   - Accepted arbitrary JSON without checks.
   - ✅ Used `pydantic` for schema validation with helpful error messages.

4. **Plaintext Password Storage**
   - Passwords stored as raw strings.
   - ✅ Implemented `bcrypt` hashing and secure verification.

5. **No Environment Configuration**
   - Hardcoded DB name, port, and debug flag.
   - ✅ Moved all config to `.env` + `python-dotenv`.

6. **Poor API Responses**
   - Returned strings instead of JSON.
   - ✅ Now uses proper `jsonify()` with status codes.

7. **Missing Error Handling**
   - No clear feedback or code for bad inputs.
   - ✅ Standardized all error responses with 400/401/404 codes.

---

## 🧠 Architectural Decisions

- Blueprint-based modular routing
- `db.py` handles safe connection management per request
- `config.py` isolates environment config
- `validators.py` centralizes input schemas
- `security.py` hashes and verifies passwords using `bcrypt`

---

## ⚖️ Trade-offs

- Still using SQLite for simplicity, although PostgreSQL is better for production.
- No JWT or session-based auth (out of scope).
- No Swagger docs or OpenAPI — time-focused trade-off.

---

## ⏳ With More Time

- Add API auth (JWT/session)
- Use migrations (like Alembic) for DB evolution
- Add request/response logging
- Implement pagination and sorting for `/users`
- Build Postman collection or Swagger for API

---

## 🤖 AI Usage Disclosure

Used **ChatGPT-4** to:
- Plan and organize refactor
- Write secure, modular, clean Flask code
- Generate `pydantic` models and bcrypt logic
- Draft and polish this `CHANGES.md`

All generated code was reviewed and customized by me.
