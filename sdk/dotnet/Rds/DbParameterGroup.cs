// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds
{
    /// <summary>
    /// The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:DbParameterGroup")]
    public partial class DbParameterGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies the name of the DB parameter group
        /// </summary>
        [Output("dbParameterGroupName")]
        public Output<string?> DbParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// Provides the customer-specified description for this DB parameter group.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The DB parameter group family name.
        /// </summary>
        [Output("family")]
        public Output<string> Family { get; private set; } = null!;

        /// <summary>
        /// An array of parameter names and values for the parameter update.
        /// </summary>
        [Output("parameters")]
        public Output<object?> Parameters { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DbParameterGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DbParameterGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DbParameterGroup(string name, DbParameterGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:rds:DbParameterGroup", name, args ?? new DbParameterGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DbParameterGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:DbParameterGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "dbParameterGroupName",
                    "description",
                    "family",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DbParameterGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DbParameterGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DbParameterGroup(name, id, options);
        }
    }

    public sealed class DbParameterGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the name of the DB parameter group
        /// </summary>
        [Input("dbParameterGroupName")]
        public Input<string>? DbParameterGroupName { get; set; }

        /// <summary>
        /// Provides the customer-specified description for this DB parameter group.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The DB parameter group family name.
        /// </summary>
        [Input("family", required: true)]
        public Input<string> Family { get; set; } = null!;

        /// <summary>
        /// An array of parameter names and values for the parameter update.
        /// </summary>
        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("tags")]
        private InputList<Inputs.DbParameterGroupTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.DbParameterGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DbParameterGroupTagArgs>());
            set => _tags = value;
        }

        public DbParameterGroupArgs()
        {
        }
        public static new DbParameterGroupArgs Empty => new DbParameterGroupArgs();
    }
}
