// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IAM.Inputs
{

    public sealed class RolePolicyArgs : Pulumi.ResourceArgs
    {
        [Input("policyDocument", required: true)]
        public Input<object> PolicyDocument { get; set; } = null!;

        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        public RolePolicyArgs()
        {
        }
    }
}
