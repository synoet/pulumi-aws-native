// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync.Inputs
{

    public sealed class GraphQLApiOpenIDConnectConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("authTtl")]
        public Input<double>? AuthTtl { get; set; }

        [Input("clientId")]
        public Input<string>? ClientId { get; set; }

        [Input("iatTtl")]
        public Input<double>? IatTtl { get; set; }

        [Input("issuer")]
        public Input<string>? Issuer { get; set; }

        public GraphQLApiOpenIDConnectConfigArgs()
        {
        }
        public static new GraphQLApiOpenIDConnectConfigArgs Empty => new GraphQLApiOpenIDConnectConfigArgs();
    }
}
