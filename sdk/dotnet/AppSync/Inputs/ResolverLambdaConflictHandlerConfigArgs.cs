// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync.Inputs
{

    public sealed class ResolverLambdaConflictHandlerConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("lambdaConflictHandlerArn")]
        public Input<string>? LambdaConflictHandlerArn { get; set; }

        public ResolverLambdaConflictHandlerConfigArgs()
        {
        }
        public static new ResolverLambdaConflictHandlerConfigArgs Empty => new ResolverLambdaConflictHandlerConfigArgs();
    }
}
