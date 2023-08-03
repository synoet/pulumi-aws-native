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
    public sealed class TemplateCustomActionUrlOperation
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateUrlTargetConfiguration UrlTarget;
        public readonly string UrlTemplate;

        [OutputConstructor]
        private TemplateCustomActionUrlOperation(
            Pulumi.AwsNative.QuickSight.TemplateUrlTargetConfiguration urlTarget,

            string urlTemplate)
        {
            UrlTarget = urlTarget;
            UrlTemplate = urlTemplate;
        }
    }
}
