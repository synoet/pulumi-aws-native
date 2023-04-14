// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    /// <summary>
    /// Settings for logging audio of conversations between Amazon Lex and a user. You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.
    /// </summary>
    [OutputType]
    public sealed class BotAudioLogSetting
    {
        public readonly Outputs.BotAudioLogDestination Destination;
        public readonly bool Enabled;

        [OutputConstructor]
        private BotAudioLogSetting(
            Outputs.BotAudioLogDestination destination,

            bool enabled)
        {
            Destination = destination;
            Enabled = enabled;
        }
    }
}
