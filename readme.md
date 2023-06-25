# 👔 Job application tracker

A job application tracking system for SWE students, by SWE students. Find jobs
that match your profile and apply! Track your progress from the resume round to
an offer!

## 🍔 Tech stack

- 📱 Front-end: React, Next.js, Material UI, Formik, JavaScript;
- ⚙️ Back-end: Django, Python, MongoDB Atlas;
- 🔑 Authentication: NextAuth.js;
- ☁️ Google Cloud products: ?;
- 🖥️ Deployment: Vercel.

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

## 🫒 Git branches

- `main`: The main branch. This branch is protected and can only be merged
  into when a new release of the app is ready via pull requests;
- `dev`: The development branch. This branch is protected and can only be
  merged into via pull requests;
- `<layer>/<type>/<description>`: An unprotected branch that will eventually get
  merged into `dev` where
  - `<layer>` is either `api` or `client`,
  - `<type>` is one of `feature`, `bugfix`, `hotfix`, `refactor`, `test`, or
    `docs`, and
  - `<description>` is a short 2-3 word description;
- `release/<version>`: A read-only branch that captures the state of the
  project at a particular release.

## 💬 Commit messages

We will be using the [Conventional Commits](https://www.conventionalcommits.org/).

In short, commit messages should be structured as follows:

```
<type><scope><exclamation mark>: <description>

<body>
```

where:

- `<type>` (**required**): one of `build`, `ci`, `docs`, `feat`, `fix`, `perf`,
  `refactor`, `revert`, `style`, `test`;
- `<scope>` (_optional_): a short description of the part of the project that is
  being changed and is enclosed in parentheses;
- `<exclamation mark>` (_optional_): an exclamation mark if the commit is a
  breaking change;
- `<description>` (**required**): a short description of the change;
- `<body>` (_optional_): the Git message body.

Examples (from the website):

```
feat: allow provided config object to extend other configs
```

```
feat!: send an email to the customer when a product is shipped
```

```
feat(api)!: send an email to the customer when a product is shipped
```

```
docs: correct spelling of CHANGELOG
```

Please visit the [Conventional Commits](https://www.conventionalcommits.org/)
website for more information.
