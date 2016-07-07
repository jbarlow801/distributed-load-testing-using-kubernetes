#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def files_1st(self):
        self.client.get("/devops/forwarder/forward?uri=/files/1")

    @task(24)
    def files_25th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/25")

    @task(25)
    def files_50th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/50")

    @task(25)
    def files_75th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/75")

    @task(20)
    def files_95th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/95")

    @task(3)
    def files_98th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/98")

    @task(1)
    def files_99th(self):
        self.client.get("/devops/forwarder/forward?uri=/files/99")

    @task(1)
    def memory_1st(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/1")

    @task(24)
    def memory_25th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/25")

    @task(49)
    def memory_50th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/50")

    @task(25)
    def memory_75th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/75")

    @task(20)
    def memory_95th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/95")

    @task(3)
    def memory_98th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/98")

    @task(1)
    def memory_99th(self):
        self.client.get("/devops/forwarder/forward?uri=/memory/99")

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
