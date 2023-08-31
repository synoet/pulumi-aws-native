// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    /// <summary>
    /// A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.
    /// </summary>
    [AwsNativeResourceType("aws-native:vpclattice:TargetGroup")]
    public partial class TargetGroup : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("config")]
        public Output<Outputs.TargetGroupConfig?> Config { get; private set; } = null!;

        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        [Output("lastUpdatedAt")]
        public Output<string> LastUpdatedAt { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.VpcLattice.TargetGroupStatus> Status { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.TargetGroupTag>> Tags { get; private set; } = null!;

        [Output("targets")]
        public Output<ImmutableArray<Outputs.TargetGroupTarget>> Targets { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.VpcLattice.TargetGroupType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a TargetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TargetGroup(string name, TargetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:TargetGroup", name, args ?? new TargetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TargetGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:TargetGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "config.ipAddressType",
                    "config.port",
                    "config.protocol",
                    "config.protocolVersion",
                    "config.vpcIdentifier",
                    "name",
                    "type",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TargetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TargetGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TargetGroup(name, id, options);
        }
    }

    public sealed class TargetGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("config")]
        public Input<Inputs.TargetGroupConfigArgs>? Config { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.TargetGroupTagArgs>? _tags;
        public InputList<Inputs.TargetGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.TargetGroupTagArgs>());
            set => _tags = value;
        }

        [Input("targets")]
        private InputList<Inputs.TargetGroupTargetArgs>? _targets;
        public InputList<Inputs.TargetGroupTargetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.TargetGroupTargetArgs>());
            set => _targets = value;
        }

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.VpcLattice.TargetGroupType> Type { get; set; } = null!;

        public TargetGroupArgs()
        {
        }
        public static new TargetGroupArgs Empty => new TargetGroupArgs();
    }
}
