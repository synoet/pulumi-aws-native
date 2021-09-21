// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Inputs
{

    public sealed class MethodMethodResponseArgs : Pulumi.ResourceArgs
    {
        [Input("responseModels")]
        public Input<object>? ResponseModels { get; set; }

        [Input("responseParameters")]
        public Input<object>? ResponseParameters { get; set; }

        [Input("statusCode", required: true)]
        public Input<string> StatusCode { get; set; } = null!;

        public MethodMethodResponseArgs()
        {
        }
    }
}
