// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dms.Outputs
{

    [OutputType]
    public sealed class Settings3PropertiesMicrosoftSqlServerSettingsProperties
    {
        public readonly string? CertificateArn;
        public readonly string? DatabaseName;
        public readonly int? Port;
        public readonly string? ServerName;
        public readonly Pulumi.AwsNative.Dms.DataProviderDmsSslModeValue? SslMode;

        [OutputConstructor]
        private Settings3PropertiesMicrosoftSqlServerSettingsProperties(
            string? certificateArn,

            string? databaseName,

            int? port,

            string? serverName,

            Pulumi.AwsNative.Dms.DataProviderDmsSslModeValue? sslMode)
        {
            CertificateArn = certificateArn;
            DatabaseName = databaseName;
            Port = port;
            ServerName = serverName;
            SslMode = sslMode;
        }
    }
}
