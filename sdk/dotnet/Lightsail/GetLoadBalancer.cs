// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    public static class GetLoadBalancer
    {
        /// <summary>
        /// Resource Type definition for AWS::Lightsail::LoadBalancer
        /// </summary>
        public static Task<GetLoadBalancerResult> InvokeAsync(GetLoadBalancerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLoadBalancerResult>("aws-native:lightsail:getLoadBalancer", args ?? new GetLoadBalancerArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Lightsail::LoadBalancer
        /// </summary>
        public static Output<GetLoadBalancerResult> Invoke(GetLoadBalancerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLoadBalancerResult>("aws-native:lightsail:getLoadBalancer", args ?? new GetLoadBalancerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLoadBalancerArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of your load balancer.
        /// </summary>
        [Input("loadBalancerName", required: true)]
        public string LoadBalancerName { get; set; } = null!;

        public GetLoadBalancerArgs()
        {
        }
        public static new GetLoadBalancerArgs Empty => new GetLoadBalancerArgs();
    }

    public sealed class GetLoadBalancerInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of your load balancer.
        /// </summary>
        [Input("loadBalancerName", required: true)]
        public Input<string> LoadBalancerName { get; set; } = null!;

        public GetLoadBalancerInvokeArgs()
        {
        }
        public static new GetLoadBalancerInvokeArgs Empty => new GetLoadBalancerInvokeArgs();
    }


    [OutputType]
    public sealed class GetLoadBalancerResult
    {
        /// <summary>
        /// The names of the instances attached to the load balancer.
        /// </summary>
        public readonly ImmutableArray<string> AttachedInstances;
        /// <summary>
        /// The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        /// </summary>
        public readonly string? HealthCheckPath;
        public readonly string? LoadBalancerArn;
        /// <summary>
        /// Configuration option to enable session stickiness.
        /// </summary>
        public readonly bool? SessionStickinessEnabled;
        /// <summary>
        /// Configuration option to adjust session stickiness cookie duration parameter.
        /// </summary>
        public readonly string? SessionStickinessLbCookieDurationSeconds;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.LoadBalancerTag> Tags;
        /// <summary>
        /// The name of the TLS policy to apply to the load balancer.
        /// </summary>
        public readonly string? TlsPolicyName;

        [OutputConstructor]
        private GetLoadBalancerResult(
            ImmutableArray<string> attachedInstances,

            string? healthCheckPath,

            string? loadBalancerArn,

            bool? sessionStickinessEnabled,

            string? sessionStickinessLbCookieDurationSeconds,

            ImmutableArray<Outputs.LoadBalancerTag> tags,

            string? tlsPolicyName)
        {
            AttachedInstances = attachedInstances;
            HealthCheckPath = healthCheckPath;
            LoadBalancerArn = loadBalancerArn;
            SessionStickinessEnabled = sessionStickinessEnabled;
            SessionStickinessLbCookieDurationSeconds = sessionStickinessLbCookieDurationSeconds;
            Tags = tags;
            TlsPolicyName = tlsPolicyName;
        }
    }
}
