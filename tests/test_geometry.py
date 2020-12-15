# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.geometry as geom


def test_exact_top_of_center_true_ok():
    assert geom.exact_top_of_center(270) is True


def test_exact_top_of_center_false_ok():
    assert geom.exact_top_of_center(270 + 1) is False


def test_exact_bottom_of_center_true_ok():
    assert geom.exact_bottom_of_center(90) is True


def test_exact_bottom_of_center_false_ok():
    assert geom.exact_bottom_of_center(90 + 1) is False


def test_right_bottom_of_center_true_ok():
    assert geom.right_bottom_of_center(90 - 1) is True


def test_right_bottom_of_center_false_ok():
    assert geom.right_bottom_of_center(90) is False


def test_right_top_of_center_true_ok():
    assert geom.right_top_of_center(270 + 1) is True


def test_right_top_of_center_false_ok():
    assert geom.right_top_of_center(270) is False


def test_left_bottom_of_center_true_ok():
    assert geom.left_bottom_of_center(90 + 1) is True


def test_left_bottom_of_center_false_ok():
    assert geom.left_bottom_of_center(90) is False


def test_left_bottom_of_center_true_other_ok():
    assert geom.left_bottom_of_center(180 - 1) is True


def test_left_bottom_of_center_false_other_ok():
    assert geom.left_bottom_of_center(180) is False


def test_left_top_of_center_true_ok():
    assert geom.left_top_of_center(180) is True


def test_left_top_of_center_false_ok():
    assert geom.left_top_of_center(180 - 1) is False


def test_left_top_of_center_true_other_ok():
    assert geom.left_top_of_center(270 - 1) is True


def test_left_top_of_center_false_other_ok():
    assert geom.left_top_of_center(270) is False


def test_left_top_of_center_bad_argument_nok():
    message = r"'<=' not supported between instances of 'int' and 'object'"
    with pytest.raises(TypeError, match=message):
        geom.left_top_of_center(object())


def test_octant_of_angle_for_n_ok():
    assert geom.octant_of_angle(270) == 'N'
