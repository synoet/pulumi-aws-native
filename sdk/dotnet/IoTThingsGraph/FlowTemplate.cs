// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTThingsGraph
{
    /// <summary>
    /// Resource Type definition for AWS::IoTThingsGraph::FlowTemplate
    /// </summary>
    [Obsolete(@"FlowTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:iotthingsgraph:FlowTemplate")]
    public partial class FlowTemplate : Pulumi.CustomResource
    {
        [Output("compatibleNamespaceVersion")]
        public Output<double?> CompatibleNamespaceVersion { get; private set; } = null!;

        [Output("definition")]
        public Output<Outputs.FlowTemplateDefinitionDocument> Definition { get; private set; } = null!;


        /// <summary>
        /// Create a FlowTemplate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FlowTemplate(string name, FlowTemplateArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotthingsgraph:FlowTemplate", name, args ?? new FlowTemplateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FlowTemplate(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotthingsgraph:FlowTemplate", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing FlowTemplate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FlowTemplate Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FlowTemplate(name, id, options);
        }
    }

    public sealed class FlowTemplateArgs : Pulumi.ResourceArgs
    {
        [Input("compatibleNamespaceVersion")]
        public Input<double>? CompatibleNamespaceVersion { get; set; }

        [Input("definition", required: true)]
        public Input<Inputs.FlowTemplateDefinitionDocumentArgs> Definition { get; set; } = null!;

        public FlowTemplateArgs()
        {
        }
    }
}
