// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTableFieldLinkContentConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("customIconContent")]
        public Input<Inputs.TemplateTableFieldCustomIconContentArgs>? CustomIconContent { get; set; }

        [Input("customTextContent")]
        public Input<Inputs.TemplateTableFieldCustomTextContentArgs>? CustomTextContent { get; set; }

        public TemplateTableFieldLinkContentConfigurationArgs()
        {
        }
        public static new TemplateTableFieldLinkContentConfigurationArgs Empty => new TemplateTableFieldLinkContentConfigurationArgs();
    }
}
