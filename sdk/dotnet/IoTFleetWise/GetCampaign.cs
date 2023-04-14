// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise
{
    public static class GetCampaign
    {
        /// <summary>
        /// Definition of AWS::IoTFleetWise::Campaign Resource Type
        /// </summary>
        public static Task<GetCampaignResult> InvokeAsync(GetCampaignArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCampaignResult>("aws-native:iotfleetwise:getCampaign", args ?? new GetCampaignArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::IoTFleetWise::Campaign Resource Type
        /// </summary>
        public static Output<GetCampaignResult> Invoke(GetCampaignInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCampaignResult>("aws-native:iotfleetwise:getCampaign", args ?? new GetCampaignInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCampaignArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetCampaignArgs()
        {
        }
        public static new GetCampaignArgs Empty => new GetCampaignArgs();
    }

    public sealed class GetCampaignInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetCampaignInvokeArgs()
        {
        }
        public static new GetCampaignInvokeArgs Empty => new GetCampaignInvokeArgs();
    }


    [OutputType]
    public sealed class GetCampaignResult
    {
        public readonly string? Arn;
        public readonly string? CreationTime;
        public readonly ImmutableArray<string> DataExtraDimensions;
        public readonly string? Description;
        public readonly string? LastModificationTime;
        public readonly ImmutableArray<Outputs.CampaignSignalInformation> SignalsToCollect;
        public readonly Pulumi.AwsNative.IoTFleetWise.CampaignStatus? Status;
        public readonly ImmutableArray<Outputs.CampaignTag> Tags;

        [OutputConstructor]
        private GetCampaignResult(
            string? arn,

            string? creationTime,

            ImmutableArray<string> dataExtraDimensions,

            string? description,

            string? lastModificationTime,

            ImmutableArray<Outputs.CampaignSignalInformation> signalsToCollect,

            Pulumi.AwsNative.IoTFleetWise.CampaignStatus? status,

            ImmutableArray<Outputs.CampaignTag> tags)
        {
            Arn = arn;
            CreationTime = creationTime;
            DataExtraDimensions = dataExtraDimensions;
            Description = description;
            LastModificationTime = lastModificationTime;
            SignalsToCollect = signalsToCollect;
            Status = status;
            Tags = tags;
        }
    }
}
