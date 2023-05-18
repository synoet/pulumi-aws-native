// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Outputs
{

    /// <summary>
    /// The OptionConfiguration property type specifies an individual option, and its settings, within an AWS::RDS::OptionGroup resource.
    /// </summary>
    [OutputType]
    public sealed class OptionGroupOptionConfiguration
    {
        /// <summary>
        /// A list of DBSecurityGroupMembership name strings used for this option.
        /// </summary>
        public readonly ImmutableArray<string> DBSecurityGroupMemberships;
        /// <summary>
        /// The configuration of options to include in a group.
        /// </summary>
        public readonly string OptionName;
        /// <summary>
        /// The option settings to include in an option group.
        /// </summary>
        public readonly ImmutableArray<Outputs.OptionGroupOptionSetting> OptionSettings;
        /// <summary>
        /// The version for the option.
        /// </summary>
        public readonly string? OptionVersion;
        /// <summary>
        /// The optional port for the option.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// A list of VpcSecurityGroupMembership name strings used for this option.
        /// </summary>
        public readonly ImmutableArray<string> VpcSecurityGroupMemberships;

        [OutputConstructor]
        private OptionGroupOptionConfiguration(
            ImmutableArray<string> dBSecurityGroupMemberships,

            string optionName,

            ImmutableArray<Outputs.OptionGroupOptionSetting> optionSettings,

            string? optionVersion,

            int? port,

            ImmutableArray<string> vpcSecurityGroupMemberships)
        {
            DBSecurityGroupMemberships = dBSecurityGroupMemberships;
            OptionName = optionName;
            OptionSettings = optionSettings;
            OptionVersion = optionVersion;
            Port = port;
            VpcSecurityGroupMemberships = vpcSecurityGroupMemberships;
        }
    }
}
