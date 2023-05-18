// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS.Inputs
{

    public sealed class EndpointMicrosoftSqlServerSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("bcpPacketSize")]
        public Input<int>? BcpPacketSize { get; set; }

        [Input("controlTablesFileGroup")]
        public Input<string>? ControlTablesFileGroup { get; set; }

        [Input("querySingleAlwaysOnNode")]
        public Input<bool>? QuerySingleAlwaysOnNode { get; set; }

        [Input("readBackupOnly")]
        public Input<bool>? ReadBackupOnly { get; set; }

        [Input("safeguardPolicy")]
        public Input<string>? SafeguardPolicy { get; set; }

        [Input("secretsManagerAccessRoleArn")]
        public Input<string>? SecretsManagerAccessRoleArn { get; set; }

        [Input("secretsManagerSecretId")]
        public Input<string>? SecretsManagerSecretId { get; set; }

        [Input("useBcpFullLoad")]
        public Input<bool>? UseBcpFullLoad { get; set; }

        [Input("useThirdPartyBackupDevice")]
        public Input<bool>? UseThirdPartyBackupDevice { get; set; }

        public EndpointMicrosoftSqlServerSettingsArgs()
        {
        }
        public static new EndpointMicrosoftSqlServerSettingsArgs Empty => new EndpointMicrosoftSqlServerSettingsArgs();
    }
}
