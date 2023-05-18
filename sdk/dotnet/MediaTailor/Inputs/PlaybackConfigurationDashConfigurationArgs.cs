// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor.Inputs
{

    /// <summary>
    /// The configuration for DASH PUT operations.
    /// </summary>
    public sealed class PlaybackConfigurationDashConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The URL generated by MediaTailor to initiate a DASH playback session. The session uses server-side reporting.
        /// </summary>
        [Input("manifestEndpointPrefix")]
        public Input<string>? ManifestEndpointPrefix { get; set; }

        /// <summary>
        /// The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.
        /// </summary>
        [Input("mpdLocation")]
        public Input<string>? MpdLocation { get; set; }

        /// <summary>
        /// The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.
        /// </summary>
        [Input("originManifestType")]
        public Input<Pulumi.AwsNative.MediaTailor.PlaybackConfigurationDashConfigurationOriginManifestType>? OriginManifestType { get; set; }

        public PlaybackConfigurationDashConfigurationArgs()
        {
        }
        public static new PlaybackConfigurationDashConfigurationArgs Empty => new PlaybackConfigurationDashConfigurationArgs();
    }
}
