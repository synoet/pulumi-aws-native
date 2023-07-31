// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDB
{
    /// <summary>
    /// The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.
    /// </summary>
    [AwsNativeResourceType("aws-native:memorydb:ParameterGroup")]
    public partial class ParameterGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the parameter group.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description of the parameter group.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the parameter group family that this parameter group is compatible with.
        /// </summary>
        [Output("family")]
        public Output<string> Family { get; private set; } = null!;

        /// <summary>
        /// The name of the parameter group.
        /// </summary>
        [Output("parameterGroupName")]
        public Output<string> ParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.
        /// </summary>
        [Output("parameters")]
        public Output<object?> Parameters { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this parameter group.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ParameterGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ParameterGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ParameterGroup(string name, ParameterGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:memorydb:ParameterGroup", name, args ?? new ParameterGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ParameterGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:memorydb:ParameterGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ParameterGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ParameterGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ParameterGroup(name, id, options);
        }
    }

    public sealed class ParameterGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the parameter group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the parameter group family that this parameter group is compatible with.
        /// </summary>
        [Input("family", required: true)]
        public Input<string> Family { get; set; } = null!;

        /// <summary>
        /// The name of the parameter group.
        /// </summary>
        [Input("parameterGroupName")]
        public Input<string>? ParameterGroupName { get; set; }

        /// <summary>
        /// An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.
        /// </summary>
        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("tags")]
        private InputList<Inputs.ParameterGroupTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this parameter group.
        /// </summary>
        public InputList<Inputs.ParameterGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ParameterGroupTagArgs>());
            set => _tags = value;
        }

        public ParameterGroupArgs()
        {
        }
        public static new ParameterGroupArgs Empty => new ParameterGroupArgs();
    }
}
