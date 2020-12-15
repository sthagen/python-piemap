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


def test_octant_of_angle_for_s_ok():
    assert geom.octant_of_angle(90) == 'S'


def test_octant_of_angle_for_e_ok():
    assert geom.octant_of_angle(0) == 'E'


def test_octant_of_angle_for_se_ok():
    assert geom.octant_of_angle(90 - 1) == 'SE'


def test_octant_of_angle_for_w_ok():
    assert geom.octant_of_angle(180) == 'W'


def test_octant_of_angle_for_nw_ok():
    assert geom.octant_of_angle(270 - 1) == 'NW'


def test_octant_of_angle_for_sw_ok():
    assert geom.octant_of_angle(90 + 1) == 'SW'


def test_octant_of_angle_for_ne_ok():
    assert geom.octant_of_angle(270 + 1) == 'NE'


def test_xy_point_from_radius_angle_minimal_ok():
    r, a, dx, dy = 1, 0, 0, 0
    x, y = 1, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_x_ok():
    r, a, dx, dy = 1, 0, 1, 0
    x, y = 2, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_y_ok():
    r, a, dx, dy = 1, 0, 0, 1
    x, y = 1, 1
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_angle_minimal_shift_x_y_ok():
    r, a, dx, dy = 1, 0, 1, 1
    x, y = 2, 1
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_all_zero_ok():
    r, a, dx, dy = 0, 0, 0, 0
    x, y = 0, 0
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_radius_zero_ok():
    r, a, dx, dy = 0, 1, 2, 3
    x, y = 2, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_angle_zero_ok():
    r, a, dx, dy = 1, 0, 2, 3
    x, y = 3, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_angle_negative_and_zero_radius_ok():
    r, a, dx, dy = 0, -1, 2, 3
    x, y = 2, 3
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_xy_point_from_angle_negative_ok():
    r, a, dx, dy = 1000, -360, 25, 14
    x, y = 1025, pytest.approx(14, abs=1e-11)
    assert geom.xy_point_from_radius_angle(r, a, dx, dy) == (x, y)


def test_segment_angle_map_one_ok():
    assert geom.segment_angle_map(1) == [(0, 360, 360)]


def test_segment_angle_map_two_ok():
    assert geom.segment_angle_map(2) == [(270, 90, 360), (90, 270, 180)]


def test_segment_angle_map_three_ok():
    assert geom.segment_angle_map(3) == [(300, 60, 360), (60, 180, 120), (180, 300, 240)]


def test_segment_angle_map_four_ok():
    assert geom.segment_angle_map(4) == [
        (315, 45, 360),
        (45, 135, 90),
        (135, 225, 180),
        (225, 315, 270)]


def test_segment_angle_map_five_ok():
    assert geom.segment_angle_map(5) == [
        (324, 36, 360),
        (36, 108, 72),
        (108, 180, 144),
        (180, 252, 216),
        (252, 324, 288)]


def test_segment_angle_map_six_ok():
    assert geom.segment_angle_map(6) == [
        (330, 30, 360),
        (30, 90, 60),
        (90, 150, 120),
        (150, 210, 180),
        (210, 270, 240),
        (270, 330, 300)] 


def test_segment_angle_map_seven_ok():
    assert geom.segment_angle_map(7) == [
        (pytest.approx(334.2857), pytest.approx(25.7143), 360),
        (pytest.approx(25.7143), pytest.approx(77.1429), pytest.approx(51.4286)),
        (pytest.approx(77.1429), pytest.approx(128.5714), pytest.approx(102.8571)),
        (pytest.approx(128.5714), 180, pytest.approx(154.2857)),
        (180, pytest.approx(231.4286), pytest.approx(205.7143)),
        (pytest.approx(231.4286), pytest.approx(282.8571), pytest.approx(257.1429)),
        (pytest.approx(282.8571), pytest.approx(334.2857), pytest.approx(308.5714))]


def test_segment_angle_map_eight_ok():
    assert geom.segment_angle_map(8) == [
        (337.5, 22.5, 360),
        (22.5, 67.5, 45),
        (67.5, 112.5, 90),
        (112.5, 157.5, 135),
        (157.5, 202.5, 180),
        (202.5, 247.5, 225),
        (247.5, 292.5, 270),
        (292.5, 337.5, 315)]


def test_segment_angle_map_nine_ok():
    assert geom.segment_angle_map(9) == [
        (340, 20, 360),
        (20, 60, 40),
        (60, 100, 80),
        (100, 140, 120),
        (140, 180, 160),
        (180, 220, 200),
        (220, 260, 240),
        (260, 300, 280),
        (300, 340, 320)]


def test_segment_angle_map_ten_ok():
    assert geom.segment_angle_map(10) == [
        (342, 18, 360),
        (18, 54, 36),
        (54, 90, 72),
        (90, 126, 108),
        (126, 162, 144),
        (162, 198, 180),
        (198, 234, 216),
        (234, 270, 252),
        (270, 306, 288),
        (306, 342, 324)]


def test_segment_angle_map_eleven_ok():
    assert geom.segment_angle_map(11) == [
        (343.6363636363636, 16.363636363636374, 360),
        (16.363636363636374, 49.09090909090912, 32.72727272727275),
        (49.09090909090912, 81.81818181818187, 65.4545454545455),
        (81.81818181818181, 114.5454545454545, 98.18181818181816),
        (114.54545454545456, 147.27272727272725, 130.9090909090909),
        (147.27272727272725, 180, 163.63636363636363),
        (180, 212.72727272727275, 196.36363636363637),
        (212.72727272727275, 245.4545454545455, 229.09090909090912),
        (245.4545454545455, 278.18181818181824, 261.81818181818187),
        (278.18181818181824, 310.909090909091, 294.5454545454546),
        (310.9090909090909, 343.6363636363636, 327.27272727272725)]


