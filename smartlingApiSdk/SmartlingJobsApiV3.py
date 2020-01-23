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

# JobsApiV3 class implementation

from .JobsApiV3 import JobsApiV3


class SmartlingJobsApiV3(JobsApiV3):
    """ Wrapper class providing access to jobs API commands, all methods below represent API commands.
        Each command returns tuple = (response, status_code)
        where response is ApiResponse object and status code = HTTP response status code

        ApiResponse object is python object as a result of json response parsing
        ApiResponse attributes depend on response json.
        To view all attributes of response use:
        for k,v in response.items(): print k, ':' ,v

        Response also can be a string to provide backward compatibility with previous versions
        in case you need json response as a string use :
        api = SmartlingJobsApi(userIdentifier, userSecret, projectId)
        api.response_as_string = True

        Some of methods may be called with optional parameters
        like `list` method may have locale optional parameter or offset parameter
        simple list:
             api.list()
        list with additional parameters:
             api.list(limit=100, offset=50)
        """

    def __init__(self, userIdentifier, userSecret, proxySettings=None):
        JobsApiV3.__init__(self, userIdentifier, userSecret, proxySettings)

    def list(self, projectId):
        """
        Returns a list of all jobs in a project
        returns (response, status_code) tuple
        Detail at https://api-reference.smartling.com/#operation/getJobsByProject
        """
        return self.commandJobList(projectId)

    def create(self, projectId, jobName, description, reference_number=None, callback_uri=None, callback_method=None,
               custom_fields=None):
        """
        Returns basic details on a specific Smartling project.
        returns (response, status_code) tuple
        for details see http://docs.smartling.com/pages/API/v2/Projects/Project-Details/
        """
        return self.commandJobCreate(projectId, jobName, description, reference_number, callback_uri, callback_method,
                                     custom_fields)

    def details(self, projectId, jobGuid):
        """
        Get details of a job
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobDetails(projectId, jobGuid)

    def delete(self, projectId, jobGuid):
        """
        Deletes a smartling job
        :param projectId:
        :param jobGuid:
        :return: delete jobs response
        """
        return self.commandJobDelete(projectId, jobGuid)

    def cancel(self, projectId, jobGuid):
        """
        Cancels an uncompleted job
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobCancel(projectId, jobGuid)

    def authorize(self, projectId, jobGuid):
        """
        Authorize a smartling job.
        This tells translators to start translating all untranslated strings from files associated with jobs
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobAuthorize(projectId, jobGuid)

    def list_files(self, projectId, jobGuid):
        """
        List files attached to job
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobListFiles(projectId, jobGuid)

    def progress(self, projectId, jobGuid):
        """
        Get job progress
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobProgress(projectId, jobGuid)

    def close(self, projectId, jobGuid):
        """
        Close a completed job (must be done once job is processed)
        :param projectId:
        :param jobGuid:
        :return:
        """
        return self.commandJobClose(projectId, jobGuid)

    def add_file(self, projectId, jobGuid, fileUri):
        """
        Adds a file to a job
        :param projectId:
        :param jobGuid:
        :param fileUri:
        :return:
        """
        return self.commandJobAddFile(projectId, jobGuid, fileUri)

    def create_custom_fields(self, account_id, field_name, description):
        """
        Creates account level custom fields that can be applied to jobs
        :param field_name:
        :param description:
        :param account_id:
        :return:
        """
        return self.commandCreateCustomFields(account_id, field_name, description)

    def list_account_custom_fields(self, account_id):
        """
        Creates account level custom fields that can be applied to jobs
        :param account_id:
        :return:
        """
        return self.commandListAccountCustomFields(account_id)

    def add_project_custom_field(self, projectId, fieldUid):
        """
        Adds custom field to project for use in jobs
        :param projectId
        :param fieldUid
        :return:
        """
        return self.commandAddCustomFieldToProject(projectId, fieldUid)

    def list_project_custom_fields(self, projectId):
        """
        Creates account level custom fields that can be applied to jobs
        :param projectId:
        :return:
        """
        return self.commandListProjectCustomFields(projectId)
