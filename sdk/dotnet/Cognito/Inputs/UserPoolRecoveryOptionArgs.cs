// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolRecoveryOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("priority")]
        public Input<int>? Priority { get; set; }

        public UserPoolRecoveryOptionArgs()
        {
        }
        public static new UserPoolRecoveryOptionArgs Empty => new UserPoolRecoveryOptionArgs();
    }
}
