// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancing
{
    /// <summary>
    /// Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer
    /// </summary>
    [Obsolete(@"LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:elasticloadbalancing:LoadBalancer")]
    public partial class LoadBalancer : global::Pulumi.CustomResource
    {
        [Output("accessLoggingPolicy")]
        public Output<Outputs.LoadBalancerAccessLoggingPolicy?> AccessLoggingPolicy { get; private set; } = null!;

        [Output("appCookieStickinessPolicy")]
        public Output<ImmutableArray<Outputs.LoadBalancerAppCookieStickinessPolicy>> AppCookieStickinessPolicy { get; private set; } = null!;

        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        [Output("canonicalHostedZoneName")]
        public Output<string> CanonicalHostedZoneName { get; private set; } = null!;

        [Output("canonicalHostedZoneNameId")]
        public Output<string> CanonicalHostedZoneNameId { get; private set; } = null!;

        [Output("connectionDrainingPolicy")]
        public Output<Outputs.LoadBalancerConnectionDrainingPolicy?> ConnectionDrainingPolicy { get; private set; } = null!;

        [Output("connectionSettings")]
        public Output<Outputs.LoadBalancerConnectionSettings?> ConnectionSettings { get; private set; } = null!;

        [Output("crossZone")]
        public Output<bool?> CrossZone { get; private set; } = null!;

        [Output("dnsName")]
        public Output<string> DnsName { get; private set; } = null!;

        [Output("healthCheck")]
        public Output<Outputs.LoadBalancerHealthCheck?> HealthCheck { get; private set; } = null!;

        [Output("instances")]
        public Output<ImmutableArray<string>> Instances { get; private set; } = null!;

        [Output("lbCookieStickinessPolicy")]
        public Output<ImmutableArray<Outputs.LoadBalancerLBCookieStickinessPolicy>> LbCookieStickinessPolicy { get; private set; } = null!;

        [Output("listeners")]
        public Output<ImmutableArray<Outputs.LoadBalancerListeners>> Listeners { get; private set; } = null!;

        [Output("loadBalancerName")]
        public Output<string?> LoadBalancerName { get; private set; } = null!;

        [Output("policies")]
        public Output<ImmutableArray<Outputs.LoadBalancerPolicies>> Policies { get; private set; } = null!;

        [Output("scheme")]
        public Output<string?> Scheme { get; private set; } = null!;

        [Output("securityGroups")]
        public Output<ImmutableArray<string>> SecurityGroups { get; private set; } = null!;

        [Output("sourceSecurityGroupGroupName")]
        public Output<string?> SourceSecurityGroupGroupName { get; private set; } = null!;

        [Output("sourceSecurityGroupOwnerAlias")]
        public Output<string?> SourceSecurityGroupOwnerAlias { get; private set; } = null!;

        [Output("subnets")]
        public Output<ImmutableArray<string>> Subnets { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.LoadBalancerTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancer(string name, LoadBalancerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticloadbalancing:LoadBalancer", name, args ?? new LoadBalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancer(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticloadbalancing:LoadBalancer", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancer Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LoadBalancer(name, id, options);
        }
    }

    public sealed class LoadBalancerArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessLoggingPolicy")]
        public Input<Inputs.LoadBalancerAccessLoggingPolicyArgs>? AccessLoggingPolicy { get; set; }

        [Input("appCookieStickinessPolicy")]
        private InputList<Inputs.LoadBalancerAppCookieStickinessPolicyArgs>? _appCookieStickinessPolicy;
        public InputList<Inputs.LoadBalancerAppCookieStickinessPolicyArgs> AppCookieStickinessPolicy
        {
            get => _appCookieStickinessPolicy ?? (_appCookieStickinessPolicy = new InputList<Inputs.LoadBalancerAppCookieStickinessPolicyArgs>());
            set => _appCookieStickinessPolicy = value;
        }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        [Input("connectionDrainingPolicy")]
        public Input<Inputs.LoadBalancerConnectionDrainingPolicyArgs>? ConnectionDrainingPolicy { get; set; }

        [Input("connectionSettings")]
        public Input<Inputs.LoadBalancerConnectionSettingsArgs>? ConnectionSettings { get; set; }

        [Input("crossZone")]
        public Input<bool>? CrossZone { get; set; }

        [Input("healthCheck")]
        public Input<Inputs.LoadBalancerHealthCheckArgs>? HealthCheck { get; set; }

        [Input("instances")]
        private InputList<string>? _instances;
        public InputList<string> Instances
        {
            get => _instances ?? (_instances = new InputList<string>());
            set => _instances = value;
        }

        [Input("lbCookieStickinessPolicy")]
        private InputList<Inputs.LoadBalancerLBCookieStickinessPolicyArgs>? _lbCookieStickinessPolicy;
        public InputList<Inputs.LoadBalancerLBCookieStickinessPolicyArgs> LbCookieStickinessPolicy
        {
            get => _lbCookieStickinessPolicy ?? (_lbCookieStickinessPolicy = new InputList<Inputs.LoadBalancerLBCookieStickinessPolicyArgs>());
            set => _lbCookieStickinessPolicy = value;
        }

        [Input("listeners", required: true)]
        private InputList<Inputs.LoadBalancerListenersArgs>? _listeners;
        public InputList<Inputs.LoadBalancerListenersArgs> Listeners
        {
            get => _listeners ?? (_listeners = new InputList<Inputs.LoadBalancerListenersArgs>());
            set => _listeners = value;
        }

        [Input("loadBalancerName")]
        public Input<string>? LoadBalancerName { get; set; }

        [Input("policies")]
        private InputList<Inputs.LoadBalancerPoliciesArgs>? _policies;
        public InputList<Inputs.LoadBalancerPoliciesArgs> Policies
        {
            get => _policies ?? (_policies = new InputList<Inputs.LoadBalancerPoliciesArgs>());
            set => _policies = value;
        }

        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        [Input("sourceSecurityGroupGroupName")]
        public Input<string>? SourceSecurityGroupGroupName { get; set; }

        [Input("sourceSecurityGroupOwnerAlias")]
        public Input<string>? SourceSecurityGroupOwnerAlias { get; set; }

        [Input("subnets")]
        private InputList<string>? _subnets;
        public InputList<string> Subnets
        {
            get => _subnets ?? (_subnets = new InputList<string>());
            set => _subnets = value;
        }

        [Input("tags")]
        private InputList<Inputs.LoadBalancerTagArgs>? _tags;
        public InputList<Inputs.LoadBalancerTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.LoadBalancerTagArgs>());
            set => _tags = value;
        }

        public LoadBalancerArgs()
        {
        }
        public static new LoadBalancerArgs Empty => new LoadBalancerArgs();
    }
}
