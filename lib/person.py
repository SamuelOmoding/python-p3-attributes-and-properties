#!/usr/bin/env python3
# List of approved jobs
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# Person class definition
class Person:
     # Class variable to store the list of approved jobs
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales",
                     "General Management", "Research & Development", "Marketing", "Purchasing"]

     # Constructor method
    def __init__(self, name="Juma", job="Customer Service"):
        self.name = name
        self.job = job

    # Getter and setter methods for the 'name' property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, job):
        # Checking if the name is a string and its length is between 1 and 25 characters
        if not isinstance(job, str) or not (1 <= len(job) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = job.title()

    # Getter and setter methods for the 'job' property
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        # Checking if the breed is in the list of approved jobs
        if job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    pass
