// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS.Inputs
{

    public sealed class EndpointOracleSettingsArgs : Pulumi.ResourceArgs
    {
        [Input("secretsManagerAccessRoleArn")]
        public Input<string>? SecretsManagerAccessRoleArn { get; set; }

        [Input("secretsManagerOracleAsmAccessRoleArn")]
        public Input<string>? SecretsManagerOracleAsmAccessRoleArn { get; set; }

        [Input("secretsManagerOracleAsmSecretId")]
        public Input<string>? SecretsManagerOracleAsmSecretId { get; set; }

        [Input("secretsManagerSecretId")]
        public Input<string>? SecretsManagerSecretId { get; set; }

        public EndpointOracleSettingsArgs()
        {
        }
    }
}
