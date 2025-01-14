// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateCascadingControlSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("columnToMatch")]
        public Input<Inputs.TemplateColumnIdentifierArgs>? ColumnToMatch { get; set; }

        [Input("sourceSheetControlId")]
        public Input<string>? SourceSheetControlId { get; set; }

        public TemplateCascadingControlSourceArgs()
        {
        }
        public static new TemplateCascadingControlSourceArgs Empty => new TemplateCascadingControlSourceArgs();
    }
}
