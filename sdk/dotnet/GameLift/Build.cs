// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift
{
    /// <summary>
    /// Resource Type definition for AWS::GameLift::Build
    /// </summary>
    [AwsNativeResourceType("aws-native:gamelift:Build")]
    public partial class Build : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
        /// </summary>
        [Output("buildId")]
        public Output<string> BuildId { get; private set; } = null!;

        /// <summary>
        /// A descriptive label that is associated with a build. Build names do not need to be unique.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.
        /// </summary>
        [Output("operatingSystem")]
        public Output<Pulumi.AwsNative.GameLift.BuildOperatingSystem?> OperatingSystem { get; private set; } = null!;

        /// <summary>
        /// A server SDK version you used when integrating your game server build with Amazon GameLift. By default Amazon GameLift sets this value to 4.0.2.
        /// </summary>
        [Output("serverSdkVersion")]
        public Output<string?> ServerSdkVersion { get; private set; } = null!;

        /// <summary>
        /// Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.
        /// </summary>
        [Output("storageLocation")]
        public Output<Outputs.BuildStorageLocation?> StorageLocation { get; private set; } = null!;

        /// <summary>
        /// Version information that is associated with this build. Version strings do not need to be unique.
        /// </summary>
        [Output("version")]
        public Output<string?> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Build resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Build(string name, BuildArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:gamelift:Build", name, args ?? new BuildArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Build(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:gamelift:Build", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "operatingSystem",
                    "serverSdkVersion",
                    "storageLocation",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Build resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Build Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Build(name, id, options);
        }
    }

    public sealed class BuildArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A descriptive label that is associated with a build. Build names do not need to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.
        /// </summary>
        [Input("operatingSystem")]
        public Input<Pulumi.AwsNative.GameLift.BuildOperatingSystem>? OperatingSystem { get; set; }

        /// <summary>
        /// A server SDK version you used when integrating your game server build with Amazon GameLift. By default Amazon GameLift sets this value to 4.0.2.
        /// </summary>
        [Input("serverSdkVersion")]
        public Input<string>? ServerSdkVersion { get; set; }

        /// <summary>
        /// Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.
        /// </summary>
        [Input("storageLocation")]
        public Input<Inputs.BuildStorageLocationArgs>? StorageLocation { get; set; }

        /// <summary>
        /// Version information that is associated with this build. Version strings do not need to be unique.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public BuildArgs()
        {
        }
        public static new BuildArgs Empty => new BuildArgs();
    }
}
