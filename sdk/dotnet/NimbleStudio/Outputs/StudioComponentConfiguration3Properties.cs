// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Outputs
{

    /// <summary>
    /// &lt;p&gt;The configuration of the studio component, based on component type.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class StudioComponentConfiguration3Properties
    {
        public readonly Outputs.StudioComponentSharedFileSystemConfiguration SharedFileSystemConfiguration;

        [OutputConstructor]
        private StudioComponentConfiguration3Properties(Outputs.StudioComponentSharedFileSystemConfiguration sharedFileSystemConfiguration)
        {
            SharedFileSystemConfiguration = sharedFileSystemConfiguration;
        }
    }
}
