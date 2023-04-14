// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSM
{
    public static class GetResourceDataSync
    {
        /// <summary>
        /// Resource Type definition for AWS::SSM::ResourceDataSync
        /// </summary>
        public static Task<GetResourceDataSyncResult> InvokeAsync(GetResourceDataSyncArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetResourceDataSyncResult>("aws-native:ssm:getResourceDataSync", args ?? new GetResourceDataSyncArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SSM::ResourceDataSync
        /// </summary>
        public static Output<GetResourceDataSyncResult> Invoke(GetResourceDataSyncInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetResourceDataSyncResult>("aws-native:ssm:getResourceDataSync", args ?? new GetResourceDataSyncInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResourceDataSyncArgs : global::Pulumi.InvokeArgs
    {
        [Input("syncName", required: true)]
        public string SyncName { get; set; } = null!;

        public GetResourceDataSyncArgs()
        {
        }
        public static new GetResourceDataSyncArgs Empty => new GetResourceDataSyncArgs();
    }

    public sealed class GetResourceDataSyncInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("syncName", required: true)]
        public Input<string> SyncName { get; set; } = null!;

        public GetResourceDataSyncInvokeArgs()
        {
        }
        public static new GetResourceDataSyncInvokeArgs Empty => new GetResourceDataSyncInvokeArgs();
    }


    [OutputType]
    public sealed class GetResourceDataSyncResult
    {
        public readonly Outputs.ResourceDataSyncSyncSource? SyncSource;

        [OutputConstructor]
        private GetResourceDataSyncResult(Outputs.ResourceDataSyncSyncSource? syncSource)
        {
            SyncSource = syncSource;
        }
    }
}
