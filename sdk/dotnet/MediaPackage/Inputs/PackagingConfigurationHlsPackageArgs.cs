// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MediaPackage.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html
    /// </summary>
    public sealed class PackagingConfigurationHlsPackageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption
        /// </summary>
        [Input("Encryption")]
        public Input<Inputs.PackagingConfigurationHlsEncryptionArgs>? Encryption { get; set; }

        [Input("HlsManifests", required: true)]
        private InputList<Inputs.PackagingConfigurationHlsManifestArgs>? _HlsManifests;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests
        /// </summary>
        public InputList<Inputs.PackagingConfigurationHlsManifestArgs> HlsManifests
        {
            get => _HlsManifests ?? (_HlsManifests = new InputList<Inputs.PackagingConfigurationHlsManifestArgs>());
            set => _HlsManifests = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds
        /// </summary>
        [Input("SegmentDurationSeconds")]
        public Input<int>? SegmentDurationSeconds { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup
        /// </summary>
        [Input("UseAudioRenditionGroup")]
        public Input<bool>? UseAudioRenditionGroup { get; set; }

        public PackagingConfigurationHlsPackageArgs()
        {
        }
    }
}