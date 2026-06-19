# Programming-languages
A collection of Python, Java, sql scripts developed during my training at NareshIT academy to demonstrate automation and database security concepts.

# Foundational Software Engineering & Core Security Logic

This repository documents my foundational programming and database training. Rather than showcasing advanced exploit tools, these projects focus on the absolute bedrock of cybersecurity: **robust application logic, file-system integrity, and defensive database structures**. 

## 📁 Repository Map

### 1. 📂 [Bank](./Bank)
* **Language:** Python
* **Security Focus:** Business Logic Enforcement & Input Boundaries
* **Description:** A flat-file simulation of a bank account manager. Focuses on state-checking algorithms that prevent logical exploits (such as ensuring zero-balance or negative-withdrawal protection thresholds).

### 2. 📂 [Java JDBC Project](./Java JDBC Project)
* **Language:** Java + SQL
* **Security Focus:** SQL Injection (SQLi) Mitigation
* **Description:** An inventory processing driver connecting to an Oracle DB instance. Demonstrates strict use of compiled parameterization (`PreparedStatement`) to completely neutralize code injection vectors at the software layer.

### 3. 📂 [Sql_basics](./Sql_basics)
* **Language:** Oracle SQL
* **Security Focus:** Storage-Layer Data Integrity & Schema Constraints
* **Description:** Clean Data Definition Language (DDL) and Data Manipulation Language (DML) configurations. Focuses on using database constraints (`PRIMARY KEY`, `CHECK`, `NOT NULL`) as a built-in server-side firewall against corrupted inputs.

### 4. 📂 [Basic Python Programs](./Basic Python Programs)
* **Language:** Python
* **Security Focus:** Automation Foundations & Syntax Mechanics
* **Description:** Standard logic handling and operational loops which establish the foundational syntax tracking needed to write automation and log-parsing scripts.
