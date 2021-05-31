#!/usr/bin/python3

import fitts_impl

#########################################
# Configuration options for experiment

#WINDOW_WIDTH = 800
#WINDOW_HEIGHT = 600

fitts_impl.AMPLITUDES = [64, 128, 256, 512]
fitts_impl.WIDTHS = [8, 16, 32]
fitts_impl.REPETITIONS = 8

#########################################

fitts_impl.main()

