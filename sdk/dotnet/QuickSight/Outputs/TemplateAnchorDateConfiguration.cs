// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateAnchorDateConfiguration
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateAnchorOption? AnchorOption;
        public readonly string? ParameterName;

        [OutputConstructor]
        private TemplateAnchorDateConfiguration(
            Pulumi.AwsNative.QuickSight.TemplateAnchorOption? anchorOption,

            string? parameterName)
        {
            AnchorOption = anchorOption;
            ParameterName = parameterName;
        }
    }
}
