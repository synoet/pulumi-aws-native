// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    /// </summary>
    [AwsNativeResourceType("aws-native:apprunner:Service")]
    public partial class Service : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        /// </summary>
        [Output("autoScalingConfigurationArn")]
        public Output<string?> AutoScalingConfigurationArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        /// </summary>
        [Output("encryptionConfiguration")]
        public Output<Outputs.ServiceEncryptionConfiguration?> EncryptionConfiguration { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        /// </summary>
        [Output("healthCheckConfiguration")]
        public Output<Outputs.ServiceHealthCheckConfiguration?> HealthCheckConfiguration { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        /// </summary>
        [Output("instanceConfiguration")]
        public Output<Outputs.ServiceInstanceConfiguration?> InstanceConfiguration { get; private set; } = null!;

        [Output("serviceArn")]
        public Output<string> ServiceArn { get; private set; } = null!;

        [Output("serviceId")]
        public Output<string> ServiceId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        /// </summary>
        [Output("serviceName")]
        public Output<string?> ServiceName { get; private set; } = null!;

        [Output("serviceUrl")]
        public Output<string> ServiceUrl { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        /// </summary>
        [Output("sourceConfiguration")]
        public Output<Outputs.ServiceSourceConfiguration> SourceConfiguration { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Service resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Service(string name, ServiceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apprunner:Service", name, args ?? new ServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Service(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apprunner:Service", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Service resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Service Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Service(name, id, options);
        }
    }

    public sealed class ServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        /// </summary>
        [Input("autoScalingConfigurationArn")]
        public Input<string>? AutoScalingConfigurationArn { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        /// </summary>
        [Input("encryptionConfiguration")]
        public Input<Inputs.ServiceEncryptionConfigurationArgs>? EncryptionConfiguration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        /// </summary>
        [Input("healthCheckConfiguration")]
        public Input<Inputs.ServiceHealthCheckConfigurationArgs>? HealthCheckConfiguration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        /// </summary>
        [Input("instanceConfiguration")]
        public Input<Inputs.ServiceInstanceConfigurationArgs>? InstanceConfiguration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        /// </summary>
        [Input("sourceConfiguration", required: true)]
        public Input<Inputs.ServiceSourceConfigurationArgs> SourceConfiguration { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ServiceArgs()
        {
        }
    }
}
