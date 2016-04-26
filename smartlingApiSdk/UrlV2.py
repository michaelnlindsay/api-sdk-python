#!/usr/bin/python
# -*- coding: utf-8 -*-


''' Copyright 2012 Smartling, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this work except in compliance with the License.
 * You may obtain a copy of the License in the LICENSE file, or at:
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

class UrlV2:
    
    GET = "/files-api/v2/projects/{projectId}/locales/{localeId}/file"
    GET_MULTIPLE_LOCALES = "/files-api/v2/projects/{projectId}/files/zip"
    GET_ALL_LOCALES_ZIP = "/files-api/v2/projects/{projectId}/locales/all/file/zip"
    GET_ALL_LOCALES_CSV = "/files-api/v2/projects/{projectId}/locales/all/file"
    GET_ORIGINAL = "/files-api/v2/projects/{projectId}/file"
    LIST_FILES = "/files-api/v2/projects/{projectId}/files/list"
    LIST_FILE_TYPES = "/files-api/v2/projects/{projectId}/file-types"
    
    def __init__(self, projectId, localeId):
        self.projectId = projectId
        self.localeId = localeId

    def getUrl(self, urlWithPlaceholders):
        url = urlWithPlaceholders.replace("{projectId}", self.projectId)
        return url.replace("{localeId}", self.localeId)
