// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppStream
{
    /// <summary>
    /// Resource Type definition for AWS::AppStream::Fleet
    /// </summary>
    [Obsolete(@"Fleet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appstream:Fleet")]
    public partial class Fleet : global::Pulumi.CustomResource
    {
        [Output("computeCapacity")]
        public Output<Outputs.FleetComputeCapacity?> ComputeCapacity { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("disconnectTimeoutInSeconds")]
        public Output<int?> DisconnectTimeoutInSeconds { get; private set; } = null!;

        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        [Output("domainJoinInfo")]
        public Output<Outputs.FleetDomainJoinInfo?> DomainJoinInfo { get; private set; } = null!;

        [Output("enableDefaultInternetAccess")]
        public Output<bool?> EnableDefaultInternetAccess { get; private set; } = null!;

        [Output("fleetType")]
        public Output<string?> FleetType { get; private set; } = null!;

        [Output("iamRoleArn")]
        public Output<string?> IamRoleArn { get; private set; } = null!;

        [Output("idleDisconnectTimeoutInSeconds")]
        public Output<int?> IdleDisconnectTimeoutInSeconds { get; private set; } = null!;

        [Output("imageArn")]
        public Output<string?> ImageArn { get; private set; } = null!;

        [Output("imageName")]
        public Output<string?> ImageName { get; private set; } = null!;

        [Output("instanceType")]
        public Output<string> InstanceType { get; private set; } = null!;

        [Output("maxConcurrentSessions")]
        public Output<int?> MaxConcurrentSessions { get; private set; } = null!;

        [Output("maxSessionsPerInstance")]
        public Output<int?> MaxSessionsPerInstance { get; private set; } = null!;

        [Output("maxUserDurationInSeconds")]
        public Output<int?> MaxUserDurationInSeconds { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("platform")]
        public Output<string?> Platform { get; private set; } = null!;

        [Output("sessionScriptS3Location")]
        public Output<Outputs.FleetS3Location?> SessionScriptS3Location { get; private set; } = null!;

        [Output("streamView")]
        public Output<string?> StreamView { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.FleetTag>> Tags { get; private set; } = null!;

        [Output("usbDeviceFilterStrings")]
        public Output<ImmutableArray<string>> UsbDeviceFilterStrings { get; private set; } = null!;

        [Output("vpcConfig")]
        public Output<Outputs.FleetVpcConfig?> VpcConfig { get; private set; } = null!;


        /// <summary>
        /// Create a Fleet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Fleet(string name, FleetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appstream:Fleet", name, args ?? new FleetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Fleet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appstream:Fleet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "fleetType",
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Fleet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Fleet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Fleet(name, id, options);
        }
    }

    public sealed class FleetArgs : global::Pulumi.ResourceArgs
    {
        [Input("computeCapacity")]
        public Input<Inputs.FleetComputeCapacityArgs>? ComputeCapacity { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("disconnectTimeoutInSeconds")]
        public Input<int>? DisconnectTimeoutInSeconds { get; set; }

        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("domainJoinInfo")]
        public Input<Inputs.FleetDomainJoinInfoArgs>? DomainJoinInfo { get; set; }

        [Input("enableDefaultInternetAccess")]
        public Input<bool>? EnableDefaultInternetAccess { get; set; }

        [Input("fleetType")]
        public Input<string>? FleetType { get; set; }

        [Input("iamRoleArn")]
        public Input<string>? IamRoleArn { get; set; }

        [Input("idleDisconnectTimeoutInSeconds")]
        public Input<int>? IdleDisconnectTimeoutInSeconds { get; set; }

        [Input("imageArn")]
        public Input<string>? ImageArn { get; set; }

        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        [Input("maxConcurrentSessions")]
        public Input<int>? MaxConcurrentSessions { get; set; }

        [Input("maxSessionsPerInstance")]
        public Input<int>? MaxSessionsPerInstance { get; set; }

        [Input("maxUserDurationInSeconds")]
        public Input<int>? MaxUserDurationInSeconds { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("platform")]
        public Input<string>? Platform { get; set; }

        [Input("sessionScriptS3Location")]
        public Input<Inputs.FleetS3LocationArgs>? SessionScriptS3Location { get; set; }

        [Input("streamView")]
        public Input<string>? StreamView { get; set; }

        [Input("tags")]
        private InputList<Inputs.FleetTagArgs>? _tags;
        public InputList<Inputs.FleetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FleetTagArgs>());
            set => _tags = value;
        }

        [Input("usbDeviceFilterStrings")]
        private InputList<string>? _usbDeviceFilterStrings;
        public InputList<string> UsbDeviceFilterStrings
        {
            get => _usbDeviceFilterStrings ?? (_usbDeviceFilterStrings = new InputList<string>());
            set => _usbDeviceFilterStrings = value;
        }

        [Input("vpcConfig")]
        public Input<Inputs.FleetVpcConfigArgs>? VpcConfig { get; set; }

        public FleetArgs()
        {
        }
        public static new FleetArgs Empty => new FleetArgs();
    }
}
