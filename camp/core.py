#
# CAMP
#
# Copyright (C) 2017, 2018 SINTEF Digital
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.
#



class Camp(object):


    def __init__(self, sfinder, sbuilder, ofinder, obuilder):
        self._find_stacks = sfinder
        self._build_stacks = sbuilder
        self._find_orchestrations = ofinder
        self._build_orchestrations = obuilder


    def generate(self, arguments):
        self._find_stacks(arguments)
        self._build_stacks(arguments)
        self._find_orchestrations(arguments)
        self._build_orchestrations(arguments)


    def realize(self, arguments):
        pass