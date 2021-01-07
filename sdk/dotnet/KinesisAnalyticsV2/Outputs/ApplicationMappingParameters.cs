// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.KinesisAnalyticsV2.Outputs
{

    [OutputType]
    public sealed class ApplicationMappingParameters
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
        /// </summary>
        public readonly Outputs.ApplicationCSVMappingParameters? CSVMappingParameters;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
        /// </summary>
        public readonly Outputs.ApplicationJSONMappingParameters? JSONMappingParameters;

        [OutputConstructor]
        private ApplicationMappingParameters(
            Outputs.ApplicationCSVMappingParameters? CSVMappingParameters,

            Outputs.ApplicationJSONMappingParameters? JSONMappingParameters)
        {
            this.CSVMappingParameters = CSVMappingParameters;
            this.JSONMappingParameters = JSONMappingParameters;
        }
    }
}