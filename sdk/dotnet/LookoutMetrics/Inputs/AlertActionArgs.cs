// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutMetrics.Inputs
{

    public sealed class AlertActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("lambdaConfiguration")]
        public Input<Inputs.AlertLambdaConfigurationArgs>? LambdaConfiguration { get; set; }

        [Input("snsConfiguration")]
        public Input<Inputs.AlertSnsConfigurationArgs>? SnsConfiguration { get; set; }

        public AlertActionArgs()
        {
        }
        public static new AlertActionArgs Empty => new AlertActionArgs();
    }
}
