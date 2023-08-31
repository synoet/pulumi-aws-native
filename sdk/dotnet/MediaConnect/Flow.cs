// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect
{
    /// <summary>
    /// Resource schema for AWS::MediaConnect::Flow
    /// </summary>
    [AwsNativeResourceType("aws-native:mediaconnect:Flow")]
    public partial class Flow : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string?> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
        /// </summary>
        [Output("flowArn")]
        public Output<string> FlowArn { get; private set; } = null!;

        /// <summary>
        /// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)
        /// </summary>
        [Output("flowAvailabilityZone")]
        public Output<string> FlowAvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The name of the flow.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The source of the flow.
        /// </summary>
        [Output("source")]
        public Output<Outputs.FlowSource> Source { get; private set; } = null!;

        /// <summary>
        /// The source failover config of the flow.
        /// </summary>
        [Output("sourceFailoverConfig")]
        public Output<Outputs.FlowFailoverConfig?> SourceFailoverConfig { get; private set; } = null!;


        /// <summary>
        /// Create a Flow resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Flow(string name, FlowArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:Flow", name, args ?? new FlowArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Flow(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:Flow", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "availabilityZone",
                    "name",
                    "source.name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Flow resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Flow Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Flow(name, id, options);
        }
    }

    public sealed class FlowArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The name of the flow.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The source of the flow.
        /// </summary>
        [Input("source", required: true)]
        public Input<Inputs.FlowSourceArgs> Source { get; set; } = null!;

        /// <summary>
        /// The source failover config of the flow.
        /// </summary>
        [Input("sourceFailoverConfig")]
        public Input<Inputs.FlowFailoverConfigArgs>? SourceFailoverConfig { get; set; }

        public FlowArgs()
        {
        }
        public static new FlowArgs Empty => new FlowArgs();
    }
}
