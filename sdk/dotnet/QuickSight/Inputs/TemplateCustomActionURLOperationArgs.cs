// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateCustomActionURLOperationArgs : global::Pulumi.ResourceArgs
    {
        [Input("uRLTarget", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateURLTargetConfiguration> URLTarget { get; set; } = null!;

        [Input("uRLTemplate", required: true)]
        public Input<string> URLTemplate { get; set; } = null!;

        public TemplateCustomActionURLOperationArgs()
        {
        }
        public static new TemplateCustomActionURLOperationArgs Empty => new TemplateCustomActionURLOperationArgs();
    }
}
