# E-Learning Course Management System

## Overview

The E-Learning Course Management System is a Django-based Learning Management System (LMS) that facilitates online teaching and learning. Instructors create and manage courses with lessons and quizzes, while students enroll, work through lesson material, take quizzes, and track their progress toward course completion.

---

## Objectives

- Provide an interactive online learning platform.
- Enable instructors to organize learning content.
- Allow students to learn at their own pace.
- Conduct online quizzes and assessments.
- Monitor student learning progress.
- Award completion certificates.

---

## Technology Stack

### Backend

- Django 6.0
- SQLite (default development database)
- python-dotenv for environment configuration

### Frontend

- Django templates
- Bootstrap 5.3
- Custom CSS theme

---

## Applications

### Users

Custom `User` model (`students` and `instructors`) plus registration, login, logout, and role-based dashboard redirection.

---

### Courses

Course, lesson, and enrollment management. Instructors create courses and add lessons (written content and/or a PDF attachment); students browse and enroll in courses.

---

### Quizzes

Quiz, question, and multiple-choice management. Students take quizzes tied to a course and receive a score; instructors create quizzes from the course page, with questions and choices managed through the Django admin.

---

### Progress

Tracks which lessons a student has completed per course and computes a completion percentage. A `Certificate` record is automatically created once a student completes every lesson in a course.

---

## Features

### Student

- Register an account and log in
- Browse available courses
- Enroll in courses
- Read lesson content and open PDF lesson material
- Mark lessons complete and track course progress
- Take quizzes and view results
- Earn a certificate on course completion

### Instructor

- Create and manage their own courses
- Add lessons (text content and/or PDF material) to a course
- Create quizzes for a course
- View enrollment counts per course

### Administrator

- Manage users, courses, lessons, enrollments, quizzes, questions/choices, and certificates via the Django admin site

---

## Getting Started

```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root with:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

Then run migrations and start the dev server:

```bash
python manage.py migrate
python manage.py createsuperuser   # optional, for admin access
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

---

## Future Enhancements

- In-app UI for instructors to create and edit quiz questions/choices (currently managed via the Django admin)
- Support for video lessons, not just text and PDF material
- Multiple question types (currently single-correct-choice only) and downloadable/printable certificates
- Assignment submissions and grading
- Discussion forums and direct messaging between students and instructors
- Real-time and email notifications
- Search, filtering, and pagination for course listings
- Automated test suite and CI/CD pipeline
- Production deployment setup (PostgreSQL, static/media file hosting, hardened settings)
- REST API for mobile app integration
- Course recommendations and an AI learning assistant
- Leaderboards and gamification badges
- Live/virtual classroom sessions

---

## Project Goal

To build a scalable, secure, and user-friendly Learning Management System capable of supporting online education in universities, colleges, and training institutions.
