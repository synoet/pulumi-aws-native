// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GlobalAccelerator
{
    /// <summary>
    /// Resource Type definition for AWS::GlobalAccelerator::EndpointGroup
    /// </summary>
    [AwsNativeResourceType("aws-native:globalaccelerator:EndpointGroup")]
    public partial class EndpointGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The list of endpoint objects.
        /// </summary>
        [Output("endpointConfigurations")]
        public Output<ImmutableArray<Outputs.EndpointGroupEndpointConfiguration>> EndpointConfigurations { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the endpoint group
        /// </summary>
        [Output("endpointGroupArn")]
        public Output<string> EndpointGroupArn { get; private set; } = null!;

        /// <summary>
        /// The name of the AWS Region where the endpoint group is located
        /// </summary>
        [Output("endpointGroupRegion")]
        public Output<string> EndpointGroupRegion { get; private set; } = null!;

        /// <summary>
        /// The time in seconds between each health check for an endpoint. Must be a value of 10 or 30
        /// </summary>
        [Output("healthCheckIntervalSeconds")]
        public Output<int?> HealthCheckIntervalSeconds { get; private set; } = null!;

        [Output("healthCheckPath")]
        public Output<string?> HealthCheckPath { get; private set; } = null!;

        /// <summary>
        /// The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
        /// </summary>
        [Output("healthCheckPort")]
        public Output<int?> HealthCheckPort { get; private set; } = null!;

        /// <summary>
        /// The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
        /// </summary>
        [Output("healthCheckProtocol")]
        public Output<Pulumi.AwsNative.GlobalAccelerator.EndpointGroupHealthCheckProtocol?> HealthCheckProtocol { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the listener
        /// </summary>
        [Output("listenerArn")]
        public Output<string> ListenerArn { get; private set; } = null!;

        [Output("portOverrides")]
        public Output<ImmutableArray<Outputs.EndpointGroupPortOverride>> PortOverrides { get; private set; } = null!;

        /// <summary>
        /// The number of consecutive health checks required to set the state of the endpoint to unhealthy.
        /// </summary>
        [Output("thresholdCount")]
        public Output<int?> ThresholdCount { get; private set; } = null!;

        /// <summary>
        /// The percentage of traffic to sent to an AWS Region
        /// </summary>
        [Output("trafficDialPercentage")]
        public Output<double?> TrafficDialPercentage { get; private set; } = null!;


        /// <summary>
        /// Create a EndpointGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EndpointGroup(string name, EndpointGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:globalaccelerator:EndpointGroup", name, args ?? new EndpointGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EndpointGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:globalaccelerator:EndpointGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "endpointGroupRegion",
                    "listenerArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing EndpointGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EndpointGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EndpointGroup(name, id, options);
        }
    }

    public sealed class EndpointGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("endpointConfigurations")]
        private InputList<Inputs.EndpointGroupEndpointConfigurationArgs>? _endpointConfigurations;

        /// <summary>
        /// The list of endpoint objects.
        /// </summary>
        public InputList<Inputs.EndpointGroupEndpointConfigurationArgs> EndpointConfigurations
        {
            get => _endpointConfigurations ?? (_endpointConfigurations = new InputList<Inputs.EndpointGroupEndpointConfigurationArgs>());
            set => _endpointConfigurations = value;
        }

        /// <summary>
        /// The name of the AWS Region where the endpoint group is located
        /// </summary>
        [Input("endpointGroupRegion", required: true)]
        public Input<string> EndpointGroupRegion { get; set; } = null!;

        /// <summary>
        /// The time in seconds between each health check for an endpoint. Must be a value of 10 or 30
        /// </summary>
        [Input("healthCheckIntervalSeconds")]
        public Input<int>? HealthCheckIntervalSeconds { get; set; }

        [Input("healthCheckPath")]
        public Input<string>? HealthCheckPath { get; set; }

        /// <summary>
        /// The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
        /// </summary>
        [Input("healthCheckPort")]
        public Input<int>? HealthCheckPort { get; set; }

        /// <summary>
        /// The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
        /// </summary>
        [Input("healthCheckProtocol")]
        public Input<Pulumi.AwsNative.GlobalAccelerator.EndpointGroupHealthCheckProtocol>? HealthCheckProtocol { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the listener
        /// </summary>
        [Input("listenerArn", required: true)]
        public Input<string> ListenerArn { get; set; } = null!;

        [Input("portOverrides")]
        private InputList<Inputs.EndpointGroupPortOverrideArgs>? _portOverrides;
        public InputList<Inputs.EndpointGroupPortOverrideArgs> PortOverrides
        {
            get => _portOverrides ?? (_portOverrides = new InputList<Inputs.EndpointGroupPortOverrideArgs>());
            set => _portOverrides = value;
        }

        /// <summary>
        /// The number of consecutive health checks required to set the state of the endpoint to unhealthy.
        /// </summary>
        [Input("thresholdCount")]
        public Input<int>? ThresholdCount { get; set; }

        /// <summary>
        /// The percentage of traffic to sent to an AWS Region
        /// </summary>
        [Input("trafficDialPercentage")]
        public Input<double>? TrafficDialPercentage { get; set; }

        public EndpointGroupArgs()
        {
        }
        public static new EndpointGroupArgs Empty => new EndpointGroupArgs();
    }
}
