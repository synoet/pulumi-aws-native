// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation
{
    /// <summary>
    /// Resource Type definition for AWS::CloudFormation::WaitCondition
    /// </summary>
    [Obsolete(@"WaitCondition is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:cloudformation:WaitCondition")]
    public partial class WaitCondition : Pulumi.CustomResource
    {
        [Output("count")]
        public Output<int?> Count { get; private set; } = null!;

        [Output("data")]
        public Output<object> Data { get; private set; } = null!;

        [Output("handle")]
        public Output<string?> Handle { get; private set; } = null!;

        [Output("timeout")]
        public Output<string?> Timeout { get; private set; } = null!;


        /// <summary>
        /// Create a WaitCondition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WaitCondition(string name, WaitConditionArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:WaitCondition", name, args ?? new WaitConditionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WaitCondition(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:WaitCondition", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing WaitCondition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WaitCondition Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new WaitCondition(name, id, options);
        }
    }

    public sealed class WaitConditionArgs : Pulumi.ResourceArgs
    {
        [Input("count")]
        public Input<int>? Count { get; set; }

        [Input("handle")]
        public Input<string>? Handle { get; set; }

        [Input("timeout")]
        public Input<string>? Timeout { get; set; }

        public WaitConditionArgs()
        {
        }
    }
}
