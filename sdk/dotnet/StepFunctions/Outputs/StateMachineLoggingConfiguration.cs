// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.StepFunctions.Outputs
{

    [OutputType]
    public sealed class StateMachineLoggingConfiguration
    {
        public readonly ImmutableArray<Outputs.StateMachineLogDestination> Destinations;
        public readonly bool? IncludeExecutionData;
        public readonly Pulumi.AwsNative.StepFunctions.StateMachineLoggingConfigurationLevel? Level;

        [OutputConstructor]
        private StateMachineLoggingConfiguration(
            ImmutableArray<Outputs.StateMachineLogDestination> destinations,

            bool? includeExecutionData,

            Pulumi.AwsNative.StepFunctions.StateMachineLoggingConfigurationLevel? level)
        {
            Destinations = destinations;
            IncludeExecutionData = includeExecutionData;
            Level = level;
        }
    }
}
