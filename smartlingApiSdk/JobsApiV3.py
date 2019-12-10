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

from .Constants import ReqMethod
from .Constants import Params
from .UrlV2Helper import UrlV2Helper
from .ApiV3 import ApiV3


class JobsApiV3(ApiV3):
    """ basic class implementing Jobs api calls """

    def __init__(self, userIdentifier, userSecret, proxySettings=None):
        ApiV3.__init__(self, userIdentifier, userSecret, proxySettings)
        self.urlHelper = UrlV2Helper(None)

    def commandJobList(self, projectId): #
        """ https://api-reference.smartling.com/#operation/getJobsByProject """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_LIST, projectId=projectId)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobCreate(self, projectId, name, description): #
        """ https://api-reference.smartling.com/#operation/addJob """
        kw = {}
        kw[Params.JOB_NAME] = name
        kw[Params.JOB_DESCRIPTION] = description
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CREATE, projectId=projectId)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobDetails(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/getJobDetails """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_DETAILS, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobDelete(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/deleteJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CREATE, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.DELETE, url, kw)

    def commandJobCancel(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/cancelJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CANCEL, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobAuthorize(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/authorizeJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_AUTHORIZE, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobListFiles(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/getJobFilesList """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_LIST_FILES, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobProgress(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/getJobFileProgress """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_PROGRESS, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobClose(self, projectId, jobGuid):
        """ https://api-reference.smartling.com/#operation/closeJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CLOSE, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobAddFile(self, projectId, jobGuid, fileUri):
        """ https://api-reference.smartling.com/#operation/addFileToJob """
        kw = {}
        kw[Params.FILE_URI] = fileUri
        kw[Params.JOB_TARGET_LOCALES] = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_ADD_FILE, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.POST, url, kw)
