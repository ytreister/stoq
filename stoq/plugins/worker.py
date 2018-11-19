#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    .. _worker:

    Overview
    ========

    Worker plugins are the primary data producers within `stoQ`. These plugins
    allow for tasks such as scanning payloads with yara, hashing payloads, and
    even extracting indicators of compromise (IOC) from documents. Worker plugins
    can be defined in all scanning modes. Additionally worker plugins can be
    dynamically loaded using dispatching plugins. More information on dispatcher
    plugins can be found in the :ref:`dispatcher plugin section <dispatcher>`.

    Worker plugins can be defined multiple ways. In these examples, we will use
    the ``hash`` worker plugin.

    From the command line, worker plugins can be defined two different ways,
    depending on the use.

    If *only* the original payload must be scanned, then ``--start-dispatch``
    or ``-s`` command line argument may be used.::

        $ stoq scan -s hash [...]

    However, if the original payload and all subsequent payloads must be scanned,
    the ``--always-dispatch`` or ``-a`` command line argument may be used::

        $ stoq scan -a hash [...]

    .. note:: The difference between ``--start-dispatch`` and ``--always-dispatch``
              can be somewhat confusing. The primary difference between the two is
              that if a worker plugin extracts any payloads for further scanning,
              any extracted payloads will only be scanned by workers defined by
              ``--always-dispatch``. If ``--start-dispatch`` was used, the plugin
              defined will not be used to scan any extracted payloads.

    Or, when instantiating the ``Stoq()`` class::

        import stoq
        workers= ['yara']
        s = Stoq(always_dispatch=workers, [...])

    Lastly, worker plugins can be defined by dispatcher plugins. As mentioned previously,
    more information on them can be found in the :ref:`dispatcher plugin section <dispatcher>`


    Extracted Payloads
    ------------------


    API
    ===

"""
from abc import abstractmethod
from typing import Optional

from stoq.data_classes import Payload, RequestMeta, WorkerResponse
from stoq.plugins import BasePlugin


class WorkerPlugin(BasePlugin):
    @abstractmethod
    def scan(
        self, payload: Payload, request_meta: RequestMeta
    ) -> Optional[WorkerResponse]:
        pass
