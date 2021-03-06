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


class IoArgoprojWorkflowV1alpha1S3Artifact(object):
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
        'access_key_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'bucket': 'str',
        'endpoint': 'str',
        'insecure': 'bool',
        'key': 'str',
        'region': 'str',
        'secret_key_secret': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'access_key_secret': 'accessKeySecret',
        'bucket': 'bucket',
        'endpoint': 'endpoint',
        'insecure': 'insecure',
        'key': 'key',
        'region': 'region',
        'secret_key_secret': 'secretKeySecret'
    }

    def __init__(self, access_key_secret=None, bucket=None, endpoint=None, insecure=None, key=None, region=None, secret_key_secret=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1S3Artifact - a model defined in Swagger"""  # noqa: E501
        self._access_key_secret = None
        self._bucket = None
        self._endpoint = None
        self._insecure = None
        self._key = None
        self._region = None
        self._secret_key_secret = None
        self.discriminator = None
        self.access_key_secret = access_key_secret
        self.bucket = bucket
        self.endpoint = endpoint
        if insecure is not None:
            self.insecure = insecure
        self.key = key
        if region is not None:
            self.region = region
        self.secret_key_secret = secret_key_secret

    @property
    def access_key_secret(self):
        """Gets the access_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501


        :return: The access_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, access_key_secret):
        """Sets the access_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.


        :param access_key_secret: The access_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """
        if access_key_secret is None:
            raise ValueError("Invalid value for `access_key_secret`, must not be `None`")  # noqa: E501

        self._access_key_secret = access_key_secret

    @property
    def bucket(self):
        """Gets the bucket of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501

        Bucket is the name of the bucket  # noqa: E501

        :return: The bucket of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this IoArgoprojWorkflowV1alpha1S3Artifact.

        Bucket is the name of the bucket  # noqa: E501

        :param bucket: The bucket of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """
        if bucket is None:
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def endpoint(self):
        """Gets the endpoint of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501

        Endpoint is the hostname of the bucket endpoint  # noqa: E501

        :return: The endpoint of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this IoArgoprojWorkflowV1alpha1S3Artifact.

        Endpoint is the hostname of the bucket endpoint  # noqa: E501

        :param endpoint: The endpoint of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def insecure(self):
        """Gets the insecure of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501

        Insecure will connect to the service with TLS  # noqa: E501

        :return: The insecure of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this IoArgoprojWorkflowV1alpha1S3Artifact.

        Insecure will connect to the service with TLS  # noqa: E501

        :param insecure: The insecure of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def key(self):
        """Gets the key of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501

        Key is the key in the bucket where the artifact resides  # noqa: E501

        :return: The key of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoArgoprojWorkflowV1alpha1S3Artifact.

        Key is the key in the bucket where the artifact resides  # noqa: E501

        :param key: The key of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def region(self):
        """Gets the region of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501

        Region contains the optional bucket region  # noqa: E501

        :return: The region of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this IoArgoprojWorkflowV1alpha1S3Artifact.

        Region contains the optional bucket region  # noqa: E501

        :param region: The region of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def secret_key_secret(self):
        """Gets the secret_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501


        :return: The secret_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._secret_key_secret

    @secret_key_secret.setter
    def secret_key_secret(self, secret_key_secret):
        """Sets the secret_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.


        :param secret_key_secret: The secret_key_secret of this IoArgoprojWorkflowV1alpha1S3Artifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """
        if secret_key_secret is None:
            raise ValueError("Invalid value for `secret_key_secret`, must not be `None`")  # noqa: E501

        self._secret_key_secret = secret_key_secret

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
        if issubclass(IoArgoprojWorkflowV1alpha1S3Artifact, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1S3Artifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
