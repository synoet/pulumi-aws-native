// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
    /// </summary>
    [AwsNativeResourceType("aws-native:datasync:LocationFSxWindows")]
    public partial class LocationFSxWindows : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
        /// </summary>
        [Output("domain")]
        public Output<string?> Domain { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
        /// </summary>
        [Output("fsxFilesystemArn")]
        public Output<string> FsxFilesystemArn { get; private set; } = null!;

        [Output("locationArn")]
        public Output<string> LocationArn { get; private set; } = null!;

        [Output("locationUri")]
        public Output<string> LocationUri { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
        /// </summary>
        [Output("securityGroupArns")]
        public Output<ImmutableArray<string>> SecurityGroupArns { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
        /// </summary>
        [Output("subdirectory")]
        public Output<string?> Subdirectory { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
        /// </summary>
        [Output("user")]
        public Output<string> User { get; private set; } = null!;


        /// <summary>
        /// Create a LocationFSxWindows resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LocationFSxWindows(string name, LocationFSxWindowsArgs args, CustomResourceOptions? options = null)
            : base("aws-native:datasync:LocationFSxWindows", name, args ?? new LocationFSxWindowsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LocationFSxWindows(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:datasync:LocationFSxWindows", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing LocationFSxWindows resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LocationFSxWindows Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LocationFSxWindows(name, id, options);
        }
    }

    public sealed class LocationFSxWindowsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
        /// </summary>
        [Input("fsxFilesystemArn", required: true)]
        public Input<string> FsxFilesystemArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
        /// </summary>
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("securityGroupArns", required: true)]
        private InputList<string>? _securityGroupArns;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
        /// </summary>
        public InputList<string> SecurityGroupArns
        {
            get => _securityGroupArns ?? (_securityGroupArns = new InputList<string>());
            set => _securityGroupArns = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
        /// </summary>
        [Input("subdirectory")]
        public Input<string>? Subdirectory { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
        /// </summary>
        [Input("user", required: true)]
        public Input<string> User { get; set; } = null!;

        public LocationFSxWindowsArgs()
        {
        }
    }
}
