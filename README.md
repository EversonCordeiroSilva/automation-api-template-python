# 🧪 Python API Test Automation – BDD Showcase

This repository showcases a **professional and intentional Python test automation framework**, designed and implemented by a **QA Engineer** to demonstrate:

* clean architecture
* BDD best practices
* API automation maturity
* conscious design decisions (what to include *and* what to avoid)

The project focuses on **API testing using BDD (Behave)**, while keeping the structure open for future evolution without premature abstraction.

---

## 🎯 Purpose

The main goal of this project is to demonstrate **how to design a maintainable and scalable automation framework**, not just how to write tests.

Key principles:

* clarity over overengineering
* explicit intent over generic templates
* separation of concerns
* realistic, production-like test design

---

## 🧰 Tech Stack

* **Python 3.14+**
* **Behave (Cucumber for Python)** – BDD
* **Requests** – API interaction
* **AssertPy** – expressive assertions

---

## 📁 Project Structure

```text
automation-project/
│
├── resources/                  # Non-executable assets
│   └── features/               # BDD specifications (Gherkin only)
│       └── api_login.feature
│
├── src/
│   ├── services/               # API service layer (integration logic)
│   │   └── store/
│   │       └── auth_service.py
│   │
│   ├── tests/
│   │   ├── steps/              # BDD step definitions
│   │   │   └── store/
│   │   │       └── login_steps.py
│   │   └── environment.py      # Behave hooks
│   │
│   ├── config/                 # Reserved (documented, intentionally unused)
│   ├── core/                   # Reserved (documented, intentionally unused)
│   ├── pages/                  # Reserved (UI automation placeholder)
│   └── utils/                  # Reserved (intentional, no generic helpers)
│
├── reports/
├── script.py                   # Test runner (Behave entry point)
├── requirements.txt
└── README.md
```

---

## 🧠 Architectural Design

### Active Test Flow

```
Feature (Gherkin)
   ↓
Step Definitions
   ↓
Service Layer
   ↓
External API
```

This flow ensures:

* steps remain readable and free of technical noise
* API logic is centralized
* changes in the API affect only the service layer

---

## 🧩 Service Layer (`src/services`)

The service layer:

* encapsulates API endpoints
* builds payloads and headers
* performs HTTP calls

> Step definitions **never** call `requests` directly.

This mirrors how mature teams isolate integration logic.

---

## 🧪 BDD with Behave

* Gherkin files live **only** in `resources/features`
* Step definitions live **only** in `src/tests/steps`
* Hooks and shared context are handled in `environment.py`

Tags (`@smoke`, `@api`, `@negative`) are used to support selective execution.

---

## ▶️ Running the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all BDD tests:

```bash
behave
```

Run via the custom runner (Java-like approach):

```bash
python runner.py
```

Run by tag:

```bash
behave --tags=@smoke
```

---

## 📐 Reserved Folders (Intentional)

Some folders are intentionally present but not used yet.
Each contains a local `README.md` explaining its purpose.

### Why keep them?

Because this is a **showcase**, and architectural awareness matters.

These folders represent **future scalability**, not current needs:

* `config/` → environment and configuration management
* `core/` → framework-level abstractions (HTTP client, retries, logging)
* `pages/` → UI automation (Page Object Model)
* `support/` → specific utilities *only if real reuse emerges*

> No abstractions were introduced without a concrete need.

---

## ✅ What This Project Demonstrates

✔ Clean BDD modeling <br>
✔ Proper separation of responsibilities <br>
✔ No overuse of helpers or “magic” layers <br>
✔ Conscious architectural trade-offs <br>
✔ Production-oriented mindset

This is **not** a copy-paste framework.
It is a **designed system**.

---

## 🚀 Possible Next Evolutions

* Allure reporting
* Contract testing
* CI/CD (GitHub Actions)
* Token reuse across scenarios
* Multi-environment support

---

## 📌 Final Note

This repository reflects how a **Senior QA Engineer** thinks about automation:

> *Automation is not about writing more code —
> it is about writing the right code, at the right time.*

---

🔹 *Powered by AI — ChatGPT assisted framework design and documentation.*

---