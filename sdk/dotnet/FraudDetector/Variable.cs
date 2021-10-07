// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FraudDetector
{
    /// <summary>
    /// A resource schema for a Variable in Amazon Fraud Detector.
    /// </summary>
    [AwsNativeResourceType("aws-native:frauddetector:Variable")]
    public partial class Variable : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the variable.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The time when the variable was created.
        /// </summary>
        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        /// <summary>
        /// The source of the data.
        /// </summary>
        [Output("dataSource")]
        public Output<Pulumi.AwsNative.FraudDetector.VariableDataSource> DataSource { get; private set; } = null!;

        /// <summary>
        /// The data type.
        /// </summary>
        [Output("dataType")]
        public Output<Pulumi.AwsNative.FraudDetector.VariableDataType> DataType { get; private set; } = null!;

        /// <summary>
        /// The default value for the variable when no value is received.
        /// </summary>
        [Output("defaultValue")]
        public Output<string> DefaultValue { get; private set; } = null!;

        /// <summary>
        /// The description.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The time when the variable was last updated.
        /// </summary>
        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        /// <summary>
        /// The name of the variable.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Tags associated with this variable.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.VariableTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        /// </summary>
        [Output("variableType")]
        public Output<Pulumi.AwsNative.FraudDetector.VariableType?> VariableType { get; private set; } = null!;


        /// <summary>
        /// Create a Variable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Variable(string name, VariableArgs args, CustomResourceOptions? options = null)
            : base("aws-native:frauddetector:Variable", name, args ?? new VariableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Variable(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:frauddetector:Variable", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Variable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Variable Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Variable(name, id, options);
        }
    }

    public sealed class VariableArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The source of the data.
        /// </summary>
        [Input("dataSource", required: true)]
        public Input<Pulumi.AwsNative.FraudDetector.VariableDataSource> DataSource { get; set; } = null!;

        /// <summary>
        /// The data type.
        /// </summary>
        [Input("dataType", required: true)]
        public Input<Pulumi.AwsNative.FraudDetector.VariableDataType> DataType { get; set; } = null!;

        /// <summary>
        /// The default value for the variable when no value is received.
        /// </summary>
        [Input("defaultValue", required: true)]
        public Input<string> DefaultValue { get; set; } = null!;

        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the variable.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.VariableTagArgs>? _tags;

        /// <summary>
        /// Tags associated with this variable.
        /// </summary>
        public InputList<Inputs.VariableTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.VariableTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        /// </summary>
        [Input("variableType")]
        public Input<Pulumi.AwsNative.FraudDetector.VariableType>? VariableType { get; set; }

        public VariableArgs()
        {
        }
    }
}
