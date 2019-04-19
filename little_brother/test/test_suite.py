#!/usr/bin/env python3 

# -*- coding: utf-8 -*-
#    Copyright (C) 2019  Marcus Rickert
#
#    See https://github.com/marcus67/little_brother
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest

from python_base_app import log_handling

from python_base_app.test import base_test

from little_brother.test import test_process_info
from little_brother.test import test_client_process_handler
from little_brother.test import test_audio_handler
from little_brother.test import test_german_vacation_context_rule_handler
from little_brother.test import test_simple_weekday_context_rule_handler
from little_brother.test import test_rule_handler
from little_brother.test import test_persistence
from little_brother.test import test_status_server

def add_test_cases(p_test_suite, p_config_filename=None):

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite, 
        p_test_unit_class=test_process_info.TestProcessInfo, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite, 
        p_test_unit_class=test_client_process_handler.TestClientProcessHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=test_audio_handler.TestAudioHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=test_german_vacation_context_rule_handler.TestGermanVacationContextRuleHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=test_simple_weekday_context_rule_handler.TestWeekDayContextRuleHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=test_rule_handler.TestRuleHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
         p_test_suite=p_test_suite,
         p_test_unit_class=test_persistence.TestPersistence, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=test_status_server.TestStatusServer, p_config_filename=p_config_filename)


def main():
    log_handling.start_logging(p_use_filter=False)
    test_suite = unittest.TestSuite()
    add_test_cases(p_test_suite=test_suite, p_config_filename=base_test.get_config_filename())
    base_test.run_test_suite(p_test_suite=test_suite)

if __name__ == '__main__':
    main()
    
    
    