# Copyright 2014 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import oslo_config.cfg
import oslo_utils.importutils

_volume_opts = [
    oslo_config.cfg.StrOpt('cluster_api_class',
                           default='meteos.cluster.sahara.API',
                           help='The full class name of the '
                           'Cluster API class to use.'),
]

oslo_config.cfg.CONF.register_opts(_volume_opts)


def API():
    importutils = oslo_utils.importutils
    cluster_api_class = oslo_config.cfg.CONF.cluster_api_class
    cls = importutils.import_class(cluster_api_class)
    return cls()
