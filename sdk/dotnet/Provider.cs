// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative
{
    /// <summary>
    /// The provider type for the AWS native package. By default, resources use package-wide configuration settings, however an explicit `Provider` instance may be created and passed during resource construction to achieve fine-grained programmatic control over provider settings. See the [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [AwsNativeResourceType("pulumi:providers:aws-native")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// The profile for API operations. If not set, the default profile created with `aws configure` will be used.
        /// </summary>
        [Output("profile")]
        public Output<string?> Profile { get; private set; } = null!;

        /// <summary>
        /// The region where AWS operations will take place. Examples are `us-east-1`, `us-west-2`, etc.
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. Note, this is a unique feature for server side security enforcement, not to be confused with assumeRole, which is used to obtain temporary client credentials. If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials instead.
        /// </summary>
        [Output("roleArn")]
        public Output<string?> RoleArn { get; private set; } = null!;

        /// <summary>
        /// The path to the shared credentials file. If not set this defaults to `~/.aws/credentials`.
        /// </summary>
        [Output("sharedCredentialsFile")]
        public Output<string?> SharedCredentialsFile { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("aws-native", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessKey")]
        private Input<string>? _accessKey;

        /// <summary>
        /// The access key for API operations. You can retrieve this from the ‘Security &amp; Credentials’ section of the AWS console.
        /// </summary>
        public Input<string>? AccessKey
        {
            get => _accessKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _accessKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("allowedAccountIds", json: true)]
        private InputList<string>? _allowedAccountIds;

        /// <summary>
        /// List of allowed AWS account IDs to prevent you from mistakenly using an incorrect one. Conflicts with `forbiddenAccountIds`.
        /// </summary>
        public InputList<string> AllowedAccountIds
        {
            get => _allowedAccountIds ?? (_allowedAccountIds = new InputList<string>());
            set => _allowedAccountIds = value;
        }

        /// <summary>
        /// Configuration for retrieving temporary credentials from the STS service.
        /// </summary>
        [Input("assumeRole", json: true)]
        public Input<Inputs.ProviderAssumeRoleArgs>? AssumeRole { get; set; }

        /// <summary>
        /// Configuration block with resource tag settings to apply across all resources handled by this provider. This is designed to replace redundant per-resource `tags` configurations. Provider tags can be overridden with new values, but not excluded from specific resources. To override provider tag values, use the `tags` argument within a resource to configure new tag values for matching keys.
        /// </summary>
        [Input("defaultTags", json: true)]
        public Input<Inputs.ProviderDefaultTagsArgs>? DefaultTags { get; set; }

        [Input("endpoints", json: true)]
        private InputList<Inputs.ProviderEndpointArgs>? _endpoints;

        /// <summary>
        /// Configuration block for customizing service endpoints.
        /// </summary>
        public InputList<Inputs.ProviderEndpointArgs> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<Inputs.ProviderEndpointArgs>());
            set => _endpoints = value;
        }

        [Input("forbiddenAccountIds", json: true)]
        private InputList<string>? _forbiddenAccountIds;

        /// <summary>
        /// List of forbidden AWS account IDs to prevent you from mistakenly using the wrong one (and potentially end up destroying a live environment). Conflicts with `allowedAccountIds`.
        /// </summary>
        public InputList<string> ForbiddenAccountIds
        {
            get => _forbiddenAccountIds ?? (_forbiddenAccountIds = new InputList<string>());
            set => _forbiddenAccountIds = value;
        }

        /// <summary>
        /// Configuration block with resource tag settings to ignore across all resources handled by this provider (except any individual service tag resources such as `ec2.Tag`) for situations where external systems are managing certain resource tags.
        /// </summary>
        [Input("ignoreTags", json: true)]
        public Input<Inputs.ProviderIgnoreTagsArgs>? IgnoreTags { get; set; }

        /// <summary>
        /// Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`.
        /// </summary>
        [Input("insecure", json: true)]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
        /// </summary>
        [Input("maxRetries", json: true)]
        public Input<int>? MaxRetries { get; set; }

        /// <summary>
        /// The profile for API operations. If not set, the default profile created with `aws configure` will be used.
        /// </summary>
        [Input("profile")]
        public Input<string>? Profile { get; set; }

        /// <summary>
        /// The region where AWS operations will take place. Examples are `us-east-1`, `us-west-2`, etc.
        /// </summary>
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. Note, this is a unique feature for server side security enforcement, not to be confused with assumeRole, which is used to obtain temporary client credentials. If you do not specify a role, Cloud Control API uses a temporary session created using your AWS user credentials instead.
        /// </summary>
        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        /// <summary>
        /// Set this to true to force the request to use path-style addressing, i.e., `http://s3.amazonaws.com/BUCKET/KEY`. By default, the S3 client will use virtual hosted bucket addressing when possible (`http://BUCKET.s3.amazonaws.com/KEY`). Specific to the Amazon S3 service.
        /// </summary>
        [Input("s3ForcePathStyle", json: true)]
        public Input<bool>? S3ForcePathStyle { get; set; }

        [Input("secretKey")]
        private Input<string>? _secretKey;

        /// <summary>
        /// The secret key for API operations. You can retrieve this from the 'Security &amp; Credentials' section of the AWS console.
        /// </summary>
        public Input<string>? SecretKey
        {
            get => _secretKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secretKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The path to the shared credentials file. If not set this defaults to `~/.aws/credentials`.
        /// </summary>
        [Input("sharedCredentialsFile")]
        public Input<string>? SharedCredentialsFile { get; set; }

        /// <summary>
        /// Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS available/implemented.
        /// </summary>
        [Input("skipCredentialsValidation", json: true)]
        public Input<bool>? SkipCredentialsValidation { get; set; }

        /// <summary>
        /// Skip getting the supported EC2 platforms. Used by users that don't have `ec2:DescribeAccountAttributes` permissions.
        /// </summary>
        [Input("skipGetEc2Platforms", json: true)]
        public Input<bool>? SkipGetEc2Platforms { get; set; }

        /// <summary>
        /// Skip the AWS Metadata API check. Useful for AWS API implementations that do not have a metadata API endpoint. Setting to true prevents Pulumi from authenticating via the Metadata API. You may need to use other authentication methods like static credentials, configuration variables, or environment variables.
        /// </summary>
        [Input("skipMetadataApiCheck", json: true)]
        public Input<bool>? SkipMetadataApiCheck { get; set; }

        /// <summary>
        /// Skip static validation of region name. Used by users of alternative AWS-like APIs or users with access to regions that are not public.
        /// </summary>
        [Input("skipRegionValidation", json: true)]
        public Input<bool>? SkipRegionValidation { get; set; }

        /// <summary>
        /// Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
        /// </summary>
        [Input("skipRequestingAccountId", json: true)]
        public Input<bool>? SkipRequestingAccountId { get; set; }

        [Input("token")]
        private Input<string>? _token;

        /// <summary>
        /// Session token for validating temporary credentials. Typically provided after successful identity federation or Multi-Factor Authentication (MFA) login. With MFA login, this is the session token provided afterward, not the 6 digit MFA code used to get temporary credentials.
        /// </summary>
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public ProviderArgs()
        {
            Profile = Utilities.GetEnv("AWS_PROFILE");
            Region = Utilities.GetEnv("AWS_REGION", "AWS_DEFAULT_REGION");
            SharedCredentialsFile = Utilities.GetEnv("AWS_SHARED_CREDENTIALS_FILE");
            SkipCredentialsValidation = true;
            SkipGetEc2Platforms = true;
            SkipMetadataApiCheck = true;
            SkipRegionValidation = true;
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
