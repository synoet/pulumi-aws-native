// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class ConnectorProfileDynatraceConnectorProfileCredentialsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API tokens used by Dynatrace API to authenticate various API calls.
        /// </summary>
        [Input("apiToken", required: true)]
        public Input<string> ApiToken { get; set; } = null!;

        public ConnectorProfileDynatraceConnectorProfileCredentialsArgs()
        {
        }
        public static new ConnectorProfileDynatraceConnectorProfileCredentialsArgs Empty => new ConnectorProfileDynatraceConnectorProfileCredentialsArgs();
    }
}
