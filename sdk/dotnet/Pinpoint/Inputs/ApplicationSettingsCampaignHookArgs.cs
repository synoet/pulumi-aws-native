// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Inputs
{

    public sealed class ApplicationSettingsCampaignHookArgs : Pulumi.ResourceArgs
    {
        [Input("lambdaFunctionName")]
        public Input<string>? LambdaFunctionName { get; set; }

        [Input("mode")]
        public Input<string>? Mode { get; set; }

        [Input("webUrl")]
        public Input<string>? WebUrl { get; set; }

        public ApplicationSettingsCampaignHookArgs()
        {
        }
    }
}
