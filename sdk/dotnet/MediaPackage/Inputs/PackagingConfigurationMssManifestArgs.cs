// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Inputs
{

    /// <summary>
    /// A Microsoft Smooth Streaming (MSS) manifest configuration.
    /// </summary>
    public sealed class PackagingConfigurationMssManifestArgs : global::Pulumi.ResourceArgs
    {
        [Input("manifestName")]
        public Input<string>? ManifestName { get; set; }

        [Input("streamSelection")]
        public Input<Inputs.PackagingConfigurationStreamSelectionArgs>? StreamSelection { get; set; }

        public PackagingConfigurationMssManifestArgs()
        {
        }
        public static new PackagingConfigurationMssManifestArgs Empty => new PackagingConfigurationMssManifestArgs();
    }
}
