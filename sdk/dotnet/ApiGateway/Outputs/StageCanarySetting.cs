// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Outputs
{

    [OutputType]
    public sealed class StageCanarySetting
    {
        public readonly string? DeploymentId;
        public readonly double? PercentTraffic;
        public readonly object? StageVariableOverrides;
        public readonly bool? UseStageCache;

        [OutputConstructor]
        private StageCanarySetting(
            string? deploymentId,

            double? percentTraffic,

            object? stageVariableOverrides,

            bool? useStageCache)
        {
            DeploymentId = deploymentId;
            PercentTraffic = percentTraffic;
            StageVariableOverrides = stageVariableOverrides;
            UseStageCache = useStageCache;
        }
    }
}
