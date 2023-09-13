// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms
{
    public static class GetAnalysisTemplate
    {
        /// <summary>
        /// Represents a stored analysis within a collaboration
        /// </summary>
        public static Task<GetAnalysisTemplateResult> InvokeAsync(GetAnalysisTemplateArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAnalysisTemplateResult>("aws-native:cleanrooms:getAnalysisTemplate", args ?? new GetAnalysisTemplateArgs(), options.WithDefaults());

        /// <summary>
        /// Represents a stored analysis within a collaboration
        /// </summary>
        public static Output<GetAnalysisTemplateResult> Invoke(GetAnalysisTemplateInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAnalysisTemplateResult>("aws-native:cleanrooms:getAnalysisTemplate", args ?? new GetAnalysisTemplateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAnalysisTemplateArgs : global::Pulumi.InvokeArgs
    {
        [Input("analysisTemplateIdentifier", required: true)]
        public string AnalysisTemplateIdentifier { get; set; } = null!;

        [Input("membershipIdentifier", required: true)]
        public string MembershipIdentifier { get; set; } = null!;

        public GetAnalysisTemplateArgs()
        {
        }
        public static new GetAnalysisTemplateArgs Empty => new GetAnalysisTemplateArgs();
    }

    public sealed class GetAnalysisTemplateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("analysisTemplateIdentifier", required: true)]
        public Input<string> AnalysisTemplateIdentifier { get; set; } = null!;

        [Input("membershipIdentifier", required: true)]
        public Input<string> MembershipIdentifier { get; set; } = null!;

        public GetAnalysisTemplateInvokeArgs()
        {
        }
        public static new GetAnalysisTemplateInvokeArgs Empty => new GetAnalysisTemplateInvokeArgs();
    }


    [OutputType]
    public sealed class GetAnalysisTemplateResult
    {
        public readonly string? AnalysisTemplateIdentifier;
        public readonly string? Arn;
        public readonly string? CollaborationArn;
        public readonly string? CollaborationIdentifier;
        public readonly string? Description;
        public readonly string? MembershipArn;
        public readonly Outputs.AnalysisTemplateAnalysisSchema? Schema;
        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms analysis template.
        /// </summary>
        public readonly ImmutableArray<Outputs.AnalysisTemplateTag> Tags;

        [OutputConstructor]
        private GetAnalysisTemplateResult(
            string? analysisTemplateIdentifier,

            string? arn,

            string? collaborationArn,

            string? collaborationIdentifier,

            string? description,

            string? membershipArn,

            Outputs.AnalysisTemplateAnalysisSchema? schema,

            ImmutableArray<Outputs.AnalysisTemplateTag> tags)
        {
            AnalysisTemplateIdentifier = analysisTemplateIdentifier;
            Arn = arn;
            CollaborationArn = collaborationArn;
            CollaborationIdentifier = collaborationIdentifier;
            Description = description;
            MembershipArn = membershipArn;
            Schema = schema;
            Tags = tags;
        }
    }
}
