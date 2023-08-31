// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor
{
    /// <summary>
    /// Resource schema for AWS::MediaTailor::PlaybackConfiguration
    /// </summary>
    [AwsNativeResourceType("aws-native:mediatailor:PlaybackConfiguration")]
    public partial class PlaybackConfiguration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        /// </summary>
        [Output("adDecisionServerUrl")]
        public Output<string> AdDecisionServerUrl { get; private set; } = null!;

        /// <summary>
        /// The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see Ad Suppression (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        /// </summary>
        [Output("availSuppression")]
        public Output<Outputs.PlaybackConfigurationAvailSuppression?> AvailSuppression { get; private set; } = null!;

        /// <summary>
        /// The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see Bumpers (https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
        /// </summary>
        [Output("bumper")]
        public Output<Outputs.PlaybackConfigurationBumper?> Bumper { get; private set; } = null!;

        /// <summary>
        /// The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        /// </summary>
        [Output("cdnConfiguration")]
        public Output<Outputs.PlaybackConfigurationCdnConfiguration?> CdnConfiguration { get; private set; } = null!;

        /// <summary>
        /// The player parameters and aliases used as dynamic variables during session initialization. For more information, see Domain Variables. 
        /// </summary>
        [Output("configurationAliases")]
        public Output<object?> ConfigurationAliases { get; private set; } = null!;

        /// <summary>
        /// The configuration for DASH content.
        /// </summary>
        [Output("dashConfiguration")]
        public Output<Outputs.PlaybackConfigurationDashConfiguration?> DashConfiguration { get; private set; } = null!;

        /// <summary>
        /// The configuration for HLS content.
        /// </summary>
        [Output("hlsConfiguration")]
        public Output<Outputs.PlaybackConfigurationHlsConfiguration?> HlsConfiguration { get; private set; } = null!;

        /// <summary>
        /// The configuration for pre-roll ad insertion.
        /// </summary>
        [Output("livePreRollConfiguration")]
        public Output<Outputs.PlaybackConfigurationLivePreRollConfiguration?> LivePreRollConfiguration { get; private set; } = null!;

        /// <summary>
        /// The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        /// </summary>
        [Output("manifestProcessingRules")]
        public Output<Outputs.PlaybackConfigurationManifestProcessingRules?> ManifestProcessingRules { get; private set; } = null!;

        /// <summary>
        /// The identifier for the playback configuration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to ad replacement in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see Ad Behavior in AWS Elemental MediaTailor (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        /// </summary>
        [Output("personalizationThresholdSeconds")]
        public Output<int?> PersonalizationThresholdSeconds { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) for the playback configuration.
        /// </summary>
        [Output("playbackConfigurationArn")]
        public Output<string> PlaybackConfigurationArn { get; private set; } = null!;

        /// <summary>
        /// The URL that the player accesses to get a manifest from MediaTailor. This session will use server-side reporting.
        /// </summary>
        [Output("playbackEndpointPrefix")]
        public Output<string> PlaybackEndpointPrefix { get; private set; } = null!;

        /// <summary>
        /// The URL that the player uses to initialize a session that uses client-side reporting.
        /// </summary>
        [Output("sessionInitializationEndpointPrefix")]
        public Output<string> SessionInitializationEndpointPrefix { get; private set; } = null!;

        /// <summary>
        /// The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        /// </summary>
        [Output("slateAdUrl")]
        public Output<string?> SlateAdUrl { get; private set; } = null!;

        /// <summary>
        /// The tags to assign to the playback configuration.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.PlaybackConfigurationTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        /// </summary>
        [Output("transcodeProfileName")]
        public Output<string?> TranscodeProfileName { get; private set; } = null!;

        /// <summary>
        /// The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        /// </summary>
        [Output("videoContentSourceUrl")]
        public Output<string> VideoContentSourceUrl { get; private set; } = null!;


        /// <summary>
        /// Create a PlaybackConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PlaybackConfiguration(string name, PlaybackConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:PlaybackConfiguration", name, args ?? new PlaybackConfigurationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PlaybackConfiguration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:PlaybackConfiguration", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PlaybackConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PlaybackConfiguration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PlaybackConfiguration(name, id, options);
        }
    }

    public sealed class PlaybackConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        /// </summary>
        [Input("adDecisionServerUrl", required: true)]
        public Input<string> AdDecisionServerUrl { get; set; } = null!;

        /// <summary>
        /// The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see Ad Suppression (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        /// </summary>
        [Input("availSuppression")]
        public Input<Inputs.PlaybackConfigurationAvailSuppressionArgs>? AvailSuppression { get; set; }

        /// <summary>
        /// The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see Bumpers (https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
        /// </summary>
        [Input("bumper")]
        public Input<Inputs.PlaybackConfigurationBumperArgs>? Bumper { get; set; }

        /// <summary>
        /// The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        /// </summary>
        [Input("cdnConfiguration")]
        public Input<Inputs.PlaybackConfigurationCdnConfigurationArgs>? CdnConfiguration { get; set; }

        /// <summary>
        /// The player parameters and aliases used as dynamic variables during session initialization. For more information, see Domain Variables. 
        /// </summary>
        [Input("configurationAliases")]
        public Input<object>? ConfigurationAliases { get; set; }

        /// <summary>
        /// The configuration for DASH content.
        /// </summary>
        [Input("dashConfiguration")]
        public Input<Inputs.PlaybackConfigurationDashConfigurationArgs>? DashConfiguration { get; set; }

        /// <summary>
        /// The configuration for HLS content.
        /// </summary>
        [Input("hlsConfiguration")]
        public Input<Inputs.PlaybackConfigurationHlsConfigurationArgs>? HlsConfiguration { get; set; }

        /// <summary>
        /// The configuration for pre-roll ad insertion.
        /// </summary>
        [Input("livePreRollConfiguration")]
        public Input<Inputs.PlaybackConfigurationLivePreRollConfigurationArgs>? LivePreRollConfiguration { get; set; }

        /// <summary>
        /// The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        /// </summary>
        [Input("manifestProcessingRules")]
        public Input<Inputs.PlaybackConfigurationManifestProcessingRulesArgs>? ManifestProcessingRules { get; set; }

        /// <summary>
        /// The identifier for the playback configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to ad replacement in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see Ad Behavior in AWS Elemental MediaTailor (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        /// </summary>
        [Input("personalizationThresholdSeconds")]
        public Input<int>? PersonalizationThresholdSeconds { get; set; }

        /// <summary>
        /// The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        /// </summary>
        [Input("slateAdUrl")]
        public Input<string>? SlateAdUrl { get; set; }

        [Input("tags")]
        private InputList<Inputs.PlaybackConfigurationTagArgs>? _tags;

        /// <summary>
        /// The tags to assign to the playback configuration.
        /// </summary>
        public InputList<Inputs.PlaybackConfigurationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.PlaybackConfigurationTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        /// </summary>
        [Input("transcodeProfileName")]
        public Input<string>? TranscodeProfileName { get; set; }

        /// <summary>
        /// The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        /// </summary>
        [Input("videoContentSourceUrl", required: true)]
        public Input<string> VideoContentSourceUrl { get; set; } = null!;

        public PlaybackConfigurationArgs()
        {
        }
        public static new PlaybackConfigurationArgs Empty => new PlaybackConfigurationArgs();
    }
}
