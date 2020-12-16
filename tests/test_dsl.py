# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl

DEFAULT_TEXT = """\
SHOW_TITLE;A title for the plot
SHOW_VALUE;1
SHOW_MIN;0
0;D1F;FOLDED;;12;15;6;dB
2;D3F;FOLDED;;12;15;NULL;1
1;D2F;FOLDED;;12;15;12;V
;D4F;FOLDED;;12;15;16;dB
;D5F;FOLDED;;12;15;18;dB
;D6F;FOLDED;;12;15;22;dB
;D7B;BIMONOTONE;0;80;100;40;%;SHOW_MIN
;D8L;;;1;2;0.5;#
;D9F;FOLDED;;12;15;12;dB
;D10L;;;1;2;0.25;ms
;D11L;;;2;1;0.8;kbit/s
;D12L;;;0.8;1;NULL;s
"""


def test_dumps_stub_ok():
    assert dsl.dumps({}) == "{}"


def test_loads_stub_ok():
    assert dsl.loads("") is NotImplemented


def test_parse_default():
    assert dsl.parse(DEFAULT_TEXT) is True
