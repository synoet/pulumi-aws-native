// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Outputs
{

    /// <summary>
    /// An HTTP Live Streaming (HLS) manifest configuration.
    /// </summary>
    [OutputType]
    public sealed class PackagingConfigurationHlsManifest
    {
        /// <summary>
        /// This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
        /// </summary>
        public readonly Pulumi.AwsNative.MediaPackage.PackagingConfigurationHlsManifestAdMarkers? AdMarkers;
        /// <summary>
        /// When enabled, an I-Frame only stream will be included in the output.
        /// </summary>
        public readonly bool? IncludeIframeOnlyStream;
        public readonly string? ManifestName;
        /// <summary>
        /// The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
        /// </summary>
        public readonly int? ProgramDateTimeIntervalSeconds;
        /// <summary>
        /// When enabled, the EXT-X-KEY tag will be repeated in output manifests.
        /// </summary>
        public readonly bool? RepeatExtXKey;
        public readonly Outputs.PackagingConfigurationStreamSelection? StreamSelection;

        [OutputConstructor]
        private PackagingConfigurationHlsManifest(
            Pulumi.AwsNative.MediaPackage.PackagingConfigurationHlsManifestAdMarkers? adMarkers,

            bool? includeIframeOnlyStream,

            string? manifestName,

            int? programDateTimeIntervalSeconds,

            bool? repeatExtXKey,

            Outputs.PackagingConfigurationStreamSelection? streamSelection)
        {
            AdMarkers = adMarkers;
            IncludeIframeOnlyStream = includeIframeOnlyStream;
            ManifestName = manifestName;
            ProgramDateTimeIntervalSeconds = programDateTimeIntervalSeconds;
            RepeatExtXKey = repeatExtXKey;
            StreamSelection = streamSelection;
        }
    }
}
