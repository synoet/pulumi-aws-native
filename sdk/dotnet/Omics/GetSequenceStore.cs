// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Omics
{
    public static class GetSequenceStore
    {
        /// <summary>
        /// Definition of AWS::Omics::SequenceStore Resource Type
        /// </summary>
        public static Task<GetSequenceStoreResult> InvokeAsync(GetSequenceStoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSequenceStoreResult>("aws-native:omics:getSequenceStore", args ?? new GetSequenceStoreArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::Omics::SequenceStore Resource Type
        /// </summary>
        public static Output<GetSequenceStoreResult> Invoke(GetSequenceStoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSequenceStoreResult>("aws-native:omics:getSequenceStore", args ?? new GetSequenceStoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSequenceStoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("sequenceStoreId", required: true)]
        public string SequenceStoreId { get; set; } = null!;

        public GetSequenceStoreArgs()
        {
        }
        public static new GetSequenceStoreArgs Empty => new GetSequenceStoreArgs();
    }

    public sealed class GetSequenceStoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("sequenceStoreId", required: true)]
        public Input<string> SequenceStoreId { get; set; } = null!;

        public GetSequenceStoreInvokeArgs()
        {
        }
        public static new GetSequenceStoreInvokeArgs Empty => new GetSequenceStoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetSequenceStoreResult
    {
        /// <summary>
        /// The store's ARN.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// When the store was created.
        /// </summary>
        public readonly string? CreationTime;
        public readonly string? SequenceStoreId;

        [OutputConstructor]
        private GetSequenceStoreResult(
            string? arn,

            string? creationTime,

            string? sequenceStoreId)
        {
            Arn = arn;
            CreationTime = creationTime;
            SequenceStoreId = sequenceStoreId;
        }
    }
}
