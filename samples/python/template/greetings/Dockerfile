#
# CAMP
#
# Copyright (C) 2017 -- 2019 SINTEF Digital
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.
#


FROM python:3.7-slim-stretch

COPY . /greetings

WORKDIR /greetings

RUN pip install .

CMD python greetings.py
