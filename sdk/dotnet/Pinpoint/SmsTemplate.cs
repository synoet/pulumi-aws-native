// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint
{
    /// <summary>
    /// Resource Type definition for AWS::Pinpoint::SmsTemplate
    /// </summary>
    [Obsolete(@"SmsTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:pinpoint:SmsTemplate")]
    public partial class SmsTemplate : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("body")]
        public Output<string> Body { get; private set; } = null!;

        [Output("defaultSubstitutions")]
        public Output<string?> DefaultSubstitutions { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        [Output("templateDescription")]
        public Output<string?> TemplateDescription { get; private set; } = null!;

        [Output("templateName")]
        public Output<string> TemplateName { get; private set; } = null!;


        /// <summary>
        /// Create a SmsTemplate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SmsTemplate(string name, SmsTemplateArgs args, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:SmsTemplate", name, args ?? new SmsTemplateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SmsTemplate(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:SmsTemplate", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing SmsTemplate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SmsTemplate Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SmsTemplate(name, id, options);
        }
    }

    public sealed class SmsTemplateArgs : Pulumi.ResourceArgs
    {
        [Input("body", required: true)]
        public Input<string> Body { get; set; } = null!;

        [Input("defaultSubstitutions")]
        public Input<string>? DefaultSubstitutions { get; set; }

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        [Input("templateDescription")]
        public Input<string>? TemplateDescription { get; set; }

        [Input("templateName", required: true)]
        public Input<string> TemplateName { get; set; } = null!;

        public SmsTemplateArgs()
        {
        }
    }
}
