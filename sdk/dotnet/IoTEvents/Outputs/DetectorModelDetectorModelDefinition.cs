// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoTEvents.Outputs
{

    [OutputType]
    public sealed class DetectorModelDetectorModelDefinition
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename
        /// </summary>
        public readonly string? InitialStateName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-states
        /// </summary>
        public readonly ImmutableArray<Outputs.DetectorModelState> States;

        [OutputConstructor]
        private DetectorModelDetectorModelDefinition(
            string? InitialStateName,

            ImmutableArray<Outputs.DetectorModelState> States)
        {
            this.InitialStateName = InitialStateName;
            this.States = States;
        }
    }
}