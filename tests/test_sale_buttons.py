#!/usr/bin/env python
# This file is part sale_buttons module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class SaleButtonsTestCase(unittest.TestCase):
    'Test Sale Buttons module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_buttons')

    def test0005views(self):
        'Test views'
        test_view('sale_buttons')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleButtonsTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
