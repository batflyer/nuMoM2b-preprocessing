# Copyright 2019 Alexander L. Hayes

"""
Test for the get_config module.
"""

import unittest

# Tests for:
from ... import get_config


class InitializeConfigurationTest(unittest.TestCase):
    def test_initialize_configuration_1(self):

        _expected = {
            "csv_path": "../Data/",
            "files": ["Visit1.csv", "Screening.csv"],
            "target": "pregnancy_outcomes.csv",
            "paths": ["../Data/Visit1.csv", "../Data/Screening.csv"],
        }
        _params = get_config.parameters(
            config="phi/unittests/config_tests/sample_config_files/config1.json"
        )

        self.assertEqual(_params, _expected)
