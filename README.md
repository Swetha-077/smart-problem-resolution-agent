# Smart Problem Resolution Agent

## 1. Project Overview

Smart Problem Resolution Agent is a web-based problem management system that analyzes a user's problem and automatically identifies the appropriate department, priority, recommended action, and estimated response time.

The system uses a local rule-based resolution engine, FastAPI for the backend, HTML/CSS/JavaScript for the frontend, and SQLite for storing tickets and ticket history.

---

## 2. Problem Statement

In colleges and organizations, users may face different problems related to IT, HR, Finance, Facilities, or Security.

Manually identifying the correct department for every problem can take time and may result in incorrect routing.

This project provides an automated solution that analyzes the problem description and recommends the appropriate department and priority.

---

## 3. Objectives

- Automatically analyze user problems.
- Classify problems into appropriate departments.
- Assign a priority level to each problem.
- Recommend the appropriate department to contact.
- Provide recommended actions.
- Store problem tickets in a database.
- Track ticket status.
- Maintain ticket status history.
- Provide a dashboard showing ticket statistics.
- Provide a simple web interface for users.

---

## 4. Main Features

### Problem Analysis

The system analyzes the submitted problem and identifies its category.

Supported categories:

- IT
- HR
- Finance
- Facilities
- Security
- General

### Priority Detection

Problems are assigned one of the following priority levels:

- Critical
- High
- Medium
- Low

### Department Recommendation

The system provides:

- Department name
- Email address
- Phone number
- Recommended action
- Estimated response time

### Ticket Management

Every analyzed problem is stored as a ticket in the SQLite database.

Tickets can have the following statuses:

- Open
- In Progress
- Resolved

### Ticket History

The system records changes made to ticket status.

Example:

Open → In Progress → Resolved

### Dashboard

The dashboard displays:

- Total Tickets
- Open Tickets
- In Progress Tickets
- Resolved Tickets

---

## 5. Technologies Used

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn

### Database

- SQLite

### Development Tools

- Visual Studio Code
- Python Virtual Environment
- Swagger API Documentation

---

## 6. System Architecture

```text
User
  |
  v
Frontend
HTML / CSS / JavaScript
  |
  v
FastAPI REST API
  |
  v
Local Resolution Engine
  |
  +------------------+
  |                  |
  v                  v
Category &        Priority
Department        Detection
Detection
  |
  v
SQLite Database
  |
  +----------------------+
  |                      |
  v                      v
Tickets             Ticket History
  |
  v
Dashboard