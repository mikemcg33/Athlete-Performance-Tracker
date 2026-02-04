# Previous READ.MD
# Athlete-Performance-Tracker
---

# Workout Application

A full-stack workout logging and analytics application that integrates Spotify listening data to explore relationships between music features and workout performance. The platform allows users to log workouts, attach music data, and visualize performance insights.

---

## Features (v1)

### User Authentication

* Local authentication using email and password
* One account per user
* JWT-based authentication for protected routes

---

### Workout Logging

Users can log structured workouts with the following attributes:

* Workout type: **Lift, Run, or Swim**
* Duration
* Optional distance (type-dependent)
* Rate of Perceived Exertion (RPE: 1–10)
* Optional notes

Each workout is stored in a base table with additional type-specific metrics stored separately.

---

### Spotify Integration

* Connect a Spotify account via OAuth 2.0
* Import recently played tracks
* Attach tracks to individual workouts
* Store Spotify audio features for analysis

---

### Basic Analytics

* Average BPM per workout
* Relationship between music energy and perceived exertion (RPE)
* Visualization of trends using charts

---

## Tech Stack

### Frontend

* React
* TypeScript
* Charting: Recharts or Chart.js

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### Authentication

* Email / password authentication
* JWT-based authorization

### Spotify

* Spotify Web API
* OAuth 2.0

---

## Database Schema

### Users

* **id** – unique user identifier
* **email** – user email (unique)
* **password_hash** – hashed password
* **created_at** – account creation timestamp

---

### Workouts (Base Table)

Stores core workout information common to all workout types.

* **id** – unique workout identifier
* **user_id** – references `Users.id`
* **type** – workout type (`lift`, `run`, `swim`)
* **duration_min** – workout duration in minutes
* **rpe** – rate of perceived exertion (1–10)
* **notes** – optional workout notes
* **created_at** – workout timestamp

Each workout has exactly one corresponding entry in a type-specific table below.

---

### Runs

* **workout_id** – references `Workouts.id`
* **distance_miles** – total distance
* **avg_pace** – average pace
* **avg_heart_rate** – average heart rate
* **elevation_gain** – total elevation gain

---

### Swims

* **workout_id** – references `Workouts.id`
* **distance_yards** – total distance
* **stroke** – primary stroke used
* **pool_length** – pool length
* **avg_pace_per_100** – average pace per 100 yards
* **avg_heart_rate** – average heart rate

---

### Lifts

* **workout_id** – references `Workouts.id`
* **total_sets** – total sets completed
* **total_reps** – total reps completed
* **total_volume** – total weight moved
* **primary_focus** – main muscle group or lift type

---

### Tracks

Stores Spotify track metadata and audio features.

* **id** – unique track identifier
* **spotify_track_id** – Spotify track ID
* **name** – track name
* **artist** – artist name
* **album** – album name
* **duration_ms** – track duration in milliseconds
* **explicit** – explicit content flag
* **bpm** – beats per minute
* **energy** – Spotify energy score
* **valence** – Spotify valence score

---

### Workout Tracks

Many-to-many relationship between workouts and tracks.

* **workout_id** – references `Workouts.id`
* **track_id** – references `Tracks.id`
* **play_order** – order tracks were played during the workout

---

### Spotify Accounts

Stores Spotify authentication data separately from user profiles.

* **user_id** – references `Users.id`
* **spotify_user_id** – Spotify account ID
* **access_token** – Spotify access token
* **refresh_token** – Spotify refresh token
* **expires_at** – token expiration timestamp

---

## Design Rationale

* Normalized relational schema with workout subtype tables
* Separation of authentication, workout data, and Spotify integration
* Supports analytics without excessive nullable fields
* Easily extensible to social features, additional workout types, or advanced analytics

---

# New READ.MD
# Training Performance Analytics

Backend system for tracking and analyzing athlete training data over time.

## Tech Stack
- Python
- FastAPI
- PostgreSQL (planned)

## Features (Planned)
- Store training sessions
- Track performance metrics
- Analyze trends over time

## Running the Project
```bash
uvicorn main:app --reload