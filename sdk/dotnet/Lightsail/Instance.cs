// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::Instance
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:Instance")]
    public partial class Instance : global::Pulumi.CustomResource
    {
        /// <summary>
        /// An array of objects representing the add-ons to enable for the new instance.
        /// </summary>
        [Output("addOns")]
        public Output<ImmutableArray<Outputs.InstanceAddOn>> AddOns { get; private set; } = null!;

        /// <summary>
        /// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string?> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        /// </summary>
        [Output("blueprintId")]
        public Output<string> BlueprintId { get; private set; } = null!;

        /// <summary>
        /// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        /// </summary>
        [Output("bundleId")]
        public Output<string> BundleId { get; private set; } = null!;

        [Output("hardware")]
        public Output<Outputs.InstanceHardware?> Hardware { get; private set; } = null!;

        [Output("instanceArn")]
        public Output<string> InstanceArn { get; private set; } = null!;

        /// <summary>
        /// The names to use for your new Lightsail instance.
        /// </summary>
        [Output("instanceName")]
        public Output<string> InstanceName { get; private set; } = null!;

        /// <summary>
        /// Is the IP Address of the Instance is the static IP
        /// </summary>
        [Output("isStaticIp")]
        public Output<bool> IsStaticIp { get; private set; } = null!;

        /// <summary>
        /// The name of your key pair.
        /// </summary>
        [Output("keyPairName")]
        public Output<string?> KeyPairName { get; private set; } = null!;

        [Output("location")]
        public Output<Outputs.InstanceLocation?> Location { get; private set; } = null!;

        [Output("networking")]
        public Output<Outputs.InstanceNetworking?> Networking { get; private set; } = null!;

        /// <summary>
        /// Private IP Address of the Instance
        /// </summary>
        [Output("privateIpAddress")]
        public Output<string> PrivateIpAddress { get; private set; } = null!;

        /// <summary>
        /// Public IP Address of the Instance
        /// </summary>
        [Output("publicIpAddress")]
        public Output<string> PublicIpAddress { get; private set; } = null!;

        /// <summary>
        /// Resource type of Lightsail instance.
        /// </summary>
        [Output("resourceType")]
        public Output<string> ResourceType { get; private set; } = null!;

        /// <summary>
        /// SSH Key Name of the  Lightsail instance.
        /// </summary>
        [Output("sshKeyName")]
        public Output<string> SshKeyName { get; private set; } = null!;

        [Output("state")]
        public Output<Outputs.InstanceState?> State { get; private set; } = null!;

        /// <summary>
        /// Support code to help identify any issues
        /// </summary>
        [Output("supportCode")]
        public Output<string> SupportCode { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.InstanceTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        /// </summary>
        [Output("userData")]
        public Output<string?> UserData { get; private set; } = null!;

        /// <summary>
        /// Username of the  Lightsail instance.
        /// </summary>
        [Output("userName")]
        public Output<string> UserName { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Instance", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "availabilityZone",
                    "blueprintId",
                    "bundleId",
                    "instanceName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, options);
        }
    }

    public sealed class InstanceArgs : global::Pulumi.ResourceArgs
    {
        [Input("addOns")]
        private InputList<Inputs.InstanceAddOnArgs>? _addOns;

        /// <summary>
        /// An array of objects representing the add-ons to enable for the new instance.
        /// </summary>
        public InputList<Inputs.InstanceAddOnArgs> AddOns
        {
            get => _addOns ?? (_addOns = new InputList<Inputs.InstanceAddOnArgs>());
            set => _addOns = value;
        }

        /// <summary>
        /// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        /// </summary>
        [Input("blueprintId", required: true)]
        public Input<string> BlueprintId { get; set; } = null!;

        /// <summary>
        /// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        /// </summary>
        [Input("bundleId", required: true)]
        public Input<string> BundleId { get; set; } = null!;

        [Input("hardware")]
        public Input<Inputs.InstanceHardwareArgs>? Hardware { get; set; }

        /// <summary>
        /// The names to use for your new Lightsail instance.
        /// </summary>
        [Input("instanceName")]
        public Input<string>? InstanceName { get; set; }

        /// <summary>
        /// The name of your key pair.
        /// </summary>
        [Input("keyPairName")]
        public Input<string>? KeyPairName { get; set; }

        [Input("location")]
        public Input<Inputs.InstanceLocationArgs>? Location { get; set; }

        [Input("networking")]
        public Input<Inputs.InstanceNetworkingArgs>? Networking { get; set; }

        [Input("state")]
        public Input<Inputs.InstanceStateArgs>? State { get; set; }

        [Input("tags")]
        private InputList<Inputs.InstanceTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.InstanceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.InstanceTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        public InstanceArgs()
        {
        }
        public static new InstanceArgs Empty => new InstanceArgs();
    }
}
