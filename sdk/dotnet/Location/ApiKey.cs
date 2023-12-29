// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Location
{
    /// <summary>
    /// Definition of AWS::Location::APIKey Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:location:ApiKey")]
    public partial class ApiKey : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("expireTime")]
        public Output<string?> ExpireTime { get; private set; } = null!;

        [Output("forceDelete")]
        public Output<bool?> ForceDelete { get; private set; } = null!;

        [Output("forceUpdate")]
        public Output<bool?> ForceUpdate { get; private set; } = null!;

        [Output("keyArn")]
        public Output<string> KeyArn { get; private set; } = null!;

        [Output("keyName")]
        public Output<string> KeyName { get; private set; } = null!;

        [Output("noExpiry")]
        public Output<bool?> NoExpiry { get; private set; } = null!;

        [Output("restrictions")]
        public Output<Outputs.ApiKeyRestrictions> Restrictions { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ApiKeyTag>> Tags { get; private set; } = null!;

        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a ApiKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApiKey(string name, ApiKeyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:location:ApiKey", name, args ?? new ApiKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApiKey(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:location:ApiKey", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "keyName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ApiKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApiKey Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ApiKey(name, id, options);
        }
    }

    public sealed class ApiKeyArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("expireTime")]
        public Input<string>? ExpireTime { get; set; }

        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        [Input("forceUpdate")]
        public Input<bool>? ForceUpdate { get; set; }

        [Input("keyName", required: true)]
        public Input<string> KeyName { get; set; } = null!;

        [Input("noExpiry")]
        public Input<bool>? NoExpiry { get; set; }

        [Input("restrictions", required: true)]
        public Input<Inputs.ApiKeyRestrictionsArgs> Restrictions { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ApiKeyTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ApiKeyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ApiKeyTagArgs>());
            set => _tags = value;
        }

        public ApiKeyArgs()
        {
        }
        public static new ApiKeyArgs Empty => new ApiKeyArgs();
    }
}
