// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECS.Inputs
{

    public sealed class TaskDefinitionAuthorizationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessPointId")]
        public Input<string>? AccessPointId { get; set; }

        [Input("iAM")]
        public Input<Pulumi.AwsNative.ECS.TaskDefinitionAuthorizationConfigIAM>? IAM { get; set; }

        public TaskDefinitionAuthorizationConfigArgs()
        {
        }
        public static new TaskDefinitionAuthorizationConfigArgs Empty => new TaskDefinitionAuthorizationConfigArgs();
    }
}
