// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EFS.Inputs
{

    public sealed class FileSystemLifecyclePolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("transitionToIA")]
        public Input<string>? TransitionToIA { get; set; }

        [Input("transitionToPrimaryStorageClass")]
        public Input<string>? TransitionToPrimaryStorageClass { get; set; }

        public FileSystemLifecyclePolicyArgs()
        {
        }
        public static new FileSystemLifecyclePolicyArgs Empty => new FileSystemLifecyclePolicyArgs();
    }
}
