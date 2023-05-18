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
    /// Resource Type definition for AWS::Connect::TaskTemplate.
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:TaskTemplate")]
    public partial class TaskTemplate : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The identifier (arn) of the task template.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        /// <summary>
        /// The constraints for the task template
        /// </summary>
        [Output("constraints")]
        public Output<Outputs.ConstraintsProperties?> Constraints { get; private set; } = null!;

        /// <summary>
        /// The identifier of the contact flow.
        /// </summary>
        [Output("contactFlowArn")]
        public Output<string?> ContactFlowArn { get; private set; } = null!;

        [Output("defaults")]
        public Output<ImmutableArray<Outputs.TaskTemplateDefaultFieldValue>> Defaults { get; private set; } = null!;

        /// <summary>
        /// The description of the task template.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The list of task template's fields
        /// </summary>
        [Output("fields")]
        public Output<ImmutableArray<Outputs.TaskTemplateField>> Fields { get; private set; } = null!;

        /// <summary>
        /// The identifier (arn) of the instance.
        /// </summary>
        [Output("instanceArn")]
        public Output<string> InstanceArn { get; private set; } = null!;

        /// <summary>
        /// The name of the task template.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.Connect.TaskTemplateStatus?> Status { get; private set; } = null!;

        /// <summary>
        /// One or more tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.TaskTemplateTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a TaskTemplate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TaskTemplate(string name, TaskTemplateArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:TaskTemplate", name, args ?? new TaskTemplateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TaskTemplate(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:TaskTemplate", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing TaskTemplate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TaskTemplate Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TaskTemplate(name, id, options);
        }
    }

    public sealed class TaskTemplateArgs : global::Pulumi.ResourceArgs
    {
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        /// <summary>
        /// The constraints for the task template
        /// </summary>
        [Input("constraints")]
        public Input<Inputs.ConstraintsPropertiesArgs>? Constraints { get; set; }

        /// <summary>
        /// The identifier of the contact flow.
        /// </summary>
        [Input("contactFlowArn")]
        public Input<string>? ContactFlowArn { get; set; }

        [Input("defaults")]
        private InputList<Inputs.TaskTemplateDefaultFieldValueArgs>? _defaults;
        public InputList<Inputs.TaskTemplateDefaultFieldValueArgs> Defaults
        {
            get => _defaults ?? (_defaults = new InputList<Inputs.TaskTemplateDefaultFieldValueArgs>());
            set => _defaults = value;
        }

        /// <summary>
        /// The description of the task template.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("fields")]
        private InputList<Inputs.TaskTemplateFieldArgs>? _fields;

        /// <summary>
        /// The list of task template's fields
        /// </summary>
        public InputList<Inputs.TaskTemplateFieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.TaskTemplateFieldArgs>());
            set => _fields = value;
        }

        /// <summary>
        /// The identifier (arn) of the instance.
        /// </summary>
        [Input("instanceArn", required: true)]
        public Input<string> InstanceArn { get; set; } = null!;

        /// <summary>
        /// The name of the task template.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("status")]
        public Input<Pulumi.AwsNative.Connect.TaskTemplateStatus>? Status { get; set; }

        [Input("tags")]
        private InputList<Inputs.TaskTemplateTagArgs>? _tags;

        /// <summary>
        /// One or more tags.
        /// </summary>
        public InputList<Inputs.TaskTemplateTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.TaskTemplateTagArgs>());
            set => _tags = value;
        }

        public TaskTemplateArgs()
        {
        }
        public static new TaskTemplateArgs Empty => new TaskTemplateArgs();
    }
}
