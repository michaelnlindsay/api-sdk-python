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
    SUPPORTED_LOCALES = ["zh-CN", "zh-TW", "da-DK", "nl-NL", "en-GB", "fr-FR", "de-DE", "id-ID", "it-IT", "ja-JP",
                         "ko-KR", "ms-MY", "nb-NO", "pl-PL", "pt-BR", "ru-RU", "es-LA", "es-ES", "sv-SE", "th-TH",
                         "uk-UA"]

    def __init__(self, userIdentifier, userSecret, proxySettings=None):
        ApiV3.__init__(self, userIdentifier, userSecret, proxySettings)
        self.urlHelper = UrlV2Helper(None)

    def commandJobList(self, projectId, filterStatus=None):  #
        """ https://api-reference.smartling.com/#operation/getJobsByProject """
        kw = {}
        if filterStatus:
            kw[Params.JOB_TRANSLATION_STATUS] = filterStatus
        url = self.urlHelper.getUrl(self.urlHelper.JOB_LIST, projectId=projectId)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobCreate(self, projectId, name, description, reference_number=None, callback_uri=None,
                         callback_method=None, custom_fields=None):  #
        """ https://api-reference.smartling.com/#operation/addJob """
        kw = {}
        kw[Params.JOB_NAME] = name
        kw[Params.JOB_DESCRIPTION] = description
        kw[Params.JOB_TARGET_LOCALES] = self.SUPPORTED_LOCALES
        if reference_number:
            kw[Params.JOB_REFERENCE_NUMBER] = reference_number
        if callback_uri:
            kw[Params.JOB_CALLBACK_URL] = callback_uri
        if callback_method:
            kw[Params.JOB_CALLBACK_METHOD] = callback_method
        if custom_fields:
            kw[Params.JOB_CUSTOM_FIELDS] = custom_fields
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CREATE, projectId=projectId)
        print("add job request: ", url)
        print("add job payload: ", kw)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobDetails(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/getJobDetails """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_DETAILS, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobDelete(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/deleteJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_DELETE, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.DELETE, url, kw)

    def commandJobCancel(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/cancelJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CANCEL, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobAuthorize(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/authorizeJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_AUTHORIZE, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobListFiles(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/getJobFilesList """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_LIST_FILES, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobProgress(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/getJobFileProgress """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_PROGRESS, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.GET, url, kw)

    def commandJobClose(self, projectId, jobUid):
        """ https://api-reference.smartling.com/#operation/closeJob """
        kw = {}
        url = self.urlHelper.getUrl(self.urlHelper.JOB_CLOSE, projectId=projectId, jobUid=jobUid)
        return self.command(ReqMethod.POST, url, kw)

    def commandJobAddFile(self, projectId, jobUid, fileUri):
        """ https://api-reference.smartling.com/#operation/addFileToJob """
        kw = {}
        kw[Params.FILE_URI] = fileUri
        kw[Params.JOB_TARGET_LOCALES] = self.SUPPORTED_LOCALES
        url = self.urlHelper.getUrl(self.urlHelper.JOB_ADD_FILE, projectId=projectId, jobUid=jobUid)
        print("add file request: ", url)
        print("add file payload: ", kw)
        return self.command(ReqMethod.POST, url, kw)

    def commandCreateCustomFields(self, accountUid, field_name, description):
        """ https://api-reference.smartling.com/#operation/createCustomField """
        payload = {
            "type": "SHORT_TEXT",
            "fieldName": field_name,
            "enabled": "true",
            "required": "false",
            "searchable": "true",
            "displayToTranslators": "true",
            # "options": [
            #     [
            #         "option1",
            #         "option2"
            #     ]
            # ],
            # "defaultValue": "default field value",
            "description": description
        }

        url = self.urlHelper.getUrl(self.urlHelper.ACCOUNT_FIELDS, accountUid=accountUid)
        return self.command(ReqMethod.POST, url, payload)

    def commandListAccountCustomFields(self, accountUid):
        """ https://api-reference.smartling.com/#operation/getAccountCustomFields """
        url = self.urlHelper.getUrl(self.urlHelper.ACCOUNT_FIELDS, accountUid=accountUid)
        return self.command(ReqMethod.GET, url, {})

    def commandAddCustomFieldToProject(self, projectId, fieldUids):
        """ https://api-reference.smartling.com/#operation/assignCustomFieldsToProject """
        custom_fields = []
        fields = fieldUids.split(",")
        for field_id in fields:
            custom_fields.append({"fieldUid": field_id})
        url = self.urlHelper.getUrl(self.urlHelper.PROJECT_ADD_FIELDS, projectId=projectId)
        print("add job request: ", url)
        print("add job payload: ", custom_fields)
        return self.command(ReqMethod.POST, url, custom_fields)

    def commandListProjectCustomFields(self, projectId):
        """ https://api-reference.smartling.com/#operation/getProjectCustomFields """
        url = self.urlHelper.getUrl(self.urlHelper.PROJECT_FIELDS, projectId=projectId)
        return self.command(ReqMethod.GET, url, {})

    def commandCheckAsyncProcess(self, projectId, jobUid, processUid):
        """ https://api-reference.smartling.com/#operation/getJobAsyncProcessStatus """
        url = self.urlHelper.getUrl(self.urlHelper.PROCESS_STATUS, projectId=projectId, jobUid=jobUid, processUid=processUid)
