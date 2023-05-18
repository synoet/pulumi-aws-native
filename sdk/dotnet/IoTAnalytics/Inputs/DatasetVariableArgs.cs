// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class DatasetVariableArgs : global::Pulumi.ResourceArgs
    {
        [Input("datasetContentVersionValue")]
        public Input<Inputs.DatasetContentVersionValueArgs>? DatasetContentVersionValue { get; set; }

        [Input("doubleValue")]
        public Input<double>? DoubleValue { get; set; }

        [Input("outputFileUriValue")]
        public Input<Inputs.DatasetOutputFileUriValueArgs>? OutputFileUriValue { get; set; }

        [Input("stringValue")]
        public Input<string>? StringValue { get; set; }

        [Input("variableName", required: true)]
        public Input<string> VariableName { get; set; } = null!;

        public DatasetVariableArgs()
        {
        }
        public static new DatasetVariableArgs Empty => new DatasetVariableArgs();
    }
}
