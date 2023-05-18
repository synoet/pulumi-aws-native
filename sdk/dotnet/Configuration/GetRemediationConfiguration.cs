// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Configuration
{
    public static class GetRemediationConfiguration
    {
        /// <summary>
        /// Resource Type definition for AWS::Config::RemediationConfiguration
        /// </summary>
        public static Task<GetRemediationConfigurationResult> InvokeAsync(GetRemediationConfigurationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRemediationConfigurationResult>("aws-native:configuration:getRemediationConfiguration", args ?? new GetRemediationConfigurationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Config::RemediationConfiguration
        /// </summary>
        public static Output<GetRemediationConfigurationResult> Invoke(GetRemediationConfigurationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRemediationConfigurationResult>("aws-native:configuration:getRemediationConfiguration", args ?? new GetRemediationConfigurationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRemediationConfigurationArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetRemediationConfigurationArgs()
        {
        }
        public static new GetRemediationConfigurationArgs Empty => new GetRemediationConfigurationArgs();
    }

    public sealed class GetRemediationConfigurationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetRemediationConfigurationInvokeArgs()
        {
        }
        public static new GetRemediationConfigurationInvokeArgs Empty => new GetRemediationConfigurationInvokeArgs();
    }


    [OutputType]
    public sealed class GetRemediationConfigurationResult
    {
        public readonly bool? Automatic;
        public readonly Outputs.RemediationConfigurationExecutionControls? ExecutionControls;
        public readonly string? Id;
        public readonly int? MaximumAutomaticAttempts;
        public readonly object? Parameters;
        public readonly string? ResourceType;
        public readonly int? RetryAttemptSeconds;
        public readonly string? TargetId;
        public readonly string? TargetType;
        public readonly string? TargetVersion;

        [OutputConstructor]
        private GetRemediationConfigurationResult(
            bool? automatic,

            Outputs.RemediationConfigurationExecutionControls? executionControls,

            string? id,

            int? maximumAutomaticAttempts,

            object? parameters,

            string? resourceType,

            int? retryAttemptSeconds,

            string? targetId,

            string? targetType,

            string? targetVersion)
        {
            Automatic = automatic;
            ExecutionControls = executionControls;
            Id = id;
            MaximumAutomaticAttempts = maximumAutomaticAttempts;
            Parameters = parameters;
            ResourceType = resourceType;
            RetryAttemptSeconds = retryAttemptSeconds;
            TargetId = targetId;
            TargetType = targetType;
            TargetVersion = targetVersion;
        }
    }
}
