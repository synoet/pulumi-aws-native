// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR
{
    /// <summary>
    /// Resource Type definition for AWS::EMR::Cluster
    /// </summary>
    [Obsolete(@"Cluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:emr:Cluster")]
    public partial class Cluster : global::Pulumi.CustomResource
    {
        [Output("additionalInfo")]
        public Output<object?> AdditionalInfo { get; private set; } = null!;

        [Output("applications")]
        public Output<ImmutableArray<Outputs.ClusterApplication>> Applications { get; private set; } = null!;

        [Output("autoScalingRole")]
        public Output<string?> AutoScalingRole { get; private set; } = null!;

        [Output("autoTerminationPolicy")]
        public Output<Outputs.ClusterAutoTerminationPolicy?> AutoTerminationPolicy { get; private set; } = null!;

        [Output("bootstrapActions")]
        public Output<ImmutableArray<Outputs.ClusterBootstrapActionConfig>> BootstrapActions { get; private set; } = null!;

        [Output("configurations")]
        public Output<ImmutableArray<Outputs.ClusterConfiguration>> Configurations { get; private set; } = null!;

        [Output("customAmiId")]
        public Output<string?> CustomAmiId { get; private set; } = null!;

        [Output("ebsRootVolumeSize")]
        public Output<int?> EbsRootVolumeSize { get; private set; } = null!;

        [Output("instances")]
        public Output<Outputs.ClusterJobFlowInstancesConfig> Instances { get; private set; } = null!;

        [Output("jobFlowRole")]
        public Output<string> JobFlowRole { get; private set; } = null!;

        [Output("kerberosAttributes")]
        public Output<Outputs.ClusterKerberosAttributes?> KerberosAttributes { get; private set; } = null!;

        [Output("logEncryptionKmsKeyId")]
        public Output<string?> LogEncryptionKmsKeyId { get; private set; } = null!;

        [Output("logUri")]
        public Output<string?> LogUri { get; private set; } = null!;

        [Output("managedScalingPolicy")]
        public Output<Outputs.ClusterManagedScalingPolicy?> ManagedScalingPolicy { get; private set; } = null!;

        [Output("masterPublicDNS")]
        public Output<string> MasterPublicDNS { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("oSReleaseLabel")]
        public Output<string?> OSReleaseLabel { get; private set; } = null!;

        [Output("releaseLabel")]
        public Output<string?> ReleaseLabel { get; private set; } = null!;

        [Output("scaleDownBehavior")]
        public Output<string?> ScaleDownBehavior { get; private set; } = null!;

        [Output("securityConfiguration")]
        public Output<string?> SecurityConfiguration { get; private set; } = null!;

        [Output("serviceRole")]
        public Output<string> ServiceRole { get; private set; } = null!;

        [Output("stepConcurrencyLevel")]
        public Output<int?> StepConcurrencyLevel { get; private set; } = null!;

        [Output("steps")]
        public Output<ImmutableArray<Outputs.ClusterStepConfig>> Steps { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ClusterTag>> Tags { get; private set; } = null!;

        [Output("visibleToAllUsers")]
        public Output<bool?> VisibleToAllUsers { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:emr:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:emr:Cluster", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, options);
        }
    }

    public sealed class ClusterArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalInfo")]
        public Input<object>? AdditionalInfo { get; set; }

        [Input("applications")]
        private InputList<Inputs.ClusterApplicationArgs>? _applications;
        public InputList<Inputs.ClusterApplicationArgs> Applications
        {
            get => _applications ?? (_applications = new InputList<Inputs.ClusterApplicationArgs>());
            set => _applications = value;
        }

        [Input("autoScalingRole")]
        public Input<string>? AutoScalingRole { get; set; }

        [Input("autoTerminationPolicy")]
        public Input<Inputs.ClusterAutoTerminationPolicyArgs>? AutoTerminationPolicy { get; set; }

        [Input("bootstrapActions")]
        private InputList<Inputs.ClusterBootstrapActionConfigArgs>? _bootstrapActions;
        public InputList<Inputs.ClusterBootstrapActionConfigArgs> BootstrapActions
        {
            get => _bootstrapActions ?? (_bootstrapActions = new InputList<Inputs.ClusterBootstrapActionConfigArgs>());
            set => _bootstrapActions = value;
        }

        [Input("configurations")]
        private InputList<Inputs.ClusterConfigurationArgs>? _configurations;
        public InputList<Inputs.ClusterConfigurationArgs> Configurations
        {
            get => _configurations ?? (_configurations = new InputList<Inputs.ClusterConfigurationArgs>());
            set => _configurations = value;
        }

        [Input("customAmiId")]
        public Input<string>? CustomAmiId { get; set; }

        [Input("ebsRootVolumeSize")]
        public Input<int>? EbsRootVolumeSize { get; set; }

        [Input("instances", required: true)]
        public Input<Inputs.ClusterJobFlowInstancesConfigArgs> Instances { get; set; } = null!;

        [Input("jobFlowRole", required: true)]
        public Input<string> JobFlowRole { get; set; } = null!;

        [Input("kerberosAttributes")]
        public Input<Inputs.ClusterKerberosAttributesArgs>? KerberosAttributes { get; set; }

        [Input("logEncryptionKmsKeyId")]
        public Input<string>? LogEncryptionKmsKeyId { get; set; }

        [Input("logUri")]
        public Input<string>? LogUri { get; set; }

        [Input("managedScalingPolicy")]
        public Input<Inputs.ClusterManagedScalingPolicyArgs>? ManagedScalingPolicy { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("oSReleaseLabel")]
        public Input<string>? OSReleaseLabel { get; set; }

        [Input("releaseLabel")]
        public Input<string>? ReleaseLabel { get; set; }

        [Input("scaleDownBehavior")]
        public Input<string>? ScaleDownBehavior { get; set; }

        [Input("securityConfiguration")]
        public Input<string>? SecurityConfiguration { get; set; }

        [Input("serviceRole", required: true)]
        public Input<string> ServiceRole { get; set; } = null!;

        [Input("stepConcurrencyLevel")]
        public Input<int>? StepConcurrencyLevel { get; set; }

        [Input("steps")]
        private InputList<Inputs.ClusterStepConfigArgs>? _steps;
        public InputList<Inputs.ClusterStepConfigArgs> Steps
        {
            get => _steps ?? (_steps = new InputList<Inputs.ClusterStepConfigArgs>());
            set => _steps = value;
        }

        [Input("tags")]
        private InputList<Inputs.ClusterTagArgs>? _tags;
        public InputList<Inputs.ClusterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ClusterTagArgs>());
            set => _tags = value;
        }

        [Input("visibleToAllUsers")]
        public Input<bool>? VisibleToAllUsers { get; set; }

        public ClusterArgs()
        {
        }
        public static new ClusterArgs Empty => new ClusterArgs();
    }
}
