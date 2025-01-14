// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.StepFunctions
{
    public static class GetStateMachineAlias
    {
        /// <summary>
        /// Resource schema for StateMachineAlias
        /// </summary>
        public static Task<GetStateMachineAliasResult> InvokeAsync(GetStateMachineAliasArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStateMachineAliasResult>("aws-native:stepfunctions:getStateMachineAlias", args ?? new GetStateMachineAliasArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for StateMachineAlias
        /// </summary>
        public static Output<GetStateMachineAliasResult> Invoke(GetStateMachineAliasInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStateMachineAliasResult>("aws-native:stepfunctions:getStateMachineAlias", args ?? new GetStateMachineAliasInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStateMachineAliasArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the alias.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetStateMachineAliasArgs()
        {
        }
        public static new GetStateMachineAliasArgs Empty => new GetStateMachineAliasArgs();
    }

    public sealed class GetStateMachineAliasInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the alias.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetStateMachineAliasInvokeArgs()
        {
        }
        public static new GetStateMachineAliasInvokeArgs Empty => new GetStateMachineAliasInvokeArgs();
    }


    [OutputType]
    public sealed class GetStateMachineAliasResult
    {
        /// <summary>
        /// The ARN of the alias.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// An optional description of the alias.
        /// </summary>
        public readonly string? Description;
        public readonly ImmutableArray<Outputs.StateMachineAliasRoutingConfigurationVersion> RoutingConfiguration;

        [OutputConstructor]
        private GetStateMachineAliasResult(
            string? arn,

            string? description,

            ImmutableArray<Outputs.StateMachineAliasRoutingConfigurationVersion> routingConfiguration)
        {
            Arn = arn;
            Description = description;
            RoutingConfiguration = routingConfiguration;
        }
    }
}
