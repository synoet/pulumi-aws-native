// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class DomainEfsFileSystemConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("fileSystemId", required: true)]
        public Input<string> FileSystemId { get; set; } = null!;

        [Input("fileSystemPath")]
        public Input<string>? FileSystemPath { get; set; }

        public DomainEfsFileSystemConfigArgs()
        {
        }
        public static new DomainEfsFileSystemConfigArgs Empty => new DomainEfsFileSystemConfigArgs();
    }
}
