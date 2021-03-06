# Copyright (C) 2014 Universidad Politecnica de Madrid
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from keystoneclient.v3.contrib.fiware_roles import allowed
from keystoneclient.v3.contrib.fiware_roles import roles
from keystoneclient.v3.contrib.fiware_roles import role_assignments
from keystoneclient.v3.contrib.fiware_roles import permissions


class FiwareRolesManager(object):
     def __init__(self, api):
         self.roles = roles.RoleManager(api)
         self.permissions = permissions.PermissionManager(api)
         self.role_assignments = role_assignments.RoleAssignmentManager(api)
         self.allowed = allowed.AllowedManager(api)
  