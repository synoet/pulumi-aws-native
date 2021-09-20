// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Inputs
{

    /// <summary>
    /// A StreamSelection configuration.
    /// </summary>
    public sealed class PackagingConfigurationStreamSelectionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum video bitrate (bps) to include in output.
        /// </summary>
        [Input("maxVideoBitsPerSecond")]
        public Input<int>? MaxVideoBitsPerSecond { get; set; }

        /// <summary>
        /// The minimum video bitrate (bps) to include in output.
        /// </summary>
        [Input("minVideoBitsPerSecond")]
        public Input<int>? MinVideoBitsPerSecond { get; set; }

        /// <summary>
        /// A directive that determines the order of streams in the output.
        /// </summary>
        [Input("streamOrder")]
        public Input<Pulumi.AwsNative.MediaPackage.PackagingConfigurationStreamSelectionStreamOrder>? StreamOrder { get; set; }

        public PackagingConfigurationStreamSelectionArgs()
        {
        }
    }
}
