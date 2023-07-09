# Development documentation

## 🍔 Tech stack

- 📱 Front-end: React, Next.js, Material UI, Formik, JavaScript;
- ⚙️ Back-end: Flask, Python, MongoDB Atlas;
- 🔑 Authentication: NextAuth.js;
- ☁️ Google Cloud products: ?;
- 🖥️ Deployment: Vercel.

## ✨ Functionalities

- Sign up/log in with email or Google
- Create a profile
- Search for jobs
- Apply to jobs
- Track job applications
- Receive notifications when new jobs open

## 🌟 Potential original features

- 🦾 A ML model to match users with jobs.
- 🤖 A crawler that aggregates open jobs.
- 🔔 Push notifications when new jobs open.
- 📋 A table view with each column being a stage in a job application and the
  rows being the applications that the user has submitted.
- 🗺️ A map displaying open and applied to internships.
- 📊 Job application analytics (using MongoDB Atlas?).

## 📂 Directory structure

- `api/`: The back-end;
- `client/`: The front-end;
- `docs/`, `api/docs/`, `client/docs/`: Documentation for the project, the
  back-end, and the front-end, respectively.

## 🧩 Git

See [git.md](git.md).

## 🗃️ Data model

See [model.md](model.md).

## 📡 Routes

See [routes.md](routes.md).

## 📄 Pages

Front-end only.

- 🏠 **Home page**: can have multiple sections, including:
  - Recommended jobs,
  - Applied jobs;
- 👤 **Profile page**: a user's profile page, which lists their information and
  their applications;
- 🔍 **Search page**: a page where the user can search for jobs;
- 📊 **Tracker page**: a page with a kanban board so the user can track their
  applications.
