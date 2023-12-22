// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Fis
{
    public static class GetTargetAccountConfiguration
    {
        /// <summary>
        /// Resource schema for AWS::FIS::TargetAccountConfiguration
        /// </summary>
        public static Task<GetTargetAccountConfigurationResult> InvokeAsync(GetTargetAccountConfigurationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTargetAccountConfigurationResult>("aws-native:fis:getTargetAccountConfiguration", args ?? new GetTargetAccountConfigurationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::FIS::TargetAccountConfiguration
        /// </summary>
        public static Output<GetTargetAccountConfigurationResult> Invoke(GetTargetAccountConfigurationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTargetAccountConfigurationResult>("aws-native:fis:getTargetAccountConfiguration", args ?? new GetTargetAccountConfigurationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTargetAccountConfigurationArgs : global::Pulumi.InvokeArgs
    {
        [Input("accountId", required: true)]
        public string AccountId { get; set; } = null!;

        [Input("experimentTemplateId", required: true)]
        public string ExperimentTemplateId { get; set; } = null!;

        public GetTargetAccountConfigurationArgs()
        {
        }
        public static new GetTargetAccountConfigurationArgs Empty => new GetTargetAccountConfigurationArgs();
    }

    public sealed class GetTargetAccountConfigurationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        [Input("experimentTemplateId", required: true)]
        public Input<string> ExperimentTemplateId { get; set; } = null!;

        public GetTargetAccountConfigurationInvokeArgs()
        {
        }
        public static new GetTargetAccountConfigurationInvokeArgs Empty => new GetTargetAccountConfigurationInvokeArgs();
    }


    [OutputType]
    public sealed class GetTargetAccountConfigurationResult
    {
        public readonly string? Description;
        public readonly string? RoleArn;

        [OutputConstructor]
        private GetTargetAccountConfigurationResult(
            string? description,

            string? roleArn)
        {
            Description = description;
            RoleArn = roleArn;
        }
    }
}
