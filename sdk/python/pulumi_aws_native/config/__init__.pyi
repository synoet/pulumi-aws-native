# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

accessKey: Optional[str]
"""
The access key for API operations. You can retrieve this from the ‘Security & Credentials’ section of the AWS console.
"""

allowedAccountIds: Optional[str]
"""
List of allowed AWS account IDs to prevent you from mistakenly using an incorrect one. Conflicts with `forbiddenAccountIds`.
"""

assumeRole: Optional[str]
"""
Configuration for retrieving temporary credentials from the STS service.
"""

defaultTags: Optional[str]
"""
Configuration block with resource tag settings to apply across all resources handled by this provider. This is designed to replace redundant per-resource `tags` configurations. Provider tags can be overridden with new values, but not excluded from specific resources. To override provider tag values, use the `tags` argument within a resource to configure new tag values for matching keys.
"""

endpoints: Optional[str]
"""
Configuration block for customizing service endpoints.
"""

forbiddenAccountIds: Optional[str]
"""
List of forbidden AWS account IDs to prevent you from mistakenly using the wrong one (and potentially end up destroying a live environment). Conflicts with `allowedAccountIds`.
"""

ignoreTags: Optional[str]
"""
Configuration block with resource tag settings to ignore across all resources handled by this provider (except any individual service tag resources such as `ec2.Tag`) for situations where external systems are managing certain resource tags.
"""

insecure: Optional[bool]
"""
Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`.
"""

maxRetries: Optional[int]
"""
The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
"""

profile: Optional[str]
"""
The profile for API operations. If not set, the default profile created with `aws configure` will be used.
"""

region: Optional[str]
"""
The region where AWS operations will take place. Examples are `us-east-1`, `us-west-2`, etc.
"""

roleArn: Optional[str]
"""
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. Note, this is a unique feature for server side security enforcement, not to be confused with assumeRole, which is used to obtain temporary client credentials. If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials instead.
"""

s3ForcePathStyle: Optional[bool]
"""
Set this to true to force the request to use path-style addressing, i.e., `http://s3.amazonaws.com/BUCKET/KEY`. By default, the S3 client will use virtual hosted bucket addressing when possible (`http://BUCKET.s3.amazonaws.com/KEY`). Specific to the Amazon S3 service.
"""

secretKey: Optional[str]
"""
The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
"""

sharedCredentialsFile: Optional[str]
"""
The path to the shared credentials file. If not set this defaults to `~/.aws/credentials`.
"""

skipCredentialsValidation: bool
"""
Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented.
"""

skipGetEc2Platforms: bool
"""
Skip getting the supported EC2 platforms. Used by users that don't have `ec2:DescribeAccountAttributes` permissions.
"""

skipMetadataApiCheck: bool
"""
Skip the AWS Metadata API check. Useful for AWS API implementations that do not have a metadata API endpoint. Setting to true prevents Pulumi from authenticating via the Metadata API. You may need to use other authentication methods like static credentials, configuration variables, or environment variables.
"""

skipRegionValidation: bool
"""
Skip static validation of region name. Used by users of alternative AWS-like APIs or users with access to regions that are not public.
"""

skipRequestingAccountId: Optional[bool]
"""
Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
"""

token: Optional[str]
"""
Session token for validating temporary credentials. Typically provided after successful identity federation or Multi-Factor Authentication (MFA) login. With MFA login, this is the session token provided afterward, not the 6 digit MFA code used to get temporary credentials.
"""

