// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::Bucket
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:Bucket")]
    public partial class Bucket : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.
        /// </summary>
        [Output("ableToUpdateBundle")]
        public Output<bool> AbleToUpdateBundle { get; private set; } = null!;

        [Output("accessRules")]
        public Output<Outputs.BucketAccessRules?> AccessRules { get; private set; } = null!;

        [Output("bucketArn")]
        public Output<string> BucketArn { get; private set; } = null!;

        /// <summary>
        /// The name for the bucket.
        /// </summary>
        [Output("bucketName")]
        public Output<string> BucketName { get; private set; } = null!;

        /// <summary>
        /// The ID of the bundle to use for the bucket.
        /// </summary>
        [Output("bundleId")]
        public Output<string> BundleId { get; private set; } = null!;

        /// <summary>
        /// Specifies whether to enable or disable versioning of objects in the bucket.
        /// </summary>
        [Output("objectVersioning")]
        public Output<bool?> ObjectVersioning { get; private set; } = null!;

        /// <summary>
        /// An array of strings to specify the AWS account IDs that can access the bucket.
        /// </summary>
        [Output("readOnlyAccessAccounts")]
        public Output<ImmutableArray<string>> ReadOnlyAccessAccounts { get; private set; } = null!;

        /// <summary>
        /// The names of the Lightsail resources for which to set bucket access.
        /// </summary>
        [Output("resourcesReceivingAccess")]
        public Output<ImmutableArray<string>> ResourcesReceivingAccess { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.BucketTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The URL of the bucket.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a Bucket resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Bucket(string name, BucketArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Bucket", name, args ?? new BucketArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Bucket(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Bucket", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "bucketName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Bucket resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Bucket Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Bucket(name, id, options);
        }
    }

    public sealed class BucketArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessRules")]
        public Input<Inputs.BucketAccessRulesArgs>? AccessRules { get; set; }

        /// <summary>
        /// The name for the bucket.
        /// </summary>
        [Input("bucketName")]
        public Input<string>? BucketName { get; set; }

        /// <summary>
        /// The ID of the bundle to use for the bucket.
        /// </summary>
        [Input("bundleId", required: true)]
        public Input<string> BundleId { get; set; } = null!;

        /// <summary>
        /// Specifies whether to enable or disable versioning of objects in the bucket.
        /// </summary>
        [Input("objectVersioning")]
        public Input<bool>? ObjectVersioning { get; set; }

        [Input("readOnlyAccessAccounts")]
        private InputList<string>? _readOnlyAccessAccounts;

        /// <summary>
        /// An array of strings to specify the AWS account IDs that can access the bucket.
        /// </summary>
        public InputList<string> ReadOnlyAccessAccounts
        {
            get => _readOnlyAccessAccounts ?? (_readOnlyAccessAccounts = new InputList<string>());
            set => _readOnlyAccessAccounts = value;
        }

        [Input("resourcesReceivingAccess")]
        private InputList<string>? _resourcesReceivingAccess;

        /// <summary>
        /// The names of the Lightsail resources for which to set bucket access.
        /// </summary>
        public InputList<string> ResourcesReceivingAccess
        {
            get => _resourcesReceivingAccess ?? (_resourcesReceivingAccess = new InputList<string>());
            set => _resourcesReceivingAccess = value;
        }

        [Input("tags")]
        private InputList<Inputs.BucketTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.BucketTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.BucketTagArgs>());
            set => _tags = value;
        }

        public BucketArgs()
        {
        }
        public static new BucketArgs Empty => new BucketArgs();
    }
}
