// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3
{
    /// <summary>
    /// The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.
    /// </summary>
    [AwsNativeResourceType("aws-native:s3:AccessPoint")]
    public partial class AccessPoint : Pulumi.CustomResource
    {
        /// <summary>
        /// The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.
        /// </summary>
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the specified accesspoint.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The name of the bucket that you want to associate this Access Point with.
        /// </summary>
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        /// <summary>
        /// The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.
        /// </summary>
        [Output("networkOrigin")]
        public Output<Pulumi.AwsNative.S3.AccessPointNetworkOrigin> NetworkOrigin { get; private set; } = null!;

        /// <summary>
        /// The Access Point Policy you want to apply to this access point.
        /// </summary>
        [Output("policy")]
        public Output<object?> Policy { get; private set; } = null!;

        [Output("policyStatus")]
        public Output<object?> PolicyStatus { get; private set; } = null!;

        /// <summary>
        /// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        /// </summary>
        [Output("publicAccessBlockConfiguration")]
        public Output<Outputs.AccessPointPublicAccessBlockConfiguration?> PublicAccessBlockConfiguration { get; private set; } = null!;

        /// <summary>
        /// If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        /// </summary>
        [Output("vpcConfiguration")]
        public Output<Outputs.AccessPointVpcConfiguration?> VpcConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a AccessPoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AccessPoint(string name, AccessPointArgs args, CustomResourceOptions? options = null)
            : base("aws-native:s3:AccessPoint", name, args ?? new AccessPointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AccessPoint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:s3:AccessPoint", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing AccessPoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AccessPoint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AccessPoint(name, id, options);
        }
    }

    public sealed class AccessPointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the bucket that you want to associate this Access Point with.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// The Access Point Policy you want to apply to this access point.
        /// </summary>
        [Input("policy")]
        public Input<object>? Policy { get; set; }

        [Input("policyStatus")]
        public Input<object>? PolicyStatus { get; set; }

        /// <summary>
        /// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        /// </summary>
        [Input("publicAccessBlockConfiguration")]
        public Input<Inputs.AccessPointPublicAccessBlockConfigurationArgs>? PublicAccessBlockConfiguration { get; set; }

        /// <summary>
        /// If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        /// </summary>
        [Input("vpcConfiguration")]
        public Input<Inputs.AccessPointVpcConfigurationArgs>? VpcConfiguration { get; set; }

        public AccessPointArgs()
        {
        }
    }
}
