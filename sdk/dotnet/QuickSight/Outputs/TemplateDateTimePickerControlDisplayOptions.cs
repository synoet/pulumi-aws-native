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
    public sealed class TemplateDateTimePickerControlDisplayOptions
    {
        public readonly string? DateTimeFormat;
        public readonly Outputs.TemplateLabelOptions? TitleOptions;

        [OutputConstructor]
        private TemplateDateTimePickerControlDisplayOptions(
            string? dateTimeFormat,

            Outputs.TemplateLabelOptions? titleOptions)
        {
            DateTimeFormat = dateTimeFormat;
            TitleOptions = titleOptions;
        }
    }
}
