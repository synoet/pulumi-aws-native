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
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html
    /// </summary>
    public sealed class PackagingConfigurationMssManifestArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname
        /// </summary>
        [Input("ManifestName")]
        public Input<string>? ManifestName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection
        /// </summary>
        [Input("StreamSelection")]
        public Input<Inputs.PackagingConfigurationStreamSelectionArgs>? StreamSelection { get; set; }

        public PackagingConfigurationMssManifestArgs()
        {
        }
    }
}