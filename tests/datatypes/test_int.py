from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

import unittest


class IntTests(TranspileTestCase):
    @unittest.expectedFailure
    def test_setattr(self):
        self.assertCodeExecution("""
            x = 37
            x.attr = 42
            print('Done.')
            """)

    @unittest.expectedFailure
    def test_getattr(self):
        self.assertCodeExecution("""
            x = 37
            print(x.attr)
            print('Done.')
            """)

    def test_invalid_literal(self):
        self.assertCodeExecution("""
            int('q', 16)
            """, run_in_function=False)

    def test_addition_promotes_past_32bits(self):
        self.assertCodeExecution("""
            print(0x80000000 + 1)
            """)

    def test_addition_promotes_past_64bits(self):
        self.assertCodeExecution("""
            print(0x7fffffffffffffff + 2)
            """)

    def test_subtraction_promotes_past_32bits(self):
        self.assertCodeExecution("""
            print(-0x7fffffff - 3)
            """)

    def test_subtraction_promotes_past_64bits(self):
        self.assertCodeExecution("""
            print(-0x7fffffffffffffff - 3)
            """)

    def test_multiplication_promotes(self):
        self.assertCodeExecution("""
            print(2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2+1)
            """)

    def test_pow_promotes(self):
        self.assertCodeExecution("""
            print((2**1024)+1)
            """)


class UnaryIntOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'int'


class BinaryIntOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'int'

    not_implemented = [
        'test_add_complex',
        'test_add_frozenset',

        'test_and_frozenset',

        'test_eq_frozenset',

        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_bytearray',
        'test_ge_bytes',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',

        'test_gt_bytearray',
        'test_gt_bytes',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',

        'test_le_bytearray',
        'test_le_bytes',
        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',

        'test_lshift_frozenset',

        'test_lt_bytearray',
        'test_lt_bytes',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',

        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_ne_frozenset',

        'test_or_frozenset',

        'test_power_complex',
        'test_power_float',
        'test_power_frozenset',

        'test_rshift_frozenset',

        'test_subscr_frozenset',

        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_frozenset',
    ]


class InplaceIntOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'int'

    not_implemented = [
        'test_add_complex',
        'test_add_frozenset',

        'test_and_frozenset',

        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_frozenset',

        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_or_frozenset',

        'test_power_complex',
        'test_power_float',
        'test_power_frozenset',

        'test_rshift_int', # this works, but some of the cases are too large
                           # until we replace bignumber.js
        'test_rshift_frozenset',

        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_frozenset',
    ]
