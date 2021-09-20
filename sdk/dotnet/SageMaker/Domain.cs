// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// Resource Type definition for AWS::SageMaker::Domain
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:Domain")]
    public partial class Domain : Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        /// </summary>
        [Output("appNetworkAccessType")]
        public Output<Pulumi.AwsNative.SageMaker.DomainAppNetworkAccessType?> AppNetworkAccessType { get; private set; } = null!;

        /// <summary>
        /// The mode of authentication that members use to access the domain.
        /// </summary>
        [Output("authMode")]
        public Output<Pulumi.AwsNative.SageMaker.DomainAuthMode> AuthMode { get; private set; } = null!;

        /// <summary>
        /// The default user settings.
        /// </summary>
        [Output("defaultUserSettings")]
        public Output<Outputs.DomainUserSettings> DefaultUserSettings { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the created domain.
        /// </summary>
        [Output("domainArn")]
        public Output<string> DomainArn { get; private set; } = null!;

        /// <summary>
        /// The domain name.
        /// </summary>
        [Output("domainId")]
        public Output<string> DomainId { get; private set; } = null!;

        /// <summary>
        /// A name for the domain.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon Elastic File System (EFS) managed by this Domain.
        /// </summary>
        [Output("homeEfsFileSystemId")]
        public Output<string> HomeEfsFileSystemId { get; private set; } = null!;

        /// <summary>
        /// SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The SSO managed application instance ID.
        /// </summary>
        [Output("singleSignOnManagedApplicationInstanceId")]
        public Output<string> SingleSignOnManagedApplicationInstanceId { get; private set; } = null!;

        /// <summary>
        /// The VPC subnets that Studio uses for communication.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// A list of tags to apply to the user profile.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DomainTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The URL to the created domain.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Domain", name, null, MakeResourceOptions(options, id))
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
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, options);
        }
    }

    public sealed class DomainArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
        /// </summary>
        [Input("appNetworkAccessType")]
        public Input<Pulumi.AwsNative.SageMaker.DomainAppNetworkAccessType>? AppNetworkAccessType { get; set; }

        /// <summary>
        /// The mode of authentication that members use to access the domain.
        /// </summary>
        [Input("authMode", required: true)]
        public Input<Pulumi.AwsNative.SageMaker.DomainAuthMode> AuthMode { get; set; } = null!;

        /// <summary>
        /// The default user settings.
        /// </summary>
        [Input("defaultUserSettings", required: true)]
        public Input<Inputs.DomainUserSettingsArgs> DefaultUserSettings { get; set; } = null!;

        /// <summary>
        /// A name for the domain.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        /// <summary>
        /// SageMaker uses AWS KMS to encrypt the EFS volume attached to the domain with an AWS managed customer master key (CMK) by default.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// The VPC subnets that Studio uses for communication.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.DomainTagArgs>? _tags;

        /// <summary>
        /// A list of tags to apply to the user profile.
        /// </summary>
        public InputList<Inputs.DomainTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DomainTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public DomainArgs()
        {
        }
    }
}
