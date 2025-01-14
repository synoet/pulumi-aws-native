// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppStream.Outputs
{

    [OutputType]
    public sealed class StackApplicationSettings
    {
        public readonly bool Enabled;
        public readonly string? SettingsGroup;

        [OutputConstructor]
        private StackApplicationSettings(
            bool enabled,

            string? settingsGroup)
        {
            Enabled = enabled;
            SettingsGroup = settingsGroup;
        }
    }
}
