// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelCaptionDescription
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-captionselectorname
        /// </summary>
        public readonly string? CaptionSelectorName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-destinationsettings
        /// </summary>
        public readonly Outputs.ChannelCaptionDestinationSettings? DestinationSettings;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagecode
        /// </summary>
        public readonly string? LanguageCode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagedescription
        /// </summary>
        public readonly string? LanguageDescription;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-name
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private ChannelCaptionDescription(
            string? CaptionSelectorName,

            Outputs.ChannelCaptionDestinationSettings? DestinationSettings,

            string? LanguageCode,

            string? LanguageDescription,

            string? Name)
        {
            this.CaptionSelectorName = CaptionSelectorName;
            this.DestinationSettings = DestinationSettings;
            this.LanguageCode = LanguageCode;
            this.LanguageDescription = LanguageDescription;
            this.Name = Name;
        }
    }
}