// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalytics.Inputs
{

    public sealed class ApplicationReferenceDataSourceMappingParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("cSVMappingParameters")]
        public Input<Inputs.ApplicationReferenceDataSourceCSVMappingParametersArgs>? CSVMappingParameters { get; set; }

        [Input("jSONMappingParameters")]
        public Input<Inputs.ApplicationReferenceDataSourceJSONMappingParametersArgs>? JSONMappingParameters { get; set; }

        public ApplicationReferenceDataSourceMappingParametersArgs()
        {
        }
        public static new ApplicationReferenceDataSourceMappingParametersArgs Empty => new ApplicationReferenceDataSourceMappingParametersArgs();
    }
}
