# coding: utf-8

"""
    Argo

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2.3.0-rc1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from kubernetes.client.models.v1_secret_key_selector import V1SecretKeySelector
#from swagger_client.models.io_k8s_api_core_v1_secret_key_selector import IoK8sApiCoreV1SecretKeySelector  # noqa: F401,E501


class IoArgoprojWorkflowV1alpha1GitArtifact(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'insecure_ignore_host_key': 'bool',
        'password_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'repo': 'str',
        'revision': 'str',
        'ssh_private_key_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'username_secret': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'insecure_ignore_host_key': 'insecureIgnoreHostKey',
        'password_secret': 'passwordSecret',
        'repo': 'repo',
        'revision': 'revision',
        'ssh_private_key_secret': 'sshPrivateKeySecret',
        'username_secret': 'usernameSecret'
    }

    def __init__(self, insecure_ignore_host_key=None, password_secret=None, repo=None, revision=None, ssh_private_key_secret=None, username_secret=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1GitArtifact - a model defined in Swagger"""  # noqa: E501
        self._insecure_ignore_host_key = None
        self._password_secret = None
        self._repo = None
        self._revision = None
        self._ssh_private_key_secret = None
        self._username_secret = None
        self.discriminator = None
        if insecure_ignore_host_key is not None:
            self.insecure_ignore_host_key = insecure_ignore_host_key
        if password_secret is not None:
            self.password_secret = password_secret
        self.repo = repo
        if revision is not None:
            self.revision = revision
        if ssh_private_key_secret is not None:
            self.ssh_private_key_secret = ssh_private_key_secret
        if username_secret is not None:
            self.username_secret = username_secret

    @property
    def insecure_ignore_host_key(self):
        """Gets the insecure_ignore_host_key of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501

        InsecureIgnoreHostKey disables SSH strict host key checking during git clone  # noqa: E501

        :return: The insecure_ignore_host_key of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_ignore_host_key

    @insecure_ignore_host_key.setter
    def insecure_ignore_host_key(self, insecure_ignore_host_key):
        """Sets the insecure_ignore_host_key of this IoArgoprojWorkflowV1alpha1GitArtifact.

        InsecureIgnoreHostKey disables SSH strict host key checking during git clone  # noqa: E501

        :param insecure_ignore_host_key: The insecure_ignore_host_key of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: bool
        """

        self._insecure_ignore_host_key = insecure_ignore_host_key

    @property
    def password_secret(self):
        """Gets the password_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501


        :return: The password_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """Sets the password_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.


        :param password_secret: The password_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._password_secret = password_secret

    @property
    def repo(self):
        """Gets the repo of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501

        Repo is the git repository  # noqa: E501

        :return: The repo of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this IoArgoprojWorkflowV1alpha1GitArtifact.

        Repo is the git repository  # noqa: E501

        :param repo: The repo of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: str
        """
        if repo is None:
            raise ValueError("Invalid value for `repo`, must not be `None`")  # noqa: E501

        self._repo = repo

    @property
    def revision(self):
        """Gets the revision of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501

        Revision is the git commit, tag, branch to checkout  # noqa: E501

        :return: The revision of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this IoArgoprojWorkflowV1alpha1GitArtifact.

        Revision is the git commit, tag, branch to checkout  # noqa: E501

        :param revision: The revision of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def ssh_private_key_secret(self):
        """Gets the ssh_private_key_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501


        :return: The ssh_private_key_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._ssh_private_key_secret

    @ssh_private_key_secret.setter
    def ssh_private_key_secret(self, ssh_private_key_secret):
        """Sets the ssh_private_key_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.


        :param ssh_private_key_secret: The ssh_private_key_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._ssh_private_key_secret = ssh_private_key_secret

    @property
    def username_secret(self):
        """Gets the username_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501


        :return: The username_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._username_secret

    @username_secret.setter
    def username_secret(self, username_secret):
        """Sets the username_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.


        :param username_secret: The username_secret of this IoArgoprojWorkflowV1alpha1GitArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._username_secret = username_secret

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoArgoprojWorkflowV1alpha1GitArtifact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoArgoprojWorkflowV1alpha1GitArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
