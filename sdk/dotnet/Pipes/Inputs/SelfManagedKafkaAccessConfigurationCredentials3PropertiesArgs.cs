// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Inputs
{

    public sealed class SelfManagedKafkaAccessConfigurationCredentials3PropertiesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional SecretManager ARN which stores the database credentials
        /// </summary>
        [Input("clientCertificateTlsAuth", required: true)]
        public Input<string> ClientCertificateTlsAuth { get; set; } = null!;

        public SelfManagedKafkaAccessConfigurationCredentials3PropertiesArgs()
        {
        }
        public static new SelfManagedKafkaAccessConfigurationCredentials3PropertiesArgs Empty => new SelfManagedKafkaAccessConfigurationCredentials3PropertiesArgs();
    }
}
