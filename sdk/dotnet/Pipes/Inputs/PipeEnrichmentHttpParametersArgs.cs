// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Inputs
{

    public sealed class PipeEnrichmentHttpParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("headerParameters")]
        public Input<Inputs.PipeHeaderParametersMapArgs>? HeaderParameters { get; set; }

        [Input("pathParameterValues")]
        private InputList<string>? _pathParameterValues;
        public InputList<string> PathParameterValues
        {
            get => _pathParameterValues ?? (_pathParameterValues = new InputList<string>());
            set => _pathParameterValues = value;
        }

        [Input("queryStringParameters")]
        public Input<Inputs.PipeQueryStringParametersMapArgs>? QueryStringParameters { get; set; }

        public PipeEnrichmentHttpParametersArgs()
        {
        }
        public static new PipeEnrichmentHttpParametersArgs Empty => new PipeEnrichmentHttpParametersArgs();
    }
}
