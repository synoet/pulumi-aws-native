// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateSectionLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("freeFormLayout", required: true)]
        public Input<Inputs.TemplateFreeFormSectionLayoutConfigurationArgs> FreeFormLayout { get; set; } = null!;

        public TemplateSectionLayoutConfigurationArgs()
        {
        }
        public static new TemplateSectionLayoutConfigurationArgs Empty => new TemplateSectionLayoutConfigurationArgs();
    }
}
