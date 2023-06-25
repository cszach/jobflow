# Data model documentation

This document describes the data types for our project and what each data type
consists of. Each field is numbered so it may be referenced easily. If more
fields are to be added in the future, they should be appended to the end of the
list.

## User profile

A user profile has the following fields:

1. `id` (string)
2. `email` (string)
3. `name` (string)
4. `picture` (blob)
5. `bio` (string)
6. `location` (string)
7. `education` (string)
8. `experience` (array of experience)
9. `skills` (array of strings)
10. `interests` (array of strings)
11. `applications` (array of applications)
12. `notifications` (array of notifications)

At the moment, we need at least fields 1, 2, 3, 4, 5, 11, and 12. The rest is
useful for job matching (which is a feature that will be implemented later).

## Experience

An experience has the following fields:

1. `id` (string)
2. `title` (string)
3. `company` (company object)
4. `location` (string)
5. `start_date` (date)
6. `end_date` (date)
7. `description` (string)

## Company

A company has the following fields:

1. `id` (string)
2. `name` (string)
3. `logo` (blob)
4. `description` (string)
5. `location` (string)
6. `website` (string)

## Application

An application has the following fields:

1. `id` (string)
2. `job` (job object)
3. `status` (status)
4. `date` (date)

### Status

The status enumerates the following values: `applied`, `interview`, `offer`,
`rejected`.

We may consider more values such as `interview2`, `interview3`, `takehome`, etc.

## Job

A job object has the following fields:

1. `id` (string)
2. `title` (string)
3. `company` (company object)
4. `location` (string)
5. `description` (string)
6. `requirements` (string)
7. `date` (date)

## Notification

A notification object has the following fields:

1. `id` (string)
2. `title` (string)
3. `description` (string)
4. `date` (date)
