// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Iam
{
    /// <summary>
    /// Resource Type definition for AWS::IAM::VirtualMFADevice
    /// </summary>
    [AwsNativeResourceType("aws-native:iam:VirtualMfaDevice")]
    public partial class VirtualMfaDevice : global::Pulumi.CustomResource
    {
        [Output("path")]
        public Output<string?> Path { get; private set; } = null!;

        [Output("serialNumber")]
        public Output<string> SerialNumber { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.VirtualMfaDeviceTag>> Tags { get; private set; } = null!;

        [Output("users")]
        public Output<ImmutableArray<string>> Users { get; private set; } = null!;

        [Output("virtualMfaDeviceName")]
        public Output<string?> VirtualMfaDeviceName { get; private set; } = null!;


        /// <summary>
        /// Create a VirtualMfaDevice resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VirtualMfaDevice(string name, VirtualMfaDeviceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iam:VirtualMfaDevice", name, args ?? new VirtualMfaDeviceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VirtualMfaDevice(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iam:VirtualMfaDevice", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VirtualMfaDevice resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VirtualMfaDevice Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VirtualMfaDevice(name, id, options);
        }
    }

    public sealed class VirtualMfaDeviceArgs : global::Pulumi.ResourceArgs
    {
        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("tags")]
        private InputList<Inputs.VirtualMfaDeviceTagArgs>? _tags;
        public InputList<Inputs.VirtualMfaDeviceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.VirtualMfaDeviceTagArgs>());
            set => _tags = value;
        }

        [Input("users", required: true)]
        private InputList<string>? _users;
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        [Input("virtualMfaDeviceName")]
        public Input<string>? VirtualMfaDeviceName { get; set; }

        public VirtualMfaDeviceArgs()
        {
        }
        public static new VirtualMfaDeviceArgs Empty => new VirtualMfaDeviceArgs();
    }
}
