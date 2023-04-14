// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES.Inputs
{

    /// <summary>
    /// An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
    /// </summary>
    public sealed class ConfigurationSetDeliveryOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the dedicated IP pool to associate with the configuration set.
        /// </summary>
        [Input("sendingPoolName")]
        public Input<string>? SendingPoolName { get; set; }

        /// <summary>
        /// Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is Require , messages are only delivered if a TLS connection can be established. If the value is Optional , messages can be delivered in plain text if a TLS connection can't be established.
        /// </summary>
        [Input("tlsPolicy")]
        public Input<string>? TlsPolicy { get; set; }

        public ConfigurationSetDeliveryOptionsArgs()
        {
        }
        public static new ConfigurationSetDeliveryOptionsArgs Empty => new ConfigurationSetDeliveryOptionsArgs();
    }
}
