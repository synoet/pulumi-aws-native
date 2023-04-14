// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Inputs
{

    /// <summary>
    /// Settings for using an Amazon Polly voice to communicate with a user.
    /// </summary>
    public sealed class BotVoiceSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the engine parameter of the SynthesizeSpeech operation in the Amazon Polly developer guide.
        /// </summary>
        [Input("engine")]
        public Input<Pulumi.AwsNative.Lex.BotVoiceSettingsEngine>? Engine { get; set; }

        /// <summary>
        /// The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.
        /// </summary>
        [Input("voiceId", required: true)]
        public Input<string> VoiceId { get; set; } = null!;

        public BotVoiceSettingsArgs()
        {
        }
        public static new BotVoiceSettingsArgs Empty => new BotVoiceSettingsArgs();
    }
}
