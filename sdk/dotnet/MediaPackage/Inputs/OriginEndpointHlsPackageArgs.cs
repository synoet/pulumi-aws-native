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
    /// An HTTP Live Streaming (HLS) packaging configuration.
    /// </summary>
    public sealed class OriginEndpointHlsPackageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source. "DATERANGE" inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.
        /// </summary>
        [Input("adMarkers")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointHlsPackageAdMarkers>? AdMarkers { get; set; }

        [Input("adTriggers")]
        private InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointHlsPackageAdTriggersItem>? _adTriggers;

        /// <summary>
        /// A list of SCTE-35 message types that are treated as ad markers in the output.  If empty, no ad markers are output.  Specify multiple items to create ad markers for all of the included message types.
        /// </summary>
        public InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointHlsPackageAdTriggersItem> AdTriggers
        {
            get => _adTriggers ?? (_adTriggers = new InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointHlsPackageAdTriggersItem>());
            set => _adTriggers = value;
        }

        [Input("adsOnDeliveryRestrictions")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointAdsOnDeliveryRestrictions>? AdsOnDeliveryRestrictions { get; set; }

        [Input("encryption")]
        public Input<Inputs.OriginEndpointHlsEncryptionArgs>? Encryption { get; set; }

        /// <summary>
        /// When enabled, an I-Frame only stream will be included in the output.
        /// </summary>
        [Input("includeIframeOnlyStream")]
        public Input<bool>? IncludeIframeOnlyStream { get; set; }

        /// <summary>
        /// The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
        /// </summary>
        [Input("playlistType")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointHlsPackagePlaylistType>? PlaylistType { get; set; }

        /// <summary>
        /// Time window (in seconds) contained in each parent manifest.
        /// </summary>
        [Input("playlistWindowSeconds")]
        public Input<int>? PlaylistWindowSeconds { get; set; }

        /// <summary>
        /// The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
        /// </summary>
        [Input("programDateTimeIntervalSeconds")]
        public Input<int>? ProgramDateTimeIntervalSeconds { get; set; }

        /// <summary>
        /// Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
        /// </summary>
        [Input("segmentDurationSeconds")]
        public Input<int>? SegmentDurationSeconds { get; set; }

        [Input("streamSelection")]
        public Input<Inputs.OriginEndpointStreamSelectionArgs>? StreamSelection { get; set; }

        /// <summary>
        /// When enabled, audio streams will be placed in rendition groups in the output.
        /// </summary>
        [Input("useAudioRenditionGroup")]
        public Input<bool>? UseAudioRenditionGroup { get; set; }

        public OriginEndpointHlsPackageArgs()
        {
        }
    }
}
