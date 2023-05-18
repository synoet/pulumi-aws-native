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
    public sealed class ChannelDvbSubSourceSettings
    {
        public readonly string? OcrLanguage;
        public readonly int? Pid;

        [OutputConstructor]
        private ChannelDvbSubSourceSettings(
            string? ocrLanguage,

            int? pid)
        {
            OcrLanguage = ocrLanguage;
            Pid = pid;
        }
    }
}
