// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently
{
    public static class GetProject
    {
        /// <summary>
        /// Resource Type definition for AWS::Evidently::Project
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("aws-native:evidently:getProject", args ?? new GetProjectArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Evidently::Project
        /// </summary>
        public static Output<GetProjectResult> Invoke(GetProjectInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetProjectResult>("aws-native:evidently:getProject", args ?? new GetProjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProjectArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetProjectArgs()
        {
        }
        public static new GetProjectArgs Empty => new GetProjectArgs();
    }

    public sealed class GetProjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetProjectInvokeArgs()
        {
        }
        public static new GetProjectInvokeArgs Empty => new GetProjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        public readonly Outputs.ProjectAppConfigResourceObject? AppConfigResource;
        public readonly string? Arn;
        public readonly Outputs.ProjectDataDeliveryObject? DataDelivery;
        public readonly string? Description;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.ProjectTag> Tags;

        [OutputConstructor]
        private GetProjectResult(
            Outputs.ProjectAppConfigResourceObject? appConfigResource,

            string? arn,

            Outputs.ProjectDataDeliveryObject? dataDelivery,

            string? description,

            ImmutableArray<Outputs.ProjectTag> tags)
        {
            AppConfigResource = appConfigResource;
            Arn = arn;
            DataDelivery = dataDelivery;
            Description = description;
            Tags = tags;
        }
    }
}
