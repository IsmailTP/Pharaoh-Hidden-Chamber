# Pharaoh's Hidden Chamber

An Egyptian-themed web exploitation challenge focused on Insecure Direct Object References (IDOR) and broken access control vulnerabilities.

---

## Challenge Information

* **Category:** Web Security
* **Difficulty:** Easy–Medium
* **Author:** Ismail TP

---

## Description

Pharaoh's Hidden Chamber is a Capture The Flag (CTF) challenge where players explore a restricted ancient temple system protected by weak access controls.

The application uses encoded identifiers to manage user access levels. Players must investigate how the system handles authorization and discover how hidden resources can be accessed by manipulating object references.

The challenge demonstrates how insecure direct object references can expose sensitive functionality and allow unauthorized access to privileged areas.

---

## Features

* Egyptian-themed challenge environment
* Hidden chamber exploration
* Encoded user identifiers
* Access control bypass scenario
* Real-world inspired IDOR vulnerability
* Beginner-friendly exploitation path
* Interactive web interface

---

## Concepts Covered

* Insecure Direct Object References (IDOR)
* Broken access control
* Base64 encoding analysis
* URL parameter manipulation
* Authorization bypass
* User enumeration
* Web application reconnaissance

---

## Technologies Used

* Python
* Flask
* HTML/CSS/JavaScript

---

## Skills Practiced

* URL manipulation
* Access control testing
* Identifier analysis
* Web reconnaissance
* Authentication and authorization testing
* Web exploitation methodology

---

## Setup Instructions

### Clone Repository

```bash id="l5q8ga"
git clone https://github.com/IsmailTP/pharaohs-hidden-chamber.git
cd pharaohs-hidden-chamber
```

### Install Dependencies

```bash id="m1x4vr"
pip install -r requirements.txt
```

### Run the Challenge

```bash id="6v9jtb"
python app.py
```

---

## Screenshots

Add challenge screenshots here.

Suggested screenshots:

* Login page
* Temple interface
* Encoded glyph parameter
* Hidden chamber access
* Final challenge environment

---

## Educational Purpose

This project was created for ethical cybersecurity education and hands-on security training purposes only.

Do not use these techniques against systems without proper authorization.