def test_segment_angle_map_twelve_ok():
    assert geom.segment_angle_map(12) == [
        (345, 15, 360),
        (15, 45, 30),
        (45, 75, 60),
        (75, 105, 90),
        (105, 135, 120),
        (135, 165, 150),
        (165, 195, 180),
        (195, 225, 210),
        (225, 255, 240),
        (255, 285, 270),
        (285, 315, 300),
        (315, 345, 330)]


def test_segment_angle_map_thirteen_ok():
    tol = 5e-3
    assert geom.segment_angle_map(13) == [
        (pytest.approx(346.1538, abs=tol), pytest.approx(13.8462, abs=tol), 360),
        (pytest.approx(13.8462, abs=tol), pytest.approx(41.5385, abs=tol), pytest.approx(27.6923, abs=tol)),
        (pytest.approx(41.5385, abs=tol), pytest.approx(69.2308, abs=tol), pytest.approx(55.3846, abs=tol)),
        (pytest.approx(69.2308, abs=tol), pytest.approx(96.9239, abs=tol), pytest.approx(83.0769, abs=tol)),
        (pytest.approx(96.9239, abs=tol), pytest.approx(124.6154, abs=tol), pytest.approx(110.7692, abs=tol)),
        (pytest.approx(124.6154, abs=tol), pytest.approx(152.3077, abs=tol), pytest.approx(138.4615, abs=tol)),
        (pytest.approx(152.3077, abs=tol), 180, pytest.approx(166.1538, abs=tol)),
        (180, pytest.approx(207.6923, abs=tol), pytest.approx(193.8462, abs=tol)),
        (pytest.approx(207.6923, abs=tol), pytest.approx(235.3846, abs=tol), pytest.approx(221.5385, abs=tol)),
        (pytest.approx(235.3846, abs=tol), pytest.approx(263.0769, abs=tol), pytest.approx(249.2308, abs=tol)),
        (pytest.approx(263.0769, abs=tol), pytest.approx(290.7692, abs=tol), pytest.approx(276.9231, abs=tol)),
        (pytest.approx(290.7692, abs=tol), pytest.approx(318.4615, abs=tol), pytest.approx(304.6154, abs=tol)),
        (pytest.approx(318.4615, abs=tol), pytest.approx(346.1538, abs=tol), pytest.approx(332.3077, abs=tol))]


def test_segment_angle_map_fourteen_ok():
    assert geom.segment_angle_map(14) == [
        (347.14285714285717, 12.85714285714289, 360),
        (12.857142857142833, 38.571428571428555, 25.714285714285694),
        (38.571428571428555, 64.28571428571428, 51.428571428571416),
        (64.28571428571428, 90, 77.14285714285714),
        (90, 115.71428571428572, 102.85714285714286),
        (115.71428571428572, 141.42857142857144, 128.57142857142858),
        (141.42857142857144, 167.1428571428571, 154.28571428571428),
        (167.1428571428571, 192.8571428571429, 180),
        (192.8571428571429, 218.57142857142867, 205.71428571428578),
        (218.57142857142856, 244.28571428571422, 231.4285714285714),
        (244.28571428571433, 270, 257.14285714285717),
        (270, 295.7142857142858, 282.8571428571429),
        (295.7142857142858, 321.42857142857156, 308.57142857142867),
        (321.42857142857144, 347.1428571428571, 334.2857142857143)]


def test_segment_angle_map_fifteen_ok():
    assert geom.segment_angle_map(15) == [
        (348, 12, 360),
        (12, 36, 24),
        (36, 60, 48),
        (60, 84, 72),
        (84, 108, 96),
        (108, 132, 120),
        (132, 156, 144),
        (156, 180, 168),
        (180, 204, 192),
        (204, 228, 216),
        (228, 252, 240),
        (252, 276, 264),
        (276, 300, 288),
        (300, 324, 312),
        (324, 348, 336)]


def test_segment_angle_map_sixteen_ok():
    assert geom.segment_angle_map(16) == [
        (348.75, 11.25, 360),
        (11.25, 33.75, 22.5),
        (33.75, 56.25, 45),
        (56.25, 78.75, 67.5),
        (78.75, 101.25, 90),
        (101.25, 123.75, 112.5),
        (123.75, 146.25, 135),
        (146.25, 168.75, 157.5),
        (168.75, 191.25, 180),
        (191.25, 213.75, 202.5),
        (213.75, 236.25, 225),
        (236.25, 258.75, 247.5),
        (258.75, 281.25, 270),
        (281.25, 303.75, 292.5),
        (303.75, 326.25, 315),
        (326.25, 348.75, 337.5)]


def test_transform_angle_map_ncw_icw_minimal_ok():
    assert geom.transform_angle_map_ncw_icw([(0, 360, 360)]) == [(270, 270, 270)]


def test_transform_angle_map_ncw_icw_minimal_idempotent_ok():
    assert geom.transform_angle_map_ncw_icw([(270, 270, 270)]) == [(270, 270, 270)]


def test_transform_angle_map_ncw_icw_two_ok():
    assert geom.transform_angle_map_ncw_icw([(270, 90, 360), (90, 270, 180)]) == [(180, 360, 270), (0, 180, 90)]


def test_transform_angle_map_ncw_icw_two_rotate_once_ok():
    assert geom.transform_angle_map_ncw_icw([(180, 360, 270), (0, 180, 90)]) == [(90, 270, 180), (270, 90, 360)]


def test_transform_angle_map_ncw_icw_two_rotate_twice_ok():
    assert geom.transform_angle_map_ncw_icw([(90, 270, 180), (270, 90, 360)]) == [(0, 180, 90), (180, 360, 270)]
