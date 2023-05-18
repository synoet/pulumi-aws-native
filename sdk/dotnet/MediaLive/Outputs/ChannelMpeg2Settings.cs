// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelMpeg2Settings
    {
        public readonly string? AdaptiveQuantization;
        public readonly string? AfdSignaling;
        public readonly string? ColorMetadata;
        public readonly string? ColorSpace;
        public readonly string? DisplayAspectRatio;
        public readonly Outputs.ChannelMpeg2FilterSettings? FilterSettings;
        public readonly string? FixedAfd;
        public readonly int? FramerateDenominator;
        public readonly int? FramerateNumerator;
        public readonly int? GopClosedCadence;
        public readonly int? GopNumBFrames;
        public readonly double? GopSize;
        public readonly string? GopSizeUnits;
        public readonly string? ScanType;
        public readonly string? SubgopLength;
        public readonly Outputs.ChannelTimecodeBurninSettings? TimecodeBurninSettings;
        public readonly string? TimecodeInsertion;

        [OutputConstructor]
        private ChannelMpeg2Settings(
            string? adaptiveQuantization,

            string? afdSignaling,

            string? colorMetadata,

            string? colorSpace,

            string? displayAspectRatio,

            Outputs.ChannelMpeg2FilterSettings? filterSettings,

            string? fixedAfd,

            int? framerateDenominator,

            int? framerateNumerator,

            int? gopClosedCadence,

            int? gopNumBFrames,

            double? gopSize,

            string? gopSizeUnits,

            string? scanType,

            string? subgopLength,

            Outputs.ChannelTimecodeBurninSettings? timecodeBurninSettings,

            string? timecodeInsertion)
        {
            AdaptiveQuantization = adaptiveQuantization;
            AfdSignaling = afdSignaling;
            ColorMetadata = colorMetadata;
            ColorSpace = colorSpace;
            DisplayAspectRatio = displayAspectRatio;
            FilterSettings = filterSettings;
            FixedAfd = fixedAfd;
            FramerateDenominator = framerateDenominator;
            FramerateNumerator = framerateNumerator;
            GopClosedCadence = gopClosedCadence;
            GopNumBFrames = gopNumBFrames;
            GopSize = gopSize;
            GopSizeUnits = gopSizeUnits;
            ScanType = scanType;
            SubgopLength = subgopLength;
            TimecodeBurninSettings = timecodeBurninSettings;
            TimecodeInsertion = timecodeInsertion;
        }
    }
}
