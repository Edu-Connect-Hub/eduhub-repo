from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/eduhub_db"

engine = create_engine(URL)

Base = declarative_base()
#table for users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    applications = relationship("Application", back_populates="user")
    enrollments = relationship("Enrollment", back_populates="user")
    exams = relationship("Exam", back_populates="user")

#table for courses
class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_title = Column(String, nullable=False)
    instructor_name = Column(String, nullable=False)
    course_time = Column(String, nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")
    exams = relationship("Exam", back_populates="course")

#table for jobs
class Job(Base):
    __tablename__ = 'jobs_list'
    job_id = Column(Integer, primary_key=True)
    job_title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    applications = relationship("Application", back_populates="job")

#table for applicatin
class Application(Base):
    __tablename__ = 'applications'
    application_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    job_id = Column(Integer, ForeignKey('jobs_list.job_id'))
    status = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")


#table for enrollments
class Enrollment(Base):
    __tablename__ = 'enrollments'
    enroll_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    
    user = relationship('User', back_populates='enrollments')
    course = relationship("Course", back_populates='enrollments')

#table for exams
class Exam(Base):
    __tablename__ = 'exams'
    exam_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    exam_time = Column(String, nullable=False)
    percentage = Column(String, nullable=False)

    user = relationship("User", back_populates="exams")
    course = relationship("Course", back_populates="exams")
#it create tables in db
Base.metadata.create_all(engine)
