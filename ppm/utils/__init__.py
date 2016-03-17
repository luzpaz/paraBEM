from __future__ import division
import os
import numpy as np

import ppm


def check_path(path):
    _dir = os.path.dirname(path)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    return path


def vinf_deg_range2(v_inf, alpha0, alpha1, num=10):
    phi = np.linspace(np.deg2rad(alpha0), np.deg2rad(alpha1), num)
    return [abs(v_inf) * ppm.Vector2(np.cos(p), np.sin(p)) for p in phi]


def vinf_deg_range3(v_inf, alpha0, alpha1, num=10):
    phi = np.linspace(np.deg2rad(alpha0), np.deg2rad(alpha1), num)
    return [abs(v_inf) * ppm.Vector3(np.cos(p), 0, np.sin(p)) for p in phi]


def Vector(array, *args):
    if args:
        return Vector([array] + list(args))
    if len(array) == 2:
        return ppm.Vector2(*array)
    elif len(array) == 3:
        return ppm.Vector3(*array)
    else:
        raise AttributeError("array has too many values, 2d and 3d is supported")
