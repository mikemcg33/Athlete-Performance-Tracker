from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    sport = Column(String, nullable=True)
    workouts = relationship("Workout", back_populates="athlete")


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"))
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    
    athlete = relationship("Athlete", back_populates="workouts")
    swimming = relationship("SwimmingWorkout", back_populates="workout", uselist=False)
    running = relationship("RunningWorkout", back_populates="workout", uselist=False)
    lifting = relationship("LiftingWorkout", back_populates="workout", uselist=False)


class SwimmingWorkout(Base):
    __tablename__ = "swimming_workouts"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    distance_meters = Column(Float)
    time_minutes = Column(Float)
    stroke = Column(String)

    workout = relationship("Workout", back_populates="swimming")


class RunningWorkout(Base):
    __tablename__ = "running_workouts"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    distance_km = Column(Float)
    time_minutes = Column(Float)
    terrain = Column(String)

    workout = relationship("Workout", back_populates="running")


class LiftingWorkout(Base):
    __tablename__ = "lifting_workouts"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    exercise = 1(String)
    weight_kg = Column(Float)
    reps = Column(Integer)
    sets = Column(Integer)

    workout = relationship("Workout", back_populates="lifting")