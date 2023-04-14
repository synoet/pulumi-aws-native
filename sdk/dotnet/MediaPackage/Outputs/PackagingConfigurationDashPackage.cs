// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Outputs
{

    /// <summary>
    /// A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    /// </summary>
    [OutputType]
    public sealed class PackagingConfigurationDashPackage
    {
        /// <summary>
        /// A list of DASH manifest configurations.
        /// </summary>
        public readonly ImmutableArray<Outputs.PackagingConfigurationDashManifest> DashManifests;
        public readonly Outputs.PackagingConfigurationDashEncryption? Encryption;
        /// <summary>
        /// When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.
        /// </summary>
        public readonly bool? IncludeEncoderConfigurationInSegments;
        /// <summary>
        /// When enabled, an I-Frame only stream will be included in the output.
        /// </summary>
        public readonly bool? IncludeIframeOnlyStream;
        /// <summary>
        /// A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.MediaPackage.PackagingConfigurationDashPackagePeriodTriggersItem> PeriodTriggers;
        public readonly int? SegmentDurationSeconds;
        /// <summary>
        /// Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
        /// </summary>
        public readonly Pulumi.AwsNative.MediaPackage.PackagingConfigurationDashPackageSegmentTemplateFormat? SegmentTemplateFormat;

        [OutputConstructor]
        private PackagingConfigurationDashPackage(
            ImmutableArray<Outputs.PackagingConfigurationDashManifest> dashManifests,

            Outputs.PackagingConfigurationDashEncryption? encryption,

            bool? includeEncoderConfigurationInSegments,

            bool? includeIframeOnlyStream,

            ImmutableArray<Pulumi.AwsNative.MediaPackage.PackagingConfigurationDashPackagePeriodTriggersItem> periodTriggers,

            int? segmentDurationSeconds,

            Pulumi.AwsNative.MediaPackage.PackagingConfigurationDashPackageSegmentTemplateFormat? segmentTemplateFormat)
        {
            DashManifests = dashManifests;
            Encryption = encryption;
            IncludeEncoderConfigurationInSegments = includeEncoderConfigurationInSegments;
            IncludeIframeOnlyStream = includeIframeOnlyStream;
            PeriodTriggers = periodTriggers;
            SegmentDurationSeconds = segmentDurationSeconds;
            SegmentTemplateFormat = segmentTemplateFormat;
        }
    }
}
