// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    /// <summary>
    /// Resource Type definition for AWS::Connect::Instance
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:Instance")]
    public partial class Instance : global::Pulumi.CustomResource
    {
        /// <summary>
        /// An instanceArn is automatically generated on creation based on instanceId.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The attributes for the instance.
        /// </summary>
        [Output("attributes")]
        public Output<Outputs.InstanceAttributes> Attributes { get; private set; } = null!;

        /// <summary>
        /// Timestamp of instance creation logged as part of instance creation.
        /// </summary>
        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        /// <summary>
        /// Existing directoryId user wants to map to the new Connect instance.
        /// </summary>
        [Output("directoryId")]
        public Output<string?> DirectoryId { get; private set; } = null!;

        /// <summary>
        /// Specifies the type of directory integration for new instance.
        /// </summary>
        [Output("identityManagementType")]
        public Output<Pulumi.AwsNative.Connect.InstanceIdentityManagementType> IdentityManagementType { get; private set; } = null!;

        /// <summary>
        /// Alias of the new directory created as part of new instance creation.
        /// </summary>
        [Output("instanceAlias")]
        public Output<string?> InstanceAlias { get; private set; } = null!;

        /// <summary>
        /// Specifies the creation status of new instance.
        /// </summary>
        [Output("instanceStatus")]
        public Output<Pulumi.AwsNative.Connect.InstanceStatus> InstanceStatus { get; private set; } = null!;

        /// <summary>
        /// Service linked role created as part of instance creation.
        /// </summary>
        [Output("serviceRole")]
        public Output<string> ServiceRole { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.InstanceTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:Instance", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "directoryId",
                    "identityManagementType",
                    "instanceAlias",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, options);
        }
    }

    public sealed class InstanceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The attributes for the instance.
        /// </summary>
        [Input("attributes", required: true)]
        public Input<Inputs.InstanceAttributesArgs> Attributes { get; set; } = null!;

        /// <summary>
        /// Existing directoryId user wants to map to the new Connect instance.
        /// </summary>
        [Input("directoryId")]
        public Input<string>? DirectoryId { get; set; }

        /// <summary>
        /// Specifies the type of directory integration for new instance.
        /// </summary>
        [Input("identityManagementType", required: true)]
        public Input<Pulumi.AwsNative.Connect.InstanceIdentityManagementType> IdentityManagementType { get; set; } = null!;

        /// <summary>
        /// Alias of the new directory created as part of new instance creation.
        /// </summary>
        [Input("instanceAlias")]
        public Input<string>? InstanceAlias { get; set; }

        [Input("tags")]
        private InputList<Inputs.InstanceTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.InstanceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.InstanceTagArgs>());
            set => _tags = value;
        }

        public InstanceArgs()
        {
        }
        public static new InstanceArgs Empty => new InstanceArgs();
    }
}
