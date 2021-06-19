"""Unit tests for schedule.py"""

import datetime
import time
import functools
import unittest
from unittest.mock import Mock
import crud

import schedule
from schedule import(
    every,
    repeat,
    ScheduleError,
    ScheduleValueError,
    IntervalError)

# def make_mock_job(name=None):
#     job = unittest.mock.Mock()
#     job.__name__ = name or "job"
#     return job

