// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Inputs
{

    public sealed class DeploymentDeploymentCanarySettingsArgs : Pulumi.ResourceArgs
    {
        [Input("percentTraffic")]
        public Input<double>? PercentTraffic { get; set; }

        [Input("stageVariableOverrides")]
        public Input<object>? StageVariableOverrides { get; set; }

        [Input("useStageCache")]
        public Input<bool>? UseStageCache { get; set; }

        public DeploymentDeploymentCanarySettingsArgs()
        {
        }
    }
}
