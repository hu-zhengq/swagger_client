# IoArgoprojWorkflowV1alpha1GitArtifact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure_ignore_host_key** | **bool** | InsecureIgnoreHostKey disables SSH strict host key checking during git clone | [optional] 
**password_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 
**repo** | **str** | Repo is the git repository | 
**revision** | **str** | Revision is the git commit, tag, branch to checkout | [optional] 
**ssh_private_key_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 
**username_secret** | [**IoK8sApiCoreV1SecretKeySelector**](IoK8sApiCoreV1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

