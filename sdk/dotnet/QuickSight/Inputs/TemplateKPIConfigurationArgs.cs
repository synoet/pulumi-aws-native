// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateKPIConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldWells")]
        public Input<Inputs.TemplateKPIFieldWellsArgs>? FieldWells { get; set; }

        [Input("kPIOptions")]
        public Input<Inputs.TemplateKPIOptionsArgs>? KPIOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.TemplateKPISortConfigurationArgs>? SortConfiguration { get; set; }

        public TemplateKPIConfigurationArgs()
        {
        }
        public static new TemplateKPIConfigurationArgs Empty => new TemplateKPIConfigurationArgs();
    }
}
