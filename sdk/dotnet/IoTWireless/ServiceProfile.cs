// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless
{
    /// <summary>
    /// An example resource schema demonstrating some basic constructs and validation rules.
    /// </summary>
    [AwsNativeResourceType("aws-native:iotwireless:ServiceProfile")]
    public partial class ServiceProfile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Service profile Arn. Returned after successful create.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
        /// </summary>
        [Output("loRaWan")]
        public Output<Outputs.ServiceProfileLoRaWanServiceProfile?> LoRaWan { get; private set; } = null!;

        /// <summary>
        /// Name of service profile
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the service profile.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ServiceProfileTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceProfile(string name, ServiceProfileArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:ServiceProfile", name, args ?? new ServiceProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotwireless:ServiceProfile", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ServiceProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ServiceProfile(name, id, options);
        }
    }

    public sealed class ServiceProfileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
        /// </summary>
        [Input("loRaWan")]
        public Input<Inputs.ServiceProfileLoRaWanServiceProfileArgs>? LoRaWan { get; set; }

        /// <summary>
        /// Name of service profile
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.ServiceProfileTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the service profile.
        /// </summary>
        public InputList<Inputs.ServiceProfileTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ServiceProfileTagArgs>());
            set => _tags = value;
        }

        public ServiceProfileArgs()
        {
        }
        public static new ServiceProfileArgs Empty => new ServiceProfileArgs();
    }
}
