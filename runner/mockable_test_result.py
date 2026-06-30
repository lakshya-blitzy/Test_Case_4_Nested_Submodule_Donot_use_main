#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Needed to stop unittest.TestResult itself getting Mocked out of existence,
# which is a problem when testing the helper classes! (It confuses the runner)

class MockableTestResult(unittest.TestResult):
    '''
    Concrete ``unittest.TestResult`` subclass used throughout the runner.

    It adds no behaviour of its own (the body is simply ``pass``); its sole
    purpose is to provide a stable, non-mocked ``TestResult`` type. When
    the runner's own tests mock out ``unittest.TestResult``, ``Sensei``
    still inherits from this real class, so result handling keeps working
    instead of being "Mocked out of existence" (see the note above).

    Source: runner/mockable_test_result.py:L9-L21
    '''
    pass