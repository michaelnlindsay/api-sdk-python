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


    # todo: get locale list from project details
    SUPPORTED_LOCALES = ["zh-CN","zh-TW","da-DK","nl-NL","en-GB","fr-FR","de-DE","id-ID","it-IT","ja-JP","ko-KR","ms-MY","nb-NO","pl-PL","pt-BR","ru-RU","es-LA","es-ES","sv-SE","th-TH","uk-UA"]

    def __init__(self, userIdentifier, userSecret, proxySettings=None):
        ApiV3.__init__(self, userIdentifier, userSecret, proxySettings)
        self.urlHelper = UrlV2Helper(None)

    def commandJobList(self, projectId): #
        """ https://api-reference.smartling.com/#operation/getJobsByProject """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_LIST, projectId=projectId)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobCreate(self, projectId, name, description, reference_number = None, callback_uri = None, callback_method = None, custom_fields = None): #
        """ https://api-reference.smartling.com/#operation/addJob """
        kw = {}
        kw[Params.JOB_NAME] = name
        kw[Params.JOB_DESCRIPTION] = description
        if reference_number:
            kw[Params.JOB_REFERENCE_NUMBER] = reference_number
        if callback_uri:
            kw[Params.JOB_CALLBACK_URL] = callback_uri
        if callback_method:
            kw[Params.JOB_CALLBACK_METHOD] = callback_method
        if custom_fields:
            kw[Params.JOB_CUSTOM_FIELDS] = custom_fields
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
        url = self.urlHelper.getUrl(self.urlHelper.JOB_DELETE, projectId=projectId, jobGuid=jobGuid)
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
        kw[Params.JOB_TARGET_LOCALES] = self.SUPPORTED_LOCALES
        url = self.urlHelper.getUrl(self.urlHelper.JOB_ADD_FILE, projectId=projectId, jobGuid=jobGuid)
        return self.command(ReqMethod.POST, url, kw)

    def commandCreateCustomFields(self, accountUid, custom_fields):
        """ https://api-reference.smartling.com/#operation/createCustomField """
        data = []
        for field_name in custom_fields:
            field = {
                "type": "SHORT_TEXT",
                "fieldName": field_name,
                "required": "false"
            }
            data.append(field)

        url = self.urlHelper.getUrl(self.urlHelper.ACCOUNT_FIELDS, accountUid=accountUid)
        return self.command(ReqMethod.POST, url, data)

    def commandListCustomFields(self, accountUid):
        """ https://api-reference.smartling.com/#operation/getAccountCustomFields """
        url = self.urlHelper.getUrl(self.urlHelper.ACCOUNT_FIELDS, accountUid=accountUid)
        return self.command(ReqMethod.GET, url, {})


"""
"data": {
"type": "SHORT_TEXT | LONG_TEXT | SELECTBOX | CHECKBOX",
"fieldName": "field-name",
"enabled": true,
"required": true,
"searchable": true,
"displayToTranslators": true,
"options": [],
"defaultValue": "default field value",
"description": "Custom field example"
}

"""


