// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events
{
    public static class GetEventBus
    {
        /// <summary>
        /// Resource type definition for AWS::Events::EventBus
        /// </summary>
        public static Task<GetEventBusResult> InvokeAsync(GetEventBusArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEventBusResult>("aws-native:events:getEventBus", args ?? new GetEventBusArgs(), options.WithDefaults());

        /// <summary>
        /// Resource type definition for AWS::Events::EventBus
        /// </summary>
        public static Output<GetEventBusResult> Invoke(GetEventBusInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEventBusResult>("aws-native:events:getEventBus", args ?? new GetEventBusInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventBusArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the event bus.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetEventBusArgs()
        {
        }
        public static new GetEventBusArgs Empty => new GetEventBusArgs();
    }

    public sealed class GetEventBusInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the event bus.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetEventBusInvokeArgs()
        {
        }
        public static new GetEventBusInvokeArgs Empty => new GetEventBusInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventBusResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) for the event bus.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// A JSON string that describes the permission policy statement for the event bus.
        /// </summary>
        public readonly object? Policy;
        /// <summary>
        /// Any tags assigned to the event bus.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventBusTag> Tags;

        [OutputConstructor]
        private GetEventBusResult(
            string? arn,

            object? policy,

            ImmutableArray<Outputs.EventBusTag> tags)
        {
            Arn = arn;
            Policy = policy;
            Tags = tags;
        }
    }
}
